---
title: "Rendering Pipeline"
section: "architecture"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Rendering Pipeline

## Summary

The rendering pipeline transforms data series and chart configuration into pixels. The pipeline runs in the .NET engine with GPU acceleration (DirectX 12) or CPU rendering (Skia).

---

## Pipeline Stages

`mermaid
graph LR
    A[Data Series] --> B[Coordinate Transform]
    B --> C[Clipping]
    C --> D[Series Rendering]
    D --> E[Annotation Overlay]
    E --> F[Legend / Title]
    F --> G[Output Encoding]
`

1. **Coordinate Transform** -- maps data values to pixel positions using axis ranges
2. **Clipping** -- removes data outside the visible viewport
3. **Series Rendering** -- draws lines, bars, points using the selected renderer
4. **Annotation Overlay** -- renders annotations on top of series
5. **Legend / Title** -- adds text elements
6. **Output Encoding** -- encodes to PNG, JPEG, or buffered for display

---

## DirectX 12 Pipeline

The DirectX 12 renderer uses:

- **Compute shaders** for data-to-pixel transformation (parallel processing)
- **SDF text rendering** for resolution-independent text
- **GPU-side vertex buffers** for line and point geometry
- **Double buffering** for tear-free real-time updates

---

## Skia Pipeline

The Skia renderer uses:

- **SkCanvas** for 2D drawing operations
- **Anti-aliased rendering** for smooth lines and text
- **CPU-based** -- no GPU requirement
- **Cross-platform** -- works identically on Windows, Linux, macOS

---

## Related

- [System Overview](system-overview.md)
- [DirectX 12 Setup](../rendering/directx12/setup.md)
- [GPU Acceleration](../performance/gpu-acceleration.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
