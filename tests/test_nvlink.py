import math
import pytest
from pysim.nvlink import link_bw_gbps

def test_basic_bw():
    assert math.isclose(link_bw_gbps(8, 50.0), 400.0, rel_tol=1e-9)

def test_invalid_params():
    with pytest.raises(ValueError):
        link_bw_gbps(0, 50.0)
    with pytest.raises(ValueError):
        link_bw_gbps(8, 0.0)
