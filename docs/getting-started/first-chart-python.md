---
title: "First Chart in Python"
section: "getting-started"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# First Chart in Python

## Summary

Create your first Chartexa chart in Python with just a few lines of code. The fluent builder API lets you chain series, axes, and styling into a single expressive statement.

---

## Quick Start

```python
import chartexa as cx

# One-liner: plot y-values with auto-generated x-values
cx.line([10, 20, 15, 30, 25]).save("quick.png")
```

That single line creates an 800x600 PNG with a line series, auto-ranged axes, and the default dark theme.

---

## The Chart Builder

For more control, use the `Chart` class directly:

```python
import chartexa as cx

chart = (
    cx.Chart(width=1200, height=600)
    .line(
        [0, 1, 2, 3, 4, 5, 6],
        [28.3, 29.1, 30.5, 31.2, 29.8, 28.6, 27.9],
        stroke="#F38BA8",
        thickness=2,
        label="Temperature (C)",
    )
    .x_axis(title="Day of Week")
    .y_axis(title="Temperature", range=(25, 35))
    .title("Weekly Temperature")
    .background("#1E1E2E")
    .theme("catppuccin_mocha")
)

chart.save("temperature.png")
```

Every method returns the chart, so calls chain naturally. The chart renders only when you call `.save()`, `.show()`, or `.to_bytes()`.

---

## Convenience Functions

Chartexa provides top-level functions for the most common chart types. Each returns a `Chart` that you can further customise:

```python
import chartexa as cx

# Scatter plot
cx.scatter([1, 2, 3, 4], [10, 40, 20, 30], marker="diamond").save("scatter.png")

# Bar chart
cx.column([0, 1, 2, 3], [50, 80, 45, 90], fill="#A6E3A1").save("bars.png")

# Mountain (area) chart
cx.mountain([0, 1, 2, 3, 4], [5, 15, 10, 20, 12], fill="#89B4FA").save("area.png")

# Candlestick chart
cx.candlestick(
    x=[0, 1, 2, 3],
    open=[100, 105, 102, 108],
    high=[110, 108, 107, 112],
    low=[98, 101, 99, 105],
    close=[105, 102, 106, 110],
).save("candles.png")
```

Available convenience functions: `line`, `scatter`, `bar`, `column`, `mountain`, `candlestick`, `band`, `heatmap`, `bubble`, `pie`, `donut`.

---

## Multiple Series

Add as many series as you need by chaining calls:

```python
import chartexa as cx
import math

x = [i * 0.1 for i in range(100)]
sin_y = [math.sin(v) for v in x]
cos_y = [math.cos(v) for v in x]

chart = (
    cx.Chart(width=1000, height=500)
    .line(x, sin_y, stroke="#F38BA8", label="sin(x)")
    .line(x, cos_y, stroke="#89B4FA", label="cos(x)")
    .title("Trigonometric Functions")
    .legend()
)

chart.save("trig.png")
```

---

## Output Formats

```python
# PNG (default)
chart.save("chart.png")

# JPEG with quality setting
chart.save_jpeg("chart.jpg", quality=85)

# Raw bytes (for web frameworks, APIs)
png_bytes = chart.to_bytes()
jpeg_bytes = chart.to_bytes(fmt="jpeg", quality=90)

# Interactive HTML
chart.save_html("chart.html")

# Embeddable HTML div (for Flask / Django templates)
html_snippet = chart.to_html_div()

# Display in Jupyter notebook
chart.show()
```

---

## Jupyter Notebooks

In Jupyter or VS Code notebooks, charts render inline automatically:

```python
import chartexa as cx

# Just return the chart from the last expression in a cell
cx.Chart().line([1, 2, 3], [10, 20, 15])
```

No `.show()` call needed -- Chartexa registers `_repr_html_` and `_repr_png_` methods that IPython picks up automatically.

---

## Next Steps

- [Chart Builder API](../python/chart-builder.md) -- full reference for all `Chart` methods
- [Image Export](../python/image-export.md) -- PNG, JPEG, HTML export options
- [Jupyter Integration](../python/jupyter.md) -- notebooks, widgets, live charts
- [Line Series](../chart-types/2d/line-series.md) -- deep dive into line chart options

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
