---
title: "Render Commands"
section: "rendering"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Render Commands

## Summary

Render commands are the internal drawing primitives that the chart surface emits and the renderer consumes. They abstract the drawing operations across all backends.

---

## Command Types

| Command | Description |
|---|---|
| DrawLine | Draw a line between two points |
| DrawPolyline | Draw a connected sequence of points |
| FillRectangle | Fill a rectangular region |
| DrawText | Render text at a position |
| DrawMarker | Draw a marker shape |
| SetClip | Set the clipping region |

---

## Related

- [Rendering Overview](overview.md)
- [Rendering Pipeline](../architecture/rendering-pipeline.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
