# ruff: noqa: A001, E501, N803
"""
icclim's API for generic indices.

This module has been auto-generated.
To modify these, edit the extractor tool in `tools/extract-icclim-funs.py`.
This module exposes each climate index as individual functions for convenience.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import icclim
from icclim.generic.registry import GenericIndicatorRegistry

if TYPE_CHECKING:
    import datetime as dt
    from collections.abc import Sequence
    from typing import FrequencyLike, InFileLike, SamplingMethodLike

    from xarray import Dataset

    from icclim._core.legacy.user_index.model import UserIndexDict
    from icclim._core.model.netcdf_version import NetcdfVersion
    from icclim._core.model.quantile_interpolation import QuantileInterpolation
    from icclim._core.model.threshold import Threshold
    from icclim.frequency import Frequency
    from icclim.logger import Verbosity

__all__ = [
    "average",
    "count_occurrences",
    "custom_index",
    "deficit",
    "difference_of_extremes",
    "difference_of_means",
    "excess",
    "fraction_of_total",
    "max_consecutive_occurrence",
    "max_of_rolling_average",
    "max_of_rolling_sum",
    "maximum",
    "mean_of_absolute_one_time_step_difference",
    "mean_of_difference",
    "min_of_rolling_average",
    "min_of_rolling_sum",
    "minimum",
    "percentile",
    "standard_deviation",
    "sum",
    "sum_of_spell_lengths",
]


def count_occurrences(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Count occurrences when threshold(s) are met (e.g. SU, Tx90p, RR1).

    count_occurrences: Count occurrences when threshold(s) are met (e.g. SU, Tx90p, RR1).


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.CountOccurrences,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
    )


def max_consecutive_occurrence(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Count the maximum number of consecutive occurrences when threshold(s) are met (e.g. CDD, CSU, CWD).

    max_consecutive_occurrence: Count the maximum number of consecutive occurrences when threshold(s) are met (e.g. CDD, CSU, CWD).


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.MaxConsecutiveOccurrence,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
    )


def sum_of_spell_lengths(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
    min_spell_length: int | None = 6,
) -> Dataset:
    """Sum the lengths of each consecutive occurrence spell when threshold(s) are met. The minimum spell length is controlled by `min_spell_length` (e.g. WSDI, CSDI).

    sum_of_spell_lengths: Sum the lengths of each consecutive occurrence spell when threshold(s) are met. The minimum spell length is controlled by `min_spell_length` (e.g. WSDI, CSDI).


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    min_spell_length : int
        ``optional`` Minimum spell duration to be taken into account when computing
        the sum_of_spell_lengths.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.SumOfSpellLengths,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        min_spell_length=min_spell_length,
    )


def excess(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Compute the excess over the given threshold. The excess is `sum(x[x>t] - t)` where x is the studied variable and t the threshold (e.g. GD4).

    excess: Compute the excess over the given threshold. The excess is `sum(x[x>t] - t)` where x is the studied variable and t the threshold (e.g. GD4).


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.Excess,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
    )


def deficit(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Compute the deficit below the given threshold. The deficit is `sum(t - x[x<t])` where x is the studied variable and t the threshold (e.g. HD17).

    deficit: Compute the deficit below the given threshold. The deficit is `sum(t - x[x<t])` where x is the studied variable and t the threshold (e.g. HD17).


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.Deficit,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
    )


def fraction_of_total(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Compute the fraction of values meeting threshold(s) over the sum of every values (e.g. R75pTOT, R95pTOT).

    fraction_of_total: Compute the fraction of values meeting threshold(s) over the sum of every values (e.g. R75pTOT, R95pTOT).


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.FractionOfTotal,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
    )


def maximum(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Maximum of values that met threshold(s), if threshold(s) are given (e.g. Txx, Tnx).

    maximum: Maximum of values that met threshold(s), if threshold(s) are given (e.g. Txx, Tnx).


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.Maximum,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
    )


def minimum(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Minimum of values that met threshold(s), if threshold(s) are given (e.g. Txn, Tnn).

    minimum: Minimum of values that met threshold(s), if threshold(s) are given (e.g. Txn, Tnn).


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.Minimum,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
    )


def average(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Average of values that met threshold(s), if threshold(s) are given (e.g. Tx, Tn).

    average: Average of values that met threshold(s), if threshold(s) are given (e.g. Tx, Tn).


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.Average,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
    )


def sum(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Sum of values that met threshold(s), if threshold(s) are given (e.g. PRCPTOT, RR).

    sum: Sum of values that met threshold(s), if threshold(s) are given (e.g. PRCPTOT, RR).


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.Sum,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
    )


def standard_deviation(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Standard deviation of values that met threshold(s), if threshold(s) are given.

    standard_deviation: Standard deviation of values that met threshold(s), if threshold(s) are given.


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """  # noqa: D401
    return icclim.index(
        index_name=GenericIndicatorRegistry.StandardDeviation,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
    )


def max_of_rolling_sum(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
    rolling_window_width: int | None = 5,
) -> Dataset:
    """Maximum of rolling sum over time dimension (e.g. RX5DAY: maximum 5 days window of precipitation accumulation).

    max_of_rolling_sum: Maximum of rolling sum over time dimension (e.g. RX5DAY: maximum 5 days window of precipitation accumulation).


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    rolling_window_width : int
        ``optional`` Window width of the rolling window for indicators such as
        `{max_of_rolling_sum, max_of_rolling_average, min_of_rolling_sum, min_of_rolling_average}`
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.MaxOfRollingSum,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        rolling_window_width=rolling_window_width,
    )


def min_of_rolling_sum(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
    rolling_window_width: int | None = 5,
) -> Dataset:
    """Minimum of rolling sum over time dimension.

    min_of_rolling_sum: Minimum of rolling sum over time dimension.


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    rolling_window_width : int
        ``optional`` Window width of the rolling window for indicators such as
        `{max_of_rolling_sum, max_of_rolling_average, min_of_rolling_sum, min_of_rolling_average}`
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.MinOfRollingSum,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        rolling_window_width=rolling_window_width,
    )


def max_of_rolling_average(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
    rolling_window_width: int | None = 5,
) -> Dataset:
    """Maximum of rolling average over time dimension.

    max_of_rolling_average: Maximum of rolling average over time dimension.


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    rolling_window_width : int
        ``optional`` Window width of the rolling window for indicators such as
        `{max_of_rolling_sum, max_of_rolling_average, min_of_rolling_sum, min_of_rolling_average}`
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.MaxOfRollingAverage,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        rolling_window_width=rolling_window_width,
    )


def min_of_rolling_average(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
    rolling_window_width: int | None = 5,
) -> Dataset:
    """Minimum of rolling average over time dimension.

    min_of_rolling_average: Minimum of rolling average over time dimension.


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    rolling_window_width : int
        ``optional`` Window width of the rolling window for indicators such as
        `{max_of_rolling_sum, max_of_rolling_average, min_of_rolling_sum, min_of_rolling_average}`
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.MinOfRollingAverage,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        rolling_window_width=rolling_window_width,
    )


def mean_of_difference(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Average of the difference between two variables, or one variable and it's reference period values (e.g. DTR: `mean(tasmax - tasmin)`).

    mean_of_difference: Average of the difference between two variables, or one variable and it's reference period values (e.g. DTR: `mean(tasmax - tasmin)`).


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.MeanOfDifference,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
    )


def difference_of_extremes(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Difference of extremes between two variables, or one variable and it's reference period values. The extremes are always `maximum` for the first variable and `minimum` for the second variable (e.g. ETR: `max(tasmax) - min(tasmin)`).

    difference_of_extremes: Difference of extremes between two variables, or one variable and it's reference period values. The extremes are always `maximum` for the first variable and `minimum` for the second variable (e.g. ETR: `max(tasmax) - min(tasmin)`).


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.DifferenceOfExtremes,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
    )


def mean_of_absolute_one_time_step_difference(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Average of the absolute one time step by one time step difference between two variables, or one variable and it's reference period values (e.g. vDTR: `mean((tasmax[i] - tasmin[i]) - (tasmax[i-1] - tasmin[i-1])` ; where i is the day of measure).

    mean_of_absolute_one_time_step_difference: Average of the absolute one time step by one time step difference between two variables, or one variable and it's reference period values (e.g. vDTR: `mean((tasmax[i] - tasmin[i]) - (tasmax[i-1] - tasmin[i-1])` ; where i is the day of measure).


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.MeanOfAbsoluteOneTimeStepDifference,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
    )


def difference_of_means(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
    sampling_method: SamplingMethodLike = "resample",
) -> Dataset:
    """Difference of the average between two variables, or one variable and it's reference period values (e.g. anomaly: `mean(tasmax) - mean(tasmax_ref]))`.

    difference_of_means: Difference of the average between two variables, or one variable and it's reference period values (e.g. anomaly: `mean(tasmax) - mean(tasmax_ref]))`.


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")
    sampling_method : str
        Choose whether the output sampling configured in `slice_mode` is a
        `groupby` operation or a `resample` operation (as per xarray definitions).
        Possible values:
        ``{"groupby", "resample", "groupby_ref_and_resample_study"}``
        (default: "resample")
        `groupby_ref_and_resample_study` may only be used when computing the
        `difference_of_means` (a.k.a the anomaly).

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.DifferenceOfMeans,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        sampling_method=sampling_method,
    )


def percentile(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    threshold: str | Threshold | Sequence[str | Threshold] | None = None,
    ignore_Feb29th: bool = False,
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Percentile of a variable.

    percentile: Percentile of a variable.


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    threshold : float | list[float] | None
        ``optional`` User defined threshold for certain indices.
        Default depend on the index, see their individual definition.
        When a list of threshold is provided, the index will be computed for each
        thresholds.
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        index_name=GenericIndicatorRegistry.Percentile,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        threshold=threshold,
        ignore_Feb29th=ignore_Feb29th,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
    )


def custom_index(
    user_index: UserIndexDict,
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    base_period_time_range: Sequence[dt.datetime] | Sequence[str] | None = None,
    doy_window_width: int = 5,
    only_leap_years: bool = False,
    ignore_Feb29th: bool = False,
    interpolation: str | QuantileInterpolation = "median_unbiased",
    out_unit: str | None = None,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
    min_spell_length: int | None = 6,
    rolling_window_width: int | None = 5,
    sampling_method: SamplingMethodLike = "resample",
) -> Dataset:
    """Compute custom indices using simple operators.

    Use the `user_index` parameter to describe how the index should be computed.
    You can find some examples in icclim documentation at :ref:`custom indices`


    Parameters
    ----------
    in_files : str | list[str] | Dataset | DataArray | InputDictionary
        Absolute path(s) to NetCDF dataset(s), including OPeNDAP URLs,
        or path to zarr store, or xarray.Dataset or xarray.DataArray.
    var_name : str | list[str] | None
        ``optional`` Target variable name to process corresponding to ``in_files``.
        If None (default) on ECA&D index, the variable is guessed based on the
        climate index wanted.
        Mandatory for a user index.
    slice_mode : FrequencyLike | Frequency
        Type of temporal aggregation:
        The possibles values are ``{"year", "month", "DJF", "MAM", "JJA", "SON",
        "ONDJFM" or "AMJJAS", ("season", [1,2,3]), ("month", [1,2,3,])}``
        (where season and month lists can be customized) or any valid pandas
        frequency.
        A season can also be defined between two exact dates:
        ``("season", ("19 july", "14 august"))``.
        Default is "year".
        See :ref:`slice_mode` for details.
    time_range : list[datetime.datetime ] | list[str]  | tuple[str, str] | None
        ``optional`` Temporal range: upper and lower bounds for temporal subsetting.
        If ``None``, whole period of input files will be processed.
        The dates can either be given as instance of datetime.datetime or as string
        values. For strings, many format are accepted.
        Default is ``None``.
    out_file : str | None
        Output NetCDF file name (default: "icclim_out.nc" in the current directory).
        Default is "icclim_out.nc".
        If the input ``in_files`` is a ``Dataset``, ``out_file`` field is ignored.
        Use the function returned value instead to retrieve the computed value.
        If ``out_file`` already exists, icclim will overwrite it!
    base_period_time_range : list[datetime.datetime ] | list[str] | tuple[str, str] | None
        ``optional`` Temporal range of the reference period.
        The dates can either be given as instance of datetime.datetime or as string
        values.
        It is used either:
        #. to compute percentiles if threshold is filled.
        When missing, the studied period is used to compute percentiles.
        The study period is either the dataset filtered by `time_range` or the whole
        dataset if `time_range` is missing.
        For day of year percentiles (doy_per), on extreme percentiles the
        overlapping period between `base_period_time_range` and the study period is
        bootstrapped.
        #. to compute a reference period for indices such as difference_of_mean
        (a.k.a anomaly) if a single variable is given in input.
    doy_window_width : int
        ``optional`` Window width used to aggreagte day of year values when computing
        day of year percentiles (doy_per)
        Default: 5 (5 days).
    min_spell_length : int
        ``optional`` Minimum spell duration to be taken into account when computing
        the sum_of_spell_lengths.
    rolling_window_width : int
        ``optional`` Window width of the rolling window for indicators such as
        `{max_of_rolling_sum, max_of_rolling_average, min_of_rolling_sum, min_of_rolling_average}`
    only_leap_years : bool
        ``optional`` Option for February 29th (default: False).
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    interpolation : str | QuantileInterpolation | None
        ``optional`` Interpolation method to compute percentile values:
        ``{"linear", "median_unbiased"}``
        Default is "median_unbiased", a.k.a type 8 or method 8.
        Ignored for non percentile based indices.
    out_unit : str | None
        ``optional`` Output unit for certain indices: "days" or "%"
        (default: "days").
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    save_thresholds : bool
        ``optional`` True if the thresholds should be saved within the resulting
        netcdf file (default: False).
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")
    sampling_method : str
        Choose whether the output sampling configured in `slice_mode` is a
        `groupby` operation or a `resample` operation (as per xarray definitions).
        Possible values:
        ``{"groupby", "resample", "groupby_ref_and_resample_study"}``
        (default: "resample")
        `groupby_ref_and_resample_study` may only be used when computing the
        `difference_of_means` (a.k.a the anomaly).

    Notes
    -----
    This function has been auto-generated.

    """
    return icclim.index(
        user_index=user_index,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        base_period_time_range=base_period_time_range,
        doy_window_width=doy_window_width,
        only_leap_years=only_leap_years,
        ignore_Feb29th=ignore_Feb29th,
        interpolation=interpolation,
        out_unit=out_unit,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        min_spell_length=min_spell_length,
        rolling_window_width=rolling_window_width,
        sampling_method=sampling_method,
    )
