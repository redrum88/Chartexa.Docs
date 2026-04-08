---
title: "Python Getting Started"
section: "python"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Python Getting Started

## Summary

The Chartexa Python wrapper provides a fluent, Pythonic API for creating publication-quality charts. It bridges to the .NET charting engine via pythonnet, giving Python developers access to the full rendering pipeline.

---

## Installation

`ash
pip install chartexa
`

Requires Python 3.9+ and .NET 10 runtime. See [Installation](../getting-started/installation.md) for details.

---

## Quick Start

`python
import chartexa as cx

# Convenience function -- creates and returns a Chart
cx.line([10, 20, 15, 30, 25]).save("quick.png")
`

---

## The `Chart` Class

`Chart` is the primary entry point. Every method returns `self` for fluent chaining:

`python
import chartexa as cx
import math

x = [i * 0.1 for i in range(200)]
y = [math.sin(v) * math.exp(-v * 0.05) for v in x]

chart = (
    cx.Chart(width=1200, height=600)
    .line(x, y, stroke="#CBA6F7", thickness=2, label="Damped sine")
    .x_axis(title="Time (s)")
    .y_axis(title="Amplitude")
    .title("Damped Oscillation")
    .theme("catppuccin_mocha")
    .legend()
)

chart.save("damped.png")
`

---

## Available Series Types

| Method | Chart Type | Key Parameters |
|---|---|---|
| `.line()` | Line / spline | `stroke`, `thickness`, `dash`, `spline` |
| `.scatter()` | XY scatter | `marker`, `size`, `fill` |
| `.column()` / `.bar()` | Column / bar | `fill`, `bar_width`, `baseline` |
| `.mountain()` | Area / mountain | `stroke`, `fill`, `baseline` |
| `.candlestick()` | OHLC candles | `bullish_fill`, `bearish_fill` |
| `.band()` | Fill-between | `y_upper`, `y_lower` |
| `.heatmap()` | 2D heatmap | `palette`, `min_value`, `max_value` |
| `.bubble()` | Bubble | `sizes`, `min_size`, `max_size` |
| `.pie()` / `.donut()` | Pie / donut | `labels`, `colors`, `hole_radius` |
| `.stacked_column()` | Stacked columns | `layers`, `stacked_100` |
| `.stacked_mountain()` | Stacked area | `layers`, `stacked_100` |
| `.error_bar()` | Error bars | `error_y`, `error_high`, `error_low` |
| `.box_plot()` | Box plot | `raw_data`, `box_width` |
| `.impulse()` | Stem plot | `baseline`, `marker` |
| `.polar()` | Polar line | `theta`, `r`, `degrees` |
| `.radar()` | Radar chart | `datasets`, `category_labels` |
| `.digital_line()` | Step function | `stroke`, `dash` |
| `.fan()` | Confidence bands | `bands`, `band_colors` |
| `.gantt()` | Gantt chart | `categories`, `starts`, `ends` |

---

## Axes

`python
chart = (
    cx.Chart()
    .line(x, y)
    .x_axis(type="numeric", title="X", range=(0, 100))
    .y_axis(type="log", title="Y (log scale)", log_base=10)
)
`

Axis types: `"numeric"` (default), `"datetime"`, `"category"`, `"log"`.

---

## Themes

`python
chart.theme("catppuccin_mocha")   # or any preset name
chart.theme("dark")
chart.theme("github_dark")
`

Available presets: `dark`, `light`, `catppuccin_mocha`, `catppuccin_latte`, `catppuccin_frappe`, `catppuccin_macchiato`, `github_dark`, `github_light`, `dracula`, `nord`, `solarized_dark`, `solarized_light`, `minimal`, `scientific`.

---

## Interactivity

`python
chart = (
    cx.Chart()
    .line(x, y)
    .zoom_pan()           # Scroll to zoom, drag to pan
    .crosshair()          # Follow the mouse
    .tooltips()           # Show values on hover
    .save_html("interactive.html")
)
`

Interactivity is available in HTML exports and Jupyter notebooks.

---

## Related

- [Chart Builder Reference](chart-builder.md) -- complete method reference
- [Image Export](image-export.md) -- PNG, JPEG, HTML export
- [Jupyter Integration](jupyter.md) -- notebook rendering

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
