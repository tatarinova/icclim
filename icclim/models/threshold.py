from __future__ import annotations

from datetime import datetime
from functools import partial
from typing import Any, Callable, Sequence, Union

import numpy as np
from xarray import DataArray, Dataset
from xclim.core.units import convert_units_to
from xclim.core.utils import PercentileDataArray

from icclim.generic_indices.generic_index_functions import (
    build_doy_per,
    build_period_per,
)
from icclim.icclim_exceptions import InvalidIcclimArgumentError
from icclim.models.constants import DOY_PERCENTILE_UNIT, PERIOD_PERCENTILE_UNIT
from icclim.models.frequency import Frequency
from icclim.models.operator import Operator, OperatorRegistry
from icclim.models.quantile_interpolation import (
    QuantileInterpolation,
    QuantileInterpolationRegistry,
)
from icclim.pre_processing.input_parsing import (
    is_dataset_path,
    read_dataset,
    read_string_threshold,
    read_threshold_DataArray,
)
from icclim.utils import is_number_sequence

ThresholdValueType = Union[
    str, float, int, Dataset, DataArray, Sequence[Union[float, int, str]], None
]


class Threshold:
    """
    - scalar thresh:                               "> 25 ºC"
    - per grid cell thresh:                        "> data.nc"
    - doy percentile threshold:                    "> 98th doy_per"
    - period percentile threshold:                 "> 75th period_per"
    - period percentile threshold with min value:  "> 98th period_per", min_value= "1mm"
    - sequence thresholds (or):                    "> 10 ºC, > 25 ºC"
                                                     thresholds are a new dimension
    """

    operator: Operator
    value: DataArray | Callable[[Frequency, DataArray], PercentileDataArray]
    threshold_var_name: str | None  # may be guessed if missing
    additional_metadata: list[str]

    # -- Percentile specific properties:
    climatology_bounds: Sequence[str, str] | None  # may be guessed if missing
    reference_period: Sequence[str]
    window: int
    only_leap_years: bool
    interpolation: QuantileInterpolation
    threshold_min_value: str | float | None

    @property
    def unit(self) -> str | None:
        if isinstance(self.value, Callable):
            return None
        return self.value.attrs["units"]

    @unit.setter
    def unit(self, unit):
        if not isinstance(self.value, Callable):
            if self.value.attrs.get("units", None) is not None:
                self.value = convert_units_to(self.value, unit)
            self.value.attrs["units"] = unit

    def __init__(
        self,
        query: str | None | Operator = None,
        value: ThresholdValueType = None,
        unit: str | None = None,
        threshold_var_name: str | None = None,
        climatology_bounds: Sequence[str, str] | None = None,
        window: int = 5,
        only_leap_years: bool = False,
        interpolation=QuantileInterpolationRegistry.MEDIAN_UNBIASED,
        base_period_time_range: Sequence[datetime | str] | None = None,
        threshold_min_value: str | float | None = None,
    ):
        is_doy_per_threshold = False
        if isinstance(query, str) and value is None and unit is None:
            operator, unit, value = read_string_threshold(query)
        else:
            operator = query
        if is_dataset_path(value) or isinstance(value, Dataset):
            # e.g. Threshold(">", "thresh*.nc" , "degC")
            ds = value if isinstance(value, Dataset) else read_dataset(value)
            _check_threshold_var_name(threshold_var_name)
            value = read_threshold_DataArray(
                ds[threshold_var_name],
                threshold_min_value=threshold_min_value,
                climatology_bounds=climatology_bounds,
                unit=unit,
            )
        elif is_number_sequence(value):
            # e.g. Threshold(">", [2,3,4], "degC")
            value = DataArray(
                data=value,
                coords={"threshold": value},  # todo: [no magic string]
            )
        elif unit == DOY_PERCENTILE_UNIT:
            value = partial(
                build_doy_per,
                per_val=float(value),
                base_period_time_range=base_period_time_range,
                interpolation=interpolation,
                only_leap_years=only_leap_years,
                window=window,
                percentile_min_value=threshold_min_value,
            )
            is_doy_per_threshold = True
        elif unit == PERIOD_PERCENTILE_UNIT:
            value = partial(
                build_period_per,
                per_val=float(value),
                base_period_time_range=base_period_time_range,
                interpolation=interpolation,
                only_leap_years=only_leap_years,
                percentile_min_value=threshold_min_value,
            )
        elif isinstance(value, (float, int)):
            value = DataArray(
                data=value, coords={"threshold": value}
            )  # todo: no magic string
        elif isinstance(value, DataArray):
            #  nothing to do
            ...
        else:
            raise NotImplementedError("Threshold could not be built.")
        self.is_doy_per_threshold = is_doy_per_threshold
        self.operator = (
            OperatorRegistry.lookup(operator, no_error=True) or OperatorRegistry.REACH
        )
        self.value = value
        self.unit = unit
        self.additional_metadata = []
        self.threshold_var_name = threshold_var_name
        self.climatology_bounds = climatology_bounds
        self.window = window
        self.only_leap_years = only_leap_years
        self.interpolation = interpolation
        self.base_period_time_range = base_period_time_range
        self.threshold_min_value = threshold_min_value

    def get_metadata(self, src_freq: Frequency) -> dict[str, Any]:
        # TODO: [xclim backport] localize/translate these
        if self.value.size == 1:
            res = {
                "standard_name": f"{self.operator.standard_name}_"
                f"{self.value.values[()]}"
                f"_{self.unit}",
                "long_name": f"{self.operator.long_name} "
                f"{self.value.values[()]} "
                f"{self.unit}",
            }
        elif isinstance(self.value, PercentileDataArray):
            percentiles = self.value.coords["percentiles"].values
            bds = self.value.attrs.get("climatology_bounds")
            if self.is_doy_per_threshold:
                if percentiles.size == 1:
                    display_perc = f"{percentiles[0]}th day of year percentile"
                    standard_name = f"{percentiles[0]}th_doy_percentile"
                else:
                    display_perc = str(list(map(lambda x: f"{x}th", percentiles)))
                    standard_name = "_doy_percentiles"
                window = self.value.attrs.get("window", "")
                self.additional_metadata.append(
                    f"day of year percentiles were computed on the {bds} period,"
                    f" with a {window} {src_freq.units} window for each day of year"
                )
            #     todo: add if bootstrap ran or not ro metadata
            else:
                if percentiles.size == 1:
                    display_perc = f"{percentiles[0]}th period percentile"
                    standard_name = f"{percentiles[0]}th_period_percentile"
                else:
                    display_perc = (
                        str(list(map(lambda x: f"{x}th", percentiles)))
                        + " period percentiles"
                    )
                    standard_name = "_period_percentiles"
                self.additional_metadata.append(
                    f"period percentiles were computed on the {bds} period"
                )
            res = {
                "standard_name": f"{self.operator.standard_name}_{standard_name}",
                "long_name": f"{self.operator.long_name} {display_perc}",
            }
        elif isinstance(self.value, DataArray):
            if self.value.size < 10:
                display_value = f"{self.value.values} {self.unit}"
            else:
                display_value = (
                    f"per grid cell values between"
                    f" {np.format_float_positional(self.value.min().values[()], 3)}"
                    f" {self.unit}"
                    f" and {np.format_float_positional(self.value.max().values[()], 3)}"
                    f" {self.unit}"
                )
            res = {
                "standard_name": f"{self.operator.standard_name}_thresholds",
                "long_name": f"{self.operator.long_name} {display_value}",
            }
        else:
            raise NotImplementedError(
                f"Threshold::value must be a DataArray."
                f" It was a {type(self.value)}."
            )
        if len(self.additional_metadata) > 0:
            added_meta = "(" + (", ".join(self.additional_metadata) + ")")
            res.update({"additional_metadata": added_meta})
        return res


def _check_threshold_var_name(threshold_var_name: str | None) -> None:
    if threshold_var_name is None:
        raise InvalidIcclimArgumentError(
            "When threshold is a Dataset, "
            "threshold_var_name must be given to "
            "find the data_variable in the "
            "dataset."
        )
