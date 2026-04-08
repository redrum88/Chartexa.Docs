---
title: "Axes Overview"
section: "axes"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Axes Overview

## Summary

Axes define the coordinate space for chart series. Chartexa provides four axis types, each optimised for different data domains. Axes are added via the `x_axis()` and `y_axis()` methods on the `Chart` builder, or by constructing axis classes directly in C#.

---

## Axis Types

| Type | Class | Use Case |
|---|---|---|
| **Numeric** | `NumericAxis` | General-purpose continuous data (default) |
| **DateTime** | `DateTimeAxis` | Time-based data with date formatting |
| **Category** | `CategoryAxis` | Discrete labels (product names, regions) |
| **Logarithmic** | `LogarithmicAxis` | Data spanning orders of magnitude |

---

## Quick Start

=== "Python"

    `python
    import chartexa as cx

    chart = (
        cx.Chart()
        .line([0, 1, 2, 3], [10, 20, 15, 30])
        .x_axis(type="numeric", title="Sample Index")
        .y_axis(type="numeric", title="Value", range=(0, 40))
    )
    chart.save("axes_example.png")
    `

=== "C#"

    `csharp
    surface.XAxes.Add(new NumericAxis
    {
        AxisTitle = "Sample Index"
    });
    surface.YAxes.Add(new NumericAxis
    {
        AxisTitle = "Value",
        VisibleRange = new DoubleRange(0, 40)
    });
    `

---

## Common Properties

All axis types share these configuration options:

| Property | Type | Default | Description |
|---|---|---|---|
| `type` | str | `"numeric"` | Axis type |
| `id` | str | `"DefaultXAxis"` / `"DefaultYAxis"` | Identifier for multi-axis binding |
| `alignment` | str | `"bottom"` / `"left"` | `"top"`, `"bottom"`, `"left"`, `"right"` |
| `title` | str | `None` | Axis label text |
| `range` | tuple | `None` | Fixed visible range `(min, max)` |
| `grow_by` | float | `0.05` | Extra padding as fraction of range |
| `grid_visible` | bool | `True` | Show grid lines |
| `grid_color` | str / tuple | `None` | Grid line colour |
| `grid_thickness` | float | `1.0` | Grid line width |
| `grid_dash` | str | `None` | Grid dash style |

---

## Multi-Axis Charts

Bind series to specific axes using `x_axis_id` and `y_axis_id`:

`python
chart = (
    cx.Chart(width=1200, height=600)
    .line(x, temp, stroke="#F38BA8", y_axis_id="TempAxis", label="Temperature")
    .line(x, humidity, stroke="#89B4FA", y_axis_id="HumAxis", label="Humidity")
    .y_axis(id="TempAxis", title="Temp (C)", alignment="left")
    .y_axis(id="HumAxis", title="Humidity (%)", alignment="right")
    .legend()
)
`

---

## Related

- [Numeric Axis](numeric-axis.md)
- [DateTime Axis](datetime-axis.md)
- [Category Axis](category-axis.md)
- [Logarithmic Axis](logarithmic-axis.md)
- [Multiple Axes](multiple-axes.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
