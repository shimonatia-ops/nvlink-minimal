import ctypes, os
from ctypes import c_int, c_double, Structure

class NvlinkConfig(Structure):
    _fields_ = [("lanes", c_int), ("lane_gbps", c_double)]

def _dll_path():
    # Expect DLL in ../csrc/nvlink_sim.dll relative to this file
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    return os.path.join(root, "csrc", "nvlink_sim.dll")

def _load_lib():
    dll = _dll_path()
    if not os.path.exists(dll):
        raise FileNotFoundError(f"Missing DLL at: {dll}")
    return ctypes.CDLL(dll)

_lib = _load_lib()
_lib.nvlink_link_bw_gbps.argtypes = [NvlinkConfig]
_lib.nvlink_link_bw_gbps.restype  = c_double
_lib.nvlink_validate.argtypes     = [c_int, c_double]
_lib.nvlink_validate.restype      = c_int

def link_bw_gbps(lanes: int, lane_gbps: float) -> float:
    """Compute effective link bandwidth in Gbps: lanes * lane_gbps."""
    if not _lib.nvlink_validate(int(lanes), float(lane_gbps)):
        raise ValueError("Invalid lanes or lane_gbps")
    cfg = NvlinkConfig(lanes=int(lanes), lane_gbps=float(lane_gbps))
    return float(_lib.nvlink_link_bw_gbps(cfg))
