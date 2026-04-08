---
title: "Your First Chart in C#"
section: "getting-started"
last_updated: "2024-06-11 17:42 UTC"
status: draft
---

# Your First Chart in C#

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

This guide walks you through creating your first Chartexa chart in a C# WPF application. You'll learn how to set up the library, add axes, plot data, and render a simple line chart.

---

## Installation

### .NET (NuGet)

Install Chartexa via NuGet:

```bash
dotnet add package Chartexa.Core
dotnet add package Chartexa.Wpf
```

> **Note:** Chartexa requires .NET 10 or later and Windows 10+ for DirectX 12 rendering.

### Python (PyPI)

For Python users, install via pip:

```bash
pip install chartexa
```

> **Note:** Python integration requires the .NET 10 Runtime to be installed.

---

## Quick Start

=== "C#"

```csharp
using System.Windows;
using Chartexa.Wpf;
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.RenderableSeries;

// Create a WPF window with a ChartexaChart control
public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();

        var chart = new ChartexaChart();

        // Add axes
        chart.XAxes.Add(new NumericAxis { Id = "X", AxisTitle = "Time (s)" });
        chart.YAxes.Add(new NumericAxis { Id = "Y", AxisTitle = "Amplitude" });

        // Prepare data
        var xValues = new double[] { 0, 1, 2, 3, 4, 5 };
        var yValues = new double[] { 0, 2, 4, 3, 6, 8 };

        var dataSeries = new XyDataSeries();
        dataSeries.Append(xValues, yValues);

        // Add a line series
        var lineSeries = new FastLineRenderableSeries
        {
            DataSeries = dataSeries,
            StrokeColor = new ChartColor(70, 130, 180), // Steel blue
            StrokeThickness = 2
        };

        chart.RenderableSeries.Add(lineSeries);

        // Add chart to window
        this.Content = chart;
    }
}
```

=== "Python"

```python
from chartexa import Chart

x_values = [0, 1, 2, 3, 4, 5]
y_values = [0, 2, 4, 3, 6, 8]

chart = (
    Chart(width=800, height=400)
    .line(x_values, y_values, stroke="#4682B4", thickness=2)
    .x_axis(title="Time (s)")
    .y_axis(title="Amplitude")
    .background("#F5F5F7")
    .save("first_chart.png")
)
```

---

## Concepts

Chartexa enables developers to visualize real-time and large-scale datasets efficiently. The engine leverages DirectX 12 for hardware-accelerated rendering, ensuring smooth performance even with millions of data points.

- **What it does:** Chartexa provides a flexible API for constructing charts, adding axes, and rendering various series types (line, scatter, column, etc.).
- **When to use it:** Use Chartexa when you need interactive, high-performance charts in desktop applications, especially for scientific, financial, or engineering data.
- **Why it exists:** Existing charting libraries often struggle with large datasets or lack real-time responsiveness. Chartexa fills this gap with a modern rendering pipeline and seamless integration for both C# and Python.

---

## Basic Usage

=== "C#"

```csharp
using System.Windows;
using Chartexa.Wpf;
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.RenderableSeries;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();

        var chart = new ChartexaChart();

        // Configure axes
        var xAxis = new NumericAxis
        {
            Id = "X",
            AxisTitle = "Time (s)",
            AutoRange = AxisAutoRange.Always
        };
        var yAxis = new NumericAxis
        {
            Id = "Y",
            AxisTitle = "Amplitude",
            AutoRange = AxisAutoRange.Always
        };

        chart.XAxes.Add(xAxis);
        chart.YAxes.Add(yAxis);

        // Add data points
        var xValues = new double[] { 0, 1, 2, 3, 4, 5, 6 };
        var yValues = new double[] { 0, 1.5, 3, 2.7, 5.2, 7.1, 6.8 };

        var dataSeries = new XyDataSeries();
        dataSeries.Append(xValues, yValues);

        // Create and configure line series
        var lineSeries = new FastLineRenderableSeries
        {
            DataSeries = dataSeries,
            StrokeColor = new ChartColor(34, 139, 34), // Forest green
            StrokeThickness = 2
        };

        chart.RenderableSeries.Add(lineSeries);

        // Optional: set chart background
        chart.Background = new ChartColor(245, 245, 247);

        // Add chart to window
        this.Content = chart;
    }
}
```

=== "Python"

```python
from chartexa import Chart

x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1.5, 3, 2.7, 5.2, 7.1, 6.8]

chart = (
    Chart(width=800, height=400)
    .line(x, y, stroke="#228B22", thickness=2)
    .x_axis(title="Time (s)", auto_range=True)
    .y_axis(title="Amplitude", auto_range=True)
    .background("#F5F5F7")
    .save("basic_chart.png")
)
```

---

## Configuration

| Property         | Type        | Default         | Description                                     |
|------------------|-------------|-----------------|-------------------------------------------------|
| `XAxes`          | Collection  | Empty           | List of X axes for the chart                    |
| `YAxes`          | Collection  | Empty           | List of Y axes for the chart                    |
| `RenderableSeries`| Collection | Empty           | List of series to render (line, scatter, etc.)  |
| `Background`     | ChartColor  | System default  | Chart background color                          |
| `Width`          | int         | 800             | Chart width (pixels)                            |
| `Height`         | int         | 400             | Chart height (pixels)                           |
| `AutoRange`      | enum        | AxisAutoRange.Never | Axis auto-ranging mode                     |
| `StrokeColor`    | ChartColor  | #000000         | Line color for series                           |
| `StrokeThickness`| int         | 1               | Line thickness (pixels)                         |
| `AxisTitle`      | string      | ""              | Axis title text                                 |

---

## Examples

### Example 1: Scientific Data Plot

=== "C#"

```csharp
using System.Windows;
using Chartexa.Wpf;
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.RenderableSeries;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();

        var chart = new ChartexaChart();

        chart.XAxes.Add(new NumericAxis { Id = "X", AxisTitle = "Time (ms)" });
        chart.YAxes.Add(new NumericAxis { Id = "Y", AxisTitle = "Voltage (V)" });

        // Simulated sensor data
        var x = new double[] { 0, 10, 20, 30, 40, 50, 60 };
        var y = new double[] { 0.2, 0.5, 1.1, 0.9, 1.5, 1.8, 2.0 };

        var series = new XyDataSeries();
        series.Append(x, y);

        var line = new FastLineRenderableSeries
        {
            DataSeries = series,
            StrokeColor = new ChartColor(255, 99, 71), // Tomato
            StrokeThickness = 2
        };

        chart.RenderableSeries.Add(line);
        this.Content = chart;
    }
}
```

=== "Python"

```python
from chartexa import Chart

x = [0, 10, 20, 30, 40, 50, 60]
y = [0.2, 0.5, 1.1, 0.9, 1.5, 1.8, 2.0]

chart = (
    Chart(width=600, height=300)
    .line(x, y, stroke="#FF6347", thickness=2)
    .x_axis(title="Time (ms)")
    .y_axis(title="Voltage (V)")
    .background("#FFFFFF")
    .save("scientific_plot.png")
)
```

### Example 2: Financial Data Visualization

=== "C#"

```csharp
using System.Windows;
using Chartexa.Wpf;
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.RenderableSeries;

public partial class MainWindow : Window
{
    public MainWindow()
    {
        InitializeComponent();

        var chart = new ChartexaChart();

        chart.XAxes.Add(new NumericAxis { Id = "X", AxisTitle = "Day" });
        chart.YAxes.Add(new NumericAxis { Id = "Y", AxisTitle = "Price (USD)" });

        // Stock closing prices
        var days = new double[] { 1, 2, 3, 4, 5, 6, 7 };
        var prices = new double[] { 120.5, 121.0, 122.3, 121.8, 123.5, 124.2, 125.0 };

        var series = new XyDataSeries();
        series.Append(days, prices);

        var line = new FastLineRenderableSeries
        {
            DataSeries = series,
            StrokeColor = new ChartColor(30, 144, 255), // Dodger blue
            StrokeThickness = 2
        };

        chart.RenderableSeries.Add(line);
        this.Content = chart;
    }
}
```

=== "Python"

```python
from chartexa import Chart

days = [1, 2, 3, 4, 5, 6, 7]
prices = [120.5, 121.0, 122.3, 121.8, 123.5, 124.2, 125.0]

chart = (
    Chart(width=700, height=350)
    .line(days, prices, stroke="#1E90FF", thickness=2)
    .x_axis(title="Day")
    .y_axis(title="Price (USD)")
    .background("#F0F8FF")
    .save("financial_chart.png")
)
```

### Example 3: Real-Time Streaming

!!! example "Real-Time Streaming"

=== "C#"

```csharp
using System.Windows;
using System.Windows.Threading;
using Chartexa.Wpf;
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.RenderableSeries;

public partial class MainWindow : Window
{
    private XyDataSeries _dataSeries;
    private int _tick = 0;

    public MainWindow()
    {
        InitializeComponent();

        var chart = new ChartexaChart();

        chart.XAxes.Add(new NumericAxis { Id = "X", AxisTitle = "Tick" });
        chart.YAxes.Add(new NumericAxis { Id = "Y", AxisTitle = "Value" });

        _dataSeries = new XyDataSeries();

        var line = new FastLineRenderableSeries
        {
            DataSeries = _dataSeries,
            StrokeColor = new ChartColor(255, 140, 0), // Dark orange
            StrokeThickness = 2
        };

        chart.RenderableSeries.Add(line);
        this.Content = chart;

        var timer = new DispatcherTimer { Interval = TimeSpan.FromMilliseconds(100) };
        timer.Tick += (s, e) =>
        {
            _tick++;
            _dataSeries.Append(_tick, Math.Sin(_tick * 0.1));
        };
        timer.Start();
    }
}
```

=== "Python"

```python
import time
from chartexa import Chart

x = []
y = []

chart = Chart(width=800, height=400).x_axis(title="Tick").y_axis(title="Value")

for tick in range(50):
    x.append(tick)
    y.append(math.sin(tick * 0.1))
    chart.line(x, y, stroke="#FF8C00", thickness=2)
    chart.save(f"stream_{tick}.png")
    time.sleep(0.1)
```

---

## Performance Notes

Chartexa's DirectX 12 renderer is optimized for handling large datasets:

- Rendering up to 1 million points in under 50 ms on modern GPUs.
- Minimal UI thread blocking; chart updates remain responsive during streaming.
- Memory usage scales linearly with data size.
- For best performance, use `FastLineRenderableSeries` and avoid excessive redraws.

!!! tip "Performance Tip"
    Use DirectX 12 backend for datasets exceeding 100K points. For static charts with fewer points, WPF or Skia backends are sufficient.

---

## When to Use

- When you need interactive, high-performance charts in desktop applications.
- For scientific, engineering, or financial data visualization.
- When working with real-time or streaming data.
- If your datasets exceed tens of thousands of points and require smooth rendering.
- When you want seamless C# and Python integration for visualization workflows.

---

## Related

- [Line Series](../chart-types/2d/line-series.md)
- [Numeric Axis](../axes/numeric-axis.md)
- [Axis Ranging](../axes/axis-ranging.md)
- [DirectX 12 Renderer](../rendering/directx12.md)

---

> **Last updated:** 2024-06-11 17:42 UTC | **Status:** draft