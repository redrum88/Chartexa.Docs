---
title: "Axis Ranging"
section: "axes"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Axis Ranging

## Summary

Axis ranging controls which portion of the data is visible. Chartexa supports auto-ranging (fit all data), fixed ranges, and padded ranges.

---

## Auto-Range (Default)

By default, axes auto-range to fit all attached series data with a 5% padding (`grow_by=0.05`):

`python
# Auto-ranges to fit data with default 5% padding
chart = cx.Chart().line(x, y)
`

---

## Fixed Range

`python
chart = (
    cx.Chart()
    .line(x, y)
    .y_axis(range=(0, 100))   # Fix Y axis from 0 to 100
)
`

---

## Grow By (Padding)

`python
chart = (
    cx.Chart()
    .line(x, y)
    .y_axis(grow_by=0.1)   # 10% padding on each side
)
`

---

## Related

- [Axes Overview](overview.md)
- [Zoom Pan Modifier](../interaction/zoom-pan-modifier.md) -- interactive range changes

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
