---
title: "Multiple Axes"
section: "axes"
last_updated: "2024-06-12 15:40 UTC"
status: draft
---

# Multiple Axes

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

Multiple axes allow you to display data series with different scales, units, or domains on the same chart. This feature supports secondary axes, vertical and horizontal axis layouts, and complex multi-axis arrangements for advanced visualization needs.

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
using Chartexa.Core.Chart;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Colors;

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (s)" };
var yAxisLeft = new NumericAxis { Id = "Y1", AxisTitle = "Temperature (°C)", Alignment = AxisAlignment.Left };
var yAxisRight = new NumericAxis { Id = "Y2", AxisTitle = "Pressure (kPa)", Alignment = AxisAlignment.Right };

// Create data series
var tempSeries = new XyDataSeries();
tempSeries.Append(new double[] { 0, 1, 2, 3 }, new double[] { 22.5, 23.0, 23.8, 24.2 });

var pressureSeries = new XyDataSeries();
pressureSeries.Append(new double[] { 0, 1, 2, 3 }, new double[] { 101.2, 100.8, 100.5, 100.3 });

// Create renderable series
var tempLine = new FastLineRenderableSeries
{
    DataSeries = tempSeries,
    StrokeColor = new ChartColor(255, 99, 71), // Tomato
    YAxisId = "Y1"
};

var pressureLine = new FastLineRenderableSeries
{
    DataSeries = pressureSeries,
    StrokeColor = new ChartColor(70, 130, 180), // Steel blue
    YAxisId = "Y2"
};

// Create chart and add axes/series
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxisLeft);
chart.Axes.Add(yAxisRight);
chart.RenderableSeries.Add(tempLine);
chart.RenderableSeries.Add(pressureLine);
```

=== "Python"

```python
from chartexa import Chart

# Data for temperature and pressure
time = [0, 1, 2, 3]
temperature = [22.5, 23.0, 23.8, 24.2]
pressure = [101.2, 100.8, 100.5, 100.3]

chart = (
    Chart(width=800, height=400)
    .axis("numeric", id="X", title="Time (s)")
    .axis("numeric", id="Y1", title="Temperature (°C)", align="left")
    .axis("numeric", id="Y2", title="Pressure (kPa)", align="right")
    .line(time, temperature, stroke="#FF6347", y_axis="Y1", label="Temperature")
    .line(time, pressure, stroke="#4682B4", y_axis="Y2", label="Pressure")
    .background("#F9F9F9")
    .save("multi_axes_quickstart.png")
)
```

---

## Concepts

Multiple axes enable you to visualize data with differing units or scales within a single chart. For example, you can plot temperature and pressure, each with its own y-axis, sharing a common x-axis. Chartexa supports any number of axes, both vertical (y) and horizontal (x), allowing for flexible layouts such as dual-axis, quadrant, or overlay charts.

This feature is essential when comparing datasets that would otherwise be unreadable if forced onto a single scale. Each axis can be independently configured for range, ticks, labels, and alignment. Renderable series are linked to axes via their `XAxisId` and `YAxisId` properties, ensuring data is mapped correctly.

Use multiple axes when you need to:

- Display data series with different units or scales
- Compare related but distinct measurements (e.g., price and volume)
- Create scientific, engineering, or financial charts with complex axis arrangements

---

## Basic Usage

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.Chart;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Colors;

// Define axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (min)" };
var yAxisLeft = new NumericAxis { Id = "Y1", AxisTitle = "Voltage (V)", Alignment = AxisAlignment.Left };
var yAxisRight = new NumericAxis { Id = "Y2", AxisTitle = "Current (A)", Alignment = AxisAlignment.Right };

// Voltage data
var voltageSeries = new XyDataSeries();
voltageSeries.Append(new double[] { 0, 5, 10, 15 }, new double[] { 3.3, 3.2, 3.1, 3.0 });

// Current data
var currentSeries = new XyDataSeries();
currentSeries.Append(new double[] { 0, 5, 10, 15 }, new double[] { 0.5, 0.55, 0.6, 0.65 });

// Renderable series
var voltageLine = new FastLineRenderableSeries
{
    DataSeries = voltageSeries,
    StrokeColor = new ChartColor(34, 139, 34), // Forest green
    YAxisId = "Y1"
};

var currentLine = new FastLineRenderableSeries
{
    DataSeries = currentSeries,
    StrokeColor = new ChartColor(255, 140, 0), // Dark orange
    YAxisId = "Y2"
};

// Chart setup
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxisLeft);
chart.Axes.Add(yAxisRight);
chart.RenderableSeries.Add(voltageLine);
chart.RenderableSeries.Add(currentLine);

// Optionally, configure axis ranges
yAxisLeft.AutoRange = true;
yAxisRight.AutoRange = true;
```

=== "Python"

```python
from chartexa import Chart

minutes = [0, 5, 10, 15]
voltage = [3.3, 3.2, 3.1, 3.0]
current = [0.5, 0.55, 0.6, 0.65]

chart = (
    Chart(width=800, height=400)
    .axis("numeric", id="X", title="Time (min)")
    .axis("numeric", id="Y1", title="Voltage (V)", align="left", auto_range=True)
    .axis("numeric", id="Y2", title="Current (A)", align="right", auto_range=True)
    .line(minutes, voltage, stroke="#228B22", y_axis="Y1", label="Voltage")
    .line(minutes, current, stroke="#FF8C00", y_axis="Y2", label="Current")
    .background("#EAEAEA")
    .save("multi_axes_basic.png")
)
```

---

## Configuration

| Property      | Type         | Default    | Description                                             |
|---------------|--------------|------------|---------------------------------------------------------|
| `Id`          | string       | required   | Unique identifier for the axis                          |
| `AxisTitle`   | string       | ""         | Axis label displayed on the chart                       |
| `Alignment`   | enum         | Left/Bottom| Axis placement (`Left`, `Right`, `Top`, `Bottom`)       |
| `AutoRange`   | bool         | true       | Automatically adjusts axis range to fit data            |
| `Visible`     | bool         | true       | Controls axis visibility                                |
| `TickSpacing` | double       | auto       | Spacing between major ticks                             |
| `LabelFormat` | string       | auto       | Format string for axis labels                           |
| `Min`         | double       | auto       | Minimum axis value                                      |
| `Max`         | double       | auto       | Maximum axis value                                      |
| `Color`       | ChartColor   | auto       | Axis line and label color                               |

!!! tip "Axis Alignment"
    Use `Alignment` to position axes on any side of the chart. For example, `Alignment = AxisAlignment.Right` places the axis on the right edge.

!!! warning
    Each axis must have a unique `Id`. Renderable series reference axes by their `XAxisId` and `YAxisId`.

---

## Examples

### Example 1: Dual Y-Axis for Financial Data

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.Chart;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Colors;

// X axis: DateTime
var xAxis = new DateTimeAxis { Id = "X", AxisTitle = "Date" };

// Y axes: Price and Volume
var priceAxis = new NumericAxis { Id = "Y1", AxisTitle = "Price (USD)", Alignment = AxisAlignment.Left };
var volumeAxis = new NumericAxis { Id = "Y2", AxisTitle = "Volume", Alignment = AxisAlignment.Right };

// Price data
var dates = new DateTime[]
{
    new DateTime(2024, 6, 10),
    new DateTime(2024, 6, 11),
    new DateTime(2024, 6, 12),
    new DateTime(2024, 6, 13)
};
var prices = new double[] { 120.5, 121.2, 119.8, 122.0 };

var priceSeries = new XyDataSeries<DateTime, double>();
priceSeries.Append(dates, prices);

// Volume data
var volumes = new double[] { 15000, 18000, 17000, 16000 };
var volumeSeries = new XyDataSeries<DateTime, double>();
volumeSeries.Append(dates, volumes);

// Renderable series
var priceLine = new FastLineRenderableSeries
{
    DataSeries = priceSeries,
    StrokeColor = new ChartColor(0, 128, 255),
    YAxisId = "Y1"
};

var volumeColumn = new FastColumnRenderableSeries
{
    DataSeries = volumeSeries,
    FillColor = new ChartColor(200, 200, 200),
    YAxisId = "Y2"
};

// Chart setup
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(priceAxis);
chart.Axes.Add(volumeAxis);
chart.RenderableSeries.Add(priceLine);
chart.RenderableSeries.Add(volumeColumn);
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
prices = [120.5, 121.2, 119.8, 122.0]
volumes = [15000, 18000, 17000, 16000]

chart = (
    Chart(width=900, height=500)
    .axis("datetime", id="X", title="Date")
    .axis("numeric", id="Y1", title="Price (USD)", align="left")
    .axis("numeric", id="Y2", title="Volume", align="right")
    .line(dates, prices, stroke="#0080FF", y_axis="Y1", label="Price")
    .column(dates, volumes, fill="#C8C8C8", y_axis="Y2", label="Volume")
    .background("#FFFFFF")
    .save("finance_dual_axis.png")
)
```

### Example 2: Multiple X Axes for Comparative Analysis

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.Chart;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Colors;

// Two X axes: Time and Frequency
var timeAxis = new NumericAxis { Id = "X1", AxisTitle = "Time (s)", Alignment = AxisAlignment.Bottom };
var freqAxis = new NumericAxis { Id = "X2", AxisTitle = "Frequency (Hz)", Alignment = AxisAlignment.Top };

// Y axis: Amplitude
var amplitudeAxis = new NumericAxis { Id = "Y", AxisTitle = "Amplitude", Alignment = AxisAlignment.Left };

// Time domain data
var time = new double[] { 0, 1, 2, 3 };
var amplitude = new double[] { 0.5, 0.7, 0.6, 0.8 };
var timeSeries = new XyDataSeries();
timeSeries.Append(time, amplitude);

// Frequency domain data
var freq = new double[] { 10, 20, 30, 40 };
var amplitudeFreq = new double[] { 0.2, 0.3, 0.25, 0.35 };
var freqSeries = new XyDataSeries();
freqSeries.Append(freq, amplitudeFreq);

// Renderable series
var timeLine = new FastLineRenderableSeries
{
    DataSeries = timeSeries,
    StrokeColor = new ChartColor(255, 0, 0),
    XAxisId = "X1",
    YAxisId = "Y"
};

var freqLine = new FastLineRenderableSeries
{
    DataSeries = freqSeries,
    StrokeColor = new ChartColor(0, 0, 255),
    XAxisId = "X2",
    YAxisId = "Y"
};

// Chart setup
var chart = new Chart();
chart.Axes.Add(timeAxis);
chart.Axes.Add(freqAxis);
chart.Axes.Add(amplitudeAxis);
chart.RenderableSeries.Add(timeLine);
chart.RenderableSeries.Add(freqLine);
```

=== "Python"

```python
from chartexa import Chart

time = [0, 1, 2, 3]
amplitude = [0.5, 0.7, 0.6, 0.8]
freq = [10, 20, 30, 40]
amplitude_freq = [0.2, 0.3, 0.25, 0.35]

chart = (
    Chart(width=800, height=400)
    .axis("numeric", id="X1", title="Time (s)", align="bottom")
    .axis("numeric", id="X2", title="Frequency (Hz)", align="top")
    .axis("numeric", id="Y", title="Amplitude", align="left")
    .line(time, amplitude, stroke="#FF0000", x_axis="X1", y_axis="Y", label="Time Domain")
    .line(freq, amplitude_freq, stroke="#0000FF", x_axis="X2", y_axis="Y", label="Frequency Domain")
    .background("#F5F5F5")
    .save("multi_x_axes.png")
)
```

### Example 3: Four Quadrant Chart

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.Chart;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Colors;

// Four axes: left, right, top, bottom
var xAxisBottom = new NumericAxis { Id = "X1", AxisTitle = "X (Bottom)", Alignment = AxisAlignment.Bottom };
var xAxisTop = new NumericAxis { Id = "X2", AxisTitle = "X (Top)", Alignment = AxisAlignment.Top };
var yAxisLeft = new NumericAxis { Id = "Y1", AxisTitle = "Y (Left)", Alignment = AxisAlignment.Left };
var yAxisRight = new NumericAxis { Id = "Y2", AxisTitle = "Y (Right)", Alignment = AxisAlignment.Right };

// Data series
var series1 = new XyDataSeries();
series1.Append(new double[] { 1, 2, 3 }, new double[] { 4, 5, 6 });

var series2 = new XyDataSeries();
series2.Append(new double[] { 1, 2, 3 }, new double[] { 6, 5, 4 });

// Renderable series
var line1 = new FastLineRenderableSeries
{
    DataSeries = series1,
    StrokeColor = new ChartColor(0, 128, 0),
    XAxisId = "X1",
    YAxisId = "Y1"
};

var line2 = new FastLineRenderableSeries
{
    DataSeries = series2,
    StrokeColor = new ChartColor(128, 0, 0),
    XAxisId = "X2",
    YAxisId = "Y2"
};

// Chart setup
var chart = new Chart();
chart.Axes.Add(xAxisBottom);
chart.Axes.Add(xAxisTop);
chart.Axes.Add(yAxisLeft);
chart.Axes.Add(yAxisRight);
chart.RenderableSeries.Add(line1);
chart.RenderableSeries.Add(line2);
```

=== "Python"

```python
from chartexa import Chart

x1 = [1, 2, 3]
y1 = [4, 5, 6]
x2 = [1, 2, 3]
y2 = [6, 5, 4]

chart = (
    Chart(width=700, height=400)
    .axis("numeric", id="X1", title="X (Bottom)", align="bottom")
    .axis("numeric", id="X2", title="X (Top)", align="top")
    .axis("numeric", id="Y1", title="Y (Left)", align="left")
    .axis("numeric", id="Y2", title="Y (Right)", align="right")
    .line(x1, y1, stroke="#008000", x_axis="X1", y_axis="Y1", label="Quadrant 1")
    .line(x2, y2, stroke="#800000", x_axis="X2", y_axis="Y2", label="Quadrant 2")
    .background("#F0F0F0")
    .save("four_quadrant_chart.png")
)
```

---

## Performance Notes

Multiple axes add minimal overhead to rendering, as Chartexa efficiently manages axis layout and scaling. Performance remains high even with several axes, provided the number of renderable series and data points is reasonable.

- Rendering up to 8 axes (4 x, 4 y) with 100K points per series shows no measurable impact on DirectX 12 backend (<2% overhead).
- Axis label rendering is GPU-accelerated; complex layouts (e.g., rotated labels, custom ticks) may slightly affect CPU usage.
- Python integration maintains performance parity, but large axis counts may increase chart initialization time.

!!! tip "Performance Tip"
    For charts with more than 10 axes, use the DirectX 12 backend and avoid excessive custom label formatting.

---

## When to Use

- Visualizing data series with different units or scales (e.g., temperature vs. humidity)
- Comparing financial metrics (e.g., price vs. volume)
- Overlaying time and frequency domain data
- Scientific charts requiring quadrant or multi-domain layouts
- Engineering dashboards with multiple sensor readings

---

## Related

- [Axis Ranging](axis-ranging.md)
- [Numeric Axis](numeric-axis.md)
- [DateTime Axis](datetime-axis.md)
- [Renderable Series](../data-series/renderable-series.md)

---

> **Last updated:** 2024-06-12 15:40 UTC | **Status:** draft