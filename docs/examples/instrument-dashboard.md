---
title: "Instrument Dashboard"
section: "examples"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Instrument Dashboard

## Summary

A dashboard combining gauges, meters, and status indicators for industrial monitoring.

---

## Python

`python
import chartexa as cx
from chartexa import Dashboard

dash = Dashboard(width=1920, height=1080)

# Temperature gauge
temp = (
    cx.Chart(width=400, height=400)
    .pie([72, 28], colors=["#F38BA8", "#313244"])
    .title("Temperature: 72C")
    .theme("catppuccin_mocha")
)
dash.add(temp, x=0, y=0, width=480, height=540)

# Pressure gauge
pressure = (
    cx.Chart(width=400, height=400)
    .pie([85, 15], colors=["#89B4FA", "#313244"])
    .title("Pressure: 85%")
    .theme("catppuccin_mocha")
)
dash.add(pressure, x=480, y=0, width=480, height=540)

# Signal chart
import math
x = list(range(500))
y = [math.sin(i * 0.05) * (1 + 0.3 * math.sin(i * 0.01)) for i in x]

signal = (
    cx.Chart(width=960, height=540)
    .line(x, y, stroke="#A6E3A1", thickness=1.5)
    .title("Live Signal")
    .theme("catppuccin_mocha")
)
dash.add(signal, x=960, y=0, width=960, height=540)

# Bottom strip: volume bars
volumes = [50 + 30 * abs(math.sin(i * 0.1)) for i in range(20)]
vol_chart = (
    cx.Chart(width=1920, height=400)
    .column(list(range(20)), volumes, fill="#CBA6F7")
    .title("Throughput")
    .theme("catppuccin_mocha")
)
dash.add(vol_chart, x=0, y=540, width=1920, height=540)

dash.save("instrument_dashboard.png")
`

---

## Related

- [Gauges & Widgets](../chart-types/gauges-and-widgets/angular-gauge.md)
- [Layout Overview](../layout/overview.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
