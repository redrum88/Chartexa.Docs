---
title: "IoT Sensor Dashboard"
section: "examples"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# IoT Sensor Dashboard

## Summary

A multi-sensor monitoring dashboard with real-time line charts, each connected to a different Y axis.

---

## Python

`python
import chartexa as cx
import math

x = list(range(200))
temp = [22 + 3 * math.sin(i * 0.05) + 0.5 * math.sin(i * 0.3) for i in x]
humidity = [65 + 10 * math.cos(i * 0.03) for i in x]
pressure = [1013 + 5 * math.sin(i * 0.02) for i in x]
light = [max(0, 500 + 200 * math.sin(i * 0.04)) for i in x]

chart = (
    cx.Chart(width=1400, height=700)
    .line(x, temp, stroke="#F38BA8", thickness=2, label="Temperature (C)", y_axis_id="TempAxis")
    .line(x, humidity, stroke="#89B4FA", thickness=2, label="Humidity (%)", y_axis_id="HumAxis")
    .line(x, pressure, stroke="#A6E3A1", thickness=1.5, label="Pressure (hPa)", y_axis_id="PressAxis")
    .line(x, light, stroke="#F9E2AF", thickness=1.5, label="Light (lux)", y_axis_id="LightAxis")
    .y_axis(id="TempAxis", title="Temp (C)", alignment="left")
    .y_axis(id="HumAxis", title="Humidity (%)", alignment="right")
    .x_axis(title="Sample")
    .title("IoT Sensor Dashboard")
    .subtitle("4-channel environmental monitor")
    .theme("catppuccin_mocha")
    .legend(position="top_center", orientation="horizontal")
    .crosshair()
    .tooltips(mode="multi")
)

chart.save("iot_dashboard.png")

# Also export as interactive HTML
chart.save_html("iot_dashboard.html")
`

!!! tip "Multi-Axis Binding"
    Use `y_axis_id` to bind each series to its own Y axis. This keeps scales independent. Only add as many visible Y axes as the chart can fit without clutter (typically 2 -- 3).

---

## Related

- [Multiple Axes](../axes/multiple-axes.md)
- [Tooltips](../interaction/tooltip-modifier.md)
- [Themes](../theming/overview.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
