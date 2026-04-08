---
title: "Layout Overview"
section: "layout"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Layout Overview

## Summary

Chartexa supports multi-chart layouts through the `Figure`, `Dashboard`, and `subplots()` APIs. Arrange multiple charts in grid or absolute-positioned layouts.

---

## Subplots (Quick Grid)

`python
import chartexa as cx
from chartexa import subplots

fig = subplots(rows=2, cols=2, width=1600, height=1200)

fig[0, 0].line([1, 2, 3], [10, 20, 15])
fig[0, 1].scatter([1, 2, 3], [30, 10, 25])
fig[1, 0].column([0, 1, 2], [50, 80, 65])
fig[1, 1].mountain([1, 2, 3], [5, 15, 10])

fig.save("subplots.png")
`

---

## Figure

`python
from chartexa import Figure

fig = Figure(width=1600, height=800)

chart1 = cx.Chart(width=800, height=800).line(x, y1)
chart2 = cx.Chart(width=800, height=800).scatter(x, y2)

fig.add(chart1, row=0, col=0)
fig.add(chart2, row=0, col=1)

fig.save("figure.png")
`

---

## Dashboard

`python
from chartexa import Dashboard

dash = Dashboard(width=1920, height=1080)
dash.add(chart1, x=0, y=0, width=960, height=540)
dash.add(chart2, x=960, y=0, width=960, height=540)
dash.add(chart3, x=0, y=540, width=1920, height=540)

dash.save("dashboard.png")
`

---

## Related

- [Grid Layout](grid-layout.md)
- [Absolute Layout](absolute-layout.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
