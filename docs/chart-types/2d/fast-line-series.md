---
title: "Fast Line Series"
section: "chart-types/2d"
last_updated: "2024-06-12 15:32 UTC"
status: draft
---

# Fast Line Series

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The FastLineRenderableSeries displays a connected sequence of data points as a line, optimized for rendering large datasets and real-time updates. Use this series to visualize trends, signals, or time-series data where performance and responsiveness are critical.

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
using Chartexa.ChartTypes;
using Chartexa.Rendering;

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (s)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Voltage (V)" };

// Create data series
var dataSeries = new XyDataSeries();
dataSeries.Append(
    new double[] { 0, 1, 2, 3, 4, 5 },
    new double[] { 0.0, 1.2, 0.9, 1.5, 1.1, 0.8 }
);

// Create line series
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(34, 139, 34),   // Forest green
    StrokeThickness = 2
};

// Add to chart
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(lineSeries);
chart.Render();
```

=== "Python"
```python
from chartexa import Chart

# Time (s) and Voltage (V) data
x = [0, 1, 2, 3, 4, 5]
y = [0.0, 1.2, 0.9, 1.5, 1.1, 0.8]

chart = (
    Chart(width=600, height=400)
    .line(x, y, stroke="#228B22", thickness=2)  # Forest green
    .x_axis(title="Time (s)")
    .y_axis(title="Voltage (V)")
    .save("line_chart.png")
)
```

---

## Concepts

The Fast Line Series is designed for efficient rendering of connected data points as a continuous line. It leverages GPU acceleration (DirectX 12) to handle datasets with hundreds of thousands or millions of points without compromising interactivity.

Use FastLineRenderableSeries when you need to:
- Visualize time-series, sensor signals, or trends over time.
- Render large datasets with minimal latency.
- Stream real-time data and update the chart dynamically.

Unlike standard line series, FastLineRenderableSeries prioritizes performance, making it suitable for applications such as scientific visualization, financial charting, and industrial monitoring.

---

## Basic Usage

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using Chartexa.Rendering;

// Generate sample data: Sine wave
var sampleCount = 1000;
var xValues = new double[sampleCount];
var yValues = new double[sampleCount];
for (int i = 0; i < sampleCount; i++)
{
    xValues[i] = i * 0.01;
    yValues[i] = Math.Sin(xValues[i] * 2 * Math.PI);
}

// Set up axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (s)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Amplitude" };

// Create data series
var dataSeries = new XyDataSeries();
dataSeries.Append(xValues, yValues);

// Configure line series
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(70, 130, 180), // Steel blue
    StrokeThickness = 2,
    AntiAliasing = true
};

// Build chart
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(lineSeries);
chart.Render();
```

=== "Python"
```python
import numpy as np
from chartexa import Chart

# Generate sine wave data
x = np.linspace(0, 10, 1000)
y = np.sin(x * 2 * np.pi)

chart = (
    Chart(width=800, height=400)
    .line(x, y, stroke="#4682B4", thickness=2, antialias=True)  # Steel blue
    .x_axis(title="Time (s)")
    .y_axis(title="Amplitude")
    .background("#F5F5F5")
    .save("sine_wave.png")
)
```

---

## Configuration

| Property        | Type         | Default      | Description                                   |
|-----------------|-------------|--------------|-----------------------------------------------|
| DataSeries      | XyDataSeries | (required)   | The data to render as a line.                 |
| StrokeColor     | ChartColor   | Black        | Line color.                                   |
| StrokeThickness | int          | 1            | Line width in pixels.                         |
| AntiAliasing    | bool         | false        | Enables smoother line rendering.              |
| DashPattern     | int[]        | null         | Custom dash pattern for the line.             |
| Opacity         | double       | 1.0          | Line opacity (0.0 - 1.0).                     |
| IsVisible       | bool         | true         | Controls series visibility.                   |
| Name            | string       | ""           | Series name (for legend/tooltips).            |

!!! tip "Performance Tip"
    For datasets exceeding 500,000 points, enable DirectX 12 rendering and avoid using dash patterns for maximum throughput.

---

## Examples

### Example 1: Real-Time Streaming

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using Chartexa.Rendering;

// Simulate real-time data streaming
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (s)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Temperature (°C)" };

var dataSeries = new XyDataSeries();
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(255, 69, 0), // Orange-red
    StrokeThickness = 2
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(lineSeries);
chart.Render();

// Simulate streaming: append new data every second
for (int t = 0; t < 60; t++)
{
    double temp = 20 + 5 * Math.Sin(t * 0.1);
    dataSeries.Append(t, temp);
    chart.Update();
    System.Threading.Thread.Sleep(1000);
}
```

=== "Python"
```python
import time
import numpy as np
from chartexa import Chart

x = []
y = []

chart = (
    Chart(width=600, height=300)
    .line(x, y, stroke="#FF4500", thickness=2)  # Orange-red
    .x_axis(title="Time (s)")
    .y_axis(title="Temperature (°C)")
    .show()
)

for t in range(60):
    temp = 20 + 5 * np.sin(t * 0.1)
    x.append(t)
    y.append(temp)
    chart.update_line(x, y)
    time.sleep(1)
```

!!! example "Real-Time Streaming"
    The Fast Line Series supports dynamic updates for real-time data visualization. Append new points and call `Update()` (C#) or `update_line()` (Python) to refresh the chart.

---

### Example 2: Multiple Series Comparison

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using Chartexa.Rendering;

// Generate two signals
var xValues = Enumerable.Range(0, 500).Select(i => i * 0.02).ToArray();
var y1 = xValues.Select(x => Math.Sin(x)).ToArray();
var y2 = xValues.Select(x => Math.Cos(x)).ToArray();

var ds1 = new XyDataSeries();
ds1.Append(xValues, y1);

var ds2 = new XyDataSeries();
ds2.Append(xValues, y2);

var line1 = new FastLineRenderableSeries
{
    DataSeries = ds1,
    StrokeColor = new ChartColor(0, 0, 255), // Blue
    StrokeThickness = 2,
    Name = "Sine"
};

var line2 = new FastLineRenderableSeries
{
    DataSeries = ds2,
    StrokeColor = new ChartColor(255, 0, 0), // Red
    StrokeThickness = 2,
    Name = "Cosine"
};

var chart = new Chart();
chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "X" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Value" });
chart.Series.Add(line1);
chart.Series.Add(line2);
chart.Render();
```

=== "Python"
```python
import numpy as np
from chartexa import Chart

x = np.linspace(0, 10, 500)
y1 = np.sin(x)
y2 = np.cos(x)

chart = (
    Chart(width=700, height=350)
    .line(x, y1, stroke="#0000FF", thickness=2, name="Sine")  # Blue
    .line(x, y2, stroke="#FF0000", thickness=2, name="Cosine")  # Red
    .x_axis(title="X")
    .y_axis(title="Value")
    .legend(position="top-right")
    .save("multi_series.png")
)
```

---

### Example 3: Custom Line Style

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using Chartexa.Rendering;

// Generate data
var x = Enumerable.Range(0, 100).Select(i => i * 0.1).ToArray();
var y = x.Select(val => Math.Exp(-val / 10) * Math.Sin(val)).ToArray();

var ds = new XyDataSeries();
ds.Append(x, y);

var dashedLine = new FastLineRenderableSeries
{
    DataSeries = ds,
    StrokeColor = new ChartColor(128, 0, 128), // Purple
    StrokeThickness = 3,
    DashPattern = new int[] { 6, 2 }, // Dash: 6px, Gap: 2px
    Opacity = 0.7
};

var chart = new Chart();
chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Time" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Damped Signal" });
chart.Series.Add(dashedLine);
chart.Render();
```

=== "Python"
```python
import numpy as np
from chartexa import Chart

x = np.arange(0, 10, 0.1)
y = np.exp(-x / 10) * np.sin(x)

chart = (
    Chart(width=600, height=300)
    .line(
        x, y,
        stroke="#800080",
        thickness=3,
        dash=[6, 2],
        opacity=0.7,
        name="Damped"
    )
    .x_axis(title="Time")
    .y_axis(title="Damped Signal")
    .save("damped_signal.png")
)
```

---

## Performance Notes

FastLineRenderableSeries is optimized for GPU rendering and can handle millions of points with minimal frame latency. On modern hardware (DirectX 12), rendering 1 million points typically completes in under 30 ms per frame.

- AntiAliasing increases visual quality but may reduce throughput for very large datasets.
- Dash patterns are rendered efficiently but may impact performance above 500K points.
- Python integration uses .NET runtime; ensure .NET 10 is installed for best performance.

!!! note
    Python requires the .NET 10 Runtime to be installed. 

---

## When to Use

- Visualizing time-series or signal data with thousands to millions of points.
- Streaming real-time sensor or financial data.
- Comparing multiple trends on the same chart.
- Rendering large datasets where responsiveness is critical.
- Creating scientific, engineering, or monitoring dashboards.

---

## Related


---

> **Last updated:** 2024-06-12 15:32 UTC | **Status:** draft
