---
title: "Absolute Layout"
section: "layout"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Absolute Layout

## Summary

Absolute layout positions charts at specific pixel coordinates using the `Dashboard` class. Use this for custom dashboard arrangements where grid layout is too restrictive.

---

## Quick Start

`python
from chartexa import Dashboard, Chart

dash = Dashboard(width=1920, height=1080)

# Main chart (left 2/3)
main = Chart(width=1280, height=1080).line(x, y, label="Main")
dash.add(main, x=0, y=0, width=1280, height=1080)

# Sidebar chart (right 1/3, top half)
sidebar1 = Chart(width=640, height=540).pie([30, 70])
dash.add(sidebar1, x=1280, y=0, width=640, height=540)

# Sidebar chart (right 1/3, bottom half)
sidebar2 = Chart(width=640, height=540).column([0, 1, 2], [40, 60, 50])
dash.add(sidebar2, x=1280, y=540, width=640, height=540)

dash.save("dashboard.png")
`

---

## Related

- [Layout Overview](overview.md)
- [Grid Layout](grid-layout.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
