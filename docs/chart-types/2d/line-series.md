---
title: "Line Series"
section: "chart-types/2d"
last_updated: "2024-06-12 14:22 UTC"
status: draft
---

# Line Series

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `FastLineRenderableSeries` provides a high-performance line chart for visualizing continuous or discrete data. It supports millions of points, optional Catmull-Rom spline interpolation for smooth curves, and customizable styling. Use line series to display trends, signals, or time-series data efficiently.

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
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;
using Chartexa.Core.Drawing;

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (s)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Voltage (V)" };

// Create data
var time = new double[] { 0, 1, 2, 3, 4, 5 };
var voltage = new double[] { 0.2, 1.1, 2.3, 1.8, 2.9, 3.5 };
var dataSeries = new XyDataSeries();
dataSeries.Append(time, voltage);

// Create line series
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(34, 139, 34),   // Forest green
    StrokeThickness = 2
};

// Create chart and add series
var chart = new ChartSurface();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(lineSeries);
chart.SaveToFile("line_chart.png");
```

=== "Python"
```python
from chartexa import Chart

time = [0, 1, 2, 3, 4, 5]
voltage = [0.2, 1.1, 2.3, 1.8, 2.9, 3.5]

chart = (
    Chart(width=600, height=400)
    .line(time, voltage, stroke="#228B22", thickness=2)
    .x_axis(title="Time (s)")
    .y_axis(title="Voltage (V)")
    .background("#F8F8FF")
    .save("line_chart.png")
)
```

---

## Concepts

A line series connects a sequence of data points with straight or smoothed lines, making it ideal for visualizing trends, signals, and time-series data. Chartexa's `FastLineRenderableSeries` is optimized for large datasets, leveraging GPU acceleration via DirectX 12 to render millions of points interactively.

Spline interpolation (Catmull-Rom) can be enabled for smooth curves, which is useful for visualizing noisy data or emphasizing trends. Line series are commonly used in scientific, financial, and engineering applications to show changes over time or compare multiple signals.

Choose line series when you need to display continuous data, monitor real-time streams, or compare multiple datasets efficiently.

---

## Basic Usage

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;
using Chartexa.Core.Drawing;

// Example: Plot temperature over time

// Prepare axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Hour" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Temperature (°C)" };

// Prepare data
var hours = new double[] { 0, 1, 2, 3, 4, 5, 6, 7 };
var temp = new double[] { 15.2, 15.8, 16.0, 16.5, 17.1, 17.8, 18.0, 18.3 };
var dataSeries = new XyDataSeries();
dataSeries.Append(hours, temp);

// Configure line series
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(70, 130, 180),   // Steel blue
    StrokeThickness = 2,
    SplineEnabled = false
};

// Assemble chart
var chart = new ChartSurface();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(lineSeries);

// Save chart to file
chart.SaveToFile("temperature_line.png");
```

=== "Python"
```python
from chartexa import Chart

hours = [0, 1, 2, 3, 4, 5, 6, 7]
temp = [15.2, 15.8, 16.0, 16.5, 17.1, 17.8, 18.0, 18.3]

chart = (
    Chart(width=700, height=350)
    .line(hours, temp, stroke="#4682B4", thickness=2)
    .x_axis(title="Hour")
    .y_axis(title="Temperature (°C)")
    .background("#E6F2FF")
    .save("temperature_line.png")
)
```

---

## Configuration

| Property         | Type         | Default    | Description                                              |
|------------------|--------------|------------|----------------------------------------------------------|
| `DataSeries`     | XyDataSeries | (required) | Source data for the line series                          |
| `StrokeColor`    | ChartColor   | Black      | Line color                                               |
| `StrokeThickness`| int          | 1          | Line width in pixels                                     |
| `SplineEnabled`  | bool         | false      | Enables Catmull-Rom spline interpolation for smooth lines |
| `AntiAliasing`   | bool         | true       | Enables anti-aliased rendering                           |
| `Visible`        | bool         | true       | Toggles series visibility                                |
| `Opacity`        | float        | 1.0        | Line opacity (0.0-1.0)                                   |
| `ZIndex`         | int          | 0          | Rendering order among series                             |

!!! tip "Performance Tip"
    Disabling anti-aliasing (`AntiAliasing = false`) can improve rendering speed for extremely large datasets.

!!! warning
    Spline interpolation (`SplineEnabled = true`) increases GPU workload and may impact performance for datasets over 1 million points.

---

## Examples

### Example 1: Real-Time Signal Monitoring

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;
using Chartexa.Core.Drawing;

// Simulate real-time data streaming
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (ms)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Amplitude" };

var dataSeries = new XyDataSeries();
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(255, 0, 0),   // Red
    StrokeThickness = 2
};

var chart = new ChartSurface();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(lineSeries);

// Stream 1000 points
for (int i = 0; i < 1000; i++)
{
    double t = i * 0.01;
    double value = Math.Sin(2 * Math.PI * t) + 0.2 * Math.Cos(5 * Math.PI * t);
    dataSeries.Append(t, value);
}

// Save chart
chart.SaveToFile("realtime_signal.png");
```

=== "Python"
```python
from chartexa import Chart
import numpy as np

t = np.linspace(0, 10, 1000)
signal = np.sin(2 * np.pi * t) + 0.2 * np.cos(5 * np.pi * t)

chart = (
    Chart(width=800, height=400)
    .line(t, signal, stroke="#FF0000", thickness=2)
    .x_axis(title="Time (ms)")
    .y_axis(title="Amplitude")
    .background("#FFF5F5")
    .save("realtime_signal.png")
)
```

### Example 2: Spline-Interpolated Trend

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;
using Chartexa.Core.Drawing;

// Show smoothed trend with spline
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Day" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Stock Price ($)" };

var days = new double[] { 1, 2, 3, 4, 5, 6, 7 };
var price = new double[] { 100, 102, 101, 105, 107, 106, 110 };
var dataSeries = new XyDataSeries();
dataSeries.Append(days, price);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(0, 120, 215),   // Blue
    StrokeThickness = 3,
    SplineEnabled = true
};

var chart = new ChartSurface();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(lineSeries);
chart.SaveToFile("spline_trend.png");
```

=== "Python"
```python
from chartexa import Chart

days = [1, 2, 3, 4, 5, 6, 7]
price = [100, 102, 101, 105, 107, 106, 110]

chart = (
    Chart(width=600, height=350)
    .line(days, price, stroke="#0078D7", thickness=3, spline=True)
    .x_axis(title="Day")
    .y_axis(title="Stock Price ($)")
    .background("#F0F8FF")
    .save("spline_trend.png")
)
```

### Example 3: Multiple Line Series

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;
using Chartexa.Core.Drawing;

// Compare two signals
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (s)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Value" };

var t = new double[] { 0, 1, 2, 3, 4, 5 };
var y1 = new double[] { 10, 12, 15, 13, 16, 18 };
var y2 = new double[] { 8, 9, 11, 10, 12, 13 };

var ds1 = new XyDataSeries();
ds1.Append(t, y1);

var ds2 = new XyDataSeries();
ds2.Append(t, y2);

var series1 = new FastLineRenderableSeries
{
    DataSeries = ds1,
    StrokeColor = new ChartColor(255, 140, 0),   // Orange
    StrokeThickness = 2
};

var series2 = new FastLineRenderableSeries
{
    DataSeries = ds2,
    StrokeColor = new ChartColor(0, 191, 255),   // Deep sky blue
    StrokeThickness = 2
};

var chart = new ChartSurface();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(series1);
chart.RenderableSeries.Add(series2);
chart.SaveToFile("multi_line.png");
```

=== "Python"
```python
from chartexa import Chart

t = [0, 1, 2, 3, 4, 5]
y1 = [10, 12, 15, 13, 16, 18]
y2 = [8, 9, 11, 10, 12, 13]

chart = (
    Chart(width=650, height=350)
    .line(t, y1, stroke="#FF8C00", thickness=2)
    .line(t, y2, stroke="#00BFFF", thickness=2)
    .x_axis(title="Time (s)")
    .y_axis(title="Value")
    .background("#F9F9F9")
    .save("multi_line.png")
)
```

---

## Performance Notes

- The `FastLineRenderableSeries` is optimized for GPU rendering with DirectX 12, enabling interactive visualization of datasets up to 10 million points.
- Rendering speed depends on line thickness, anti-aliasing, and spline interpolation. For maximum throughput, use `StrokeThickness = 1`, `AntiAliasing = false`, and disable splines.
- Python integration leverages .NET runtime for backend performance; ensure .NET 10+ is installed for optimal results.

!!! note
    Python requires the .NET 10 Runtime to be installed for Chartexa chart rendering.

- On typical hardware (RTX 3060), rendering 1 million points with anti-aliasing enabled completes in under 50 ms.
- Spline interpolation increases GPU workload; avoid enabling it for real-time streaming of very large datasets.

---

## When to Use

- Visualizing time-series or signal data (e.g., sensor readings, stock prices)
- Monitoring real-time data streams
- Comparing multiple datasets on the same axes
- Displaying trends and patterns in scientific or engineering applications
- Rendering large datasets interactively

---

## Related

- [Scatter Series](scatter-series.md)
- [Column Series](column-series.md)
- [Axis Ranging](../axes/axis-ranging.md)
- [ThemeEngine](../../theming/theme-engine.md)

---

> **Last updated:** 2024-06-12 14:22 UTC | **Status:** draft