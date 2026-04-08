---
title: "Rubber Band Zoom"
section: "interaction"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Rubber Band Zoom

## Summary

The rubber band zoom modifier enables click-drag rectangle selection to zoom into a specific region. Uses `RubberBandZoomModifier` in the .NET engine.

---

## Quick Start

```python
chart = cx.Chart().line(x, y).rubber_band_zoom()
chart.save_html("rubber_band.html")
```

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `min_drag_px` | int | `5` | Minimum drag distance to trigger zoom |
| `enabled` | bool | `True` | Enable/disable |

---

## Related

- [Zoom & Pan](zoom-pan-modifier.md)
- [Interaction Overview](overview.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
