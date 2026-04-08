---
title: "Numeric Axis"
section: "axes"
last_updated: "2024-06-13 15:45 UTC"
status: draft
---

# Numeric Axis

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `NumericAxis` provides a linear, double-precision axis for plotting numeric data. It is used for both X and Y axes in charts where values are continuous and quantitative, such as time series, scientific measurements, and financial data.

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
using Chartexa.Core.Chart;

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (s)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Voltage (V)" };

// Create data series
var dataSeries = new XyDataSeries();
dataSeries.Append(
    new double[] { 0, 1, 2, 3, 4, 5 },
    new double[] { 0.2, 1.5, 2.1, 3.0, 2.8, 4.2 }
);

// Create renderable series
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(34, 139, 34), // Forest green
    StrokeThickness = 2
};

// Create chart and add axes/series
var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(lineSeries);
chart.Render();
```

=== "Python"

```python
from chartexa import Chart

# Sample data
time = [0, 1, 2, 3, 4, 5]
voltage = [0.2, 1.5, 2.1, 3.0, 2.8, 4.2]

# Create chart with numeric axes
chart = (
    Chart(width=600, height=400)
    .axis_x(type="numeric", title="Time (s)")
    .axis_y(type="numeric", title="Voltage (V)")
    .line(time, voltage, stroke="#228B22", thickness=2)
    .background("#F8F8FF")
    .save("numeric_axis_quickstart.png")
)
```

---

## Concepts

The `NumericAxis` is a fundamental building block for charts that require linear scaling of numeric values. It maps double-precision data to screen coordinates, enabling accurate visualization of quantitative relationships.

Use `NumericAxis` when your data consists of real numbers, such as measurements, sensor readings, or financial values. It supports auto-ranging, manual range specification, axis titles, tick formatting, and custom grid lines.

Numeric axes are essential for time series, scatter plots, line charts, and any visualization where the axis represents a continuous numeric domain. They provide precise control over axis scaling, labeling, and appearance.

---

## Basic Usage

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering;
using Chartexa.Core.Chart;

// Configure numeric axes with custom range and formatting
var xAxis = new NumericAxis
{
    Id = "X",
    AxisTitle = "Frequency (Hz)",
    Min = 10,
    Max = 1000,
    TickLabelFormat = "F0", // Integer formatting
    MajorTickInterval = 100,
    MinorTickInterval = 20,
    ShowGridLines = true,
    GridLineColor = new ChartColor(220, 220, 220)
};

var yAxis = new NumericAxis
{
    Id = "Y",
    AxisTitle = "Amplitude (dB)",
    Min = -60,
    Max = 0,
    TickLabelFormat = "F1", // One decimal place
    MajorTickInterval = 10,
    MinorTickInterval = 2,
    ShowGridLines = true,
    GridLineColor = new ChartColor(200, 200, 255)
};

// Create data series
var dataSeries = new XyDataSeries();
dataSeries.Append(
    new double[] { 10, 50, 100, 500, 1000 },
    new double[] { -55.2, -40.5, -20.1, -5.0, -1.8 }
);

// Renderable series
var scatterSeries = new FastScatterRenderableSeries
{
    DataSeries = dataSeries,
    PointColor = new ChartColor(70, 130, 180),
    PointSize = 8
};

// Chart setup
var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(scatterSeries);
chart.Render();
```

=== "Python"

```python
from chartexa import Chart

frequency = [10, 50, 100, 500, 1000]
amplitude = [-55.2, -40.5, -20.1, -5.0, -1.8]

chart = (
    Chart(width=800, height=500)
    .axis_x(
        type="numeric",
        title="Frequency (Hz)",
        range=(10, 1000),
        major_tick=100,
        minor_tick=20,
        tick_format="{:.0f}",
        grid_color="#DCDCDC"
    )
    .axis_y(
        type="numeric",
        title="Amplitude (dB)",
        range=(-60, 0),
        major_tick=10,
        minor_tick=2,
        tick_format="{:.1f}",
        grid_color="#C8C8FF"
    )
    .scatter(frequency, amplitude, color="#4682B4", size=8)
    .background("#FFFFFF")
    .save("numeric_axis_basic_usage.png")
)
```

---

## Configuration

| Property           | Type        | Default     | Description                                             |
|--------------------|-------------|-------------|---------------------------------------------------------|
| `Id`               | string      | ""          | Unique axis identifier                                  |
| `AxisTitle`        | string      | ""          | Axis label displayed on chart                           |
| `Min`              | double?     | null        | Minimum axis value (auto-range if null)                 |
| `Max`              | double?     | null        | Maximum axis value (auto-range if null)                 |
| `MajorTickInterval`| double      | auto        | Interval between major ticks                            |
| `MinorTickInterval`| double      | auto        | Interval between minor ticks                            |
| `TickLabelFormat`  | string      | "G"         | .NET format string for tick labels                      |
| `ShowGridLines`    | bool        | true        | Display grid lines for axis                             |
| `GridLineColor`    | ChartColor  | light gray  | Color of grid lines                                     |
| `IsLogarithmic`    | bool        | false       | Use logarithmic scaling (set to true for log axis)      |
| `AutoRange`        | bool        | true        | Automatically fit axis to data range                    |
| `Inverted`         | bool        | false       | Reverse axis direction                                  |
| `Visible`          | bool        | true        | Show/hide axis                                          |

!!! tip "AutoRange"
    By default, `NumericAxis` automatically adjusts its range to fit the data. Set `AutoRange=false` and specify `Min`/`Max` for manual control.

!!! warning
    Setting `IsLogarithmic=true` on `NumericAxis` requires all data values to be positive. Negative or zero values will cause rendering errors.

---

## Examples

### Example 1: Scientific Measurement Chart

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering;
using Chartexa.Core.Chart;

// Plot temperature vs. time
var xAxis = new NumericAxis
{
    Id = "Time",
    AxisTitle = "Time (min)",
    Min = 0,
    Max = 60,
    MajorTickInterval = 10,
    TickLabelFormat = "F0"
};

var yAxis = new NumericAxis
{
    Id = "Temp",
    AxisTitle = "Temperature (°C)",
    Min = 20,
    Max = 100,
    MajorTickInterval = 10,
    TickLabelFormat = "F1"
};

var tempSeries = new XyDataSeries();
tempSeries.Append(
    new double[] { 0, 10, 20, 30, 40, 50, 60 },
    new double[] { 22.5, 30.2, 45.0, 60.1, 75.3, 90.0, 98.7 }
);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = tempSeries,
    StrokeColor = new ChartColor(255, 69, 0), // Orange-red
    StrokeThickness = 2
};

var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(lineSeries);
chart.Render();
```

=== "Python"

```python
from chartexa import Chart

time = [0, 10, 20, 30, 40, 50, 60]
temperature = [22.5, 30.2, 45.0, 60.1, 75.3, 90.0, 98.7]

chart = (
    Chart(width=700, height=400)
    .axis_x(type="numeric", title="Time (min)", range=(0, 60), major_tick=10, tick_format="{:.0f}")
    .axis_y(type="numeric", title="Temperature (°C)", range=(20, 100), major_tick=10, tick_format="{:.1f}")
    .line(time, temperature, stroke="#FF4500", thickness=2)
    .background("#FFF5E1")
    .save("numeric_axis_scientific.png")
)
```

### Example 2: Financial Data with Inverted Axis

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering;
using Chartexa.Core.Chart;

// Price vs. index with inverted Y axis
var xAxis = new NumericAxis
{
    Id = "Index",
    AxisTitle = "Index",
    Min = 1,
    Max = 5,
    MajorTickInterval = 1
};

var yAxis = new NumericAxis
{
    Id = "Price",
    AxisTitle = "Price ($)",
    Min = 100,
    Max = 200,
    Inverted = true, // Highest value at bottom
    MajorTickInterval = 20
};

var priceSeries = new XyDataSeries();
priceSeries.Append(
    new double[] { 1, 2, 3, 4, 5 },
    new double[] { 120, 150, 180, 160, 190 }
);

var columnSeries = new FastColumnRenderableSeries
{
    DataSeries = priceSeries,
    FillColor = new ChartColor(30, 144, 255)
};

var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(columnSeries);
chart.Render();
```

=== "Python"

```python
from chartexa import Chart

index = [1, 2, 3, 4, 5]
price = [120, 150, 180, 160, 190]

chart = (
    Chart(width=600, height=350)
    .axis_x(type="numeric", title="Index", range=(1, 5), major_tick=1)
    .axis_y(type="numeric", title="Price ($)", range=(100, 200), major_tick=20, inverted=True)
    .column(index, price, fill="#1E90FF")
    .background("#E6F7FF")
    .save("numeric_axis_inverted.png")
)
```

### Example 3: Logarithmic Axis

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering;
using Chartexa.Core.Chart;

// Frequency response plot with log X axis
var xAxis = new NumericAxis
{
    Id = "Freq",
    AxisTitle = "Frequency (Hz)",
    Min = 10,
    Max = 10000,
    IsLogarithmic = true,
    MajorTickInterval = 1, // Log scale: interval is exponent
    TickLabelFormat = "G"
};

var yAxis = new NumericAxis
{
    Id = "Gain",
    AxisTitle = "Gain (dB)",
    Min = -40,
    Max = 10,
    MajorTickInterval = 10
};

var freq = new double[] { 10, 100, 1000, 5000, 10000 };
var gain = new double[] { -35, -20, -5, 0, 5 };

var dataSeries = new XyDataSeries();
dataSeries.Append(freq, gain);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(255, 140, 0),
    StrokeThickness = 2
};

var chart = new ChartSurface();
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(lineSeries);
chart.Render();
```

=== "Python"

```python
from chartexa import Chart

freq = [10, 100, 1000, 5000, 10000]
gain = [-35, -20, -5, 0, 5]

chart = (
    Chart(width=800, height=400)
    .axis_x(type="numeric", title="Frequency (Hz)", range=(10, 10000), log=True)
    .axis_y(type="numeric", title="Gain (dB)", range=(-40, 10), major_tick=10)
    .line(freq, gain, stroke="#FF8C00", thickness=2)
    .background("#FFF")
    .save("numeric_axis_log.png")
)
```

---

## Performance Notes

The `NumericAxis` is optimized for real-time rendering and large datasets. Axis calculations are performed using double-precision arithmetic, ensuring accuracy for scientific and financial applications.

- DirectX 12 backend supports charts with millions of points, with axis auto-ranging and tick calculation remaining performant (<1 ms for 1M points).
- Python integration leverages .NET runtime for axis computations; performance is comparable to C#.
- Custom tick intervals and grid lines do not significantly impact rendering speed.

!!! tip "Performance Tip"
    For charts with >1 million points, use `AutoRange=false` and specify `Min`/`Max` to avoid unnecessary axis recalculation.

---

## When to Use

- Visualizing continuous numeric data (time, measurements, financial values)
- Creating line, scatter, column, and area charts
- When axis scaling must be linear or logarithmic
- When precise control over axis range, ticks, and formatting is required
- For scientific, engineering, and analytics applications

---

## Related

- [Axis Ranging](axis-ranging.md)
- [Datetime Axis](datetime-axis.md)
- [Logarithmic Axis](log-axis.md)
- [Renderable Series](../series/renderable-series.md)

---

> **Last updated:** 2024-06-13 15:45 UTC | **Status:** draft