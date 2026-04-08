---
title: "Column Series"
section: "chart-types/2d"
last_updated: "2024-06-13 15:42 UTC"
status: draft
---

# Column Series

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `FastColumnRenderableSeries` displays vertical columns (bars) for each data point, mapping to the classic column/bar chart visualization. Use this series to represent categorical or time-based data, such as sales figures, population counts, or sensor readings, where each value is shown as a distinct column.

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

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Month" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Revenue ($)" };

// Prepare data
var months = new[] { 1, 2, 3, 4, 5, 6 };
var revenue = new[] { 12000, 15000, 11000, 18000, 17500, 16000 };

// Create data series
var dataSeries = new XyDataSeries();
dataSeries.Append(months, revenue);

// Create column series
var columnSeries = new FastColumnRenderableSeries
{
    DataSeries = dataSeries,
    FillColor = new ChartColor(34, 139, 34), // Forest green
    StrokeColor = new ChartColor(0, 0, 0),   // Black border
    StrokeThickness = 1
};

// Create chart
var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(columnSeries);
```

=== "Python"

```python
from chartexa import Chart

months = [1, 2, 3, 4, 5, 6]
revenue = [12000, 15000, 11000, 18000, 17500, 16000]

chart = (
    Chart(width=600, height=400)
    .column(months, revenue, fill="#228B22", stroke="#000000", thickness=1)
    .x_axis(title="Month")
    .y_axis(title="Revenue ($)")
    .background("#F5F5F5")
    .save("monthly_revenue.png")
)
```

---

## Concepts

The column series visualizes each data point as a vertical bar, making it ideal for comparing discrete values across categories or time intervals. Each column's height corresponds to the Y-value, and the X-value determines its position. This format is widely used for business analytics, scientific data, and monitoring dashboards.

Column charts are preferred when:
- You need to compare values across categories (e.g., sales per region).
- You want to visualize time-based trends with discrete intervals (e.g., monthly totals).
- The dataset is sparse or moderate in size (hundreds to tens of thousands of points).

Chartexa's `FastColumnRenderableSeries` is optimized for real-time updates and large datasets, ensuring smooth rendering even when columns overlap or when the chart is zoomed/panned.

---

## Basic Usage

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;

// Example: Visualizing website visits per day

var days = new[] { 1, 2, 3, 4, 5, 6, 7 };
var visits = new[] { 250, 300, 280, 320, 310, 295, 340 };

var dataSeries = new XyDataSeries();
dataSeries.Append(days, visits);

var columnSeries = new FastColumnRenderableSeries
{
    DataSeries = dataSeries,
    FillColor = new ChartColor(70, 130, 180), // Steel blue
    StrokeColor = new ChartColor(255, 255, 255), // White border
    StrokeThickness = 2,
    ColumnWidth = 0.8, // Relative width (0.0-1.0)
    Opacity = 0.9
};

var chart = new ChartSurface();
chart.XAxes.Add(new NumericAxis { Id = "X", AxisTitle = "Day" });
chart.YAxes.Add(new NumericAxis { Id = "Y", AxisTitle = "Visits" });
chart.RenderableSeries.Add(columnSeries);
```

=== "Python"

```python
from chartexa import Chart

days = [1, 2, 3, 4, 5, 6, 7]
visits = [250, 300, 280, 320, 310, 295, 340]

chart = (
    Chart(width=700, height=350)
    .column(days, visits, fill="#4682B4", stroke="#FFFFFF", thickness=2, width=0.8, opacity=0.9)
    .x_axis(title="Day")
    .y_axis(title="Visits")
    .background("#E9F6FF")
    .save("weekly_visits.png")
)
```

---

## Configuration

| Property       | Type         | Default      | Description                                         |
|----------------|--------------|--------------|-----------------------------------------------------|
| `FillColor`    | ChartColor   | #4682B4      | Fill color of columns                               |
| `StrokeColor`  | ChartColor   | #000000      | Border color of columns                             |
| `StrokeThickness` | double    | 1.0          | Border thickness in pixels                          |
| `ColumnWidth`  | double       | 0.7          | Relative width (0.0-1.0) of each column             |
| `Opacity`      | double       | 1.0          | Column opacity (0.0 transparent, 1.0 opaque)        |
| `DataSeries`   | XyDataSeries | (required)   | Data source for columns                             |
| `ZIndex`       | int          | 0            | Rendering order among series                        |
| `Visible`      | bool         | true         | Whether the series is visible                       |

!!! tip "Performance Tip"
    For datasets larger than 50,000 columns, use the DirectX12 renderer for optimal performance.

---

## Examples

### Example 1: Comparing Sales Across Regions

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;

var regions = new[] { 1, 2, 3, 4, 5 };
var sales = new[] { 22000, 18500, 24000, 21000, 19500 };

var dataSeries = new XyDataSeries();
dataSeries.Append(regions, sales);

var columnSeries = new FastColumnRenderableSeries
{
    DataSeries = dataSeries,
    FillColor = new ChartColor(255, 165, 0), // Orange
    StrokeColor = new ChartColor(80, 80, 80), // Dark gray
    StrokeThickness = 1.5,
    ColumnWidth = 0.6
};

var chart = new ChartSurface();
chart.XAxes.Add(new NumericAxis { Id = "X", AxisTitle = "Region" });
chart.YAxes.Add(new NumericAxis { Id = "Y", AxisTitle = "Sales ($)" });
chart.RenderableSeries.Add(columnSeries);
```

=== "Python"

```python
from chartexa import Chart

regions = [1, 2, 3, 4, 5]
sales = [22000, 18500, 24000, 21000, 19500]

chart = (
    Chart(width=500, height=300)
    .column(regions, sales, fill="#FFA500", stroke="#505050", thickness=1.5, width=0.6)
    .x_axis(title="Region")
    .y_axis(title="Sales ($)")
    .background("#FFF8E1")
    .save("region_sales.png")
)
```

### Example 2: Real-Time Sensor Data Streaming

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;
using System.Timers;

var timeAxis = new NumericAxis { Id = "X", AxisTitle = "Seconds" };
var valueAxis = new NumericAxis { Id = "Y", AxisTitle = "Sensor Value" };

var dataSeries = new XyDataSeries();

var columnSeries = new FastColumnRenderableSeries
{
    DataSeries = dataSeries,
    FillColor = new ChartColor(0, 191, 255), // Deep sky blue
    StrokeColor = new ChartColor(30, 30, 30),
    StrokeThickness = 1,
    ColumnWidth = 0.5
};

var chart = new ChartSurface();
chart.XAxes.Add(timeAxis);
chart.YAxes.Add(valueAxis);
chart.RenderableSeries.Add(columnSeries);

// Simulate real-time streaming
var timer = new Timer(1000); // 1 second interval
int seconds = 0;
timer.Elapsed += (s, e) =>
{
    var sensorValue = GetSensorReading();
    dataSeries.Append(seconds++, sensorValue);
    chart.Refresh();
};
timer.Start();

double GetSensorReading()
{
    // Simulate sensor value
    return 100 + 20 * Math.Sin(seconds / 10.0);
}
```

=== "Python"

```python
from chartexa import Chart
import time
import math

chart = Chart(width=600, height=300)
x_values = []
y_values = []

for t in range(0, 30):
    sensor_value = 100 + 20 * math.sin(t / 10.0)
    x_values.append(t)
    y_values.append(sensor_value)
    chart.column(x_values, y_values, fill="#00BFFF", stroke="#1E1E1E", thickness=1, width=0.5)
    chart.x_axis(title="Seconds")
    chart.y_axis(title="Sensor Value")
    chart.background("#F0F8FF")
    chart.save(f"sensor_{t}.png")
    time.sleep(1)
```

!!! example "Real-Time Streaming"
    Both C# and Python examples above show how to append new data to a column series for live sensor monitoring.

---

## Performance Notes

- The `FastColumnRenderableSeries` leverages GPU acceleration via DirectX 12 for rapid rendering of thousands to millions of columns.
- Rendering speed is primarily limited by the number of columns visible and their overlap; performance remains high for up to 100,000 columns on modern hardware.
- Column series are optimized for real-time updates; appending new data points incurs minimal overhead.
- Python integration uses .NET runtime and DirectX backend where available, ensuring parity with C# performance.

!!! note
    Python requires the .NET 10 Runtime to be installed for DirectX rendering.

---

## When to Use

- Comparing values across categories (e.g., sales by region, population by city)
- Visualizing discrete time intervals (e.g., monthly totals, daily counts)
- Monitoring real-time streams with moderate data rates
- Displaying sparse datasets with clear separation between columns
- Creating dashboards or reports with categorical breakdowns

---

## Related

- [Line Series](./line-series.md)
- [Scatter Series](./scatter-series.md)
- [Numeric Axis](../axes/numeric-axis.md)
- [Axis Ranging](../axes/axis-ranging.md)

---

> **Last updated:** 2024-06-13 15:42 UTC | **Status:** draft