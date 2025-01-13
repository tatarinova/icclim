# ruff: noqa: A001, E501, N803
"""
icclim's API for dcsc indices.

This module has been auto-generated.
To modify these, edit the extractor tool in `tools/extract-icclim-funs.py`.
This module exposes each climate index as individual functions for convenience.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import icclim
from icclim._core.input_parsing import get_dataarray_from_dataset
from icclim.dcsc.registry import DcscIndexRegistry
from icclim.threshold.factory import build_threshold

if TYPE_CHECKING:
    import datetime as dt
    from collections.abc import Sequence
    from typing import FrequencyLike, InFileLike

    from xarray import DataArray, Dataset

    from icclim._core.model.netcdf_version import NetcdfVersion
    from icclim._core.model.quantile_interpolation import QuantileInterpolation
    from icclim.frequency import Frequency
    from icclim.logger import Verbosity

__all__ = [
    "cdd",
    "ff98",
    "ffav",
    "hdd",
    "pav",
    "pfl90",
    "pint",
    "pn20mm",
    "pq90",
    "pq99",
    "pxcdd",
    "pxcwd",
    "r99",
    "rr",
    "rr1mm",
    "sd",
    "tav",
    "tn10",
    "tn90",
    "tncwd",
    "tnfd",
    "tnht",
    "tnnd",
    "tr",
    "trav",
    "tx10",
    "tx35",
    "tx90",
    "txav",
    "txfd",
    "txhwd",
    "txnd",
]


def tav(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Moyenne de la température moyenne.

    TAV: Moyenne de la température moyenne.
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.TAV,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        out_unit="degree_Celsius",
    )


def txav(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Moyenne de la température maximale.

    TXAV: Moyenne de la température maximale.
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.TXAV,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        out_unit="degree_Celsius",
    )


def trav(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Moyenne de l'amplitude thermique.

    TRAV: Moyenne de l'amplitude thermique.
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.TRAV,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        out_unit="degree_Celsius",
    )


def tx10(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    base_period_time_range: Sequence[dt.datetime] | Sequence[str] | None = None,
    only_leap_years: bool = False,
    ignore_Feb29th: bool = False,
    interpolation: str | QuantileInterpolation = "median_unbiased",
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Extrême froid de la température maximale journalière (10e centile de la température maximale).

    TX10: Extrême froid de la température maximale journalière (10e centile de la température maximale).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    only_leap_years : bool
        ``optional`` Option for February 29th (default: False).
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    interpolation : str | QuantileInterpolation | None
        ``optional`` Interpolation method to compute percentile values:
        ``{"linear", "median_unbiased"}``
        Default is "median_unbiased", a.k.a type 8 or method 8.
        Ignored for non percentile based indices.
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
        index_name=DcscIndexRegistry.TX10,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        base_period_time_range=base_period_time_range,
        only_leap_years=only_leap_years,
        ignore_Feb29th=ignore_Feb29th,
        interpolation=interpolation,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="< 10 doy_per",
            doy_window_width=5,
            only_leap_years=only_leap_years,
            interpolation=interpolation,
            reference_period=base_period_time_range,
        ),
        out_unit="day",
    )


def tx90(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    base_period_time_range: Sequence[dt.datetime] | Sequence[str] | None = None,
    only_leap_years: bool = False,
    ignore_Feb29th: bool = False,
    interpolation: str | QuantileInterpolation = "median_unbiased",
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Extrême chaud de la température maximale journalière (90e centile de la température maximale).

    TX90: Extrême chaud de la température maximale journalière (90e centile de la température maximale).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    only_leap_years : bool
        ``optional`` Option for February 29th (default: False).
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    interpolation : str | QuantileInterpolation | None
        ``optional`` Interpolation method to compute percentile values:
        ``{"linear", "median_unbiased"}``
        Default is "median_unbiased", a.k.a type 8 or method 8.
        Ignored for non percentile based indices.
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
        index_name=DcscIndexRegistry.TX90,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        base_period_time_range=base_period_time_range,
        only_leap_years=only_leap_years,
        ignore_Feb29th=ignore_Feb29th,
        interpolation=interpolation,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="> 90 doy_per",
            doy_window_width=5,
            only_leap_years=only_leap_years,
            interpolation=interpolation,
            reference_period=base_period_time_range,
        ),
        out_unit="day",
    )


def tn10(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    base_period_time_range: Sequence[dt.datetime] | Sequence[str] | None = None,
    only_leap_years: bool = False,
    ignore_Feb29th: bool = False,
    interpolation: str | QuantileInterpolation = "median_unbiased",
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Extrême froid de la température minimale  journalière (10e centile de la température minimale).

    TN10: Extrême froid de la température minimale  journalière (10e centile de la température minimale).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    only_leap_years : bool
        ``optional`` Option for February 29th (default: False).
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    interpolation : str | QuantileInterpolation | None
        ``optional`` Interpolation method to compute percentile values:
        ``{"linear", "median_unbiased"}``
        Default is "median_unbiased", a.k.a type 8 or method 8.
        Ignored for non percentile based indices.
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
        index_name=DcscIndexRegistry.TN10,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        base_period_time_range=base_period_time_range,
        only_leap_years=only_leap_years,
        ignore_Feb29th=ignore_Feb29th,
        interpolation=interpolation,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="< 10 doy_per",
            doy_window_width=5,
            only_leap_years=only_leap_years,
            interpolation=interpolation,
            reference_period=base_period_time_range,
        ),
        out_unit="day",
    )


def tn90(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    base_period_time_range: Sequence[dt.datetime] | Sequence[str] | None = None,
    only_leap_years: bool = False,
    ignore_Feb29th: bool = False,
    interpolation: str | QuantileInterpolation = "median_unbiased",
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Extrême chaud de la température minimale journalière (90e centile de la température minimale).

    TN90: Extrême chaud de la température minimale journalière (90e centile de la température minimale).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    only_leap_years : bool
        ``optional`` Option for February 29th (default: False).
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    interpolation : str | QuantileInterpolation | None
        ``optional`` Interpolation method to compute percentile values:
        ``{"linear", "median_unbiased"}``
        Default is "median_unbiased", a.k.a type 8 or method 8.
        Ignored for non percentile based indices.
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
        index_name=DcscIndexRegistry.TN90,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        base_period_time_range=base_period_time_range,
        only_leap_years=only_leap_years,
        ignore_Feb29th=ignore_Feb29th,
        interpolation=interpolation,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="> 90 doy_per",
            doy_window_width=5,
            only_leap_years=only_leap_years,
            interpolation=interpolation,
            reference_period=base_period_time_range,
        ),
        out_unit="day",
    )


def tnfd(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Nombre de jours de gel (température minimale <= 0°C).

    TNFD: Nombre de jours de gel (température minimale <= 0°C).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.TNFD,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="< 0 degree_Celsius",
        ),
        out_unit="day",
    )


def txfd(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Nombre de jours sans dégel (température maximale <= 0°C).

    TXFD: Nombre de jours sans dégel (température maximale <= 0°C).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.TXFD,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="< 0 degree_Celsius",
        ),
        out_unit="day",
    )


def sd(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Nombre de journées d'été (température maximale > 25°C).

    SD: Nombre de journées d'été (température maximale > 25°C).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.SD,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="> 25 degree_Celsius",
        ),
        out_unit="day",
    )


def tx35(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Nombre de jours de forte chaleur (température maximale > 35°C).

    TX35: Nombre de jours de forte chaleur (température maximale > 35°C).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.TX35,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="> 35 degree_Celsius",
        ),
        out_unit="day",
    )


def tr(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Nombre de nuits tropicales (température minimale > 20°C).

    TR: Nombre de nuits tropicales (température minimale > 20°C).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.TR,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="> 20 degree_Celsius",
        ),
        out_unit="day",
    )


def txnd(
    in_files: InFileLike,
    normal: str | Sequence[str] | Dataset | DataArray,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
    normal_var_name: str | None = None,
) -> Dataset:
    """Nombre de jours anormalement chauds (température maximale supérieure de plus de 5°C à la normale).

    TXND: Nombre de jours anormalement chauds (température maximale supérieure de plus de 5°C à la normale).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")
    normal : Union[str, Sequence[str], Dataset, DataArray, None]
        The normal to be compared to.
        Typically, the expected normal dataset should have one value per `lat, lon`
        couple.
        Can be a path or a list of paths to netCDF datasets or a xarray Dataset or
        DataArray.
    normal_var_name : str | None, optional
        The name of the normal variable.
        If missing, icclim will try to guess which variable must be used in the
        `normal` dataset.
        Ignored if ``normal`` is a

    Notes
    -----
    This function has been auto-generated.

    """
    standard_index = DcscIndexRegistry.TXND
    normal_da = get_dataarray_from_dataset(
        normal_var_name, normal, standard_index.input_variables[0]
    )
    threshold = standard_index.threshold
    threshold.prepare(normal_da)
    return icclim.index(
        index_name=DcscIndexRegistry.TXND,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        out_unit="day",
    )


def tnht(
    in_files: InFileLike,
    normal: str | Sequence[str] | Dataset | DataArray,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
    normal_var_name: str | None = None,
) -> Dataset:
    """Nombre de nuits anormalement chaudes (température minimale supérieure de plus de 5°C à la normale).

    TNHT: Nombre de nuits anormalement chaudes (température minimale supérieure de plus de 5°C à la normale).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")
    normal : Union[str, Sequence[str], Dataset, DataArray, None]
        The normal to be compared to.
        Typically, the expected normal dataset should have one value per `lat, lon`
        couple.
        Can be a path or a list of paths to netCDF datasets or a xarray Dataset or
        DataArray.
    normal_var_name : str | None, optional
        The name of the normal variable.
        If missing, icclim will try to guess which variable must be used in the
        `normal` dataset.
        Ignored if ``normal`` is a

    Notes
    -----
    This function has been auto-generated.

    """
    standard_index = DcscIndexRegistry.TNHT
    normal_da = get_dataarray_from_dataset(
        normal_var_name, normal, standard_index.input_variables[0]
    )
    threshold = standard_index.threshold
    threshold.prepare(normal_da)
    return icclim.index(
        index_name=DcscIndexRegistry.TNHT,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        out_unit="day",
    )


def tnnd(
    in_files: InFileLike,
    normal: str | Sequence[str] | Dataset | DataArray,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
    normal_var_name: str | None = None,
) -> Dataset:
    """Nombre de jours anormalement froids (température minimale inférieure de plus de 5°C à la normale).

    TNND: Nombre de jours anormalement froids (température minimale inférieure de plus de 5°C à la normale).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")
    normal : Union[str, Sequence[str], Dataset, DataArray, None]
        The normal to be compared to.
        Typically, the expected normal dataset should have one value per `lat, lon`
        couple.
        Can be a path or a list of paths to netCDF datasets or a xarray Dataset or
        DataArray.
    normal_var_name : str | None, optional
        The name of the normal variable.
        If missing, icclim will try to guess which variable must be used in the
        `normal` dataset.
        Ignored if ``normal`` is a

    Notes
    -----
    This function has been auto-generated.

    """
    standard_index = DcscIndexRegistry.TNND
    normal_da = get_dataarray_from_dataset(
        normal_var_name, normal, standard_index.input_variables[0]
    )
    threshold = standard_index.threshold
    threshold.prepare(normal_da)
    return icclim.index(
        index_name=DcscIndexRegistry.TNND,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        out_unit="day",
    )


def tncwd(
    in_files: InFileLike,
    normal: str | Sequence[str] | Dataset | DataArray,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
    normal_var_name: str | None = None,
) -> Dataset:
    """Nombre de jours d'une vague de froid (température min < de plus de 5°C à la normale pdt au moins 5j consécutifs).

    TNCWD: Nombre de jours d'une vague de froid (température min < de plus de 5°C à la normale pdt au moins 5j consécutifs).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")
    normal : Union[str, Sequence[str], Dataset, DataArray, None]
        The normal to be compared to.
        Typically, the expected normal dataset should have one value per `lat, lon`
        couple.
        Can be a path or a list of paths to netCDF datasets or a xarray Dataset or
        DataArray.
    normal_var_name : str | None, optional
        The name of the normal variable.
        If missing, icclim will try to guess which variable must be used in the
        `normal` dataset.
        Ignored if ``normal`` is a

    Notes
    -----
    This function has been auto-generated.

    """
    standard_index = DcscIndexRegistry.TNCWD
    normal_da = get_dataarray_from_dataset(
        normal_var_name, normal, standard_index.input_variables[0]
    )
    threshold = standard_index.threshold
    threshold.prepare(normal_da)
    return icclim.index(
        index_name=DcscIndexRegistry.TNCWD,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        out_unit="day",
    )


def txhwd(
    in_files: InFileLike,
    normal: str | Sequence[str] | Dataset | DataArray,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
    normal_var_name: str | None = None,
) -> Dataset:
    """Nombre de jours d'une vague de chaleur (température max > de plus de 5°C à la normale pdt au moins 5j consécutifs).

    TXHWD: Nombre de jours d'une vague de chaleur (température max > de plus de 5°C à la normale pdt au moins 5j consécutifs).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
    date_event : bool
        When True the date of the event (such as when a maximum is reached) will be
        stored in coordinates variables.
        **warning** This option may significantly slow down computation.
    logs_verbosity : str | Verbosity
        ``optional`` Configure how verbose icclim is.
        Possible values: ``{"LOW", "HIGH", "SILENT"}`` (default: "LOW")
    normal : Union[str, Sequence[str], Dataset, DataArray, None]
        The normal to be compared to.
        Typically, the expected normal dataset should have one value per `lat, lon`
        couple.
        Can be a path or a list of paths to netCDF datasets or a xarray Dataset or
        DataArray.
    normal_var_name : str | None, optional
        The name of the normal variable.
        If missing, icclim will try to guess which variable must be used in the
        `normal` dataset.
        Ignored if ``normal`` is a

    Notes
    -----
    This function has been auto-generated.

    """
    standard_index = DcscIndexRegistry.TXHWD
    normal_da = get_dataarray_from_dataset(
        normal_var_name, normal, standard_index.input_variables[0]
    )
    threshold = standard_index.threshold
    threshold.prepare(normal_da)
    return icclim.index(
        index_name=DcscIndexRegistry.TXHWD,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        out_unit="day",
    )


def hdd(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Degrés-jours de chauffage (Cumul sur la période des écarts négatifs au seuil de < 17°C par la température qt moyenne).

    HDD: Degrés-jours de chauffage (Cumul sur la période des écarts négatifs au seuil de < 17°C par la température qt moyenne).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.HDD,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="17 degree_Celsius",
        ),
        out_unit="degree_Celsius day",
    )


def cdd(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Degrés-jours de climatisation(Cumul sur la période des dépassements du seuil de > 18°C par la température qt moyenne).

    CDD: Degrés-jours de climatisation(Cumul sur la période des dépassements du seuil de > 18°C par la température qt moyenne).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.CDD,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="18 degree_Celsius",
        ),
        out_unit="degree_Celsius day",
    )


def pav(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Précipitations quotidiennes moyennes.

    PAV: Précipitations quotidiennes moyennes.
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.PAV,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        out_unit="mm/day",
    )


def pint(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Précipitation moyenne des jours pluvieux (RR > 1 mm).

    PINT: Précipitation moyenne des jours pluvieux (RR > 1 mm).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.PINT,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query=">= 1 mm/day",
        ),
        out_unit="mm/day",
    )


def rr(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Cumul de précipitation.

    RR: Cumul de précipitation.
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.RR,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        out_unit="mm",
    )


def rr1mm(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Nombre de jours de pluie (précipitations >= 1 mm).

    RR1MM: Nombre de jours de pluie (précipitations >= 1 mm).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.RR1MM,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query=">= 1 mm/day",
        ),
        out_unit="day",
    )


def pn20mm(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Nombre de jours de fortes précipitations (précipitations >= 20 mm).

    PN20MM: Nombre de jours de fortes précipitations (précipitations >= 20 mm).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.PN20MM,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query=">= 20 mm/day",
        ),
        out_unit="day",
    )


def pxcdd(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Période de sécheresse (Max [Nbj consécutifs RR < 1 mm]).

    PXCDD: Période de sécheresse (Max [Nbj consécutifs RR < 1 mm]).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.PXCDD,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="< 1 mm/day",
        ),
        out_unit="day",
    )


def pxcwd(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Nombre maximum de jours pluvieux consécutifs (Max [Nbj consécutifs RR > 1 mm]).

    PXCWD: Nombre maximum de jours pluvieux consécutifs (Max [Nbj consécutifs RR > 1 mm]).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.PXCWD,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query=">= 1 mm/day",
        ),
        out_unit="day",
    )


def r99(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    base_period_time_range: Sequence[dt.datetime] | Sequence[str] | None = None,
    only_leap_years: bool = False,
    ignore_Feb29th: bool = False,
    interpolation: str | QuantileInterpolation = "median_unbiased",
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Nombre de jours de précipitations extrêmes.

    R99: Nombre de jours de précipitations extrêmes.
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    only_leap_years : bool
        ``optional`` Option for February 29th (default: False).
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    interpolation : str | QuantileInterpolation | None
        ``optional`` Interpolation method to compute percentile values:
        ``{"linear", "median_unbiased"}``
        Default is "median_unbiased", a.k.a type 8 or method 8.
        Ignored for non percentile based indices.
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
        index_name=DcscIndexRegistry.R99,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        base_period_time_range=base_period_time_range,
        only_leap_years=only_leap_years,
        ignore_Feb29th=ignore_Feb29th,
        interpolation=interpolation,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="> 99 period_per",
            doy_window_width=5,
            only_leap_years=only_leap_years,
            interpolation=interpolation,
            reference_period=base_period_time_range,
            threshold_min_value="1 mm d-1",
        ),
        out_unit="day",
    )


def pfl90(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    base_period_time_range: Sequence[dt.datetime] | Sequence[str] | None = None,
    only_leap_years: bool = False,
    ignore_Feb29th: bool = False,
    interpolation: str | QuantileInterpolation = "median_unbiased",
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Fraction des précipitations journalières intenses.

    PFL90: Fraction des précipitations journalières intenses.
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    only_leap_years : bool
        ``optional`` Option for February 29th (default: False).
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    interpolation : str | QuantileInterpolation | None
        ``optional`` Interpolation method to compute percentile values:
        ``{"linear", "median_unbiased"}``
        Default is "median_unbiased", a.k.a type 8 or method 8.
        Ignored for non percentile based indices.
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
        index_name=DcscIndexRegistry.PFL90,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        base_period_time_range=base_period_time_range,
        only_leap_years=only_leap_years,
        ignore_Feb29th=ignore_Feb29th,
        interpolation=interpolation,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="> 90 period_per",
            doy_window_width=5,
            only_leap_years=only_leap_years,
            interpolation=interpolation,
            reference_period=base_period_time_range,
            threshold_min_value="1 mm d-1",
        ),
        out_unit="%",
    )


def pq90(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    base_period_time_range: Sequence[dt.datetime] | Sequence[str] | None = None,
    only_leap_years: bool = False,
    ignore_Feb29th: bool = False,
    interpolation: str | QuantileInterpolation = "median_unbiased",
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Précipitation quotidienne intense (90e centile des précipitations).

    PQ90: Précipitation quotidienne intense (90e centile des précipitations).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    only_leap_years : bool
        ``optional`` Option for February 29th (default: False).
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    interpolation : str | QuantileInterpolation | None
        ``optional`` Interpolation method to compute percentile values:
        ``{"linear", "median_unbiased"}``
        Default is "median_unbiased", a.k.a type 8 or method 8.
        Ignored for non percentile based indices.
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
        index_name=DcscIndexRegistry.PQ90,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        base_period_time_range=base_period_time_range,
        only_leap_years=only_leap_years,
        ignore_Feb29th=ignore_Feb29th,
        interpolation=interpolation,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="> 90 doy_per",
            doy_window_width=5,
            only_leap_years=only_leap_years,
            interpolation=interpolation,
            reference_period=base_period_time_range,
            threshold_min_value="1 mm d-1",
        ),
        out_unit="%",
    )


def pq99(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    base_period_time_range: Sequence[dt.datetime] | Sequence[str] | None = None,
    only_leap_years: bool = False,
    ignore_Feb29th: bool = False,
    interpolation: str | QuantileInterpolation = "median_unbiased",
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Précipitation quotidienne extrême (99e centile des précipitations).

    PQ99: Précipitation quotidienne extrême (99e centile des précipitations).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    only_leap_years : bool
        ``optional`` Option for February 29th (default: False).
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    interpolation : str | QuantileInterpolation | None
        ``optional`` Interpolation method to compute percentile values:
        ``{"linear", "median_unbiased"}``
        Default is "median_unbiased", a.k.a type 8 or method 8.
        Ignored for non percentile based indices.
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
        index_name=DcscIndexRegistry.PQ99,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        base_period_time_range=base_period_time_range,
        only_leap_years=only_leap_years,
        ignore_Feb29th=ignore_Feb29th,
        interpolation=interpolation,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="> 99 doy_per",
            doy_window_width=5,
            only_leap_years=only_leap_years,
            interpolation=interpolation,
            reference_period=base_period_time_range,
            threshold_min_value="1 mm d-1",
        ),
        out_unit="%",
    )


def ffav(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    base_period_time_range: Sequence[dt.datetime] | Sequence[str] | None = None,
    ignore_Feb29th: bool = False,
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Écart de la vitesse du vent moyenne journalière (par rapport à une periode de référence).

    FFAV: Écart de la vitesse du vent moyenne journalière (par rapport à une periode de référence).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    netcdf_version : str | NetcdfVersion
        ``optional`` NetCDF version to create (default: "NETCDF3_CLASSIC").
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
        index_name=DcscIndexRegistry.FFAV,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        base_period_time_range=base_period_time_range,
        ignore_Feb29th=ignore_Feb29th,
        netcdf_version=netcdf_version,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        out_unit="m s-1",
    )


def ff98(
    in_files: InFileLike,
    var_name: str | Sequence[str] | None = None,
    slice_mode: FrequencyLike | Frequency = "year",
    time_range: Sequence[dt.datetime | str] | None = None,
    out_file: str | None = None,
    base_period_time_range: Sequence[dt.datetime] | Sequence[str] | None = None,
    only_leap_years: bool = False,
    ignore_Feb29th: bool = False,
    interpolation: str | QuantileInterpolation = "median_unbiased",
    netcdf_version: str | NetcdfVersion = "NETCDF4",
    save_thresholds: bool = False,
    logs_verbosity: Verbosity | str = "LOW",
    date_event: bool = False,
) -> Dataset:
    """Nombre de jours de vent fort (vent ≥ 98e centile de la période de référence).

    FF98: Nombre de jours de vent fort (vent ≥ 98e centile de la période de référence).
    Source: Portail DRIAS, DCSC, MeteoFrance.


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
    only_leap_years : bool
        ``optional`` Option for February 29th (default: False).
    ignore_Feb29th : bool
        ``optional`` Ignoring or not February 29th (default: False).
    interpolation : str | QuantileInterpolation | None
        ``optional`` Interpolation method to compute percentile values:
        ``{"linear", "median_unbiased"}``
        Default is "median_unbiased", a.k.a type 8 or method 8.
        Ignored for non percentile based indices.
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
        index_name=DcscIndexRegistry.FF98,
        in_files=in_files,
        var_name=var_name,
        slice_mode=slice_mode,
        time_range=time_range,
        out_file=out_file,
        base_period_time_range=base_period_time_range,
        only_leap_years=only_leap_years,
        ignore_Feb29th=ignore_Feb29th,
        interpolation=interpolation,
        netcdf_version=netcdf_version,
        save_thresholds=save_thresholds,
        logs_verbosity=logs_verbosity,
        date_event=date_event,
        threshold=build_threshold(
            query="> 98 period_per",
            doy_window_width=5,
            only_leap_years=only_leap_years,
            interpolation=interpolation,
            reference_period=base_period_time_range,
            threshold_min_value="1 kt",
        ),
        out_unit="days",
    )
