# runs from project root in PyCharm by default
from pysim.nvlink import link_bw_gbps
print("BW =", link_bw_gbps(8, 50.0), "Gbps")
