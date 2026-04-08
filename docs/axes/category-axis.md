---
title: "Category Axis"
section: "axes"
last_updated: "2024-06-13 15:45 UTC"
status: draft
---

# Category Axis

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `CategoryAxis` displays categorical data along an axis, mapping string labels or discrete categories to positions on the chart. Use it when your data is organized by named groups, such as product names, months, or event types, rather than numeric or date values.

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
using Chartexa.Rendering.Series;

// Create a CategoryAxis for the X axis
var xAxis = new CategoryAxis
{
    Id = "X",
    AxisTitle = "Month",
    Categories = new[] { "Jan", "Feb", "Mar", "Apr", "May" }
};

// Numeric Y axis
var yAxis = new NumericAxis
{
    Id = "Y",
    AxisTitle = "Sales (USD)"
};

// Data for each month
var dataSeries = new XyDataSeries();
dataSeries.Append(new[] { 0, 1, 2, 3, 4 }, new[] { 12000, 15000, 18000, 13000, 17000 });

// Renderable series
var columnSeries = new FastColumnRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(34, 139, 34), // Forest green
    FillColor = new ChartColor(144, 238, 144), // Light green
    StrokeThickness = 2
};
```

=== "Python"

```python
from chartexa import Chart

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [12000, 15000, 18000, 13000, 17000]

chart = (
    Chart(width=600, height=400)
    .category_axis(categories=months, axis_title="Month")
    .numeric_axis(axis_title="Sales (USD)")
    .column(range(len(months)), sales, fill="#90EE90", stroke="#228B22", thickness=2)
    .background("#F5F5F5")
    .save("monthly_sales.png")
)
```

---

## Concepts

The `CategoryAxis` is designed for charting data organized by discrete, named groups rather than continuous values. It maps string labels (categories) to evenly spaced positions along the axis. This is ideal for visualizing data like sales per product, survey responses, or event counts per category.

Unlike numeric or datetime axes, the `CategoryAxis` does not interpret values as continuous. Instead, each label represents a distinct group, and data points are positioned according to their category index. You typically use a `CategoryAxis` for bar, column, or categorical line charts.

The axis automatically handles label placement, spacing, and tick generation based on the provided categories. It supports custom ordering and can be styled to match your application's theme.

---

## Basic Usage

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.Series;

// Define categories
string[] products = { "Laptop", "Tablet", "Phone", "Monitor" };
double[] unitsSold = { 320, 210, 450, 180 };

// Create axes
var xAxis = new CategoryAxis
{
    Id = "X",
    AxisTitle = "Product",
    Categories = products,
    LabelRotation = 30, // Rotate labels for readability
    TickSpacing = 1
};

var yAxis = new NumericAxis
{
    Id = "Y",
    AxisTitle = "Units Sold",
    AutoRange = true
};

// Prepare data series (indices map to categories)
var dataSeries = new XyDataSeries();
dataSeries.Append(new[] { 0, 1, 2, 3 }, unitsSold);

// Create column series
var columnSeries = new FastColumnRenderableSeries
{
    DataSeries = dataSeries,
    FillColor = new ChartColor(70, 130, 180), // Steel blue
    StrokeColor = new ChartColor(25, 25, 112), // Midnight blue
    StrokeThickness = 2
};

// Add axes and series to chart (pseudo-code, depends on your chart container)
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(columnSeries);
```

=== "Python"

```python
from chartexa import Chart

products = ["Laptop", "Tablet", "Phone", "Monitor"]
units_sold = [320, 210, 450, 180]

chart = (
    Chart(width=500, height=350)
    .category_axis(categories=products, axis_title="Product", label_rotation=30)
    .numeric_axis(axis_title="Units Sold")
    .column(range(len(products)), units_sold, fill="#4682B4", stroke="#191970", thickness=2)
    .background("#E6F2FF")
    .save("product_sales.png")
)
```

---

## Configuration

| Property       | Type                | Default         | Description                                                |
|----------------|---------------------|-----------------|------------------------------------------------------------|
| `Categories`   | string[] / list     | Required        | List of category labels for the axis.                      |
| `AxisTitle`    | string              | ""              | Title displayed on the axis.                               |
| `LabelRotation`| double / float      | 0               | Angle (degrees) to rotate category labels.                 |
| `TickSpacing`  | int                 | 1               | Spacing between ticks (in category units).                 |
| `ShowTicks`    | bool                | true            | Whether to display axis ticks.                             |
| `ShowLabels`   | bool                | true            | Whether to display category labels.                        |
| `Id`           | string              | ""              | Unique identifier for the axis.                            |
| `Visible`      | bool                | true            | Whether the axis is visible.                               |
| `LabelStyle`   | AxisLabelStyle      | Default         | Style options for axis labels (font, color, etc.).         |
| `TickStyle`    | AxisTickStyle       | Default         | Style options for axis ticks.                              |

!!! tip "Label Rotation"
    Use `LabelRotation` to improve readability when category labels are long or overlap.

---

## Examples

### Example 1: Survey Results by Category

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.Series;

string[] responses = { "Satisfied", "Neutral", "Unsatisfied" };
double[] counts = { 85, 30, 15 };

var xAxis = new CategoryAxis
{
    Id = "X",
    AxisTitle = "Response",
    Categories = responses,
    LabelRotation = 0
};

var yAxis = new NumericAxis
{
    Id = "Y",
    AxisTitle = "Count"
};

var dataSeries = new XyDataSeries();
dataSeries.Append(new[] { 0, 1, 2 }, counts);

var barSeries = new FastColumnRenderableSeries
{
    DataSeries = dataSeries,
    FillColor = new ChartColor(255, 165, 0), // Orange
    StrokeColor = new ChartColor(255, 140, 0), // Dark orange
    StrokeThickness = 2
};
```

=== "Python"

```python
from chartexa import Chart

responses = ["Satisfied", "Neutral", "Unsatisfied"]
counts = [85, 30, 15]

chart = (
    Chart(width=400, height=300)
    .category_axis(categories=responses, axis_title="Response")
    .numeric_axis(axis_title="Count")
    .column(range(len(responses)), counts, fill="#FFA500", stroke="#FF8C00", thickness=2)
    .background("#FFF8E1")
    .save("survey_results.png")
)
```

---

### Example 2: Event Timeline

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.Series;

string[] events = { "Start", "Checkpoint", "Finish" };
double[] times = { 0, 45, 90 };

var xAxis = new CategoryAxis
{
    Id = "X",
    AxisTitle = "Event",
    Categories = events
};

var yAxis = new NumericAxis
{
    Id = "Y",
    AxisTitle = "Time (s)"
};

var dataSeries = new XyDataSeries();
dataSeries.Append(new[] { 0, 1, 2 }, times);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(0, 128, 255), // Blue
    StrokeThickness = 2
};
```

=== "Python"

```python
from chartexa import Chart

events = ["Start", "Checkpoint", "Finish"]
times = [0, 45, 90]

chart = (
    Chart(width=500, height=250)
    .category_axis(categories=events, axis_title="Event")
    .numeric_axis(axis_title="Time (s)")
    .line(range(len(events)), times, stroke="#0080FF", thickness=2)
    .background("#E0F7FA")
    .save("event_timeline.png")
)
```

---

### Example 3: Custom Category Ordering

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.Series;

string[] priorities = { "High", "Medium", "Low" };
double[] tickets = { 40, 60, 20 };

// Custom ordering: show "Medium" first
string[] customOrder = { "Medium", "High", "Low" };

var xAxis = new CategoryAxis
{
    Id = "X",
    AxisTitle = "Priority",
    Categories = customOrder
};

var yAxis = new NumericAxis
{
    Id = "Y",
    AxisTitle = "Tickets"
};

var dataSeries = new XyDataSeries();
dataSeries.Append(new[] { 0, 1, 2 }, new[] { 60, 40, 20 }); // Data matches custom order

var columnSeries = new FastColumnRenderableSeries
{
    DataSeries = dataSeries,
    FillColor = new ChartColor(255, 99, 71), // Tomato
    StrokeColor = new ChartColor(139, 0, 0), // Dark red
    StrokeThickness = 2
};
```

=== "Python"

```python
from chartexa import Chart

priorities = ["Medium", "High", "Low"]
tickets = [60, 40, 20]

chart = (
    Chart(width=400, height=300)
    .category_axis(categories=priorities, axis_title="Priority")
    .numeric_axis(axis_title="Tickets")
    .column(range(len(priorities)), tickets, fill="#FF6347", stroke="#8B0000", thickness=2)
    .background("#FFF0F0")
    .save("ticket_priority.png")
)
```

---

## Performance Notes

The `CategoryAxis` is lightweight and optimized for charts with up to several thousand categories. Rendering performance depends on the number of labels and their length:

- For charts with fewer than 100 categories, label rendering is fast and smooth.
- For 100–1000 categories, consider rotating or hiding labels to avoid overlap and maintain performance.
- For very large category sets (>1000), use `ShowLabels=false` or custom label formatting to reduce rendering load.

!!! tip "Performance Tip"
    Hide labels or reduce label rotation for charts with many categories to improve rendering speed.

!!! note
    The DirectX 12 backend efficiently handles axis rendering, but excessive label text can impact layout performance.

---

## When to Use

- Visualizing data grouped by discrete categories (e.g., product, region, event type)
- Bar, column, or categorical line charts
- Survey results, frequency counts, or event timelines
- When axis values are string labels, not numbers or dates
- Custom ordering or grouping of axis labels

---

## Related

- [Numeric Axis](numeric-axis.md)
- [Datetime Axis](datetime-axis.md)
- [Axis Ranging](axis-ranging.md)
- [Column Chart](../chart-types/2d/column-chart.md)
- [Bar Chart](../chart-types/2d/bar-chart.md)

---

> **Last updated:** 2024-06-13 15:45 UTC | **Status:** draft