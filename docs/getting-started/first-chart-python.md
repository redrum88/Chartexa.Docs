---
title: "Your First Chart in Python"
section: "getting-started"
last_updated: "2024-06-13 14:22 UTC"
status: draft
---

# Your First Chart in Python

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

This guide walks you through creating your first chart in Python using Chartexa: installing the package, importing the API, rendering a chart, and exporting the result as an image. You'll see how easy it is to visualize data with Chartexa's concise Python interface.

---

## Installation

Chartexa requires both the Python package and the .NET runtime. The Python package wraps the C# engine, so .NET 10+ must be installed.

### .NET (NuGet)

If you are developing in C#, install Chartexa via NuGet:

```bash
dotnet add package Chartexa.Core
```

### Python (PyPI)

Install Chartexa for Python using pip:

```bash
pip install chartexa
```

!!! note
    Chartexa for Python requires the .NET 10 Runtime. Download from [Microsoft .NET Downloads](https://dotnet.microsoft.com/en-us/download/dotnet/10.0).

---

## Quick Start

Create a simple line chart and export it as a PNG.

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Charting;
using Chartexa.Rendering;

// Sample data
double[] time = { 0, 1, 2, 3, 4, 5 };
double[] amplitude = { 0, 1.2, 0.8, 2.1, 1.5, 2.7 };

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (s)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Amplitude" };

// Create data series
var dataSeries = new XyDataSeries();
dataSeries.Append(time, amplitude);

// Create renderable series
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(70, 130, 180), // Steel blue
    StrokeThickness = 2
};

// Create chart
var chart = new Chart
{
    Width = 800,
    Height = 400,
    Background = new ChartColor(28, 28, 30), // Dark background
    Axes = { xAxis, yAxis },
    Series = { lineSeries }
};

// Export to PNG
chart.Save("first_chart.png");
```

=== "Python"
```python
from chartexa import Chart

# Sample data
time = [0, 1, 2, 3, 4, 5]
amplitude = [0, 1.2, 0.8, 2.1, 1.5, 2.7]

# Create and render chart
chart = (
    Chart(width=800, height=400)
    .line(time, amplitude, stroke="#4682B4", thickness=2)
    .background("#1C1C1E")
    .axes(x_title="Time (s)", y_title="Amplitude")
    .save("first_chart.png")
)
```

---

## Concepts

Chartexa's Python API provides a streamlined interface for creating charts with minimal code. The engine handles rendering, axis scaling, and exporting, allowing you to focus on your data.

- **What it does:** Chartexa renders high-quality charts from your data, supporting line, scatter, column, candlestick, and heatmap types.
- **When to use it:** Use Chartexa when you need fast, interactive, or large-scale data visualization in Python, especially for scientific, financial, or engineering applications.
- **Why it exists:** Chartexa bridges the gap between high-performance C# charting and Python's ease of use, enabling real-time visualization and export without sacrificing speed.

---

## Basic Usage

Create a chart, add axes and a line series, and export to PNG.

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Charting;
using Chartexa.Rendering;

// Data
double[] x = { 0, 1, 2, 3, 4, 5, 6 };
double[] y = { 0, 1.1, 2.3, 1.8, 2.5, 3.2, 2.9 };

// Axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Seconds" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Voltage (V)" };

// Series
var series = new XyDataSeries();
series.Append(x, y);

var line = new FastLineRenderableSeries
{
    DataSeries = series,
    StrokeColor = new ChartColor(34, 139, 34), // Forest green
    StrokeThickness = 3
};

// Chart
var chart = new Chart
{
    Width = 600,
    Height = 300,
    Background = new ChartColor(240, 240, 240), // Light background
    Axes = { xAxis, yAxis },
    Series = { line }
};

// Save as PNG
chart.Save("basic_usage_chart.png");
```

=== "Python"
```python
from chartexa import Chart

x = [0, 1, 2, 3, 4, 5, 6]
y = [0, 1.1, 2.3, 1.8, 2.5, 3.2, 2.9]

chart = (
    Chart(width=600, height=300)
    .line(x, y, stroke="#228B22", thickness=3)
    .background("#F0F0F0")
    .axes(x_title="Seconds", y_title="Voltage (V)")
    .save("basic_usage_chart.png")
)
```

---

## Configuration

Chartexa's Python Chart object exposes several configuration options:

| Property      | Type      | Default      | Description                                 |
|---------------|-----------|--------------|---------------------------------------------|
| width         | int       | 800          | Chart width in pixels                       |
| height        | int       | 400          | Chart height in pixels                      |
| background    | str       | "#1C1C1E"    | Background color (hex or named)             |
| x_title       | str       | ""           | X axis title                                |
| y_title       | str       | ""           | Y axis title                                |
| line.stroke   | str       | "#4682B4"    | Line color (hex or named)                   |
| line.thickness| int       | 2            | Line thickness in pixels                    |
| save(path)    | str       | N/A          | Export chart to PNG/JPG/SVG                 |

!!! tip "Performance Tip"
    For datasets over 100,000 points, use the default DirectX 12 backend for optimal rendering speed.

---

## Examples

### Example 1: Plotting Sensor Data

Visualize temperature readings from a sensor over time.

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Charting;

// Data
double[] time = { 0, 5, 10, 15, 20, 25 };
double[] temp = { 22.1, 22.5, 23.0, 23.4, 23.8, 24.2 };

// Axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (min)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Temperature (°C)" };

// Series
var series = new XyDataSeries();
series.Append(time, temp);

var line = new FastLineRenderableSeries
{
    DataSeries = series,
    StrokeColor = new ChartColor(255, 99, 71), // Tomato
    StrokeThickness = 2
};

// Chart
var chart = new Chart
{
    Width = 700,
    Height = 350,
    Background = new ChartColor(255, 255, 255),
    Axes = { xAxis, yAxis },
    Series = { line }
};

chart.Save("sensor_data.png");
```

=== "Python"
```python
from chartexa import Chart

time = [0, 5, 10, 15, 20, 25]
temp = [22.1, 22.5, 23.0, 23.4, 23.8, 24.2]

chart = (
    Chart(width=700, height=350)
    .line(time, temp, stroke="#FF6347", thickness=2)
    .background("#FFFFFF")
    .axes(x_title="Time (min)", y_title="Temperature (°C)")
    .save("sensor_data.png")
)
```

### Example 2: Financial Data Visualization

Plot daily closing prices for a stock.

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Charting;

// Data
double[] days = { 1, 2, 3, 4, 5 };
double[] close = { 101.5, 103.2, 102.8, 104.7, 105.3 };

// Axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Day" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Closing Price ($)" };

// Series
var series = new XyDataSeries();
series.Append(days, close);

var line = new FastLineRenderableSeries
{
    DataSeries = series,
    StrokeColor = new ChartColor(30, 144, 255), // Dodger blue
    StrokeThickness = 2
};

// Chart
var chart = new Chart
{
    Width = 500,
    Height = 250,
    Background = new ChartColor(245, 245, 245),
    Axes = { xAxis, yAxis },
    Series = { line }
};

chart.Save("stock_prices.png");
```

=== "Python"
```python
from chartexa import Chart

days = [1, 2, 3, 4, 5]
close = [101.5, 103.2, 102.8, 104.7, 105.3]

chart = (
    Chart(width=500, height=250)
    .line(days, close, stroke="#1E90FF", thickness=2)
    .background("#F5F5F5")
    .axes(x_title="Day", y_title="Closing Price ($)")
    .save("stock_prices.png")
)
```

### Example 3: Real-Time Streaming

!!! example "Real-Time Streaming"
    Visualize streaming data by updating the chart in a loop.

    === "Python"
    ```python
    import time
    from chartexa import Chart

    x = []
    y = []
    chart = Chart(width=600, height=300).background("#222")

    for i in range(20):
        x.append(i)
        y.append(2 * i + 3)
        chart.line(x, y, stroke="#FFD700", thickness=2)
        chart.save(f"stream_{i}.png")
        time.sleep(0.1)
    ```

---

## Performance Notes

Chartexa leverages DirectX 12 for rendering, achieving high throughput for large datasets:

- Rendering 1 million points: ~0.2 seconds (DirectX 12 backend)
- Exporting to PNG is hardware-accelerated; typical export times are under 0.5 seconds for charts up to 2000x1000 pixels.
- Python overhead is minimal; most processing occurs in native C#.

!!! tip "Performance Tip"
    For best performance, avoid frequent chart re-instantiation. Reuse the Chart object and update series data as needed.

---

## When to Use

- When you need to visualize data in Python with minimal code.
- For real-time or large-scale datasets (e.g., sensor streams, financial ticks).
- When exporting charts as images for reports or dashboards.
- If you require high-quality rendering and fast export.

---

## Related

- [Line Series](../chart-types/2d/line-series.md)
- [Axis Configuration](../axes/axis-configuration.md)
- [Exporting Charts](../export/exporting-charts.md)

---

> **Last updated:** 2024-06-13 14:22 UTC | **Status:** draft