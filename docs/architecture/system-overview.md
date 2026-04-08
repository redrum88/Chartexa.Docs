---
title: "System Overview"
section: "architecture"
last_updated: "2024-06-08 15:42 UTC"
status: draft
---

# System Overview

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

Chartexa's architecture is organized into distinct layers: Core, Data, Rendering, Interaction, Theming, and Layout. This modular design enables flexible integration, efficient rendering, and robust customization for a wide range of charting scenarios.

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

!!! note
    Python integration requires the .NET 10 Runtime to be installed on your system.

---

## Quick Start

### C#

=== "C#"

```csharp
using Chartexa.Core;
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.DirectX12;

// Create a chart instance
var chart = new Chart
{
    Width = 800,
    Height = 400,
    RenderContext = new DirectX12RenderContext()
};

// Add axes
chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Time (s)" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Amplitude" });

// Add data series
var dataSeries = new XyDataSeries();
dataSeries.Append(
    new double[] { 0, 1, 2, 3, 4 },
    new double[] { 0, 2, 4, 3, 5 }
);

// Add renderable series
chart.Series.Add(new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(70, 130, 180),
    StrokeThickness = 2
});

// Render to file
chart.Save("output.png");
```

### Python

=== "Python"

```python
from chartexa import Chart

# Create and render a simple line chart
chart = (
    Chart(width=800, height=400)
    .line([0, 1, 2, 3, 4], [0, 2, 4, 3, 5], stroke="#4682B4", thickness=2)
    .background("#F5F5F7")
    .axis("x", title="Time (s)")
    .axis("y", title="Amplitude")
    .save("output.png")
)
```

---

## Concepts

Chartexa's system architecture is designed for modularity and performance. Each layer addresses a distinct aspect of charting:

- **Core Layer**: Manages chart composition, axes, and series orchestration.
- **Data Layer**: Handles data structures, series management, and streaming updates.
- **Rendering Layer**: Provides high-performance rendering via DirectX 12, Skia, or WPF backends.
- **Interaction Layer**: Enables user input, zooming, panning, and tooltips.
- **Theming Layer**: Controls visual appearance, color schemes, and style customization.
- **Layout Layer**: Supports dashboard composition, multi-chart arrangements, and responsive design.

This separation allows you to build charts that scale from simple plots to real-time dashboards, while maintaining clarity and extensibility.

Chartexa exists to bridge the gap between high-volume, real-time data visualization and developer productivity, offering seamless integration in both C# and Python environments.

---

## Basic Usage

### C#

=== "C#"

```csharp
using Chartexa.Core;
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.DirectX12;
using Chartexa.Theming;

// Initialize chart with DirectX12 rendering
var chart = new Chart
{
    Width = 1024,
    Height = 600,
    RenderContext = new DirectX12RenderContext(),
    Theme = ThemeEngine.Dark
};

// Configure axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Seconds", AutoRange = true };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Voltage", AutoRange = true };
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);

// Prepare data
var time = new double[] { 0, 1, 2, 3, 4, 5 };
var voltage = new double[] { 1.2, 2.5, 3.1, 2.8, 3.6, 4.0 };
var dataSeries = new XyDataSeries();
dataSeries.Append(time, voltage);

// Add line series
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(255, 99, 71), // Tomato
    StrokeThickness = 3
};
chart.Series.Add(lineSeries);

// Save chart
chart.Save("voltage_chart.png");
```

### Python

=== "Python"

```python
from chartexa import Chart

# Voltage vs Time chart with dark theme
chart = (
    Chart(width=1024, height=600)
    .line([0, 1, 2, 3, 4, 5], [1.2, 2.5, 3.1, 2.8, 3.6, 4.0], stroke="#FF6347", thickness=3)
    .background("#1C1C1E")
    .axis("x", title="Seconds", auto_range=True)
    .axis("y", title="Voltage", auto_range=True)
    .theme("dark")
    .save("voltage_chart.png")
)
```

---

## Configuration

Chartexa's architecture exposes key configuration points across its layers:

| Component        | Property           | Type           | Default         | Description                                            |
|------------------|-------------------|----------------|-----------------|--------------------------------------------------------|
| Chart            | Width             | int            | 800             | Pixel width of the chart                               |
| Chart            | Height            | int            | 400             | Pixel height of the chart                              |
| Chart            | RenderContext     | object         | DirectX12       | Rendering backend (DirectX12, Skia, WPF)               |
| Chart            | Theme             | ThemeEngine    | Light           | Visual theme (Light, Dark, Custom)                     |
| Axis             | Id                | string         | (auto)          | Unique axis identifier                                 |
| Axis             | AxisTitle         | string         | ""              | Axis label                                             |
| Axis             | AutoRange         | bool           | true            | Automatically fit data range                           |
| DataSeries       | Capacity          | int            | 10000           | Preallocated data capacity                             |
| RenderableSeries | StrokeColor       | ChartColor     | #4682B4         | Line color                                             |
| RenderableSeries | StrokeThickness   | int            | 2               | Line thickness in pixels                               |
| Layout           | Dashboard         | object         | None            | Multi-chart arrangement                                |

!!! tip "Performance Tip"
    For datasets exceeding 100,000 points, use `DirectX12RenderContext` and set `DataSeries.Capacity` to match your expected data volume.

---

## Examples

### Example 1: Real-Time Streaming Chart

=== "C#"

```csharp
using Chartexa.Core;
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.DirectX12;
using System.Threading;

// Setup chart for real-time updates
var chart = new Chart
{
    Width = 900,
    Height = 400,
    RenderContext = new DirectX12RenderContext()
};
chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Time (s)" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Sensor Value" });

var dataSeries = new XyDataSeries { Capacity = 50000 };
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(34, 139, 34), // Forest green
    StrokeThickness = 2
};
chart.Series.Add(lineSeries);

// Simulate streaming data
for (int i = 0; i < 1000; i++)
{
    double t = i * 0.1;
    double value = Math.Sin(t) + 0.5 * Math.Cos(2 * t);
    dataSeries.Append(t, value);
    if (i % 100 == 0)
        chart.Save($"stream_{i}.png");
    Thread.Sleep(10);
}
```

=== "Python"

```python
from chartexa import Chart
import numpy as np
import time

chart = (
    Chart(width=900, height=400)
    .axis("x", title="Time (s)")
    .axis("y", title="Sensor Value")
    .background("#F0FFF0")
)

x_values = []
y_values = []

for i in range(1000):
    t = i * 0.1
    value = np.sin(t) + 0.5 * np.cos(2 * t)
    x_values.append(t)
    y_values.append(value)
    if i % 100 == 0:
        chart.line(x_values, y_values, stroke="#228B22", thickness=2)
        chart.save(f"stream_{i}.png")
    time.sleep(0.01)
```

### Example 2: Multi-Chart Dashboard Layout

=== "C#"

```csharp
using Chartexa.Core;
using Chartexa.Core.Layout;
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.DirectX12;

// Create two charts
var chart1 = new Chart { Width = 400, Height = 300, RenderContext = new DirectX12RenderContext() };
chart1.Axes.Add(new NumericAxis { Id = "X1", AxisTitle = "Day" });
chart1.Axes.Add(new NumericAxis { Id = "Y1", AxisTitle = "Temperature (°C)" });
var tempSeries = new XyDataSeries();
tempSeries.Append(new double[] { 1, 2, 3, 4, 5 }, new double[] { 22, 24, 23, 25, 26 });
chart1.Series.Add(new FastLineRenderableSeries { DataSeries = tempSeries, StrokeColor = new ChartColor(255, 140, 0), StrokeThickness = 2 });

var chart2 = new Chart { Width = 400, Height = 300, RenderContext = new DirectX12RenderContext() };
chart2.Axes.Add(new NumericAxis { Id = "X2", AxisTitle = "Day" });
chart2.Axes.Add(new NumericAxis { Id = "Y2", AxisTitle = "Humidity (%)" });
var humiditySeries = new XyDataSeries();
humiditySeries.Append(new double[] { 1, 2, 3, 4, 5 }, new double[] { 60, 65, 63, 68, 70 });
chart2.Series.Add(new FastLineRenderableSeries { DataSeries = humiditySeries, StrokeColor = new ChartColor(30, 144, 255), StrokeThickness = 2 });

// Compose dashboard
var dashboard = new DashboardLayout();
dashboard.Add(chart1, 0, 0);
dashboard.Add(chart2, 0, 1);
dashboard.Save("dashboard.png");
```

=== "Python"

```python
from chartexa import Chart, Dashboard

# Temperature chart
temp_chart = (
    Chart(width=400, height=300)
    .line([1, 2, 3, 4, 5], [22, 24, 23, 25, 26], stroke="#FF8C00", thickness=2)
    .axis("x", title="Day")
    .axis("y", title="Temperature (°C)")
)

# Humidity chart
humidity_chart = (
    Chart(width=400, height=300)
    .line([1, 2, 3, 4, 5], [60, 65, 63, 68, 70], stroke="#1E90FF", thickness=2)
    .axis("x", title="Day")
    .axis("y", title="Humidity (%)")
)

# Compose dashboard
dashboard = Dashboard()
dashboard.add(temp_chart, row=0, col=0)
dashboard.add(humidity_chart, row=0, col=1)
dashboard.save("dashboard.png")
```

---

## Performance Notes

Chartexa's architecture is optimized for large-scale and real-time data visualization:

- **DirectX 12 Backend**: Supports rendering millions of points with minimal latency. Typical throughput exceeds 2 million points/sec on modern GPUs.
- **Data Layer**: Preallocated series and streaming APIs reduce GC overhead and enable smooth updates.
- **Python Integration**: Uses .NET interop for efficient cross-language calls; performance is comparable to native C# for most charting tasks.
- **Dashboard Layout**: Multi-chart composition incurs minimal overhead; each chart instance is independently managed and rendered.

!!! tip "Performance Tip"
    For maximum throughput, use DirectX 12 rendering and preallocate your data series capacity to match expected volume.

!!! warning
    Rendering performance may degrade if using WPF backend for charts with more than 100,000 points.

---

## When to Use

- When you need real-time charting for streaming data (e.g., sensor feeds, financial tick data)
- For large-scale visualization (millions of points, multi-series dashboards)
- When integrating charts seamlessly in C# or Python applications
- When custom theming and layout flexibility are required
- For applications requiring hardware-accelerated rendering (DirectX 12)

---

## Related

- [Rendering Backends](rendering/rendering-backends.md)
- [Data Series](../data/data-series.md)
- [Axes](../axes/axis-types.md)
- [Theming](../theming/theme-engine.md)
- [Dashboard Layout](../layout/dashboard-layout.md)

---

> **Last updated:** 2024-06-08 15:42 UTC | **Status:** draft