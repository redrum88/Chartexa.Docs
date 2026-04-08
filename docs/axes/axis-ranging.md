---
title: "Axis Ranging"
section: "axes"
last_updated: "2024-06-13 15:42 UTC"
status: draft
---

# Axis Ranging

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

Axis ranging controls which portion of your data is visible on the chart. Chartexa provides three primary mechanisms: `AutoRange` (automatic fit to data), `VisibleRange` (manual control), and `ZoomToFit` (programmatic adjustment). These features allow you to focus on relevant data, enable interactive zooming, and ensure optimal presentation for both static and streaming datasets.

---

## Installation

### .NET (NuGet)

```bash
dotnet add package Chartexa.Core
```

### Python (PyPI)

```bash
pip install chartexa
```

---

## Quick Start

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering;

// Create axes with AutoRange enabled
var xAxis = new NumericAxis
{
    Id = "X",
    AxisTitle = "Time (s)",
    AutoRange = AxisAutoRange.Always
};

var yAxis = new NumericAxis
{
    Id = "Y",
    AxisTitle = "Voltage (V)",
    AutoRange = AxisAutoRange.Once
};

// Create data series and append data
var dataSeries = new XyDataSeries();
dataSeries.Append(
    new double[] { 0, 1, 2, 3, 4, 5 },
    new double[] { 0.2, 1.1, 2.8, 2.4, 3.9, 5.0 }
);

// Render chart (minimal example)
var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(new FastLineRenderableSeries { DataSeries = dataSeries });
```

=== "Python"
```python
from chartexa import Chart

# Data values
x = [0, 1, 2, 3, 4, 5]
y = [0.2, 1.1, 2.8, 2.4, 3.9, 5.0]

# Create chart with AutoRange enabled
chart = (
    Chart(width=600, height=300)
    .axis("x", type="numeric", title="Time (s)", autorange="always")
    .axis("y", type="numeric", title="Voltage (V)", autorange="once")
    .line(x, y, stroke="#4682B4", thickness=2)
    .save("axis_ranging_quickstart.png")
)
```

---

## Concepts

Axis ranging determines the minimum and maximum values displayed on each axis, directly affecting which data points are visible. Chartexa supports three main ranging modes:

- **AutoRange**: Automatically adjusts the axis range to fit the data. Useful for charts where data changes frequently, such as real-time or streaming plots.
- **VisibleRange**: Lets you manually set the axis range. This is ideal when you want to focus on a specific interval or synchronize axes across multiple charts.
- **ZoomToFit**: Programmatically adjusts the axis to fit all data, typically used in response to user actions (e.g., a "Reset Zoom" button).

These mechanisms are essential for interactive charting, ensuring users can explore, zoom, and pan data efficiently. Axis ranging also supports scenarios like fixed scientific scales, financial charting, and synchronized dashboards.

---

## Basic Usage

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering;

// Create axes with manual and automatic ranging
var xAxis = new NumericAxis
{
    Id = "X",
    AxisTitle = "Frequency (Hz)",
    AutoRange = AxisAutoRange.Never,
    VisibleRange = new AxisRange(100, 500)
};

var yAxis = new NumericAxis
{
    Id = "Y",
    AxisTitle = "Amplitude",
    AutoRange = AxisAutoRange.Always
};

// Data series
var dataSeries = new XyDataSeries();
dataSeries.Append(
    new double[] { 100, 200, 300, 400, 500, 600 },
    new double[] { 0.5, 1.2, 2.0, 1.5, 0.8, 0.3 }
);

// Chart setup
var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(new FastLineRenderableSeries { DataSeries = dataSeries });

// Zoom to fit all data on X axis
xAxis.ZoomToFit();
```

=== "Python"
```python
from chartexa import Chart

# Data values
freq = [100, 200, 300, 400, 500, 600]
amp = [0.5, 1.2, 2.0, 1.5, 0.8, 0.3]

# Manual visible range for X axis, AutoRange for Y axis
chart = (
    Chart(width=700, height=350)
    .axis("x", type="numeric", title="Frequency (Hz)", visible_range=(100, 500), autorange="never")
    .axis("y", type="numeric", title="Amplitude", autorange="always")
    .line(freq, amp, stroke="#228B22", thickness=2)
    .save("axis_ranging_basic.png")
)

# Programmatic zoom to fit (after adding data)
chart.zoom_to_fit(axis="x")
```

---

## Configuration

| Property      | Type                | Default        | Description                                                       |
|---------------|---------------------|----------------|-------------------------------------------------------------------|
| `AutoRange`   | `AxisAutoRange`     | `Never`        | Controls automatic ranging: `Never`, `Once`, `Always`.            |
| `VisibleRange`| `AxisRange`         | `null`         | Manually sets min/max values displayed on axis.                   |
| `ZoomToFit()` | Method              | N/A            | Adjusts axis to fit all current data.                             |
| `MinRange`    | `double`            | `null`         | Minimum allowed range (prevents excessive zoom-in).               |
| `MaxRange`    | `double`            | `null`         | Maximum allowed range (prevents excessive zoom-out).              |
| `GrowBy`      | `AxisGrowBy`        | `(0, 0)`       | Adds padding to axis range as fraction of data range.             |

---

## Examples

### Example 1: Real-Time Data with AutoRange

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering;
using System.Threading;

// Real-time chart with AutoRange Always
var xAxis = new NumericAxis
{
    Id = "X",
    AxisTitle = "Time (s)",
    AutoRange = AxisAutoRange.Always
};

var yAxis = new NumericAxis
{
    Id = "Y",
    AxisTitle = "Temperature (°C)",
    AutoRange = AxisAutoRange.Always
};

var dataSeries = new XyDataSeries();
var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(new FastLineRenderableSeries { DataSeries = dataSeries });

// Simulate streaming data
for (int t = 0; t < 10; t++)
{
    double temp = 20 + 5 * Math.Sin(t);
    dataSeries.Append(t, temp);
    chart.Refresh();
    Thread.Sleep(500);
}
```

=== "Python"
```python
from chartexa import Chart
import math
import time

x = []
y = []

chart = (
    Chart(width=600, height=300)
    .axis("x", type="numeric", title="Time (s)", autorange="always")
    .axis("y", type="numeric", title="Temperature (°C)", autorange="always")
    .line([], [], stroke="#FF6347", thickness=2)
    .show()
)

# Streaming data simulation
for t in range(10):
    temp = 20 + 5 * math.sin(t)
    x.append(t)
    y.append(temp)
    chart.update_line(x, y)
    time.sleep(0.5)
```

!!! tip "Performance Tip"
    Use `AutoRange = AxisAutoRange.Once` for large static datasets to avoid unnecessary recalculation.

---

### Example 2: Fixed Range for Scientific Analysis

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering;

// Fixed axis range for scientific chart
var xAxis = new NumericAxis
{
    Id = "X",
    AxisTitle = "Wavelength (nm)",
    AutoRange = AxisAutoRange.Never,
    VisibleRange = new AxisRange(400, 700)
};

var yAxis = new NumericAxis
{
    Id = "Y",
    AxisTitle = "Intensity",
    AutoRange = AxisAutoRange.Never,
    VisibleRange = new AxisRange(0, 100)
};

var dataSeries = new XyDataSeries();
dataSeries.Append(
    new double[] { 410, 450, 500, 550, 600, 650, 690 },
    new double[] { 10, 35, 80, 60, 40, 20, 5 }
);

var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(new FastLineRenderableSeries { DataSeries = dataSeries });
```

=== "Python"
```python
from chartexa import Chart

wavelength = [410, 450, 500, 550, 600, 650, 690]
intensity = [10, 35, 80, 60, 40, 20, 5]

chart = (
    Chart(width=800, height=400)
    .axis("x", type="numeric", title="Wavelength (nm)", visible_range=(400, 700), autorange="never")
    .axis("y", type="numeric", title="Intensity", visible_range=(0, 100), autorange="never")
    .line(wavelength, intensity, stroke="#6A5ACD", thickness=2)
    .save("axis_ranging_fixed.png")
)
```

!!! warning
    Setting `AutoRange = Never` requires you to specify `VisibleRange`. Otherwise, the axis may not display any data.

---

### Example 3: ZoomToFit Button for User Interaction

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering;
using System.Windows.Forms;

// Chart with ZoomToFit functionality
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Index" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Value" };

var dataSeries = new XyDataSeries();
dataSeries.Append(
    new double[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 },
    new double[] { 10, 15, 8, 12, 20, 18, 25, 22, 28, 30 }
);

var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(new FastLineRenderableSeries { DataSeries = dataSeries });

// Add a button to zoom to fit
var zoomButton = new Button { Text = "Zoom To Fit" };
zoomButton.Click += (s, e) => xAxis.ZoomToFit();
```

=== "Python"
```python
from chartexa import Chart

x = list(range(1, 11))
y = [10, 15, 8, 12, 20, 18, 25, 22, 28, 30]

chart = (
    Chart(width=600, height=300)
    .axis("x", type="numeric", title="Index")
    .axis("y", type="numeric", title="Value")
    .line(x, y, stroke="#20B2AA", thickness=2)
    .show()
)

# Zoom to fit all data (e.g., on button click)
chart.zoom_to_fit(axis="x")
```

!!! example "Real-Time Streaming"
    Use `AutoRange = Always` for axes in streaming charts to ensure new data is always visible.

---

## Performance Notes

- **AutoRange = Always** recalculates axis range every time data changes; this can impact performance for charts with frequent updates or very large datasets.
- **AutoRange = Once** fits the axis to data only at initialization, minimizing overhead for static charts.
- **VisibleRange** is lightweight and incurs no runtime cost unless changed programmatically.
- For datasets exceeding 1 million points, prefer manual ranging or `AutoRange = Once` to avoid unnecessary recomputation.
- DirectX 12 backend efficiently handles range updates, but UI responsiveness may depend on chart complexity and update rate.

---

## When to Use

- Interactive charts requiring zoom/pan functionality.
- Real-time or streaming data visualization.
- Dashboards with synchronized axis ranges across multiple charts.
- Scientific, financial, or engineering charts with fixed scales.
- Applications needing programmatic control over axis visibility (e.g., "Reset Zoom" buttons).

---

## Related

- [Numeric Axis](numeric-axis.md)
- [Datetime Axis](datetime-axis.md)
- [Zoom and Pan Interaction](../interaction/zoom-pan.md)
- [ChartSurface API](../core/chartsurface.md)

---

> **Last updated:** 2024-06-13 15:42 UTC | **Status:** draft