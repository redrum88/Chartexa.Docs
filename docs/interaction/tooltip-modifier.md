---
title: "Tooltip Modifier"
section: "interaction"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Tooltip Modifier

## Summary

The tooltip modifier displays data values in a floating popup when hovering near data points. Supports single-point and multi-series tooltip modes. Uses `TooltipModifier` in the .NET engine.

---

## Quick Start

`python
chart = (
    cx.Chart()
    .line([1, 2, 3, 4], [10, 20, 15, 30], label="Series A")
    .line([1, 2, 3, 4], [15, 25, 10, 35], label="Series B")
    .tooltips()
)
chart.save_html("tooltips.html")
`

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `threshold_px` | float | `15.0` | Maximum distance to trigger tooltip (pixels) |
| `mode` | str | `"single"` | `"single"` (nearest point) or `"multi"` (all series) |
| `show_series_name` | bool | `True` | Include series name in tooltip |
| `color` | str / tuple | `None` | Tooltip background colour |
| `text_color` | str / tuple | `None` | Tooltip text colour |
| `font_size` | float | `12.0` | Tooltip font size |
| `enabled` | bool | `True` | Enable/disable |

---

## How It Works

The tooltip pipeline:

1. C# engine exports tooltip data via `ExportTooltipDataJson()`
2. Python tracks series labels in `_series_labels`
3. HTML renderer includes tooltip JavaScript
4. On mousemove, JS finds the nearest data point and renders the tooltip

---

## Related

- [Crosshair](cursor-modifier.md)
- [Interaction Overview](overview.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
