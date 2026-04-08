---
title: "Zoom & Pan Modifier"
section: "interaction"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Zoom & Pan Modifier

## Summary

The zoom & pan modifier enables scroll-to-zoom and drag-to-pan interaction. Uses `ZoomPanModifier` in the .NET engine.

---

## Quick Start

`python
chart = cx.Chart().line(x, y).zoom_pan()
chart.save_html("zoomable.html")
`

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `zoom_in_factor` | float | `0.8` | Scale factor per scroll tick (< 1 = zoom in) |
| `zoom_out_factor` | float | `1.25` | Scale factor per scroll tick (> 1 = zoom out) |
| `x_axis_only` | bool | `False` | Restrict zoom to X axis |
| `y_axis_only` | bool | `False` | Restrict zoom to Y axis |
| `enabled` | bool | `True` | Enable/disable |

---

## Related

- [Rubber Band Zoom](rubber-band-zoom.md)
- [Interaction Overview](overview.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
