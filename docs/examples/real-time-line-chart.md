---
title: "Real-Time Line Chart"
section: "examples"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Real-Time Line Chart

## Summary

A streaming line chart that appends data in real time using a FIFO buffer. Suitable for sensor telemetry, live monitoring, and signal processing.

---

## Python

```python
import chartexa as cx
from chartexa import FifoBuffer, BatchUpdate
import math
import time

# Create a FIFO buffer with a 5000-point sliding window
buffer = FifoBuffer(capacity=5000)

# Pre-fill with initial data
for i in range(5000):
    t = i * 0.01
    buffer.append(t, math.sin(t * 2) + 0.5 * math.sin(t * 7.3))

# Create a themed chart
chart = (
    cx.Chart(width=1200, height=500)
    .line(buffer.x, buffer.y, stroke="#89B4FA", thickness=1.5, label="Signal")
    .x_axis(title="Time (s)")
    .y_axis(title="Amplitude", range=(-2, 2))
    .title("Real-Time Signal Monitor")
    .theme("catppuccin_mocha")
)

chart.save("realtime_line.png")
```

---

## Streaming with Live Updates

```python
from chartexa import NotebookLiveChart

live = NotebookLiveChart(width=1200, height=500, max_points=5000)
live.start()

# Simulate streaming data
for i in range(10000):
    t = i * 0.01
    live.append(t, math.sin(t * 2) + 0.3 * math.cos(t * 13.7))
    time.sleep(0.01)
```

---

## Related

- [FifoBuffer](../performance/optimization.md) -- sliding-window buffer
- [Line Series](../chart-types/2d/line-series.md) -- line configuration

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
