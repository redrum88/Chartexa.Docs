---
title: "Custom Modifiers"
section: "interaction"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Custom Modifiers

## Summary

Build custom interaction behaviours by creating modifier instances and adding them to the chart via `chart.modifier()`.

---

## Using Modifier Classes Directly

`python
from chartexa import (
    ZoomPanModifier,
    RubberBandZoomModifier,
    CursorModifier,
    TooltipModifier,
    DataPointSelectionModifier,
    SeriesSelectionModifier,
)

# Create a customised zoom modifier
zoom = ZoomPanModifier(
    zoom_in_factor=0.9,
    zoom_out_factor=1.1,
    x_axis_only=True,
    enabled=True,
)

# Create a customised selection modifier
select = DataPointSelectionModifier(
    multi_select=True,
    selection_color=(255, 102, 0, 255),
    selection_size=12.0,
)

chart = (
    cx.Chart()
    .line(x, y)
    .modifier(zoom)
    .modifier(select)
)
`

---

## Related

- [Modifier Group](modifier-group.md)
- [Interaction Overview](overview.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
