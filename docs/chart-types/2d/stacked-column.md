---
title: "Stacked Column"
section: "chart-types/2d"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Stacked Column

## Summary

The stacked column series renders multiple data layers stacked vertically at each X position. Supports absolute stacking and 100% normalised stacking. The stacked bar variant renders horizontally.

---

## Quick Start

=== "Python"

    `python
    import chartexa as cx

    x = [0, 1, 2, 3]
    layers = [
        [20, 30, 25, 35],  # Layer 1
        [15, 20, 30, 25],  # Layer 2
        [10, 15, 10, 20],  # Layer 3
    ]

    chart = cx.Chart().stacked_column(
        x, layers,
        colors=["#F38BA8", "#89B4FA", "#A6E3A1"],
        labels=["Product A", "Product B", "Product C"],
    )
    chart.save("stacked.png")
    `

=== "C#"

    `csharp
    var s = new StackedColumnSeries(x, layers)
    {
        Colors = new[] { ChartColor.FromHex("#F38BA8"), ... },
        Labels = new[] { "Product A", "Product B", "Product C" }
    };
    `

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `layers` | seq of seq | *required* | Y-values per layer |
| `colors` | sequence | `None` | Per-layer fill colours |
| `labels` | sequence | `None` | Per-layer labels |
| `stroke` | str / tuple | `None` | Outline colour |
| `bar_width` | float | `0.7` | Bar width fraction |
| `stacked_100` | bool | `False` | Normalise to 100% |

---

## Stacked Bar Variant

`python
chart = cx.Chart().stacked_bar(
    x, layers,
    colors=["#F38BA8", "#89B4FA", "#A6E3A1"],
    stacked_100=True,
)
`

---

## When to Use

- Part-to-whole comparisons across categories
- Revenue breakdown by product line
- Survey response distributions

---

## Related

- [Column Series](column-series.md) -- single-layer columns
- [Stacked Mountain](stacked-mountain.md) -- continuous stacked areas

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
