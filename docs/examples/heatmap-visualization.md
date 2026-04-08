---
title: "Heatmap Visualization"
section: "examples"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Heatmap Visualization

## Summary

A 2D heatmap with configurable colour palettes, suitable for correlation matrices, sensor grids, and scientific data.

---

## Python

```python
import chartexa as cx
import math

# Generate interference pattern
size = 50
data = []
for y in range(size):
    row = []
    for x in range(size):
        dx = x - size / 2
        dy = y - size / 2
        r = math.sqrt(dx * dx + dy * dy)
        row.append(math.sin(r * 0.5) * math.cos(r * 0.3))
    data.append(row)

chart = (
    cx.Chart(width=800, height=800)
    .heatmap(data, palette="viridis", min_value=-1.0, max_value=1.0)
    .title("Interference Pattern")
    .theme("dark")
)

chart.save("heatmap.png")
```

---

## Available Palettes

| Palette | Description |
|---|---|
| `"thermal"` | Black-red-yellow-white (default) |
| `"rainbow"` | Full spectrum |
| `"viridis"` | Perceptually uniform blue-green-yellow |
| `"inferno"` | Black-purple-red-yellow |
| `"diverging"` | Blue-white-red (for +/- values) |

---

## Related

- [Heatmap Series](../chart-types/2d/heatmap-series.md)
- [3D Surface Mesh](../chart-types/3d/surface-mesh.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
