from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from icclim.icclim_exceptions import InvalidIcclimArgumentError
from icclim.models.frequency import Frequency, get_seasonal_time_updater
from icclim.tests.test_utils import stub_tas


class Test_build_frequency_over_frequency:
    def test_simple(self):
        freq = Frequency.lookup(Frequency.YEAR)
        assert freq == Frequency.YEAR


class Test_build_frequency_over_string:
    def test_error(self):
        with pytest.raises(InvalidIcclimArgumentError):
            Frequency.lookup("yolo")

    def test_simple(self):
        freq = Frequency.lookup("year")
        assert freq == Frequency.YEAR


class Test_build_frequency_over_list:
    def test_error(self):
        with pytest.raises(InvalidIcclimArgumentError):
            Frequency.lookup(["cacahuêtes"])

    def test_month(self):
        freq = Frequency.lookup(["month", [1, 4, 3]])
        assert freq == Frequency.CUSTOM
        assert freq.pandas_freq == "MS"
        assert freq.accepted_values == []
        assert freq.post_processing is not None

    def test_season(self):
        freq = Frequency.lookup(["season", [1, 2, 3, 4]])
        assert freq == Frequency.CUSTOM
        assert freq.pandas_freq == "AS-JAN"
        assert freq.accepted_values == []
        assert freq.post_processing is not None

    def test_winter__deprecated_tuple(self):
        freq = Frequency.lookup(["season", ([11, 12], [1, 2, 3, 4])])
        assert freq == Frequency.CUSTOM
        assert freq.pandas_freq == "AS-NOV"
        assert freq.accepted_values == []
        assert freq.post_processing is not None

    def test_error__non_consecutive_season(self):
        with pytest.raises(InvalidIcclimArgumentError):
            Frequency.lookup(["season", ([12, 3])])

    def test_error__weird_months(self):
        with pytest.raises(InvalidIcclimArgumentError):
            Frequency.lookup(["season", ([42, 0])])

    def test_winter(self):
        freq = Frequency.lookup(["season", [11, 12, 1, 2]])
        assert freq == Frequency.CUSTOM
        assert freq.pandas_freq == "AS-NOV"
        assert freq.accepted_values == []
        assert freq.post_processing is not None

    def test_lookup_season_between_dates(self):
        freq = Frequency.lookup(["season", ["07-19", "08-14"]])
        assert freq == Frequency.CUSTOM
        assert freq.pandas_freq == "AS-JUL"
        assert freq.accepted_values == []
        assert freq.post_processing is not None


class Test_seasons_resampler:
    def test_simple(self):
        # WHEN
        test_da = filter_months(stub_tas(), [4, 5, 6]).resample(time="YS").mean()
        da_res, time_bds_res = get_seasonal_time_updater(4, 6)(test_da)
        # THEN
        np.testing.assert_array_equal(1, da_res)
        assert time_bds_res[0].data[0] == pd.to_datetime("2042-04")
        assert (
            time_bds_res[0].data[1]
            == pd.to_datetime("2042-07") - pd.tseries.offsets.Day()
        )

    def test_winter(self):
        # WHEN
        test_da = filter_months(stub_tas(), [11, 12, 1]).resample(time="AS-NOV").mean()
        da_res, time_bds_res = get_seasonal_time_updater(11, 1)(test_da)
        # THEN
        np.testing.assert_array_equal(1, da_res)
        assert time_bds_res[0].data[0] == pd.to_datetime("2041-11")
        assert (
            time_bds_res[0].data[1]
            == pd.to_datetime("2042-02") - pd.tseries.offsets.Day()
        )
        assert time_bds_res[1].data[0] == pd.to_datetime("2042-11")
        assert (
            time_bds_res[1].data[1]
            == pd.to_datetime("2043-02") - pd.tseries.offsets.Day()
        )

    @pytest.mark.parametrize("use_cf", [True, False])
    def test_between_dates(self, use_cf):
        # WHEN
        test_da = (
            filter_months(stub_tas(use_cftime=use_cf), [11, 12, 1])
            .resample(time="AS-NOV")
            .mean()
        )
        da_res, time_bds_res = get_seasonal_time_updater(11, 1, 2, 30)(test_da)
        # THEN
        np.testing.assert_array_equal(1, da_res)  # data must be unchanged
        assert time_bds_res[0].data[0] == pd.to_datetime("2041-11-02")
        assert time_bds_res[0].data[1] == pd.to_datetime("2042-01-30")


def filter_months(da, month_list: list[int]):
    return da.sel(time=da.time.dt.month.isin(month_list))
