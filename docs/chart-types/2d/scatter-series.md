---
title: "Scatter Series"
section: "chart-types/2d"
last_updated: "2024-06-10 14:42 UTC"
status: draft
---

# Scatter Series

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `XyScatterRenderableSeries` displays XY scatter plots, visualizing discrete data points with configurable marker types, sizes, and colors. Use scatter series to highlight individual observations, outliers, or clusters in your data.

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
using Chartexa.Core.Markers;
using Chartexa.Core.Chart;

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Temperature (°C)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Reaction Rate" };

// Create scatter data
var xValues = new double[] { 20.1, 22.5, 24.3, 25.0, 27.8 };
var yValues = new double[] { 1.2, 1.5, 1.7, 2.0, 2.3 };
var dataSeries = new XyDataSeries();
dataSeries.Append(xValues, yValues);

// Create scatter series with circle markers
var scatterSeries = new XyScatterRenderableSeries
{
    DataSeries = dataSeries,
    MarkerType = MarkerType.Circle,
    MarkerSize = 8,
    MarkerFill = new ChartColor(255, 99, 71), // Tomato
    MarkerStroke = new ChartColor(70, 130, 180), // Steel Blue
    MarkerStrokeThickness = 2
};

// Create chart and add axes/series
var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(scatterSeries);
```

=== "Python"

```python
from chartexa import Chart

x_values = [20.1, 22.5, 24.3, 25.0, 27.8]
y_values = [1.2, 1.5, 1.7, 2.0, 2.3]

chart = (
    Chart(width=600, height=400)
    .scatter(
        x_values, y_values,
        marker="circle",
        size=8,
        fill="#FF6347",    # Tomato
        stroke="#4682B4",  # Steel Blue
        stroke_thickness=2
    )
    .x_axis(title="Temperature (°C)")
    .y_axis(title="Reaction Rate")
    .background("#F5F5F5")
    .save("scatter_quickstart.png")
)
```

---

## Concepts

The scatter series visualizes individual data points as markers on a 2D plot, mapping each X and Y value pair to a unique position. Unlike line or column charts, scatter plots do not connect points, making them ideal for representing discrete measurements, experimental results, or relationships between variables.

Use scatter series when you need to:
- Display distributions, clusters, or outliers
- Compare two quantitative variables
- Visualize correlations without implying continuity

The series supports various marker shapes (circle, square, triangle, cross, diamond), customizable colors, and sizes. You can overlay multiple scatter series for comparative analysis or combine with other chart types.

---

## Basic Usage

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Markers;
using Chartexa.Core.Chart;

// Example: Visualizing city population vs. area

var cityNames = new[] { "Berlin", "Paris", "London", "Rome", "Madrid" };
var cityAreas = new double[] { 891.8, 105.4, 1572, 1285, 604.3 }; // km²
var cityPopulations = new double[] { 3.6, 2.1, 8.9, 2.8, 3.2 }; // millions

var xAxis = new NumericAxis { Id = "Area", AxisTitle = "City Area (km²)" };
var yAxis = new NumericAxis { Id = "Population", AxisTitle = "Population (millions)" };

var dataSeries = new XyDataSeries();
dataSeries.Append(cityAreas, cityPopulations);

var scatterSeries = new XyScatterRenderableSeries
{
    DataSeries = dataSeries,
    MarkerType = MarkerType.Diamond,
    MarkerSize = 12,
    MarkerFill = new ChartColor(34, 139, 34), // Forest Green
    MarkerStroke = new ChartColor(0, 0, 0),   // Black
    MarkerStrokeThickness = 1
};

var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(scatterSeries);

// Optionally, add tooltips or legend
```

=== "Python"

```python
from chartexa import Chart

city_areas = [891.8, 105.4, 1572, 1285, 604.3]  # km²
city_populations = [3.6, 2.1, 8.9, 2.8, 3.2]    # millions

chart = (
    Chart(width=700, height=400)
    .scatter(
        city_areas, city_populations,
        marker="diamond",
        size=12,
        fill="#228B22",    # Forest Green
        stroke="#000000",  # Black
        stroke_thickness=1
    )
    .x_axis(title="City Area (km²)")
    .y_axis(title="Population (millions)")
    .background("#E6E6FA")
    .save("city_scatter.png")
)
```

---

## Configuration

| Property              | Type         | Default      | Description                                                |
|-----------------------|-------------|--------------|------------------------------------------------------------|
| `MarkerType`          | enum         | Circle       | Shape of marker: Circle, Square, Triangle, Cross, Diamond  |
| `MarkerSize`          | int          | 8            | Diameter (pixels) of marker                                |
| `MarkerFill`          | ChartColor   | #4682B4      | Fill color of marker                                       |
| `MarkerStroke`        | ChartColor   | #FFFFFF      | Stroke color of marker border                              |
| `MarkerStrokeThickness`| int         | 1            | Border thickness (pixels)                                  |
| `DataSeries`          | XyDataSeries | (required)   | Data source for X and Y values                             |
| `Opacity`             | double       | 1.0          | Marker transparency (0.0-1.0)                              |
| `IsVisible`           | bool         | true         | Show/hide the series                                       |
| `LegendLabel`         | string       | ""           | Label for legend display                                   |

!!! tip "Marker Customization"
    Use `MarkerType` and `MarkerFill` to distinguish multiple scatter series visually.

---

## Examples

### Example 1: Comparing Student Scores

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Markers;
using Chartexa.Core.Chart;

// Math vs. Science scores for students
var mathScores = new double[] { 85, 90, 78, 92, 88, 76 };
var scienceScores = new double[] { 82, 95, 80, 89, 91, 73 };

var xAxis = new NumericAxis { Id = "Math", AxisTitle = "Math Score" };
var yAxis = new NumericAxis { Id = "Science", AxisTitle = "Science Score" };

var dataSeries = new XyDataSeries();
dataSeries.Append(mathScores, scienceScores);

var scatterSeries = new XyScatterRenderableSeries
{
    DataSeries = dataSeries,
    MarkerType = MarkerType.Square,
    MarkerSize = 10,
    MarkerFill = new ChartColor(255, 215, 0), // Gold
    MarkerStroke = new ChartColor(105, 105, 105), // Dim Gray
    MarkerStrokeThickness = 2
};

var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(scatterSeries);
```

=== "Python"

```python
from chartexa import Chart

math_scores = [85, 90, 78, 92, 88, 76]
science_scores = [82, 95, 80, 89, 91, 73]

chart = (
    Chart(width=600, height=400)
    .scatter(
        math_scores, science_scores,
        marker="square",
        size=10,
        fill="#FFD700",    # Gold
        stroke="#696969",  # Dim Gray
        stroke_thickness=2
    )
    .x_axis(title="Math Score")
    .y_axis(title="Science Score")
    .background("#FFFACD")
    .save("student_scores.png")
)
```

### Example 2: Overlaying Multiple Scatter Series

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Markers;
using Chartexa.Core.Chart;

// Two datasets: Experiment A and B
var expA_x = new double[] { 10, 15, 20, 25 };
var expA_y = new double[] { 5, 7, 8, 10 };
var expB_x = new double[] { 12, 18, 22, 28 };
var expB_y = new double[] { 6, 8, 9, 12 };

var xAxis = new NumericAxis { Id = "Input", AxisTitle = "Input Value" };
var yAxis = new NumericAxis { Id = "Output", AxisTitle = "Output Value" };

var dataA = new XyDataSeries();
dataA.Append(expA_x, expA_y);

var dataB = new XyDataSeries();
dataB.Append(expB_x, expB_y);

var scatterA = new XyScatterRenderableSeries
{
    DataSeries = dataA,
    MarkerType = MarkerType.Circle,
    MarkerSize = 8,
    MarkerFill = new ChartColor(30, 144, 255), // Dodger Blue
    MarkerStroke = new ChartColor(0, 0, 0),
    MarkerStrokeThickness = 1,
    LegendLabel = "Experiment A"
};

var scatterB = new XyScatterRenderableSeries
{
    DataSeries = dataB,
    MarkerType = MarkerType.Triangle,
    MarkerSize = 8,
    MarkerFill = new ChartColor(255, 69, 0), // Orange Red
    MarkerStroke = new ChartColor(0, 0, 0),
    MarkerStrokeThickness = 1,
    LegendLabel = "Experiment B"
};

var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(scatterA);
chart.RenderableSeries.Add(scatterB);
```

=== "Python"

```python
from chartexa import Chart

expA_x = [10, 15, 20, 25]
expA_y = [5, 7, 8, 10]
expB_x = [12, 18, 22, 28]
expB_y = [6, 8, 9, 12]

chart = (
    Chart(width=650, height=400)
    .scatter(
        expA_x, expA_y,
        marker="circle",
        size=8,
        fill="#1E90FF",    # Dodger Blue
        stroke="#000000",
        legend="Experiment A"
    )
    .scatter(
        expB_x, expB_y,
        marker="triangle",
        size=8,
        fill="#FF4500",    # Orange Red
        stroke="#000000",
        legend="Experiment B"
    )
    .x_axis(title="Input Value")
    .y_axis(title="Output Value")
    .background("#F0F8FF")
    .legend(position="top-right")
    .save("overlay_scatter.png")
)
```

### Example 3: Highlighting Outliers

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Markers;
using Chartexa.Core.Chart;

// Main data
var xValues = new double[] { 1, 2, 3, 4, 5, 6, 7 };
var yValues = new double[] { 2, 4, 6, 8, 10, 12, 14 };

// Outlier
var outlierX = new double[] { 5.5 };
var outlierY = new double[] { 25 };

var xAxis = new NumericAxis { Id = "X", AxisTitle = "X Value" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Y Value" };

var mainSeries = new XyDataSeries();
mainSeries.Append(xValues, yValues);

var outlierSeries = new XyDataSeries();
outlierSeries.Append(outlierX, outlierY);

var scatterMain = new XyScatterRenderableSeries
{
    DataSeries = mainSeries,
    MarkerType = MarkerType.Circle,
    MarkerSize = 8,
    MarkerFill = new ChartColor(70, 130, 180), // Steel Blue
    MarkerStroke = new ChartColor(255, 255, 255),
    MarkerStrokeThickness = 1
};

var scatterOutlier = new XyScatterRenderableSeries
{
    DataSeries = outlierSeries,
    MarkerType = MarkerType.Cross,
    MarkerSize = 14,
    MarkerFill = new ChartColor(255, 0, 0), // Red
    MarkerStroke = new ChartColor(0, 0, 0),
    MarkerStrokeThickness = 2
};

var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(scatterMain);
chart.RenderableSeries.Add(scatterOutlier);
```

=== "Python"

```python
from chartexa import Chart

x_values = [1, 2, 3, 4, 5, 6, 7]
y_values = [2, 4, 6, 8, 10, 12, 14]
outlier_x = [5.5]
outlier_y = [25]

chart = (
    Chart(width=600, height=400)
    .scatter(
        x_values, y_values,
        marker="circle",
        size=8,
        fill="#4682B4",    # Steel Blue
        stroke="#FFFFFF"
    )
    .scatter(
        outlier_x, outlier_y,
        marker="cross",
        size=14,
        fill="#FF0000",    # Red
        stroke="#000000",
        stroke_thickness=2
    )
    .x_axis(title="X Value")
    .y_axis(title="Y Value")
    .background("#F8F8FF")
    .save("outlier_scatter.png")
)
```

---

## Performance Notes

Scatter series are optimized for large datasets using Chartexa's DirectX 12 renderer. Rendering up to 1 million points is possible with minimal latency (<50 ms) on modern GPUs. Marker rendering is GPU-accelerated; performance depends on marker complexity and size.

- Marker shapes with fewer vertices (circle, square) render faster than complex shapes (diamond, triangle).
- For datasets exceeding 500,000 points, prefer smaller marker sizes and avoid transparency for best throughput.
- Python integration leverages the .NET backend; ensure .NET 10 Runtime is installed.

!!! tip "Performance Tip"
    Use DirectX 12 backend for scatter plots with more than 100,000 points. Skia and WPF backends are suitable for smaller datasets (<10,000 points).

!!! note
    Python requires the .NET 10 Runtime to be installed.

---

## When to Use

- Visualizing relationships between two quantitative variables
- Displaying experimental or observational data without implied continuity
- Highlighting outliers, clusters, or trends in large datasets
- Overlaying multiple datasets for comparative analysis
- Representing real-time sensor or telemetry data as discrete points

---

## Related

- [Fast Line Series](fast-line-series.md)
- [Numeric Axis](../axes/numeric-axis.md)
- [Legend and Tooltips](../interaction/legend-tooltip.md)
- [Theme Engine](../theming/theme-engine.md)

---

> **Last updated:** 2024-06-10 14:42 UTC | **Status:** draft