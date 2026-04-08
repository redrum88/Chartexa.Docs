---
title: "Scatter Series"
section: "chart-types/2d"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Scatter Series

## Summary

The scatter series renders XY data as individual markers without connecting lines. Supports 7 marker shapes with configurable size, colour, and opacity. Uses `XyScatterRenderableSeries` in the .NET engine.

---

## Quick Start

=== "Python"

    `python
    import chartexa as cx

    chart = cx.Chart().scatter(
        [1, 2, 3, 4, 5],
        [10, 40, 20, 35, 25],
        marker="circle",
        size=10,
        fill="#89B4FA",
    )
    chart.save("scatter.png")
    `

=== "C#"

    `csharp
    var ds = new XyDataSeries();
    ds.Append(new double[] { 1, 2, 3, 4, 5 },
              new double[] { 10, 40, 20, 35, 25 });

    var ms = new MarkerStyle
    {
        Type = MarkerType.Circle,
        Size = 10,
        Fill = new ChartColor(137, 180, 250)
    };

    var rs = new XyScatterRenderableSeries
    {
        DataSeries = ds,
        Marker = ms
    };
    surface.RenderableSeries.Add(rs);
    `

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `marker` | str | `"circle"` | Shape: `"circle"`, `"square"`, `"triangle"`, `"cross"`, `"diamond"`, `"plus"`, `"star"` |
| `size` | float | `8.0` | Marker diameter in pixels |
| `fill` | str / tuple | auto | Marker fill colour |
| `stroke` | str / tuple | `None` | Marker outline colour |
| `stroke_thickness` | float | `1.0` | Outline width |
| `opacity` | float | `1.0` | 0.0 -- 1.0 |

---

## Examples

### Marker Shapes

`python
import chartexa as cx
import random

shapes = ["circle", "square", "triangle", "diamond", "star", "cross", "plus"]
colors = ["#F38BA8", "#89B4FA", "#A6E3A1", "#F9E2AF", "#CBA6F7", "#94E2D5", "#FAB387"]

chart = cx.Chart(width=1200, height=600)
for i, (shape, color) in enumerate(zip(shapes, colors)):
    y = [random.gauss(i * 5, 1) for _ in range(20)]
    x = [random.gauss(i * 3, 1) for _ in range(20)]
    chart.scatter(x, y, marker=shape, size=12, fill=color, label=shape.title())

chart.legend().save("marker_shapes.png")
`

---

## When to Use

- Correlation analysis between two variables
- Cluster visualisation
- Outlier detection
- Any dataset where points are independent (no meaningful order)

---

## Related

- [Line Series](line-series.md) -- connected data points
- [Bubble Series](bubble-series.md) -- scatter with variable-size markers

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
