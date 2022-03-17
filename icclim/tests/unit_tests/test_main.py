import os
from unittest.mock import MagicMock, patch

import numpy as np
import pandas as pd
import pytest
import xarray as xr

import icclim
from icclim.models.index_group import IndexGroup


@patch("icclim.main.index")
@patch("icclim.icclim_logger.IcclimLogger")
def test_deprecated_indice(log_mock: MagicMock, index_mock: MagicMock):
    icclim.main.log = log_mock
    icclim.indice()
    log_mock.deprecation_warning.assert_called_once_with(
        old="icclim.indice", new="icclim.index"
    )
    index_mock.assert_called_once()


HEAT_INDICES = ["SU", "TR", "WSDI", "TG90p", "TN90p", "TX90p", "TXx", "TNx", "CSU"]


@pytest.mark.slow
class Test_Integration:
    """
    Simple integration test.
    We are not testing here the actual indices results, they are already tested in
    `test_ecad_indices.py` as well as in xclim directly.
    The goal it to make sure every the whole app can run smoothly

    These tests have side effect:
    - writing and removing of "out.nc" file

    """

    OUTPUT_FILE = "out.nc"
    TIME_RANGE = pd.date_range(start="2042-01-01", end="2045-12-31", freq="D")
    data = xr.DataArray(
        data=(np.full(len(TIME_RANGE), 20).reshape((len(TIME_RANGE), 1, 1))),
        dims=["time", "lat", "lon"],
        coords=dict(
            lat=[42],
            lon=[42],
            time=TIME_RANGE,
        ),
        attrs={"units": "degC"},
    )

    @pytest.fixture(autouse=True)
    def cleanup(self):
        # setup
        # ...
        yield
        # teardown
        try:
            os.remove(self.OUTPUT_FILE)
        except FileNotFoundError:
            pass

    def test_index_SU(self):
        res = icclim.index(
            indice_name="SU", in_files=self.data, out_file=self.OUTPUT_FILE
        )
        np.testing.assert_array_equal(0, res.SU)

    def test_indices_from_DataArray(self):
        res = icclim.indices(
            index_group=IndexGroup.HEAT, in_files=self.data, out_file=self.OUTPUT_FILE
        )
        for i in HEAT_INDICES:
            assert res[i] is not None

    def test_indices_from_Dataset(self):
        ds = self.data.to_dataset(name="tas")
        res = icclim.indices(
            index_group=IndexGroup.HEAT,
            in_files=ds,
            var_name="tas",
            out_file=self.OUTPUT_FILE,
        )
        for i in HEAT_INDICES:
            assert res[i] is not None
