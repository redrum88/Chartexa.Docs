---
title: "Hit Testing"
section: "interaction"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Hit Testing

## Summary

Hit testing determines which data point or series is under the mouse cursor. It is used internally by the tooltip and selection modifiers.

---

## Concepts

When the mouse moves over the chart, the hit-testing system:

1. Transforms the mouse pixel position to data coordinates
2. Searches all visible series for the nearest data point
3. Returns the series index, data index, and distance

The `threshold_px` parameter on tooltips and selection modifiers controls the maximum hit-test distance.

---

## Related

- [Tooltip Modifier](tooltip-modifier.md)
- [Interaction Overview](overview.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
