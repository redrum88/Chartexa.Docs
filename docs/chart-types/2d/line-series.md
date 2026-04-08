---
title: "Line Series"
section: "chart-types/2d"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Line Series

## Summary

The line series renders XY data as a connected line. It supports solid, dashed, and spline curves with configurable stroke colour, thickness, and opacity. Backed by `FastLineRenderableSeries` in the .NET engine for GPU-accelerated rendering of millions of data points.

---

## Quick Start

=== "Python"

    ```python
    import chartexa as cx

    chart = cx.Chart().line(
        [0, 1, 2, 3, 4],
        [10, 25, 18, 30, 22],
        stroke="#F38BA8",
        thickness=2,
    )
    chart.save("line.png")
    ```

=== "C#"

    ```csharp
    var ds = new XyDataSeries();
    ds.Append(new double[] { 0, 1, 2, 3, 4 },
              new double[] { 10, 25, 18, 30, 22 });

    var rs = new FastLineRenderableSeries
    {
        DataSeries = ds,
        Stroke = new ChartColor(243, 139, 168),
        StrokeThickness = 2
    };
    surface.RenderableSeries.Add(rs);
    ```

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `stroke` | str / tuple | auto | Line colour (hex `"#RRGGBB"` or `(R, G, B)` tuple) |
| `thickness` | float | `1.5` | Line width in pixels |
| `dash` | str | `None` | `"solid"`, `"dash"`, `"dot"`, `"dash_dot"`, `"dash_dot_dot"` |
| `opacity` | float | `1.0` | Line opacity (0.0 -- 1.0) |
| `spline` | bool | `False` | Enable Catmull-Rom spline interpolation |
| `spline_segments` | int | `16` | Interpolated segments per data point pair |
| `label` | str | `None` | Series name for legend and tooltips |

---

## Examples

### Dashed Lines

```python
import chartexa as cx

chart = (
    cx.Chart(width=1000, height=500)
    .line([0, 1, 2, 3, 4], [10, 20, 15, 25, 18], stroke="#F38BA8", dash="solid", label="Solid")
    .line([0, 1, 2, 3, 4], [12, 22, 17, 27, 20], stroke="#89B4FA", dash="dash", label="Dashed")
    .line([0, 1, 2, 3, 4], [14, 24, 19, 29, 22], stroke="#A6E3A1", dash="dot", label="Dotted")
    .legend()
)
chart.save("dash_styles.png")
```

### Spline Interpolation

```python
chart = cx.Chart().line(
    [0, 1, 2, 3, 4, 5],
    [10, 35, 20, 40, 15, 30],
    stroke="#CBA6F7",
    thickness=2.5,
    spline=True,
    spline_segments=32,
)
chart.save("spline.png")
```

### Multi-Axis Line Chart

```python
import math

x = list(range(100))
temp = [20 + 5 * math.sin(i * 0.1) for i in x]
pressure = [1013 + 10 * math.cos(i * 0.05) for i in x]

chart = (
    cx.Chart(width=1200, height=600)
    .line(x, temp, stroke="#F38BA8", label="Temperature", y_axis_id="TempAxis")
    .line(x, pressure, stroke="#89B4FA", label="Pressure", y_axis_id="PressureAxis")
    .y_axis(id="TempAxis", title="Temperature (C)", alignment="left")
    .y_axis(id="PressureAxis", title="Pressure (hPa)", alignment="right")
    .legend()
)
chart.save("multi_axis.png")
```

---

## Performance Notes

The line series uses `FastLineRenderableSeries` in the .NET engine, which batches draw calls and leverages the DirectX 12 pipeline. Rendering 1 million points at 60 FPS is typical on a modern GPU.

For datasets exceeding 10 million points, combine with LTTB downsampling:

```python
from chartexa import lttb_downsample

x_ds, y_ds = lttb_downsample(x, y, target_points=5000)
chart = cx.Chart().line(x_ds, y_ds)
```

---

## When to Use

- Time series data (sensor readings, stock prices, telemetry)
- Continuous function plots (sin, cos, signal processing)
- Trend lines and forecasts
- Any dataset where the order of X values matters

---

## Related

- [Scatter Series](scatter-series.md) -- unconnected point plots
- [Mountain Series](mountain-series.md) -- filled area under a line
- [Band Series](band-series.md) -- fill between two lines
- [Digital Signal](digital-signal.md) -- step-function lines

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
