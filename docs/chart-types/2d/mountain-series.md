---
title: "Mountain Series"
section: "chart-types/2d"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Mountain Series

## Summary

The mountain (area) series renders a filled area between a line and a baseline. Combines a line stroke on top with a solid or gradient fill below. Uses `MountainRenderableSeries` in the .NET engine.

---

## Quick Start

=== "Python"

    ```python
    import chartexa as cx

    chart = cx.Chart().mountain(
        [0, 1, 2, 3, 4, 5],
        [10, 25, 18, 30, 22, 28],
        stroke="#89B4FA",
        fill="#89B4FA",
    )
    chart.save("mountain.png")
    ```

=== "C#"

    ```csharp
    var ds = new XyDataSeries();
    ds.Append(new double[] { 0, 1, 2, 3, 4, 5 },
              new double[] { 10, 25, 18, 30, 22, 28 });

    var rs = new MountainRenderableSeries
    {
        DataSeries = ds,
        Stroke = new ChartColor(137, 180, 250),
        Fill = new ChartColor(80, 137, 180, 250),  // Semi-transparent
        StrokeThickness = 1.5
    };
    surface.RenderableSeries.Add(rs);
    ```

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `stroke` | str / tuple | auto | Top-edge line colour |
| `fill` | str / tuple | auto | Area fill colour |
| `thickness` | float | `1.5` | Stroke width |
| `baseline` | float | `0.0` | Y-value where the fill meets the axis |

---

## When to Use

- Emphasise the magnitude of values (volume, cumulative totals)
- Show trends where the area under the curve is meaningful
- Layered area charts (use stacked mountain for multiple series)

---

## Related

- [Line Series](line-series.md) -- line without fill
- [Band Series](band-series.md) -- fill between two boundaries
- [Stacked Mountain](stacked-mountain.md) -- layered area chart

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
