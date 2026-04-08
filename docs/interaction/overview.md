---
title: "Interaction Overview"
section: "interaction"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Interaction Overview

## Summary

Chartexa provides interactive chart modifiers for zoom, pan, crosshair, tooltips, and data selection. These are available in HTML exports and Jupyter notebooks. In the Python API, add them via fluent methods on the `Chart` builder.

---

## Available Modifiers

| Modifier | Python Method | Description |
|---|---|---|
| Zoom & Pan | `chart.zoom_pan()` | Scroll to zoom, drag to pan |
| Rubber Band Zoom | `chart.rubber_band_zoom()` | Click-drag rectangle to zoom into a region |
| Crosshair | `chart.crosshair()` | Lines that follow the mouse pointer |
| Tooltips | `chart.tooltips()` | Show data values on hover |
| Data Selection | `chart.selection(mode="data_point")` | Click to select data points |
| Series Selection | `chart.selection(mode="series")` | Click to highlight a series |

---

## Quick Start

```python
import chartexa as cx

chart = (
    cx.Chart()
    .line([1, 2, 3, 4, 5], [10, 30, 20, 40, 25], label="Sensor A")
    .zoom_pan()
    .crosshair()
    .tooltips()
    .save_html("interactive.html")
)
```

---

## Combining Modifiers

Modifiers can be combined freely:

```python
chart = (
    cx.Chart()
    .line(x, y, label="Data")
    .zoom_pan()
    .crosshair(snap_to_data=True, color="#FF6600")
    .tooltips(mode="single", show_series_name=True)
    .selection(mode="data_point")
)
```

---

## Related

- [Zoom & Pan](zoom-pan-modifier.md)
- [Rubber Band Zoom](rubber-band-zoom.md)
- [Crosshair](cursor-modifier.md)
- [Tooltips](tooltip-modifier.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
