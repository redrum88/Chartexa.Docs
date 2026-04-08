---
title: "Grid Layout"
section: "layout"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Grid Layout

## Summary

Grid layout arranges charts in a rows-by-columns grid with automatic sizing. Use `subplots()` for the simplest API.

---

## Quick Start

`python
from chartexa import subplots

fig = subplots(rows=2, cols=3, width=1800, height=1200)

fig[0, 0].line([1, 2, 3], [10, 20, 15])
fig[0, 1].scatter([1, 2, 3], [5, 15, 10])
fig[0, 2].column([0, 1, 2], [30, 50, 40])
fig[1, 0].mountain([1, 2, 3], [20, 10, 25])
fig[1, 1].candlestick([0, 1, 2], [100, 105, 102], [110, 108, 107], [98, 101, 99], [105, 102, 106])
fig[1, 2].pie([35, 25, 20, 15, 5])

fig.save("grid.png")
`

---

## Related

- [Layout Overview](overview.md)
- [Absolute Layout](absolute-layout.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
