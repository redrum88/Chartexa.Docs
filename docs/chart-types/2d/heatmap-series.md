---
title: "Heatmap Series"
section: "chart-types/2d"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Heatmap Series

## Summary

The heatmap series renders a 2D grid of values as coloured cells. Supports multiple colour palettes and optional cell gridlines. Uses `HeatmapSeries` in the .NET engine.

---

## Quick Start

=== "Python"

    `python
    import chartexa as cx
    import math

    # Generate a 20x20 grid
    data = [[math.sin(x * 0.3) * math.cos(y * 0.3) for x in range(20)] for y in range(20)]

    chart = cx.Chart().heatmap(
        data,
        palette="viridis",
        min_value=-1.0,
        max_value=1.0,
    )
    chart.save("heatmap.png")
    `

=== "C#"

    `csharp
    var cfg = new HeatmapConfig
    {
        Data = data2D,
        Palette = HeatmapPalette.Viridis,
        MinValue = -1.0,
        MaxValue = 1.0,
        ShowGrid = true
    };

    var rs = new HeatmapSeries { Config = cfg };
    surface.RenderableSeries.Add(rs);
    `

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `data` | 2D sequence | *required* | Row-major values `data[row][col]` |
| `palette` | str | `"thermal"` | `"thermal"`, `"rainbow"`, `"viridis"`, `"inferno"`, `"diverging"` |
| `min_value` | float | `0.0` | Colour scale minimum |
| `max_value` | float | `1.0` | Colour scale maximum |
| `show_grid` | bool | `True` | Draw cell gridlines |

---

## When to Use

- Correlation matrices
- Sensor grids (temperature, pressure)
- Image-like scientific data
- Confusion matrices in machine learning

---

## Related

- [Bubble Series](bubble-series.md) -- three-variable scatter
- [3D Surface Mesh](../3d/surface-mesh.md) -- 3D equivalent

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
