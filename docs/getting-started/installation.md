---
title: "Installation"
section: "getting-started"
last_updated: "2024-06-11 13:42 UTC"
status: draft
last_updated: "2026-04-08 02:18 UTC"
status: placeholder
---

# Installation

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

This page describes how to install Chartexa for both .NET (C#) and Python environments, including prerequisites, package installation, and environment setup. Follow these instructions to get started with Chartexa in your preferred language.

---

## Installation

### Prerequisites

#### .NET (C#)
- .NET 6.0 or later (recommended .NET 10 for maximum compatibility)
- Windows 10 or later (DirectX 12 rendering requires Windows)
- Visual Studio 2022 or later, or any compatible IDE

#### Python
- Python 3.8 or later (64-bit)
- Windows 10 or later (DirectX 12 rendering requires Windows)
- .NET 10 Runtime installed (required for Python integration)

!!! note
    Chartexa's Python integration leverages .NET via pythonnet. Ensure the .NET 10 Runtime is installed and available in your PATH.

#### DirectX 12
- DirectX 12-capable GPU and drivers (for hardware-accelerated rendering)

---

### .NET (NuGet)

Install Chartexa Core via NuGet:

```bash
dotnet add package Chartexa.Core
```

Or, in Visual Studio:
- Right-click your project > Manage NuGet Packages > Search "Chartexa.Core" > Install

---

### Python (PyPI)

Install Chartexa via pip:

```bash
pip install chartexa
```

!!! warning
    The `chartexa` Python package requires the .NET 10 Runtime. Download from [Microsoft .NET Downloads](https://dotnet.microsoft.com/en-us/download/dotnet/10.0) and install before using Chartexa in Python.

---

## Quick Start

### C#

=== "C#"
```csharp
using Chartexa.Core;
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.RenderableSeries;

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (s)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Temperature (°C)" };

// Create data series
var dataSeries = new XyDataSeries();
dataSeries.Append(
    new double[] { 0, 1, 2, 3, 4 },
    new double[] { 22.5, 23.0, 23.8, 24.2, 24.0 }
);

// Create renderable series
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(255, 99, 71), // Tomato
    StrokeThickness = 2
};

// Create chart and add components
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(lineSeries);

// Show chart window
chart.Show();
```

### Python

=== "Python"
```python
from chartexa import Chart

# Sample data: time (s) vs temperature (°C)
time = [0, 1, 2, 3, 4]
temperature = [22.5, 23.0, 23.8, 24.2, 24.0]

chart = (
    Chart(width=640, height=400)
    .line(time, temperature, stroke="#FF6347", thickness=2)  # Tomato color
    .x_axis(title="Time (s)")
    .y_axis(title="Temperature (°C)")
    .show()
)
```

---

## Concepts

Chartexa provides a unified charting engine for both C# and Python developers, enabling rapid visualization of real-time and large-scale datasets. The installation process ensures you have the necessary runtime dependencies, rendering backend, and language bindings to create interactive charts.

- **What it does:** Chartexa delivers high-performance chart rendering using DirectX 12 for hardware-accelerated graphics, with seamless integration for .NET and Python environments.
- **When to use it:** Use Chartexa when you require fast, scalable, and interactive charting in desktop applications, scientific computing, or data analysis workflows.
- **Why it exists:** Chartexa bridges the gap between high-performance native rendering and easy-to-use APIs for both C# and Python, supporting demanding visualization scenarios.

---

## Basic Usage

### C#

=== "C#"
```csharp
using Chartexa.Core;
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.RenderableSeries;

// Example: Plotting sensor data

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Seconds" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Voltage (V)" };

// Create data series
var voltageSeries = new XyDataSeries();
voltageSeries.Append(
    new double[] { 0, 1, 2, 3, 4, 5 },
    new double[] { 3.3, 3.5, 3.4, 3.6, 3.7, 3.8 }
);

// Create renderable series
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = voltageSeries,
    StrokeColor = new ChartColor(34, 139, 34), // Forest Green
    StrokeThickness = 2
};

// Create chart and add components
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(lineSeries);

// Display chart
chart.Show();
```

### Python

=== "Python"
```python
from chartexa import Chart

# Example: Plotting voltage readings over time
seconds = [0, 1, 2, 3, 4, 5]
voltage = [3.3, 3.5, 3.4, 3.6, 3.7, 3.8]

chart = (
    Chart(width=800, height=400)
    .line(seconds, voltage, stroke="#228B22", thickness=2)  # Forest Green
    .x_axis(title="Seconds")
    .y_axis(title="Voltage (V)")
    .background("#F5F5F5")
    .show()
)
```

---

## Configuration

Chartexa installation can be customized by specifying rendering backend, chart window options, and runtime settings.

| Option                | Type     | Default      | Description                                         |
|-----------------------|----------|--------------|-----------------------------------------------------|
| RendererBackend       | string   | "DirectX12"  | Rendering backend: "DirectX12", "Skia", "WPF"       |
| Chart.Width           | int      | 800          | Chart window width in pixels                        |
| Chart.Height          | int      | 600          | Chart window height in pixels                       |
| Chart.Background      | string   | "#FFFFFF"    | Background color (hex or named)                     |
| .NET Runtime Version  | string   | "10.0"       | Required for Python integration                     |
| DPI Awareness         | bool     | true         | Enables high-DPI rendering                          |

!!! tip "Performance Tip"
    For datasets exceeding 100,000 points, use the DirectX12 backend and ensure your GPU drivers are up to date.

---

## Examples

### Example 1: Real-Time Data Streaming

=== "C#"
```csharp
using Chartexa.Core;
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.RenderableSeries;
using System.Timers;

// Simulate real-time sensor data
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (s)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Pressure (kPa)" };

var dataSeries = new XyDataSeries();
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(70, 130, 180), // Steel Blue
    StrokeThickness = 2
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(lineSeries);
chart.Show();

var timer = new Timer(100);
double t = 0;
timer.Elapsed += (s, e) =>
{
    t += 0.1;
    double pressure = 101.3 + 2 * Math.Sin(t);
    dataSeries.Append(new double[] { t }, new double[] { pressure });
};
timer.Start();
```

=== "Python"
```python
from chartexa import Chart
import time
import math

chart = (
    Chart(width=800, height=400)
    .line([], [], stroke="#4682B4", thickness=2)
    .x_axis(title="Time (s)")
    .y_axis(title="Pressure (kPa)")
    .show()
)

t = 0
while t < 10:
    pressure = 101.3 + 2 * math.sin(t)
    chart.append_line_point(t, pressure)
    t += 0.1
    time.sleep(0.1)
```

### Example 2: Saving Chart as Image

=== "C#"
```csharp
using Chartexa.Core;
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.RenderableSeries;

// Plot rainfall data and save as PNG
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Day" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Rainfall (mm)" };

var rainfallSeries = new XyDataSeries();
rainfallSeries.Append(
    new double[] { 1, 2, 3, 4, 5 },
    new double[] { 5.2, 3.8, 0.0, 7.1, 2.3 }
);

var columnSeries = new FastColumnRenderableSeries
{
    DataSeries = rainfallSeries,
    FillColor = new ChartColor(30, 144, 255), // Dodger Blue
    StrokeThickness = 1
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(columnSeries);

// Save chart as PNG
chart.SaveImage("rainfall.png");
```

=== "Python"
```python
from chartexa import Chart

days = [1, 2, 3, 4, 5]
rainfall = [5.2, 3.8, 0.0, 7.1, 2.3]

chart = (
    Chart(width=600, height=300)
    .column(days, rainfall, fill="#1E90FF", thickness=1)
    .x_axis(title="Day")
    .y_axis(title="Rainfall (mm)")
    .background("#E6F7FF")
    .save("rainfall.png")
)
```

### Example 3: Custom Theme

=== "C#"
```csharp
using Chartexa.Core;
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.RenderableSeries;
using Chartexa.Theming;

// Apply a dark theme to the chart
ThemeEngine.ApplyTheme("Dark");

var xAxis = new NumericAxis { Id = "X", AxisTitle = "Hour" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "CPU Usage (%)" };

var cpuSeries = new XyDataSeries();
cpuSeries.Append(
    new double[] { 0, 1, 2, 3, 4, 5 },
    new double[] { 20, 35, 40, 50, 45, 30 }
);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = cpuSeries,
    StrokeColor = new ChartColor(255, 215, 0), // Gold
    StrokeThickness = 2
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(lineSeries);
chart.Show();
```

=== "Python"
```python
from chartexa import Chart

hours = [0, 1, 2, 3, 4, 5]
cpu_usage = [20, 35, 40, 50, 45, 30]

chart = (
    Chart(width=700, height=350)
    .line(hours, cpu_usage, stroke="#FFD700", thickness=2)  # Gold
    .x_axis(title="Hour")
    .y_axis(title="CPU Usage (%)")
    .background("#222222")
    .theme("dark")
    .show()
)
```

---

## Performance Notes

- Chartexa leverages DirectX 12 for hardware-accelerated rendering, supporting millions of data points with smooth interaction.
- Python integration incurs minimal overhead; performance is comparable to native C# usage for most chart types.
- Rendering backend selection impacts performance:
    - **DirectX12:** Best for large datasets and real-time streaming.
    - **Skia:** Cross-platform, suitable for smaller datasets or non-Windows environments.
    - **WPF:** Legacy support, limited to .NET desktop apps.
- High-DPI and multi-monitor setups are fully supported.

!!! tip "Performance Tip"
    For optimal performance, use DirectX12 backend and ensure your GPU drivers are up to date. Avoid using WPF backend for datasets larger than 100K points.

---

## When to Use

- You need high-performance charting in desktop applications (C# or Python).
- Your data requires real-time streaming or visualization of large datasets.
- You want seamless integration between .NET and Python workflows.
- You require hardware-accelerated rendering for interactive charts.
- You need to export charts as images or embed them in reports.

---

## Related

- [Quick Start](quick-start.md)
- [Axis Configuration](../axes/numeric-axis.md)
- [Rendering Backends](../rendering/rendering-backends.md)
- [Theme Engine](../theming/theme-engine.md)

---

> **Last updated:** 2024-06-11 13:42 UTC | **Status:** draft
> **Last updated:** 2026-04-08 02:18 UTC | **Status:** Placeholder -- awaiting AI expansion
