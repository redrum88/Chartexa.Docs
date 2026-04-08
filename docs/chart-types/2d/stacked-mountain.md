---
title: "Stacked Mountain"
section: "chart-types/2d"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Stacked Mountain

## Summary

The stacked mountain series renders multiple area layers stacked vertically. Each layer's fill extends from the previous layer's top edge. Supports 100% normalised stacking.

---

## Quick Start

=== "Python"

    ```python
    import chartexa as cx

    x = list(range(10))
    layers = [
        [5, 8, 6, 9, 7, 10, 8, 11, 9, 12],
        [3, 4, 5, 3, 4, 5, 6, 4, 5, 6],
        [2, 3, 2, 4, 3, 2, 3, 4, 3, 2],
    ]

    chart = cx.Chart().stacked_mountain(
        x, layers,
        colors=["#F38BA8", "#89B4FA", "#A6E3A1"],
        labels=["CPU", "Memory", "Disk"],
    )
    chart.save("stacked_mountain.png")
    ```

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `layers` | seq of seq | *required* | Y-values per layer |
| `colors` | sequence | `None` | Per-layer fill colours |
| `strokes` | sequence | `None` | Per-layer stroke colours |
| `labels` | sequence | `None` | Per-layer legend labels |
| `thickness` | float | `1.5` | Top-edge stroke width |
| `stacked_100` | bool | `False` | Normalise to 100% |

---

## When to Use

- Resource utilisation over time (CPU + memory + disk)
- Traffic composition (HTTP methods, user segments)
- Cumulative time series

---

## Related

- [Mountain Series](mountain-series.md) -- single area series
- [Stacked Column](stacked-column.md) -- discrete stacked bars

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
