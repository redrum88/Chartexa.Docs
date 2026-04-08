---
title: "Coordinate System"
section: "architecture"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Coordinate System

## Summary

Chartexa uses a standard Cartesian coordinate system where the X axis increases to the right and the Y axis increases upward. All data values are transformed from data space to pixel space by the axis system.

---

## Coordinate Spaces

| Space | Origin | Units | Description |
|---|---|---|---|
| **Data space** | Defined by data range | Data units (e.g. seconds, volts) | Where your data lives |
| **Pixel space** | Top-left of chart area | Pixels | Screen coordinates |
| **Normalised space** | (0, 0) to (1, 1) | Fraction | Used internally for layout |

---

## Transformation

The axis system transforms between spaces:


x_{pixel} = \frac{x_{data} - x_{min}}{x_{max} - x_{min}} \times width_{chart}



y_{pixel} = height_{chart} - \frac{y_{data} - y_{min}}{y_{max} - y_{min}} \times height_{chart}


The Y axis is flipped because pixel coordinates increase downward.

---

## Related

- [Axes Overview](../axes/overview.md)
- [Axis Ranging](../axes/axis-ranging.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
