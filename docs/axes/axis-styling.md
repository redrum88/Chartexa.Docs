---
title: "Axis Styling"
section: "axes"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Axis Styling

## Summary

Customise axis appearance including grid lines, label rotation, and colours.

---

## Grid Lines

```python
chart = (
    cx.Chart()
    .line(x, y)
    .x_axis(grid_visible=True, grid_color="#333333", grid_thickness=0.5, grid_dash="dot")
    .y_axis(grid_visible=False)
)
```

| Property | Type | Default | Description |
|---|---|---|---|
| `grid_visible` | bool | `True` | Show/hide grid lines |
| `grid_color` | str / tuple | `None` | Grid line colour |
| `grid_thickness` | float | `1.0` | Grid line width |
| `grid_dash` | str | `None` | `"solid"`, `"dash"`, `"dot"` |

---

## Label Rotation

```python
chart.x_axis(type="category", labels=["Long Label A", "Long Label B", ...], label_rotation=45)
```

---

## Related

- [Axes Overview](overview.md)
- [Theming](../theming/overview.md) -- theme-level axis styling

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
