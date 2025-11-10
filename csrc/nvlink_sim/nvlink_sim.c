// csrc/nvlink_sim.c
#include <stdint.h>

#ifdef _WIN32
#define EXPORTED __declspec(dllexport)
#else
#define EXPORTED
#endif

typedef struct {
    int lanes;
    double lane_gbps;
} NvlinkConfig;

// Simple "effective bandwidth" calculator: lanes * per-lane Gbps
EXPORTED double nvlink_link_bw_gbps(NvlinkConfig cfg) {
    return cfg.lanes * cfg.lane_gbps;
}

// Basic parameter validation
EXPORTED int nvlink_validate(int lanes, double lane_gbps) {
    return (lanes > 0 && lane_gbps > 0.0) ? 1 : 0;
}
