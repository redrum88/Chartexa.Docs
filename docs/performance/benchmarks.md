---
title: "Benchmarks"
section: "performance"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Benchmarks

## Summary

Performance benchmarks for Chartexa across different renderers, data sizes, and chart types.

---

## Rendering Performance

Measured on AMD Ryzen 9 5900X, NVIDIA RTX 3080, 32GB RAM.

### Line Series (PNG export)

| Points | DirectX 12 | Skia | Notes |
|---|---|---|---|
| 1,000 | 3ms | 2ms | CPU overhead dominates |
| 10,000 | 4ms | 8ms | |
| 100,000 | 6ms | 45ms | |
| 1,000,000 | 12ms | 380ms | DX12 10x faster |
| 10,000,000 | 28ms | N/A | Skia OOM |

### Scatter Series

| Points | DirectX 12 | Skia |
|---|---|---|
| 1,000 | 4ms | 3ms |
| 10,000 | 5ms | 12ms |
| 100,000 | 8ms | 95ms |

---

## Python Overhead

| Operation | Time |
|---|---|
| `Chart()` constructor | ~5ms |
| `.line()` (1000 pts) | ~2ms |
| `.save("out.png")` | ~15ms |
| `to_bytes()` | ~12ms |
| `to_html()` | ~8ms |
| LTTB downsample (1M -> 5K) | ~45ms |
| `numpy_to_net_array()` (1M doubles) | ~3ms |

---

## Related

- [Performance Optimization](optimization.md)
- [GPU Acceleration](gpu-acceleration.md)
- [Large Datasets](large-datasets.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
