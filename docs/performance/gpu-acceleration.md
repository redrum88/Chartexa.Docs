---
title: "GPU Acceleration"
section: "performance"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# GPU Acceleration

## Summary

The DirectX 12 renderer offloads rendering to the GPU for maximum performance. It uses compute shaders for data processing and SDF (Signed Distance Field) text rendering for crisp labels at any resolution.

---

## Requirements

- Windows 10 version 1903 or later
- DirectX 12 capable GPU
- .NET 10 runtime

---

## When GPU Acceleration Helps

| Scenario | CPU-Only | GPU |
|---|---|---|
| 1,000 points, static | 2ms | 3ms (overhead) |
| 100,000 points, real-time | 45ms | 4ms |
| 1,000,000 points, real-time | 400ms+ | 8ms |
| 10,000,000 points | Not feasible | 16ms |

GPU acceleration provides the most benefit with large datasets and real-time updates.

---

## Related

- [Performance Optimization](optimization.md)
- [DirectX 12 Setup](../rendering/directx12/setup.md)
- [Benchmarks](benchmarks.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
