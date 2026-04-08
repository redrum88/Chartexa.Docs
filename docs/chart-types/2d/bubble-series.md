---
title: "Bubble Series"
section: "chart-types/2d"
last_updated: "2024-06-13 14:55 UTC"
status: draft
---

# Bubble Series

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `BubbleRenderableSeries` displays a bubble chart, where each data point is represented by a circle whose position is determined by X and Y values, and whose size (radius) is determined by a third Z value. Bubble charts are useful for visualizing relationships between three numeric variables and highlighting clusters or outliers in multidimensional datasets.

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

// Sample data: Population, GDP, and CO2 emissions per country
var xData = new double[] { 1.2, 3.5, 2.1 }; // GDP (trillion USD)
var yData = new double[] { 80, 140, 60 };   // Population (millions)
var zData = new double[] { 400, 900, 250 }; // CO2 emissions (megatonnes)

var xAxis = new NumericAxis { Id = "X", AxisTitle = "GDP (Trillion USD)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Population (Millions)" };

var dataSeries = new BubbleDataSeries();
dataSeries.Append(xData, yData, zData);

var bubbleSeries = new BubbleRenderableSeries
{
    DataSeries = dataSeries,
    FillColor = new ChartColor(70, 130, 180, 128), // Semi-transparent steel blue
    StrokeColor = new ChartColor(70, 130, 180),
    StrokeThickness = 1,
    MinBubbleSize = 10,
    MaxBubbleSize = 50
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(bubbleSeries);
chart.Save("bubble_chart.png");
```

=== "Python"

```python
from chartexa import Chart

# Sample data: GDP, Population, CO2 emissions
x = [1.2, 3.5, 2.1]   # GDP (trillion USD)
y = [80, 140, 60]     # Population (millions)
z = [400, 900, 250]   # CO2 emissions (megatonnes)

chart = (
    Chart(width=800, height=600)
    .bubble(x, y, z, fill="#4682B4AA", stroke="#4682B4", min_size=10, max_size=50)
    .x_axis(title="GDP (Trillion USD)")
    .y_axis(title="Population (Millions)")
    .background("#F9F9F9")
    .save("bubble_chart.png")
)
```

---

## Concepts

Bubble charts visualize three numeric variables per data point: X and Y for position, and Z for bubble size. Each bubble's area (or radius) is proportional to the Z value, allowing you to compare magnitude visually across the dataset.

Use bubble charts when you need to:
- Show relationships between three variables.
- Highlight clusters, outliers, or trends in multidimensional data.
- Compare relative sizes (e.g., market share, population, emissions) alongside position.

The `BubbleRenderableSeries` in Chartexa maps to the `BubbleDataSeries`, which stores X, Y, and Z values. You can configure bubble appearance, scaling, and color to match your visualization needs.

---

## Basic Usage

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;

// Example: Visualizing company revenue, employee count, and market cap
var revenue = new double[] { 2.5, 4.1, 1.8, 3.7 }; // Revenue (billion USD)
var employees = new double[] { 12000, 34000, 8000, 22000 }; // Employees
var marketCap = new double[] { 15, 40, 8, 22 }; // Market Cap (billion USD)

var xAxis = new NumericAxis { Id = "X", AxisTitle = "Revenue (Billion USD)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Employees" };

var dataSeries = new BubbleDataSeries();
dataSeries.Append(revenue, employees, marketCap);

var bubbleSeries = new BubbleRenderableSeries
{
    DataSeries = dataSeries,
    FillColor = new ChartColor(255, 99, 71, 128), // Semi-transparent tomato red
    StrokeColor = new ChartColor(255, 99, 71),
    StrokeThickness = 2,
    MinBubbleSize = 15,
    MaxBubbleSize = 60
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(bubbleSeries);
chart.Background = new ChartColor(245, 245, 245); // Light gray
chart.Save("company_bubble_chart.png");
```

=== "Python"

```python
from chartexa import Chart

# Example: Company data
revenue = [2.5, 4.1, 1.8, 3.7]      # Revenue (billion USD)
employees = [12000, 34000, 8000, 22000]
market_cap = [15, 40, 8, 22]        # Market Cap (billion USD)

chart = (
    Chart(width=900, height=500)
    .bubble(revenue, employees, market_cap, fill="#FF6347AA", stroke="#FF6347", min_size=15, max_size=60)
    .x_axis(title="Revenue (Billion USD)")
    .y_axis(title="Employees")
    .background("#F5F5F5")
    .save("company_bubble_chart.png")
)
```

---

## Configuration

| Property         | Type         | Default | Description                                                                                  |
|------------------|--------------|---------|----------------------------------------------------------------------------------------------|
| FillColor        | ChartColor   | #4682B4 | Bubble fill color (supports alpha for transparency)                                          |
| StrokeColor      | ChartColor   | #4682B4 | Bubble border color                                                                          |
| StrokeThickness  | int          | 1       | Bubble border thickness (pixels)                                                             |
| MinBubbleSize    | int          | 10      | Minimum bubble diameter (pixels)                                                             |
| MaxBubbleSize    | int          | 50      | Maximum bubble diameter (pixels)                                                             |
| DataSeries       | BubbleDataSeries | N/A     | Data source for X, Y, Z values                                                               |
| Opacity          | double       | 1.0     | Bubble opacity (0.0 - 1.0)                                                                   |
| TooltipEnabled   | bool         | true    | Show tooltips on hover/click                                                                 |
| ZScaleMode       | enum         | Linear  | Scaling mode for Z values: `Linear` or `Sqrt` (area proportional to Z)                       |
| LegendLabel      | string       | ""      | Label for legend display                                                                     |

!!! tip "Performance Tip"
    For datasets with more than 10,000 bubbles, use the DirectX12 renderer for optimal performance.

---

## Examples

### Example 1: Market Share Visualization

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;

// Market share data for tech companies
var x = new double[] { 2018, 2019, 2020, 2021 };
var y = new double[] { 35, 42, 38, 45 }; // Market share (%)
var z = new double[] { 120, 180, 150, 210 }; // Revenue (million USD)

var xAxis = new NumericAxis { Id = "X", AxisTitle = "Year" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Market Share (%)" };

var dataSeries = new BubbleDataSeries();
dataSeries.Append(x, y, z);

var bubbleSeries = new BubbleRenderableSeries
{
    DataSeries = dataSeries,
    FillColor = new ChartColor(34, 139, 34, 128), // Semi-transparent forest green
    StrokeColor = new ChartColor(34, 139, 34),
    StrokeThickness = 2,
    MinBubbleSize = 20,
    MaxBubbleSize = 70
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(bubbleSeries);
chart.Save("market_share_bubble.png");
```

=== "Python"

```python
from chartexa import Chart

# Market share data
years = [2018, 2019, 2020, 2021]
market_share = [35, 42, 38, 45]
revenue = [120, 180, 150, 210]

chart = (
    Chart(width=700, height=400)
    .bubble(years, market_share, revenue, fill="#228B22AA", stroke="#228B22", min_size=20, max_size=70)
    .x_axis(title="Year")
    .y_axis(title="Market Share (%)")
    .background("#FFFFFF")
    .save("market_share_bubble.png")
)
```

### Example 2: Environmental Data (CO2 Emissions)

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;

// Environmental data: Cities' air quality index and population
var x = new double[] { 35, 55, 80, 120 }; // AQI
var y = new double[] { 1.5, 3.2, 2.8, 4.1 }; // Population (millions)
var z = new double[] { 300, 500, 400, 700 }; // CO2 emissions (kilotonnes)

var xAxis = new NumericAxis { Id = "X", AxisTitle = "Air Quality Index (AQI)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Population (Millions)" };

var dataSeries = new BubbleDataSeries();
dataSeries.Append(x, y, z);

var bubbleSeries = new BubbleRenderableSeries
{
    DataSeries = dataSeries,
    FillColor = new ChartColor(255, 215, 0, 128), // Semi-transparent gold
    StrokeColor = new ChartColor(255, 215, 0),
    StrokeThickness = 1,
    MinBubbleSize = 10,
    MaxBubbleSize = 40
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(bubbleSeries);
chart.Save("environment_bubble.png");
```

=== "Python"

```python
from chartexa import Chart

# Environmental data
aqi = [35, 55, 80, 120]
population = [1.5, 3.2, 2.8, 4.1]
co2 = [300, 500, 400, 700]

chart = (
    Chart(width=600, height=400)
    .bubble(aqi, population, co2, fill="#FFD700AA", stroke="#FFD700", min_size=10, max_size=40)
    .x_axis(title="Air Quality Index (AQI)")
    .y_axis(title="Population (Millions)")
    .background("#E6E6FA")
    .save("environment_bubble.png")
)
```

### Example 3: Real-Time Streaming

!!! example "Real-Time Streaming Bubble Chart"

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;
using System.Threading;

// Simulate real-time sensor data
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (s)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Sensor Value" };

var dataSeries = new BubbleDataSeries();
var bubbleSeries = new BubbleRenderableSeries
{
    DataSeries = dataSeries,
    FillColor = new ChartColor(70, 130, 180, 128),
    StrokeColor = new ChartColor(70, 130, 180),
    MinBubbleSize = 10,
    MaxBubbleSize = 40
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(bubbleSeries);

for (int t = 0; t < 100; t++)
{
    double sensorValue = Math.Sin(t / 10.0) * 50 + 100;
    double bubbleSize = Math.Abs(sensorValue) / 2;
    dataSeries.Append(new double[] { t }, new double[] { sensorValue }, new double[] { bubbleSize });
    chart.Save($"bubble_stream_{t}.png");
    Thread.Sleep(50); // Simulate streaming interval
}
```

=== "Python"

```python
from chartexa import Chart
import math
import time

x = []
y = []
z = []

chart = (
    Chart(width=600, height=300)
    .x_axis(title="Time (s)")
    .y_axis(title="Sensor Value")
    .background("#F0F8FF")
)

for t in range(100):
    sensor_value = math.sin(t / 10.0) * 50 + 100
    bubble_size = abs(sensor_value) / 2
    x.append(t)
    y.append(sensor_value)
    z.append(bubble_size)
    chart.bubble(x, y, z, fill="#4682B4AA", stroke="#4682B4", min_size=10, max_size=40)
    chart.save(f"bubble_stream_{t}.png")
    time.sleep(0.05)
```

---

## Performance Notes

- Bubble rendering is GPU-accelerated on DirectX 12, enabling smooth visualization of up to 100,000 bubbles.
- Rendering performance depends on bubble count, transparency, and overlap. For large datasets, prefer opaque fills and avoid excessive overlap.
- Python integration uses the .NET runtime; ensure .NET 10+ is installed for optimal speed.

!!! note
    Python requires the .NET 10 Runtime to be installed.

- Tooltips and interactivity may impact performance with dense datasets. Disable tooltips for maximum throughput.

---

## When to Use

- Visualizing relationships between three numeric variables (e.g., X=GDP, Y=Population, Z=CO2 emissions).
- Comparing magnitude and position in multidimensional datasets.
- Highlighting clusters, outliers, or trends in business, environmental, or scientific data.
- Displaying real-time sensor data with variable magnitude.

---

## Related

- [Scatter Series](scatter-series.md)
- [Column Series](column-series.md)
- [Axis Ranging](../axes/axis-ranging.md)
- [DirectX12 Renderer](../../rendering/directx12.md)

---

> **Last updated:** 2024-06-13 14:55 UTC | **Status:** draft