---
title: "3D Surface Mesh"
section: "chart-types/3d"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# 3D Surface Mesh

## Summary

The 3D surface mesh renders a function of two variables as a wireframe or solid surface in three dimensions. Uses `XYZSurfaceSeries`.

---

## Quick Start

=== "Python"

    `python
    from chartexa import XYZSurfaceSeries
    # 3D surface configuration via the series class API
    `

=== "C#"

    `csharp
    var surface3d = new XYZSurfaceSeries
    {
        XSize = 50,
        ZSize = 50,
        Data = heightMap2D
    };
    `

---

## When to Use

- Mathematical surface visualisation
- Terrain / topography
- 3D scientific data

---

## Related

- [Heatmap Series](../2d/heatmap-series.md) -- 2D equivalent

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
