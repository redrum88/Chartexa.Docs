---
title: "Axis System Overview"
section: "axes"
last_updated: "2024-06-13 12:10 UTC"
status: draft
---

# Axis System Overview

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

Chartexa's axis system provides flexible and powerful support for chart axes, including the `AxisCore` base class, automatic range calculation, customizable tick and label generation, and multi-axis layouts. Axes define how data is mapped visually, control scaling, and provide context for interpretation. The axis system is central to all chart types and supports numeric, datetime, and categorical axes.

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
using Chartexa.Rendering;
using Chartexa.Charts;

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (s)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Temperature (°C)" };

// Create data series
var dataSeries = new XyDataSeries();
dataSeries.Append(
    new double[] { 0, 1, 2, 3, 4, 5 },
    new double[] { 22.5, 23.1, 24.0, 23.8, 24.5, 25.0 }
);

// Create renderable series
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(255, 99, 71),   // Tomato
    StrokeThickness = 2
};

// Create chart and add axes/series
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(lineSeries);

// Render to window or export
chart.Show();
```

=== "Python"

```python
from chartexa import Chart

# Time (seconds) and temperature (°C) data
x = [0, 1, 2, 3, 4, 5]
y = [22.5, 23.1, 24.0, 23.8, 24.5, 25.0]

chart = (
    Chart(width=800, height=400)
    .numeric_axis(id="X", title="Time (s)")
    .numeric_axis(id="Y", title="Temperature (°C)")
    .line(x, y, stroke="#FF6347", thickness=2)
    .background("#F5F5F5")
    .save("temperature_chart.png")
)
```

---

## Concepts

Chartexa's axis system is responsible for mapping data values to visual coordinates on the chart. Each axis determines the scale, range, and labeling for its dimension (X, Y, or additional axes). Axes can be numeric, datetime, or categorical, and are built on the `AxisCore` base class, which provides common functionality such as auto-ranging, tick generation, and label formatting.

Auto-ranging ensures that axes automatically adjust their visible range to fit the data, while custom range settings allow for fixed or user-defined limits. Tick generation produces major and minor tick marks, which are used for grid lines and labels. Label formatting controls how values are displayed, including number formats, date/time formats, and custom strings.

Multi-axis layouts allow you to add multiple axes to a chart, supporting scenarios like dual Y axes, overlaying different scales, or plotting multiple series with distinct units. The axis system is designed for flexibility and performance, enabling real-time updates and large-scale data visualization.

---

## Basic Usage

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering;
using Chartexa.Charts;

// Create a numeric X axis with auto-ranging
var xAxis = new NumericAxis
{
    Id = "X",
    AxisTitle = "Elapsed Time (s)",
    AutoRange = AutoRange.Always,
    MajorTickInterval = 1.0,
    MinorTickInterval = 0.2,
    LabelFormat = "F1" // One decimal place
};

// Create a numeric Y axis with fixed range
var yAxis = new NumericAxis
{
    Id = "Y",
    AxisTitle = "Voltage (V)",
    AutoRange = AutoRange.Never,
    VisibleRange = new AxisRange(0, 10),
    MajorTickInterval = 2.0,
    MinorTickInterval = 0.5,
    LabelFormat = "F2" // Two decimal places
};

// Add axes to chart
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);

// Add a data series and renderable series
var dataSeries = new XyDataSeries();
dataSeries.Append(
    new double[] { 0, 1, 2, 3, 4 },
    new double[] { 2.5, 4.2, 6.8, 7.1, 9.0 }
);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(34, 139, 34), // Forest green
    StrokeThickness = 2
};

chart.RenderableSeries.Add(lineSeries);
chart.Show();
```

=== "Python"

```python
from chartexa import Chart

# Elapsed time and voltage data
x = [0, 1, 2, 3, 4]
y = [2.5, 4.2, 6.8, 7.1, 9.0]

chart = (
    Chart(width=600, height=300)
    .numeric_axis(id="X", title="Elapsed Time (s)", auto_range=True, major_tick=1.0, minor_tick=0.2, label_format=".1f")
    .numeric_axis(id="Y", title="Voltage (V)", auto_range=False, range=(0, 10), major_tick=2.0, minor_tick=0.5, label_format=".2f")
    .line(x, y, stroke="#228B22", thickness=2)
    .background("#E8F5E9")
    .show()
)
```

---

## Configuration

| Property         | Type              | Default           | Description                                                  |
|------------------|-------------------|-------------------|--------------------------------------------------------------|
| `Id`             | string            | `null`            | Unique identifier for the axis.                              |
| `AxisTitle`      | string            | `""`              | Title displayed on the axis.                                 |
| `AutoRange`      | enum (`Always`, `Once`, `Never`) | `Always` | Controls auto-ranging behavior.                              |
| `VisibleRange`   | `AxisRange`       | Data range        | Sets the visible range for the axis.                         |
| `MajorTickInterval` | double         | Auto              | Interval between major ticks.                                |
| `MinorTickInterval` | double         | Auto              | Interval between minor ticks.                                |
| `LabelFormat`    | string            | Auto              | Format string for axis labels (e.g., `"F2"`, `".2f"`).       |
| `TickLabelStyle` | object            | Default           | Style for tick labels (font, color, size).                   |
| `AxisPosition`   | enum (`Left`, `Right`, `Top`, `Bottom`) | `Bottom`/`Left` | Position of the axis on the chart.                           |
| `IsVisible`      | bool              | `true`            | Controls axis visibility.                                    |
| `IsPrimary`      | bool              | `true`            | Marks axis as primary for its direction.                     |
| `GridLines`      | bool              | `true`            | Show/hide grid lines for this axis.                          |
| `TickLength`     | double            | `5.0`             | Length of tick marks in pixels.                              |

!!! tip "Performance Tip"
    For charts with more than 100,000 points, keep `AutoRange` set to `Once` or `Never` to avoid unnecessary recalculation during streaming.

---

## Examples

### Example 1: Dual Y Axes for Multiple Units

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering;
using Chartexa.Charts;

// Primary Y axis: Temperature
var yAxis1 = new NumericAxis
{
    Id = "Temperature",
    AxisTitle = "Temperature (°C)",
    AxisPosition = AxisPosition.Left,
    IsPrimary = true
};

// Secondary Y axis: Humidity
var yAxis2 = new NumericAxis
{
    Id = "Humidity",
    AxisTitle = "Humidity (%)",
    AxisPosition = AxisPosition.Right,
    IsPrimary = false
};

// X axis: Time
var xAxis = new NumericAxis
{
    Id = "Time",
    AxisTitle = "Time (h)"
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis1);
chart.Axes.Add(yAxis2);

// Data series for temperature and humidity
var tempSeries = new XyDataSeries();
tempSeries.Append(new double[] { 0, 1, 2, 3 }, new double[] { 22, 23, 24, 25 });

var humiditySeries = new XyDataSeries();
humiditySeries.Append(new double[] { 0, 1, 2, 3 }, new double[] { 55, 60, 58, 62 });

var tempLine = new FastLineRenderableSeries
{
    DataSeries = tempSeries,
    StrokeColor = new ChartColor(255, 140, 0), // Dark orange
    YAxisId = "Temperature"
};

var humidityLine = new FastLineRenderableSeries
{
    DataSeries = humiditySeries,
    StrokeColor = new ChartColor(70, 130, 180), // Steel blue
    YAxisId = "Humidity"
};

chart.RenderableSeries.Add(tempLine);
chart.RenderableSeries.Add(humidityLine);
chart.Show();
```

=== "Python"

```python
from chartexa import Chart

# Time, temperature, humidity data
time = [0, 1, 2, 3]
temp = [22, 23, 24, 25]
humidity = [55, 60, 58, 62]

chart = (
    Chart(width=700, height=400)
    .numeric_axis(id="Time", title="Time (h)")
    .numeric_axis(id="Temperature", title="Temperature (°C)", position="left", primary=True)
    .numeric_axis(id="Humidity", title="Humidity (%)", position="right", primary=False)
    .line(time, temp, stroke="#FF8C00", thickness=2, y_axis="Temperature")
    .line(time, humidity, stroke="#4682B4", thickness=2, y_axis="Humidity")
    .background("#F0F8FF")
    .show()
)
```

### Example 2: Custom Tick and Label Formatting

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering;
using Chartexa.Charts;

// X axis: DateTime
var xAxis = new DateTimeAxis
{
    Id = "Date",
    AxisTitle = "Date",
    LabelFormat = "yyyy-MM-dd",
    MajorTickInterval = 86400, // One day in seconds
    MinorTickInterval = 3600   // One hour in seconds
};

var yAxis = new NumericAxis
{
    Id = "Price",
    AxisTitle = "Price ($)",
    LabelFormat = "C2" // Currency, two decimals
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);

// Data series
var dates = new DateTime[]
{
    new DateTime(2024, 6, 10),
    new DateTime(2024, 6, 11),
    new DateTime(2024, 6, 12),
    new DateTime(2024, 6, 13)
};
var prices = new double[] { 101.25, 102.10, 103.55, 104.20 };

var dataSeries = new XyDataSeries<DateTime, double>();
dataSeries.Append(dates, prices);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(0, 128, 128), // Teal
    StrokeThickness = 2
};

chart.RenderableSeries.Add(lineSeries);
chart.Show();
```

=== "Python"

```python
from chartexa import Chart
from datetime import datetime

dates = [
    datetime(2024, 6, 10),
    datetime(2024, 6, 11),
    datetime(2024, 6, 12),
    datetime(2024, 6, 13)
]
prices = [101.25, 102.10, 103.55, 104.20]

chart = (
    Chart(width=650, height=350)
    .datetime_axis(id="Date", title="Date", label_format="%Y-%m-%d", major_tick=86400, minor_tick=3600)
    .numeric_axis(id="Price", title="Price ($)", label_format="$,.2f")
    .line(dates, prices, stroke="#008080", thickness=2)
    .background("#FFF")
    .show()
)
```

### Example 3: Categorical Axis for Bar Chart

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering;
using Chartexa.Charts;

// Categorical X axis
var xAxis = new CategoryAxis
{
    Id = "Category",
    AxisTitle = "Product",
    Categories = new[] { "A", "B", "C", "D" }
};

var yAxis = new NumericAxis
{
    Id = "Sales",
    AxisTitle = "Sales (units)"
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);

var dataSeries = new XyDataSeries<string, double>();
dataSeries.Append(new[] { "A", "B", "C", "D" }, new double[] { 120, 150, 90, 180 });

var columnSeries = new FastColumnRenderableSeries
{
    DataSeries = dataSeries,
    FillColor = new ChartColor(30, 144, 255), // Dodger blue
};

chart.RenderableSeries.Add(columnSeries);
chart.Show();
```

=== "Python"

```python
from chartexa import Chart

products = ["A", "B", "C", "D"]
sales = [120, 150, 90, 180]

chart = (
    Chart(width=500, height=300)
    .category_axis(id="Category", title="Product", categories=products)
    .numeric_axis(id="Sales", title="Sales (units)")
    .column(products, sales, fill="#1E90FF")
    .background("#F9F9F9")
    .show()
)
```

---

## Performance Notes

Chartexa's axis system is optimized for real-time updates and large datasets. Auto-ranging is efficient for up to 100,000 points, but for streaming or very large datasets, set `AutoRange` to `Once` or `Never` to avoid repeated recalculation. Tick and label generation are cached and only recomputed when the axis range changes.

Multi-axis layouts and custom label formatting have negligible performance impact unless using complex formatting functions or thousands of axes. DirectX 12 rendering backend ensures smooth axis drawing, even with dense tick marks.

!!! tip "Performance Tip"
    For charts with frequent data updates, minimize axis range changes to reduce layout recalculation.

---

## When to Use

- When you need to visualize data with numeric, datetime, or categorical axes.
- For charts requiring auto-ranging, custom tick intervals, or label formatting.
- When plotting multiple series with different units or scales (multi-axis).
- To provide context and scale for any chart type (line, scatter, column, etc.).
- For dashboards requiring synchronized axes across multiple charts.

---

## Related

- [Numeric Axis](numeric-axis.md)
- [DateTime Axis](datetime-axis.md)
- [Category Axis](category-axis.md)
- [Axis Ranging](axis-ranging.md)
- [Axis Customization](axis-customization.md)

---

> **Last updated:** 2024-06-13 12:10 UTC | **Status:** draft