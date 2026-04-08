---
title: "Error Bar Series"
section: "chart-types/2d"
last_updated: "2024-06-13 17:21 UTC"
status: draft
---

# Error Bar Series

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `ErrorBarRenderableSeries` visualizes error bars for scientific and engineering data, displaying uncertainties or variability around data points. Use error bar series to represent measurement errors, confidence intervals, or statistical deviations alongside your main data.

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
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Sample" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Value" };

// Create error bar data
var xValues = new double[] { 1, 2, 3, 4, 5 };
var yValues = new double[] { 10, 12, 14, 13, 15 };
var yErrorLow = new double[] { 1, 1.5, 1, 2, 1 };
var yErrorHigh = new double[] { 2, 1, 2, 1, 1.5 };

var errorDataSeries = new ErrorBarDataSeries();
errorDataSeries.Append(xValues, yValues, yErrorLow, yErrorHigh);

// Create error bar series
var errorBarSeries = new ErrorBarRenderableSeries
{
    DataSeries = errorDataSeries,
    StrokeColor = new ChartColor(220, 20, 60), // Crimson
    StrokeThickness = 2,
    CapWidth = 8
};

// Create chart
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(errorBarSeries);
```

=== "Python"

```python
from chartexa import Chart

x_values = [1, 2, 3, 4, 5]
y_values = [10, 12, 14, 13, 15]
y_error_low = [1, 1.5, 1, 2, 1]
y_error_high = [2, 1, 2, 1, 1.5]

chart = (
    Chart(width=600, height=400)
    .error_bar(
        x_values, y_values,
        y_error_low=y_error_low,
        y_error_high=y_error_high,
        stroke="#DC143C",
        thickness=2,
        cap_width=8
    )
    .axes(x_title="Sample", y_title="Value")
    .background("#F5F5F5")
    .save("error_bar_quickstart.png")
)
```

---

## Concepts

Error bar series are used to visualize uncertainty, variability, or error margins in measured or calculated data. Each data point is accompanied by vertical lines (bars) indicating the range of possible values, typically defined by lower and upper error values. Caps at the ends of bars help distinguish the error range visually.

Use error bars when you need to communicate the reliability or precision of your data, such as in scientific experiments, quality control, or statistical analysis. Chartexa's error bar series supports asymmetric errors (different values for low and high), making it suitable for advanced use cases.

The error bar series is rendered efficiently, allowing you to display thousands of points with error information in real time. It integrates seamlessly with other chart types and axes, and supports customization of appearance and interaction.

---

## Basic Usage

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;

// Prepare data
var x = new double[] { 1, 2, 3, 4, 5, 6 };
var y = new double[] { 5.2, 6.1, 7.8, 7.0, 6.5, 8.2 };
var yErrLow = new double[] { 0.5, 0.3, 0.7, 0.4, 0.6, 0.5 };
var yErrHigh = new double[] { 0.8, 0.6, 1.0, 0.5, 0.7, 0.9 };

// Create series and axes
var errorDataSeries = new ErrorBarDataSeries();
errorDataSeries.Append(x, y, yErrLow, yErrHigh);

var errorBarSeries = new ErrorBarRenderableSeries
{
    DataSeries = errorDataSeries,
    StrokeColor = new ChartColor(34, 139, 34), // Forest Green
    StrokeThickness = 2,
    CapWidth = 10,
    CapColor = new ChartColor(0, 0, 0), // Black caps
    CapThickness = 2
};

var xAxis = new NumericAxis { Id = "X", AxisTitle = "Measurement" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Result" };

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(errorBarSeries);

// Optionally, add grid lines or background
chart.Background = new ChartColor(245, 245, 245); // Light gray
```

=== "Python"

```python
from chartexa import Chart

x = [1, 2, 3, 4, 5, 6]
y = [5.2, 6.1, 7.8, 7.0, 6.5, 8.2]
y_err_low = [0.5, 0.3, 0.7, 0.4, 0.6, 0.5]
y_err_high = [0.8, 0.6, 1.0, 0.5, 0.7, 0.9]

chart = (
    Chart(width=700, height=400)
    .error_bar(
        x, y,
        y_error_low=y_err_low,
        y_error_high=y_err_high,
        stroke="#228B22",
        thickness=2,
        cap_width=10,
        cap_color="#000000",
        cap_thickness=2
    )
    .axes(x_title="Measurement", y_title="Result")
    .background("#F5F5F5")
    .save("error_bar_basic.png")
)
```

---

## Configuration

| Property       | Type           | Default      | Description                                            |
|----------------|----------------|--------------|--------------------------------------------------------|
| `StrokeColor`  | ChartColor     | #000000      | Color of the error bar lines                           |
| `StrokeThickness` | int         | 2            | Thickness of the error bar lines (pixels)              |
| `CapWidth`     | int            | 8            | Width of the caps at the ends of error bars (pixels)   |
| `CapColor`     | ChartColor     | StrokeColor  | Color of the caps                                      |
| `CapThickness` | int            | StrokeThickness | Thickness of the caps (pixels)                     |
| `DataSeries`   | ErrorBarDataSeries | N/A      | Data series containing X, Y, YErrorLow, YErrorHigh     |
| `Visible`      | bool           | true         | Whether the series is shown                            |
| `Opacity`      | double         | 1.0          | Opacity of the error bars (0.0-1.0)                    |

!!! warning
    The `ErrorBarDataSeries.Append()` method requires all arrays (`x`, `y`, `yErrorLow`, `yErrorHigh`) to have equal length. Mismatched arrays will throw an exception.

---

## Examples

### Example 1: Scientific Measurement with Uncertainty

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;

var x = new double[] { 10, 20, 30, 40, 50 };
var y = new double[] { 100, 110, 120, 115, 130 };
var yErrLow = new double[] { 5, 7, 6, 8, 5 };
var yErrHigh = new double[] { 10, 9, 8, 7, 10 };

var errorDataSeries = new ErrorBarDataSeries();
errorDataSeries.Append(x, y, yErrLow, yErrHigh);

var errorBarSeries = new ErrorBarRenderableSeries
{
    DataSeries = errorDataSeries,
    StrokeColor = new ChartColor(70, 130, 180), // Steel Blue
    StrokeThickness = 3,
    CapWidth = 12,
    CapColor = new ChartColor(70, 130, 180),
    CapThickness = 3
};

var chart = new Chart();
chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Time (s)" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Voltage (mV)" });
chart.RenderableSeries.Add(errorBarSeries);
```

=== "Python"

```python
from chartexa import Chart

x = [10, 20, 30, 40, 50]
y = [100, 110, 120, 115, 130]
y_err_low = [5, 7, 6, 8, 5]
y_err_high = [10, 9, 8, 7, 10]

chart = (
    Chart(width=800, height=400)
    .error_bar(
        x, y,
        y_error_low=y_err_low,
        y_error_high=y_err_high,
        stroke="#4682B4",
        thickness=3,
        cap_width=12,
        cap_color="#4682B4",
        cap_thickness=3
    )
    .axes(x_title="Time (s)", y_title="Voltage (mV)")
    .background("#E6F2FF")
    .save("error_bar_scientific.png")
)
```

### Example 2: Quality Control in Manufacturing

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;

var batchNumbers = new double[] { 1, 2, 3, 4, 5, 6 };
var measuredValues = new double[] { 50, 52, 48, 51, 49, 53 };
var minDeviation = new double[] { 2, 1, 3, 2, 1, 2 };
var maxDeviation = new double[] { 3, 2, 4, 3, 2, 3 };

var errorDataSeries = new ErrorBarDataSeries();
errorDataSeries.Append(batchNumbers, measuredValues, minDeviation, maxDeviation);

var errorBarSeries = new ErrorBarRenderableSeries
{
    DataSeries = errorDataSeries,
    StrokeColor = new ChartColor(255, 140, 0), // Dark Orange
    StrokeThickness = 2,
    CapWidth = 6,
    CapColor = new ChartColor(255, 140, 0),
    CapThickness = 2
};

var chart = new Chart();
chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Batch" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Measurement (mm)" });
chart.RenderableSeries.Add(errorBarSeries);
```

=== "Python"

```python
from chartexa import Chart

batch_numbers = [1, 2, 3, 4, 5, 6]
measured_values = [50, 52, 48, 51, 49, 53]
min_deviation = [2, 1, 3, 2, 1, 2]
max_deviation = [3, 2, 4, 3, 2, 3]

chart = (
    Chart(width=600, height=350)
    .error_bar(
        batch_numbers, measured_values,
        y_error_low=min_deviation,
        y_error_high=max_deviation,
        stroke="#FF8C00",
        thickness=2,
        cap_width=6,
        cap_color="#FF8C00",
        cap_thickness=2
    )
    .axes(x_title="Batch", y_title="Measurement (mm)")
    .background("#FFF8E1")
    .save("error_bar_quality_control.png")
)
```

### Example 3: Overlay Error Bars on Line Series

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;

var x = new double[] { 1, 2, 3, 4, 5 };
var y = new double[] { 20, 22, 21, 23, 24 };
var yErrLow = new double[] { 1, 2, 1, 2, 1 };
var yErrHigh = new double[] { 2, 1, 2, 1, 2 };

var errorDataSeries = new ErrorBarDataSeries();
errorDataSeries.Append(x, y, yErrLow, yErrHigh);

var errorBarSeries = new ErrorBarRenderableSeries
{
    DataSeries = errorDataSeries,
    StrokeColor = new ChartColor(255, 0, 0), // Red
    StrokeThickness = 2,
    CapWidth = 8
};

var lineDataSeries = new XyDataSeries();
lineDataSeries.Append(x, y);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = lineDataSeries,
    StrokeColor = new ChartColor(0, 0, 255), // Blue
    StrokeThickness = 2
};

var chart = new Chart();
chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Index" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Value" });
chart.RenderableSeries.Add(lineSeries);
chart.RenderableSeries.Add(errorBarSeries);
```

=== "Python"

```python
from chartexa import Chart

x = [1, 2, 3, 4, 5]
y = [20, 22, 21, 23, 24]
y_err_low = [1, 2, 1, 2, 1]
y_err_high = [2, 1, 2, 1, 2]

chart = (
    Chart(width=600, height=400)
    .line(x, y, stroke="#0000FF", thickness=2)
    .error_bar(
        x, y,
        y_error_low=y_err_low,
        y_error_high=y_err_high,
        stroke="#FF0000",
        thickness=2,
        cap_width=8
    )
    .axes(x_title="Index", y_title="Value")
    .background("#F0F0F0")
    .save("error_bar_overlay.png")
)
```

---

## Performance Notes

Chartexa's error bar rendering is GPU-accelerated via DirectX 12, enabling real-time visualization of large datasets (up to 500,000 points per series on modern hardware). Rendering performance depends on cap width, thickness, and anti-aliasing settings. For optimal performance:

- Use moderate cap widths and thicknesses.
- Avoid excessive opacity or transparency effects.
- Overlaying multiple error bar series may increase GPU load.

!!! tip "Performance Tip"
    Use the DirectX12 renderer for datasets exceeding 100,000 points. Skia and WPF backends are suitable for smaller datasets or UI-centric applications.

---

## When to Use

- Visualizing measurement uncertainty or error margins in scientific data
- Displaying confidence intervals in statistical charts
- Quality control and manufacturing analysis
- Overlaying error bars on line, scatter, or column series
- Communicating variability or reliability in engineering datasets

---

## Related

- [Fast Line Series](./fast-line-series.md)
- [Scatter Series](./scatter-series.md)
- [Axis Ranging](../axes/axis-ranging.md)
- [XyDataSeries](../data-series/xy-data-series.md)

---

> **Last updated:** 2024-06-13 17:21 UTC | **Status:** draft