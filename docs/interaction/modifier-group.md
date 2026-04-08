---
title: "Modifier Group"
section: "interaction"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Modifier Group

## Summary

Multiple modifiers can be combined on a single chart. They process events in order and can be individually enabled or disabled.

---

## Combining Modifiers

`python
chart = (
    cx.Chart()
    .line(x, y, label="Data")
    .zoom_pan()
    .crosshair(snap_to_data=True)
    .tooltips(mode="multi")
)
`

---

## Adding Custom Modifiers

`python
from chartexa import ZoomPanModifier, TooltipModifier

mod = ZoomPanModifier(x_axis_only=True, zoom_in_factor=0.9)
chart.modifier(mod)
`

---

## Inspecting Modifiers

`python
for mod in chart.modifiers:
    print(type(mod).__name__, mod.enabled)
`

---

## Related

- [Interaction Overview](overview.md)
- [Custom Modifiers](custom-modifiers.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
