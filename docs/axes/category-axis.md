---
title: "Category Axis"
section: "axes"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Category Axis

## Summary

The category axis maps discrete labels to evenly spaced positions. Data points are indexed (0, 1, 2, ...) and displayed with string labels.

---

## Quick Start

=== "Python"

    `python
    import chartexa as cx

    chart = (
        cx.Chart()
        .column([0, 1, 2, 3], [50, 80, 45, 90], fill="#A6E3A1")
        .x_axis(type="category", labels=["Q1", "Q2", "Q3", "Q4"])
        .y_axis(title="Revenue (k)")
    )
    chart.save("category_axis.png")
    `

=== "C#"

    `csharp
    var xAxis = new CategoryAxis(new[] { "Q1", "Q2", "Q3", "Q4" })
    {
        AxisTitle = "Quarter"
    };
    `

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `labels` | seq of str | *required* | Category labels |
| `label_rotation` | float | `0.0` | Label rotation in degrees |

---

## Related

- [Axes Overview](overview.md)
- [Column Series](../chart-types/2d/column-series.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
