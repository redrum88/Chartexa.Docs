---
title: "Logarithmic Axis"
section: "axes"
last_updated: "2024-06-13 17:45 UTC"
status: draft
---

# Logarithmic Axis

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `LogarithmicAxis` provides logarithmic (base 10) scaling for chart axes, enabling visualization of data spanning multiple orders of magnitude. Use it to display exponential growth, scientific measurements, or financial data where linear scaling obscures important trends.

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

// Create a logarithmic Y axis
var yAxis = new LogarithmicAxis
{
    Id = "Y",
    AxisTitle = "Signal (dB)",
    Min = 1,
    Max = 10000
};

// Create a numeric X axis
var xAxis = new NumericAxis
{
    Id = "X",
    AxisTitle = "Frequency (Hz)"
};

// Sample data spanning several orders of magnitude
var xValues = new double[] { 10, 100, 1000, 10000 };
var yValues = new double[] { 2, 20, 200, 2000 };

var dataSeries = new XyDataSeries();
dataSeries.Append(xValues, yValues);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(34, 139, 34), // Forest green
    StrokeThickness = 2
};

// Add axes and series to chart (see Basic Usage for full chart setup)
```

=== "Python"

```python
from chartexa import Chart, LogarithmicAxis

# Sample data spanning several orders of magnitude
x_values = [10, 100, 1000, 10000]
y_values = [2, 20, 200, 2000]

chart = (
    Chart(width=600, height=400)
    .axis_x("Frequency (Hz)")
    .axis_y(LogarithmicAxis(title="Signal (dB)", min=1, max=10000))
    .line(x_values, y_values, stroke="#228B22", thickness=2)
    .background("#F8F8FF")
    .save("log_axis_quickstart.png")
)
```

---

## Concepts

The `LogarithmicAxis` transforms axis values using a logarithmic (base 10) scale. This is essential for visualizing data where values span several orders of magnitude, such as frequency spectra, decibel measurements, population growth, or financial returns.

Logarithmic scaling compresses large values and expands small values, making exponential trends and multiplicative relationships visually apparent. It prevents high-magnitude data from dominating the chart and allows for meaningful comparison across wide ranges.

Use a logarithmic axis when:
- Data covers multiple orders of magnitude (e.g., 1 to 10,000)
- The underlying phenomenon is multiplicative or exponential
- Linear scaling hides important detail in lower ranges

!!! warning
    Logarithmic axes require all data values to be strictly positive. Zero and negative values are not supported and will result in rendering errors.

---

## Basic Usage

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.Series;
using Chartexa.Rendering.Chart;

// Create axes
var xAxis = new NumericAxis
{
    Id = "X",
    AxisTitle = "Frequency (Hz)",
    Min = 10,
    Max = 10000
};

var yAxis = new LogarithmicAxis
{
    Id = "Y",
    AxisTitle = "Amplitude (dB)",
    Min = 1,
    Max = 10000,
    MajorTickCount = 5,
    MinorTickCount = 10,
    ShowGridLines = true
};

// Prepare data
var xValues = new double[] { 10, 100, 1000, 10000 };
var yValues = new double[] { 5, 50, 500, 5000 };

var dataSeries = new XyDataSeries();
dataSeries.Append(xValues, yValues);

// Create renderable series
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(70, 130, 180), // Steel blue
    StrokeThickness = 2
};

// Create chart and add axes/series
var chart = new ChartSurface
{
    Width = 800,
    Height = 400,
    Background = new ChartColor(240, 248, 255) // Alice blue
};

chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(lineSeries);

// Render or display chart as needed
```

=== "Python"

```python
from chartexa import Chart, LogarithmicAxis

# Data spanning several orders of magnitude
x_values = [10, 100, 1000, 10000]
y_values = [5, 50, 500, 5000]

chart = (
    Chart(width=800, height=400)
    .axis_x("Frequency (Hz)", min=10, max=10000)
    .axis_y(LogarithmicAxis(title="Amplitude (dB)", min=1, max=10000, major_ticks=5, minor_ticks=10, grid=True))
    .line(x_values, y_values, stroke="#4682B4", thickness=2)
    .background("#F0F8FF")
    .save("log_axis_basic.png")
)
```

---

## Configuration

| Property         | Type    | Default   | Description                                                    |
|------------------|---------|-----------|----------------------------------------------------------------|
| `Id`             | string  | `null`    | Unique axis identifier                                         |
| `AxisTitle`      | string  | `""`      | Axis label                                                     |
| `Min`            | double  | `1`       | Minimum axis value (must be > 0)                              |
| `Max`            | double  | `100`     | Maximum axis value                                             |
| `MajorTickCount` | int     | `5`       | Number of major ticks (log scale)                              |
| `MinorTickCount` | int     | `10`      | Number of minor ticks per major tick                           |
| `ShowGridLines`  | bool    | `true`    | Display grid lines                                             |
| `LabelFormat`    | string  | `"G"`     | Numeric format for axis labels                                 |
| `AutoRange`      | bool    | `true`    | Automatically adjust axis range to fit data                    |
| `LogBase`        | double  | `10`      | Base for logarithmic scaling (fixed at 10 for LogarithmicAxis) |
| `TickColor`      | ChartColor | `auto` | Color of tick marks                                            |
| `LabelColor`     | ChartColor | `auto` | Color of axis labels                                           |

!!! tip "Axis Range"
    Set `Min` and `Max` to cover the full range of your data. All values must be strictly positive.

---

## Examples

### Example 1: Audio Frequency Spectrum

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.Series;
using Chartexa.Rendering.Chart;

// Simulated frequency response data
var frequencies = new double[] { 20, 100, 1000, 5000, 10000, 20000 };
var amplitudes = new double[] { 0.5, 1.2, 3.0, 2.5, 1.0, 0.7 };

var xAxis = new NumericAxis
{
    Id = "X",
    AxisTitle = "Frequency (Hz)",
    Min = 20,
    Max = 20000
};

var yAxis = new LogarithmicAxis
{
    Id = "Y",
    AxisTitle = "Amplitude",
    Min = 0.1,
    Max = 10
};

var dataSeries = new XyDataSeries();
dataSeries.Append(frequencies, amplitudes);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(255, 99, 71), // Tomato
    StrokeThickness = 2
};

var chart = new ChartSurface
{
    Width = 700,
    Height = 350
};

chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(lineSeries);
```

=== "Python"

```python
from chartexa import Chart, LogarithmicAxis

frequencies = [20, 100, 1000, 5000, 10000, 20000]
amplitudes = [0.5, 1.2, 3.0, 2.5, 1.0, 0.7]

chart = (
    Chart(width=700, height=350)
    .axis_x("Frequency (Hz)", min=20, max=20000)
    .axis_y(LogarithmicAxis(title="Amplitude", min=0.1, max=10))
    .line(frequencies, amplitudes, stroke="#FF6347", thickness=2)
    .background("#FFF5EE")
    .save("audio_spectrum_log.png")
)
```

### Example 2: Population Growth Visualization

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.Series;
using Chartexa.Rendering.Chart;

// Years and population (exponential growth)
var years = new double[] { 1950, 1970, 1990, 2010, 2030 };
var population = new double[] { 2.5, 3.7, 5.3, 6.9, 8.5 }; // Billions

var xAxis = new NumericAxis
{
    Id = "X",
    AxisTitle = "Year",
    Min = 1950,
    Max = 2030
};

var yAxis = new LogarithmicAxis
{
    Id = "Y",
    AxisTitle = "Population (Billions)",
    Min = 1,
    Max = 10
};

var dataSeries = new XyDataSeries();
dataSeries.Append(years, population);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(0, 191, 255), // Deep sky blue
    StrokeThickness = 2
};

var chart = new ChartSurface
{
    Width = 600,
    Height = 300
};

chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(lineSeries);
```

=== "Python"

```python
from chartexa import Chart, LogarithmicAxis

years = [1950, 1970, 1990, 2010, 2030]
population = [2.5, 3.7, 5.3, 6.9, 8.5]

chart = (
    Chart(width=600, height=300)
    .axis_x("Year", min=1950, max=2030)
    .axis_y(LogarithmicAxis(title="Population (Billions)", min=1, max=10))
    .line(years, population, stroke="#00BFFF", thickness=2)
    .background("#E6F7FF")
    .save("population_log.png")
)
```

### Example 3: Financial Returns (Log Scale)

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.Series;
using Chartexa.Rendering.Chart;

// Investment returns over decades
var years = new double[] { 1980, 1990, 2000, 2010, 2020 };
var returns = new double[] { 1000, 5000, 20000, 80000, 320000 };

var xAxis = new NumericAxis
{
    Id = "X",
    AxisTitle = "Year",
    Min = 1980,
    Max = 2020
};

var yAxis = new LogarithmicAxis
{
    Id = "Y",
    AxisTitle = "Portfolio Value ($)",
    Min = 1000,
    Max = 500000
};

var dataSeries = new XyDataSeries();
dataSeries.Append(years, returns);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(255, 215, 0), // Gold
    StrokeThickness = 2
};

var chart = new ChartSurface
{
    Width = 700,
    Height = 400
};

chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(lineSeries);
```

=== "Python"

```python
from chartexa import Chart, LogarithmicAxis

years = [1980, 1990, 2000, 2010, 2020]
returns = [1000, 5000, 20000, 80000, 320000]

chart = (
    Chart(width=700, height=400)
    .axis_x("Year", min=1980, max=2020)
    .axis_y(LogarithmicAxis(title="Portfolio Value ($)", min=1000, max=500000))
    .line(years, returns, stroke="#FFD700", thickness=2)
    .background("#FFFACD")
    .save("financial_log.png")
)
```

---

## Performance Notes

The `LogarithmicAxis` is optimized for real-time rendering with large datasets. Logarithmic scaling is performed on the GPU when using the DirectX 12 backend, minimizing CPU overhead. Axis ticks and labels are dynamically generated for each zoom level, ensuring clarity even with dense data.

- Rendering performance is comparable to `NumericAxis` for datasets up to 10 million points.
- Logarithmic scaling does not introduce significant latency.
- Axis label formatting is adaptive for scientific notation when values exceed 10^6.

!!! tip "Performance Tip"
    For datasets exceeding 100,000 points, use the DirectX 12 renderer for optimal performance.

!!! note
    Python integration requires the .NET 10 Runtime for GPU-accelerated rendering.

---

## When to Use

- Visualizing data spanning several orders of magnitude (e.g., 1 Hz to 100 kHz)
- Displaying exponential growth or decay (population, investments, radioactive decay)
- Showing frequency spectra (audio, RF, seismic)
- Plotting scientific measurements (decibels, pH, luminosity)
- Comparing multiplicative relationships where linear axes obscure trends

---

## Related

- [Numeric Axis](numeric-axis.md)
- [Datetime Axis](datetime-axis.md)
- [Axis Ranging](axis-ranging.md)
- [Chart Types](../chart-types/2d/line-chart.md)

---

> **Last updated:** 2024-06-13 17:45 UTC | **Status:** draft