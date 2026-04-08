---
title: "Numeric Axis"
section: "axes"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Numeric Axis

## Summary

The numeric axis is the default axis type. It maps continuous numeric values to pixel positions. Auto-ranges to fit data unless a fixed range is specified.

---

## Quick Start

=== "Python"

    `python
    import chartexa as cx

    chart = (
        cx.Chart()
        .line([0, 1, 2, 3], [10, 20, 15, 30])
        .x_axis(type="numeric", title="Index", label_format="0.0")
        .y_axis(type="numeric", title="Value", range=(0, 40), grow_by=0.1)
    )
    chart.save("numeric_axis.png")
    `

=== "C#"

    `csharp
    var xAxis = new NumericAxis
    {
        AxisTitle = "Index",
        LabelFormat = "0.0"
    };

    var yAxis = new NumericAxis
    {
        AxisTitle = "Value",
        VisibleRange = new DoubleRange(0, 40),
        GrowBy = 0.1
    };
    `

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `label_format` | str | `None` | .NET numeric format string (e.g. `"0.00"`, `"#,##0"`) |
| `range` | tuple | `None` | Fixed `(min, max)` visible range |
| `grow_by` | float | `0.05` | Padding fraction applied to auto-range |

---

## Related

- [Axes Overview](overview.md)
- [Axis Ranging](axis-ranging.md)
- [Label Providers](label-providers.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
