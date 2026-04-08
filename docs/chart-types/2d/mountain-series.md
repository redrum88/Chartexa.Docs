---
title: "Mountain (Area) Series"
section: "chart-types/2d"
last_updated: "2024-06-13 16:22 UTC"
status: draft
---

# Mountain (Area) Series

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `MountainRenderableSeries` displays a filled area chart, also known as a mountain or area series. It visualizes quantitative data by filling the area between a line and the axis, supporting gradient fills, customizable strokes, and high-performance rendering for large datasets.

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
using Chartexa.Charting.RenderableSeries;
using Chartexa.Charting;
using Chartexa.Core.Drawing;

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Year" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Revenue (M USD)" };

// Prepare data
var years = new double[] { 2018, 2019, 2020, 2021, 2022 };
var revenue = new double[] { 120, 135, 150, 170, 210 };
var dataSeries = new XyDataSeries();
dataSeries.Append(years, revenue);

// Create mountain series
var mountainSeries = new MountainRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(34, 139, 34), // Forest Green
    FillGradient = new LinearGradientBrush(
        new ChartColor(34, 139, 34, 180), // Semi-transparent
        new ChartColor(144, 238, 144, 60), // Light Green, more transparent
        GradientDirection.Vertical
    ),
    StrokeThickness = 2
};

// Create chart
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(mountainSeries);
chart.Save("mountain_chart.png");
```

=== "Python"

```python
from chartexa import Chart

years = [2018, 2019, 2020, 2021, 2022]
revenue = [120, 135, 150, 170, 210]

chart = (
    Chart(width=800, height=400)
    .mountain(
        years, revenue,
        stroke="#228B22",           # Forest Green
        thickness=2,
        fill_gradient={
            "start": "#228B22AA",  # Semi-transparent
            "end": "#90EE9060",    # Light Green, more transparent
            "direction": "vertical"
        }
    )
    .x_axis(title="Year")
    .y_axis(title="Revenue (M USD)")
    .background("#F5F5F5")
    .save("mountain_chart.png")
)
```

---

## Concepts

The mountain (area) series visualizes data as a filled region between a plotted line and the axis baseline. This chart type is ideal for representing cumulative values, trends over time, and emphasizing the magnitude of change. The area fill can be solid or gradient, making it visually distinct and suitable for highlighting volume or aggregate metrics.

Use mountain series when you want to:
- Show how values accumulate over time (e.g., sales, population growth)
- Compare multiple series with stacked or overlapped areas
- Emphasize the area under a curve, not just the trend line

Chartexa's mountain series is optimized for real-time updates and large datasets, supporting smooth gradients, anti-aliased strokes, and hardware-accelerated rendering.

---

## Basic Usage

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Charting.RenderableSeries;
using Chartexa.Charting;
using Chartexa.Core.Drawing;

// Example: Visualizing monthly website visits

var months = new double[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 };
var visits = new double[] { 3200, 4100, 3900, 4800, 5300, 6000, 5800, 6100, 6500, 7000, 7200, 7600 };

var dataSeries = new XyDataSeries();
dataSeries.Append(months, visits);

var mountainSeries = new MountainRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(70, 130, 180), // Steel Blue
    FillGradient = new LinearGradientBrush(
        new ChartColor(70, 130, 180, 160),
        new ChartColor(176, 224, 230, 60),
        GradientDirection.Vertical
    ),
    StrokeThickness = 2
};

var chart = new Chart();
chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Month" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Visits" });
chart.RenderableSeries.Add(mountainSeries);
chart.Save("website_visits_area.png");
```

=== "Python"

```python
from chartexa import Chart

months = list(range(1, 13))
visits = [3200, 4100, 3900, 4800, 5300, 6000, 5800, 6100, 6500, 7000, 7200, 7600]

chart = (
    Chart(width=800, height=400)
    .mountain(
        months, visits,
        stroke="#4682B4",           # Steel Blue
        thickness=2,
        fill_gradient={
            "start": "#4682B4A0",  # Semi-transparent
            "end": "#B0E0E3A0",
            "direction": "vertical"
        }
    )
    .x_axis(title="Month")
    .y_axis(title="Visits")
    .background("#FFFFFF")
    .save("website_visits_area.png")
)
```

---

## Configuration

| Property        | Type                    | Default        | Description                                                                 |
|-----------------|------------------------|----------------|-----------------------------------------------------------------------------|
| DataSeries      | XyDataSeries           | Required       | The data series to render.                                                  |
| StrokeColor     | ChartColor / str       | #000000        | Color of the outline (line) above the area.                                 |
| StrokeThickness | int / float            | 1              | Thickness of the outline stroke.                                            |
| FillColor       | ChartColor / str       | #C0C0C0        | Solid fill color for the area (if no gradient).                             |
| FillGradient    | LinearGradientBrush / dict | None       | Gradient fill for the area.                                                 |
| Opacity         | float                  | 1.0            | Opacity of the filled area (0.0 - 1.0).                                     |
| AntiAliasing    | bool                   | true           | Enables smooth edges for the area and stroke.                               |
| IsVisible       | bool                   | true           | Controls visibility of the series.                                          |
| Baseline        | double                 | 0              | Y-value where the area fill starts (usually zero).                          |

---

## Examples

### Example 1: Comparing Two Product Sales

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Charting.RenderableSeries;
using Chartexa.Charting;
using Chartexa.Core.Drawing;

// Product A
var months = new double[] { 1, 2, 3, 4, 5, 6 };
var salesA = new double[] { 500, 700, 850, 900, 1050, 1200 };
var seriesA = new XyDataSeries();
seriesA.Append(months, salesA);

var mountainA = new MountainRenderableSeries
{
    DataSeries = seriesA,
    StrokeColor = new ChartColor(255, 99, 71), // Tomato
    FillColor = new ChartColor(255, 99, 71, 80),
    StrokeThickness = 2,
    Opacity = 0.7
};

// Product B
var salesB = new double[] { 400, 650, 800, 950, 1100, 1300 };
var seriesB = new XyDataSeries();
seriesB.Append(months, salesB);

var mountainB = new MountainRenderableSeries
{
    DataSeries = seriesB,
    StrokeColor = new ChartColor(30, 144, 255), // Dodger Blue
    FillColor = new ChartColor(30, 144, 255, 80),
    StrokeThickness = 2,
    Opacity = 0.5
};

var chart = new Chart();
chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Month" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Sales" });
chart.RenderableSeries.Add(mountainA);
chart.RenderableSeries.Add(mountainB);
chart.Save("product_sales_comparison.png");
```

=== "Python"

```python
from chartexa import Chart

months = [1, 2, 3, 4, 5, 6]
sales_a = [500, 700, 850, 900, 1050, 1200]
sales_b = [400, 650, 800, 950, 1100, 1300]

chart = (
    Chart(width=800, height=400)
    .mountain(
        months, sales_a,
        stroke="#FF6347",          # Tomato
        thickness=2,
        fill="#FF634780",
        opacity=0.7
    )
    .mountain(
        months, sales_b,
        stroke="#1E90FF",          # Dodger Blue
        thickness=2,
        fill="#1E90FF80",
        opacity=0.5
    )
    .x_axis(title="Month")
    .y_axis(title="Sales")
    .background("#FAFAFA")
    .save("product_sales_comparison.png")
)
```

### Example 2: Real-Time Streaming Area Chart

!!! example "Real-Time Streaming"

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Charting.RenderableSeries;
using Chartexa.Charting;
using Chartexa.Core.Drawing;
using System.Threading;

// Simulate real-time sensor data
var dataSeries = new XyDataSeries();
var mountainSeries = new MountainRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(46, 204, 113), // Emerald
    FillColor = new ChartColor(46, 204, 113, 100),
    StrokeThickness = 2
};

var chart = new Chart();
chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Time (s)" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Sensor Value" });
chart.RenderableSeries.Add(mountainSeries);

for (int t = 0; t < 100; t++)
{
    double value = 50 + 10 * Math.Sin(0.1 * t) + 5 * Math.Cos(0.05 * t);
    dataSeries.Append(t, value);
    chart.Render();
    Thread.Sleep(50); // Simulate real-time update
}
chart.Save("sensor_stream_area.png");
```

=== "Python"

```python
from chartexa import Chart
import math
import time

x = []
y = []
chart = (
    Chart(width=800, height=400)
    .mountain(
        x, y,
        stroke="#2ECC71",
        thickness=2,
        fill="#2ECC7164"
    )
    .x_axis(title="Time (s)")
    .y_axis(title="Sensor Value")
    .background("#F0FFF0")
)

for t in range(100):
    value = 50 + 10 * math.sin(0.1 * t) + 5 * math.cos(0.05 * t)
    x.append(t)
    y.append(value)
    chart.update()
    time.sleep(0.05)  # Simulate real-time streaming

chart.save("sensor_stream_area.png")
```

---

## Performance Notes

Chartexa's mountain series leverages GPU acceleration via DirectX 12, enabling smooth rendering of area charts with tens of millions of points. Gradient fills and anti-aliasing are hardware-optimized, ensuring minimal CPU overhead.

- Rendering 1M points with gradient fill: < 30 ms (DirectX12 backend)
- Supports real-time streaming and dynamic updates with negligible latency
- Python integration uses .NET runtime; performance is comparable for most chart sizes

!!! tip "Performance Tip"
    For datasets exceeding 100K points, use the DirectX12 renderer for optimal fill and stroke performance. Avoid excessive transparency layers for best throughput.

---

## When to Use

- Visualizing cumulative data (e.g., sales, rainfall, population)
- Highlighting the area under a curve for trend analysis
- Comparing multiple series with overlapping or stacked areas
- Emphasizing magnitude and volume, not just trend lines
- Real-time streaming scenarios where area visualization is needed

---

## Related

- [Fast Line Series](fast-line-series.md)
- [Column Series](column-series.md)
- [Scatter Series](scatter-series.md)
- [Axis Ranging](../axes/axis-ranging.md)
- [DirectX12 Renderer](../../rendering/directx12.md)

---

> **Last updated:** 2024-06-13 16:22 UTC | **Status:** draft