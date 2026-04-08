---
title: "Stacked Mountain Series"
section: "chart-types/2d"
last_updated: "2024-06-13 16:25 UTC"
status: draft
---

# Stacked Mountain Series

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `StackedMountainRenderableSeries` displays multiple area series stacked vertically, visualizing cumulative values across categories or time. Use it to show how individual components contribute to a total, such as energy sources, sales by region, or population breakdowns.

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
using Chartexa.Core;

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Year" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Production (GWh)" };

// Create data series for each energy source
var solar = new XyDataSeries();
solar.Append(new[] {2018, 2019, 2020, 2021}, new[] {120, 150, 180, 210});

var wind = new XyDataSeries();
wind.Append(new[] {2018, 2019, 2020, 2021}, new[] {80, 110, 140, 170});

var hydro = new XyDataSeries();
hydro.Append(new[] {2018, 2019, 2020, 2021}, new[] {200, 220, 230, 240});

// Create stacked mountain series
var stackedMountain = new StackedMountainRenderableSeries
{
    DataSeries = new[] {solar, wind, hydro},
    FillColors = new[]
    {
        new ChartColor(255, 204, 0),   // Solar: yellow
        new ChartColor(70, 130, 180),  // Wind: steel blue
        new ChartColor(34, 139, 34)    // Hydro: green
    },
    StrokeColors = new[]
    {
        new ChartColor(255, 170, 0),
        new ChartColor(100, 149, 237),
        new ChartColor(50, 205, 50)
    },
    StrokeThickness = 2
};

// Create chart and add series
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(stackedMountain);
```

=== "Python"
```python
from chartexa import Chart

years = [2018, 2019, 2020, 2021]
solar = [120, 150, 180, 210]
wind = [80, 110, 140, 170]
hydro = [200, 220, 230, 240]

chart = (
    Chart(width=800, height=400)
    .stacked_mountain(
        x=years,
        ys=[solar, wind, hydro],
        fills=["#FFCC00", "#4682B4", "#228B22"],
        strokes=["#FFAA00", "#6495ED", "#32CD32"],
        thickness=2
    )
    .x_axis(title="Year")
    .y_axis(title="Production (GWh)")
    .background("#F9F9F9")
    .save("energy_sources.png")
)
```

---

## Concepts

The stacked mountain (stacked area) chart visualizes multiple data series as areas layered on top of each other. Each series represents a component of the total, and the stacking shows how the sum evolves across the X axis (typically time or categories).

- **What it does:** Renders several area series, stacking each subsequent series atop the previous, so the topmost shape represents the cumulative sum.
- **When to use it:** Ideal for illustrating how individual groups contribute to a whole over time, such as market share, energy production, or sales breakdowns.
- **Why it exists:** It helps reveal both individual trends and total values, making it easier to spot changes in composition and overall growth.

!!! tip "Visualizing Composition"
    Stacked mountain charts are best for showing the proportional contribution of each series to the total, especially when the sum is meaningful.

---

## Basic Usage

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using Chartexa.Core;

// Example: Population by Age Group over Years

var xAxis = new NumericAxis { Id = "X", AxisTitle = "Year" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Population (millions)" };

// Data for three age groups
var children = new XyDataSeries();
children.Append(new[] {2015, 2016, 2017, 2018}, new[] {12.5, 12.7, 12.8, 13.0});

var adults = new XyDataSeries();
adults.Append(new[] {2015, 2016, 2017, 2018}, new[] {30.2, 30.5, 30.9, 31.3});

var seniors = new XyDataSeries();
seniors.Append(new[] {2015, 2016, 2017, 2018}, new[] {8.1, 8.3, 8.5, 8.7});

// Configure stacked mountain series
var stackedMountain = new StackedMountainRenderableSeries
{
    DataSeries = new[] {children, adults, seniors},
    FillColors = new[]
    {
        new ChartColor(135, 206, 250), // Children: light blue
        new ChartColor(255, 160, 122), // Adults: light salmon
        new ChartColor(192, 192, 192)  // Seniors: gray
    },
    StrokeColors = new[]
    {
        new ChartColor(70, 130, 180),
        new ChartColor(255, 99, 71),
        new ChartColor(105, 105, 105)
    },
    StrokeThickness = 2
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(stackedMountain);
chart.Save("population_by_age.png");
```

=== "Python"
```python
from chartexa import Chart

years = [2015, 2016, 2017, 2018]
children = [12.5, 12.7, 12.8, 13.0]
adults = [30.2, 30.5, 30.9, 31.3]
seniors = [8.1, 8.3, 8.5, 8.7]

chart = (
    Chart(width=700, height=350)
    .stacked_mountain(
        x=years,
        ys=[children, adults, seniors],
        fills=["#87CEFA", "#FFA07A", "#C0C0C0"],
        strokes=["#4682B4", "#FF6347", "#696969"],
        thickness=2
    )
    .x_axis(title="Year")
    .y_axis(title="Population (millions)")
    .background("#FFFFFF")
    .save("population_by_age.png")
)
```

---

## Configuration

| Property        | Type            | Default     | Description                                                        |
|-----------------|-----------------|-------------|--------------------------------------------------------------------|
| DataSeries      | XyDataSeries[]  | Required    | Array of data series to stack.                                     |
| FillColors      | ChartColor[]    | Varies      | Fill color for each stacked area.                                  |
| StrokeColors    | ChartColor[]    | Varies      | Stroke color for each stacked area.                                |
| StrokeThickness | int             | 2           | Outline thickness for each area.                                   |
| Opacity         | float           | 1.0         | Opacity of the filled areas (0.0 transparent, 1.0 opaque).         |
| AntiAliasing    | bool            | true        | Enables smooth edges for area shapes.                              |
| XAxisId         | string          | "X"         | ID of the X axis to use.                                           |
| YAxisId         | string          | "Y"         | ID of the Y axis to use.                                           |

!!! warning
    All `XyDataSeries` in `DataSeries` must have matching X values for proper stacking. If X arrays differ, stacking may be incorrect.

---

## Examples

### Example 1: Sales Breakdown by Region

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using Chartexa.Core;

var xAxis = new NumericAxis { Id = "X", AxisTitle = "Quarter" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Sales ($M)" };

var north = new XyDataSeries();
north.Append(new[] {1, 2, 3, 4}, new[] {10, 12, 15, 18});

var south = new XyDataSeries();
south.Append(new[] {1, 2, 3, 4}, new[] {8, 9, 11, 13});

var west = new XyDataSeries();
west.Append(new[] {1, 2, 3, 4}, new[] {7, 8, 9, 10});

var stackedMountain = new StackedMountainRenderableSeries
{
    DataSeries = new[] {north, south, west},
    FillColors = new[]
    {
        new ChartColor(30, 144, 255), // North: Dodger blue
        new ChartColor(255, 140, 0),  // South: Dark orange
        new ChartColor(34, 139, 34)   // West: Forest green
    },
    StrokeColors = new[]
    {
        new ChartColor(0, 0, 128),
        new ChartColor(255, 69, 0),
        new ChartColor(0, 100, 0)
    },
    StrokeThickness = 2
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(stackedMountain);
chart.Save("sales_by_region.png");
```

=== "Python"
```python
from chartexa import Chart

quarters = [1, 2, 3, 4]
north = [10, 12, 15, 18]
south = [8, 9, 11, 13]
west = [7, 8, 9, 10]

chart = (
    Chart(width=600, height=300)
    .stacked_mountain(
        x=quarters,
        ys=[north, south, west],
        fills=["#1E90FF", "#FF8C00", "#228B22"],
        strokes=["#000080", "#FF4500", "#006400"],
        thickness=2
    )
    .x_axis(title="Quarter")
    .y_axis(title="Sales ($M)")
    .background("#F0F8FF")
    .save("sales_by_region.png")
)
```

### Example 2: Real-Time Streaming Data

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using Chartexa.Core;

// Simulate real-time sensor readings
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (s)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Value" };

var sensorA = new XyDataSeries();
var sensorB = new XyDataSeries();
var sensorC = new XyDataSeries();

for (int t = 0; t <= 100; t += 5)
{
    sensorA.Append(t, Math.Sin(t * 0.05) * 10 + 20);
    sensorB.Append(t, Math.Cos(t * 0.05) * 8 + 15);
    sensorC.Append(t, Math.Sin(t * 0.1) * 5 + 10);
}

var stackedMountain = new StackedMountainRenderableSeries
{
    DataSeries = new[] {sensorA, sensorB, sensorC},
    FillColors = new[]
    {
        new ChartColor(255, 99, 132),
        new ChartColor(54, 162, 235),
        new ChartColor(255, 206, 86)
    },
    StrokeThickness = 2
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(stackedMountain);
chart.Save("streaming_sensors.png");
```

=== "Python"
```python
from chartexa import Chart
import numpy as np

times = np.arange(0, 105, 5)
sensor_a = np.sin(times * 0.05) * 10 + 20
sensor_b = np.cos(times * 0.05) * 8 + 15
sensor_c = np.sin(times * 0.1) * 5 + 10

chart = (
    Chart(width=800, height=400)
    .stacked_mountain(
        x=times.tolist(),
        ys=[sensor_a.tolist(), sensor_b.tolist(), sensor_c.tolist()],
        fills=["#FF6384", "#36A2EB", "#FFCE56"],
        thickness=2
    )
    .x_axis(title="Time (s)")
    .y_axis(title="Value")
    .background("#222")
    .save("streaming_sensors.png")
)
```

---

## Performance Notes

- The stacked mountain series leverages Chartexa's DirectX 12 renderer for efficient GPU-based area rendering.
- Rendering performance is optimal for up to 1 million points per series; stacking incurs minimal overhead compared to separate area charts.
- For real-time streaming, updating only the latest data points is efficient—avoid full redraws unless necessary.
- Anti-aliasing is hardware accelerated and does not significantly impact frame rate.

!!! tip "Performance Tip"
    Use DirectX 12 backend for datasets exceeding 100K points. For static charts or small datasets, Skia or WPF backends are also supported.

---

## When to Use

- Visualizing how multiple categories contribute to a total over time or across groups
- Showing composition changes (e.g., energy mix, sales by product)
- Comparing trends of individual series and their cumulative effect
- Highlighting proportional relationships in stacked data

---

## Related

- [Fast Mountain Series](mountain.md)
- [Stacked Column Series](stacked-column.md)
- [Axis Ranging](../axes/axis-ranging.md)
- [XY Data Series](../../data-series/xy-data-series.md)

---

> **Last updated:** 2024-06-13 16:25 UTC | **Status:** draft