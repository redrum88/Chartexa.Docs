---
title: "Pie & Donut Series"
section: "chart-types/2d"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Pie & Donut Series

## Summary

The pie and donut series render proportional data as circular segments. The donut variant adds a configurable inner hole. Both support labels, percentage display, segment explosion, and custom colours.

---

## Quick Start

=== "Python"

    ```python
    import chartexa as cx

    # Pie chart
    chart = cx.Chart().pie(
        [35, 25, 20, 15, 5],
        labels=["Chrome", "Safari", "Firefox", "Edge", "Other"],
        colors=["#F38BA8", "#89B4FA", "#A6E3A1", "#F9E2AF", "#CBA6F7"],
    )
    chart.save("pie.png")

    # Donut chart
    chart = cx.Chart().donut(
        [35, 25, 20, 15, 5],
        labels=["Chrome", "Safari", "Firefox", "Edge", "Other"],
        hole_radius=0.6,
    )
    chart.save("donut.png")
    ```

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `values` | seq of float | *required* | Segment values |
| `labels` | seq of str | `None` | Segment labels |
| `colors` | sequence | `None` | Per-segment colours |
| `explode` | seq of int | `None` | Indices to pull out |
| `start_angle` | float | `0.0` | Starting angle (degrees) |
| `show_percentage` | bool | `True` | Display percentage labels |
| `hole_radius` | float | `0.55` | Inner hole size (donut only, 0 -- 1) |
| `gap` | float | `1.5` | Gap between segments |
| `font_size` | float | `12.0` | Label font size |

---

## When to Use

- Market share / composition
- Budget allocation
- Survey response distribution

!!! warning "Limit Segments"
    Pie/donut charts become hard to read with more than 7 segments. Consider a bar chart for larger datasets.

---

## Related

- [Column Series](column-series.md) -- better for many categories
- [Stacked Column](stacked-column.md) -- comparative proportions

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
