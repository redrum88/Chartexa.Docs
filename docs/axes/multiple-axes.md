---
title: "Multiple Axes"
section: "axes"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Multiple Axes

## Summary

Charts can have multiple X and Y axes. Each series binds to a specific axis pair via `x_axis_id` and `y_axis_id`. This enables dual-Y, secondary-X, and multi-scale charts.

---

## Dual Y-Axis

```python
import chartexa as cx

x = list(range(50))
temp = [20 + i * 0.1 for i in x]
pressure = [1013 + i * 0.5 for i in x]

chart = (
    cx.Chart(width=1200, height=600)
    .line(x, temp, stroke="#F38BA8", label="Temperature", y_axis_id="TempAxis")
    .line(x, pressure, stroke="#89B4FA", label="Pressure", y_axis_id="PressAxis")
    .y_axis(id="TempAxis", title="Temperature (C)", alignment="left")
    .y_axis(id="PressAxis", title="Pressure (hPa)", alignment="right")
    .legend()
)
chart.save("dual_y.png")
```

---

## Secondary X-Axis

```python
chart = (
    cx.Chart()
    .line(x_metric, y, x_axis_id="MetricAxis")
    .secondary_x_axis(title="Imperial", id="ImperialAxis")
)
```

The `secondary_x_axis()` and `secondary_y_axis()` convenience methods default to top/right alignment.

---

## Related

- [Axes Overview](overview.md)
- [Chart Builder API](../python/chart-builder.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
