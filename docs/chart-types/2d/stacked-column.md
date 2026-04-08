---
title: "Stacked Column Series"
section: "chart-types/2d"
last_updated: "2024-06-12 14:10 UTC"
status: draft
---

# Stacked Column Series

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `StackedColumnRenderableSeries` enables visualization of multiple column/bar series stacked vertically, allowing you to compare the contribution of each series to the total at each category or x-value. Use stacked columns to display grouped categorical data, such as sales by region, population by age group, or financial breakdowns.

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
var xAxis = new CategoryAxis { Id = "X", AxisTitle = "Year" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Revenue (M USD)" };

// Data for three product lines
var years = new[] { "2019", "2020", "2021", "2022" };
var prodA = new[] { 12.5, 14.2, 16.8, 18.1 };
var prodB = new[] { 8.3, 9.7, 11.2, 12.5 };
var prodC = new[] { 5.1, 6.4, 7.9, 8.7 };

// Create data series
var dsA = new XyDataSeries<string, double> { SeriesName = "Product A" };
dsA.Append(years, prodA);

var dsB = new XyDataSeries<string, double> { SeriesName = "Product B" };
dsB.Append(years, prodB);

var dsC = new XyDataSeries<string, double> { SeriesName = "Product C" };
dsC.Append(years, prodC);

// Create stacked column series
var stackedColumns = new StackedColumnRenderableSeries
{
    DataSeries = new[] { dsA, dsB, dsC },
    FillColors = new[]
    {
        new ChartColor(52, 152, 219),   // Blue
        new ChartColor(46, 204, 113),   // Green
        new ChartColor(231, 76, 60)     // Red
    },
    StrokeThickness = 1
};

// Create chart and add axes/series
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(stackedColumns);
```

=== "Python"
```python
from chartexa import Chart

years = ["2019", "2020", "2021", "2022"]
prod_a = [12.5, 14.2, 16.8, 18.1]
prod_b = [8.3, 9.7, 11.2, 12.5]
prod_c = [5.1, 6.4, 7.9, 8.7]

chart = (
    Chart(width=600, height=400)
    .stacked_column(
        x=years,
        y=[prod_a, prod_b, prod_c],
        fill=["#3498db", "#2ecc71", "#e74c3c"],
        legend=["Product A", "Product B", "Product C"],
        stroke="#222",
        thickness=1
    )
    .x_axis(title="Year", axis_type="category")
    .y_axis(title="Revenue (M USD)")
    .background("#f4f6f7")
    .save("stacked_column.png")
)
```

---

## Concepts

A stacked column chart displays multiple column series at each x-value, stacking them vertically so each column segment represents a series' value. The total column height at each x-value shows the sum of all series, making it easy to compare overall totals and individual contributions.

Use stacked columns when:
- You want to show how different categories contribute to a total for each x-value.
- Comparing trends across groups (e.g., sales per region per year).
- Visualizing breakdowns (e.g., population by age group).

Stacked columns are preferable over grouped columns when the sum is meaningful and you want to emphasize the total, not just individual series.

---

## Basic Usage

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using Chartexa.Core;

// Example: Energy production by source over years
var years = new[] { "2018", "2019", "2020", "2021" };
var solar = new[] { 2.1, 2.5, 3.0, 3.8 };
var wind = new[] { 3.3, 3.7, 4.2, 4.9 };
var hydro = new[] { 5.0, 5.1, 5.2, 5.3 };

// Create data series for each energy source
var dsSolar = new XyDataSeries<string, double> { SeriesName = "Solar" };
dsSolar.Append(years, solar);

var dsWind = new XyDataSeries<string, double> { SeriesName = "Wind" };
dsWind.Append(years, wind);

var dsHydro = new XyDataSeries<string, double> { SeriesName = "Hydro" };
dsHydro.Append(years, hydro);

// Configure stacked column series
var stackedColumns = new StackedColumnRenderableSeries
{
    DataSeries = new[] { dsSolar, dsWind, dsHydro },
    FillColors = new[]
    {
        new ChartColor(241, 196, 15),   // Yellow (Solar)
        new ChartColor(52, 152, 219),   // Blue (Wind)
        new ChartColor(39, 174, 96)     // Green (Hydro)
    },
    StrokeThickness = 1,
    ColumnWidth = 0.8
};

// Setup axes and chart
var xAxis = new CategoryAxis { Id = "X", AxisTitle = "Year" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Production (GW)" };

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(stackedColumns);
```

=== "Python"
```python
from chartexa import Chart

years = ["2018", "2019", "2020", "2021"]
solar = [2.1, 2.5, 3.0, 3.8]
wind = [3.3, 3.7, 4.2, 4.9]
hydro = [5.0, 5.1, 5.2, 5.3]

chart = (
    Chart(width=700, height=400)
    .stacked_column(
        x=years,
        y=[solar, wind, hydro],
        fill=["#f1c40f", "#3498db", "#27ae60"],
        legend=["Solar", "Wind", "Hydro"],
        stroke="#333",
        thickness=1,
        width=0.8
    )
    .x_axis(title="Year", axis_type="category")
    .y_axis(title="Production (GW)")
    .background("#ecf0f1")
    .save("energy_stacked_column.png")
)
```

---

## Configuration

| Property         | Type                | Default | Description                                                      |
|------------------|---------------------|---------|------------------------------------------------------------------|
| DataSeries       | array               | N/A     | Array of `XyDataSeries` to stack.                               |
| FillColors       | array               | N/A     | Array of colors for each series segment.                        |
| StrokeColor      | ChartColor / str    | #222    | Outline color for columns.                                      |
| StrokeThickness  | double              | 1       | Outline thickness in pixels.                                    |
| ColumnWidth      | double              | 0.7     | Relative width (0.0–1.0) of columns within category.            |
| LegendLabels     | array               | N/A     | Labels for each stacked series (shown in legend).               |
| TooltipEnabled   | bool                | true    | Show tooltips on hover.                                         |
| Animation        | AnimationSettings   | null    | Optional animation for column appearance.                       |
| Opacity          | double              | 1.0     | Opacity of column segments (0.0–1.0).                           |

!!! tip "Legend Configuration"
    Set `LegendLabels` to display series names in the chart legend.

!!! warning
    All `XyDataSeries` must have the same length and matching x-values for stacking.

---

## Examples

### Example 1: Financial Breakdown by Quarter

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using Chartexa.Core;

var quarters = new[] { "Q1", "Q2", "Q3", "Q4" };
var revenue = new[] { 24.5, 27.1, 29.3, 31.8 };
var expenses = new[] { 15.2, 16.7, 17.9, 18.5 };
var profit = new[] { 9.3, 10.4, 11.4, 13.3 };

var dsRevenue = new XyDataSeries<string, double> { SeriesName = "Revenue" };
dsRevenue.Append(quarters, revenue);

var dsExpenses = new XyDataSeries<string, double> { SeriesName = "Expenses" };
dsExpenses.Append(quarters, expenses);

var dsProfit = new XyDataSeries<string, double> { SeriesName = "Profit" };
dsProfit.Append(quarters, profit);

var stackedColumns = new StackedColumnRenderableSeries
{
    DataSeries = new[] { dsRevenue, dsExpenses, dsProfit },
    FillColors = new[]
    {
        new ChartColor(52, 152, 219),   // Revenue (Blue)
        new ChartColor(155, 89, 182),   // Expenses (Purple)
        new ChartColor(46, 204, 113)    // Profit (Green)
    },
    LegendLabels = new[] { "Revenue", "Expenses", "Profit" },
    StrokeThickness = 1
};

var xAxis = new CategoryAxis { Id = "X", AxisTitle = "Quarter" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Amount (M USD)" };

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(stackedColumns);
```

=== "Python"
```python
from chartexa import Chart

quarters = ["Q1", "Q2", "Q3", "Q4"]
revenue = [24.5, 27.1, 29.3, 31.8]
expenses = [15.2, 16.7, 17.9, 18.5]
profit = [9.3, 10.4, 11.4, 13.3]

chart = (
    Chart(width=800, height=400)
    .stacked_column(
        x=quarters,
        y=[revenue, expenses, profit],
        fill=["#3498db", "#9b59b6", "#2ecc71"],
        legend=["Revenue", "Expenses", "Profit"],
        stroke="#222",
        thickness=1
    )
    .x_axis(title="Quarter", axis_type="category")
    .y_axis(title="Amount (M USD)")
    .background("#f5f5f5")
    .save("financial_breakdown.png")
)
```

### Example 2: Population by Age Group

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using Chartexa.Core;

var cities = new[] { "London", "Paris", "Berlin", "Madrid" };
var children = new[] { 1.2, 1.0, 0.9, 1.1 };
var adults = new[] { 4.5, 4.2, 3.8, 4.0 };
var seniors = new[] { 0.8, 0.7, 0.6, 0.7 };

var dsChildren = new XyDataSeries<string, double> { SeriesName = "Children" };
dsChildren.Append(cities, children);

var dsAdults = new XyDataSeries<string, double> { SeriesName = "Adults" };
dsAdults.Append(cities, adults);

var dsSeniors = new XyDataSeries<string, double> { SeriesName = "Seniors" };
dsSeniors.Append(cities, seniors);

var stackedColumns = new StackedColumnRenderableSeries
{
    DataSeries = new[] { dsChildren, dsAdults, dsSeniors },
    FillColors = new[]
    {
        new ChartColor(241, 196, 15),   // Children (Yellow)
        new ChartColor(52, 152, 219),   // Adults (Blue)
        new ChartColor(149, 165, 166)   // Seniors (Gray)
    },
    LegendLabels = new[] { "Children", "Adults", "Seniors" },
    StrokeThickness = 1
};

var xAxis = new CategoryAxis { Id = "X", AxisTitle = "City" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Population (M)" };

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(stackedColumns);
```

=== "Python"
```python
from chartexa import Chart

cities = ["London", "Paris", "Berlin", "Madrid"]
children = [1.2, 1.0, 0.9, 1.1]
adults = [4.5, 4.2, 3.8, 4.0]
seniors = [0.8, 0.7, 0.6, 0.7]

chart = (
    Chart(width=700, height=400)
    .stacked_column(
        x=cities,
        y=[children, adults, seniors],
        fill=["#f1c40f", "#3498db", "#95a5a6"],
        legend=["Children", "Adults", "Seniors"],
        stroke="#555",
        thickness=1
    )
    .x_axis(title="City", axis_type="category")
    .y_axis(title="Population (M)")
    .background("#fafafa")
    .save("population_by_age.png")
)
```

### Example 3: Real-Time Streaming

!!! example "Real-Time Streaming"
    === "C#"
    ```csharp
    using Chartexa.Core.Axes;
    using Chartexa.Data.Series;
    using Chartexa.ChartTypes;
    using Chartexa.Core;
    using System.Threading.Tasks;

    var categories = new[] { "A", "B", "C", "D" };
    var ds1 = new XyDataSeries<string, double> { SeriesName = "Sensor 1" };
    var ds2 = new XyDataSeries<string, double> { SeriesName = "Sensor 2" };

    // Initialize with zeros
    ds1.Append(categories, new[] { 0.0, 0.0, 0.0, 0.0 });
    ds2.Append(categories, new[] { 0.0, 0.0, 0.0, 0.0 });

    var stackedColumns = new StackedColumnRenderableSeries
    {
        DataSeries = new[] { ds1, ds2 },
        FillColors = new[]
        {
            new ChartColor(52, 152, 219),
            new ChartColor(231, 76, 60)
        },
        StrokeThickness = 1
    };

    var chart = new Chart();
    chart.Axes.Add(new CategoryAxis { Id = "X", AxisTitle = "Channel" });
    chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Value" });
    chart.RenderableSeries.Add(stackedColumns);

    // Simulate streaming update
    Task.Run(async () =>
    {
        var rnd = new Random();
        while (true)
        {
            for (int i = 0; i < categories.Length; i++)
            {
                ds1.UpdateY(i, rnd.NextDouble() * 10);
                ds2.UpdateY(i, rnd.NextDouble() * 5);
            }
            chart.Refresh();
            await Task.Delay(500);
        }
    });
    ```

    === "Python"
    ```python
    from chartexa import Chart
    import random
    import time

    categories = ["A", "B", "C", "D"]
    sensor1 = [0, 0, 0, 0]
    sensor2 = [0, 0, 0, 0]

    chart = (
        Chart(width=600, height=300)
        .stacked_column(
            x=categories,
            y=[sensor1, sensor2],
            fill=["#3498db", "#e74c3c"],
            legend=["Sensor 1", "Sensor 2"],
            stroke="#222",
            thickness=1
        )
        .x_axis(title="Channel", axis_type="category")
        .y_axis(title="Value")
        .background("#f4f6f7")
        .show()
    )

    # Streaming update (pseudo-code)
    while True:
        for i in range(len(categories)):
            sensor1[i] = random.uniform(0, 10)
            sensor2[i] = random.uniform(0, 5)
        chart.update()
        time.sleep(0.5)
    ```

---

## Performance Notes

- The DirectX 12 renderer efficiently handles stacked columns with thousands of categories and multiple series.
- Rendering time is proportional to the number of stacked segments and categories.
- For charts with more than 100 stacked segments per category, consider reducing opacity or disabling outlines to optimize performance.
- Python integration leverages .NET backend for rendering; ensure .NET 10 Runtime is installed for optimal speed.

!!! tip "Performance Tip"
    Use DirectX 12 backend for large stacked column charts (>10,000 columns) to minimize redraw latency.

---

## When to Use

- Comparing the composition of totals across categories (e.g., sales breakdown by product).
- Visualizing grouped data where the sum is meaningful.
- Showing how multiple series contribute to a total at each x-value.
- Highlighting trends in subcategories over time or across groups.

---

## Related

- [Column Series](column.md)
- [Category Axis](../axes/category-axis.md)
- [Legend Configuration](../theming/legend.md)
- [DirectX 12 Renderer](../rendering/directx12.md)

---

> **Last updated:** 2024-06-12 14:10 UTC | **Status:** draft