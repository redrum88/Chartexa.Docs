---
title: "Crosshair / Cursor Modifier"
section: "interaction"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Crosshair / Cursor Modifier

## Summary

The crosshair modifier draws horizontal and vertical lines that follow the mouse pointer. Can optionally snap to the nearest data point. Uses `CursorModifier` / `CrosshairModifier` in the .NET engine.

---

## Quick Start

```python
chart = cx.Chart().line(x, y).crosshair()
chart.save_html("crosshair.html")
```

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `snap_to_data` | bool | `False` | Snap crosshair to nearest data point |
| `show_x_line` | bool | `True` | Show vertical crosshair line |
| `show_y_line` | bool | `True` | Show horizontal crosshair line |
| `color` | str / tuple | `None` | Crosshair line colour |
| `thickness` | float | `1.0` | Line width |
| `dash_style` | str | `"dash"` | Line dash style |
| `enabled` | bool | `True` | Enable/disable |

---

## Related

- [Tooltips](tooltip-modifier.md)
- [Interaction Overview](overview.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
