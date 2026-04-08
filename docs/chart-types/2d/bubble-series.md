---
title: "Bubble Series"
section: "chart-types/2d"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Bubble Series

## Summary

The bubble series extends scatter plots with a third dimension encoded as marker size. Each data point has X, Y, and a size value. Uses `BubbleRenderableSeries` in the .NET engine.

---

## Quick Start

=== "Python"

    ```python
    import chartexa as cx

    chart = cx.Chart().bubble(
        x=[1, 2, 3, 4, 5],
        y=[10, 30, 20, 40, 25],
        sizes=[100, 250, 150, 400, 200],
        fill="#CBA6F7",
        min_size=6,
        max_size=50,
    )
    chart.save("bubble.png")
    ```

=== "C#"

    ```csharp
    var ds = new XyDataSeries();
    ds.Append(x, y);

    var rs = new BubbleRenderableSeries
    {
        DataSeries = ds,
        Sizes = Array[Double](sizes),
        MinBubbleSize = 6,
        MaxBubbleSize = 50,
        Fill = new ChartColor(128, 203, 166, 247)
    };
    ```

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `sizes` | sequence | *required* | Size values per bubble |
| `fill` | str / tuple | auto | Bubble fill colour |
| `stroke` | str / tuple | `None` | Bubble outline |
| `min_size` | float | `4.0` | Minimum radius (px) |
| `max_size` | float | `40.0` | Maximum radius (px) |
| `opacity` | float | `1.0` | 0.0 -- 1.0 |

---

## When to Use

- Three-variable correlation (GDP vs life expectancy vs population)
- Geographic scatter with magnitude
- Weighted scatter plots

---

## Related

- [Scatter Series](scatter-series.md) -- fixed-size markers
- [Heatmap Series](heatmap-series.md) -- grid-based intensity

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
