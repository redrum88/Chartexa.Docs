---
title: "Custom Themes"
section: "theming"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Custom Themes

## Summary

Create custom themes using the `ChartTheme` class. Themes define colours for every visual element of the chart.

---

## Quick Start

```python
from chartexa import Chart, ChartTheme

theme = ChartTheme(
    background="#0D1117",
    surface="#161B22",
    text="#C9D1D9",
    grid="#21262D",
    series_colors=["#58A6FF", "#3FB950", "#D29922", "#F85149", "#BC8CFF"],
)

chart = Chart().line([1, 2, 3], [10, 20, 15]).theme(theme)
chart.save("custom_theme.png")
```

---

## ChartTheme Properties

| Property | Type | Description |
|---|---|---|
| `background` | str | Chart background colour |
| `surface` | str | Panel / surface colour |
| `text` | str | Label and title text colour |
| `grid` | str | Grid line colour |
| `series_colors` | list of str | Colour cycle for auto-coloured series |
| `axis_line` | str | Axis line colour |
| `tick_text` | str | Tick label colour |

---

## Colour Utilities

```python
from chartexa import Color, gradient, ColorCycle

# Named colours
red = Color.from_hex("#FF0000")
blue = Color(r=0, g=100, b=255)

# Gradient between two colours
colors = gradient("#FF0000", "#0000FF", steps=10)

# Auto-cycling colour palette
cycle = ColorCycle(["#F38BA8", "#89B4FA", "#A6E3A1"])
print(cycle[0], cycle[1], cycle[5])  # Wraps around
```

---

## Related

- [Theming Overview](overview.md) -- available presets
- [Theme Engine](theme-engine.md) -- internals

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
