---
title: "Band Series"
section: "chart-types/2d"
last_updated: "2024-06-10 14:37 UTC"
status: draft
---

# Band Series

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `BandRenderableSeries` displays a ribbon or band between two lines, representing upper and lower bounds across a shared X axis. Use it to visualize ranges, uncertainty, confidence intervals, or spread between two datasets.

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
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (s)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Temperature (°C)" };

// Prepare data
double[] xValues = { 0, 1, 2, 3, 4, 5 };
double[] upper = { 22, 23, 24, 25, 26, 27 };
double[] lower = { 18, 19, 20, 21, 22, 23 };

// Create band data series
var bandSeries = new BandDataSeries();
bandSeries.Append(xValues, upper, lower);

// Create band renderable series
var bandRenderable = new BandRenderableSeries
{
    DataSeries = bandSeries,
    FillColor = new ChartColor(135, 206, 250, 120), // Light blue, semi-transparent
    StrokeColorUpper = new ChartColor(70, 130, 180), // Steel blue
    StrokeColorLower = new ChartColor(255, 99, 71),  // Tomato
    StrokeThickness = 2
};

// Create chart and add series
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(bandRenderable);
```

=== "Python"
```python
from chartexa import Chart

x = [0, 1, 2, 3, 4, 5]
upper = [22, 23, 24, 25, 26, 27]
lower = [18, 19, 20, 21, 22, 23]

chart = (
    Chart(width=800, height=400)
    .band(x, upper, lower,
          fill="#87CEFA80",  # Light blue, 50% opacity
          stroke_upper="#4682B4",
          stroke_lower="#FF6347",
          thickness=2)
    .x_axis(title="Time (s)")
    .y_axis(title="Temperature (°C)")
    .background("#F5F5F7")
    .save("band_chart.png")
)
```

---

## Concepts

A Band Series visualizes the area between two lines, typically representing an upper and lower bound for each X value. This is useful for:

- Displaying ranges, such as minimum/maximum, confidence intervals, or error margins.
- Comparing two datasets and highlighting the spread between them.
- Visualizing uncertainty or variability in measurements.

The band is rendered as a filled region between the two lines, with customizable colors and opacity. Both lines are drawn, and the area between them is filled. The X values must be shared between the upper and lower bounds.

Band Series exist to make it easy to represent uncertainty, variability, or spread in data, which is common in scientific, financial, and engineering applications.

---

## Basic Usage

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;

// Example: Visualizing daily temperature range

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Day" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Temperature (°C)" };

// Data: Days, Highs, Lows
double[] days = { 1, 2, 3, 4, 5, 6, 7 };
double[] highs = { 28, 30, 29, 31, 32, 33, 34 };
double[] lows  = { 18, 19, 20, 21, 22, 22, 23 };

// Create band data series
var bandSeries = new BandDataSeries();
bandSeries.Append(days, highs, lows);

// Configure band renderable series
var bandRenderable = new BandRenderableSeries
{
    DataSeries = bandSeries,
    FillColor = new ChartColor(255, 215, 0, 80), // Gold, semi-transparent
    StrokeColorUpper = new ChartColor(255, 140, 0), // Dark orange
    StrokeColorLower = new ChartColor(70, 130, 180), // Steel blue
    StrokeThickness = 2
};

// Create chart and add series
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(bandRenderable);

// Optionally, export or display chart
chart.Save("temperature_band.png");
```

=== "Python"
```python
from chartexa import Chart

days = [1, 2, 3, 4, 5, 6, 7]
highs = [28, 30, 29, 31, 32, 33, 34]
lows  = [18, 19, 20, 21, 22, 22, 23]

chart = (
    Chart(width=800, height=400)
    .band(days, highs, lows,
          fill="#FFD70080",         # Gold, 50% opacity
          stroke_upper="#FF8C00",   # Dark orange
          stroke_lower="#4682B4",   # Steel blue
          thickness=2)
    .x_axis(title="Day")
    .y_axis(title="Temperature (°C)")
    .background("#FFF")
    .save("temperature_band.png")
)
```

---

## Configuration

| Property           | Type         | Default           | Description                                              |
|--------------------|--------------|-------------------|----------------------------------------------------------|
| `DataSeries`       | BandDataSeries | (required)      | Data series containing X, upper, and lower values        |
| `FillColor`        | ChartColor   | Semi-transparent  | Fill color for the band area between lines               |
| `StrokeColorUpper` | ChartColor   | Steel blue        | Stroke color for the upper line                          |
| `StrokeColorLower` | ChartColor   | Tomato            | Stroke color for the lower line                          |
| `StrokeThickness`  | int          | 2                 | Line thickness for both upper and lower strokes          |
| `Opacity`          | double       | 0.5               | Band fill opacity (0.0–1.0)                              |
| `IsVisible`        | bool         | true              | Controls visibility of the series                        |
| `ZIndex`           | int          | 0                 | Rendering order                                          |

!!! warning
    The `BandDataSeries.Append()` method requires all three arrays (`x`, `upper`, `lower`) to have equal length.

!!! tip "Performance Tip"
    For large datasets (100K+ points), use the DirectX 12 renderer for optimal performance.

---

## Examples

### Example 1: Confidence Interval Visualization

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;

// Simulated measurement with confidence interval
double[] x = { 0, 1, 2, 3, 4, 5, 6 };
double[] mean = { 10, 12, 13, 15, 14, 16, 17 };
double[] upper = { 12, 14, 15, 17, 16, 18, 19 };
double[] lower = { 8, 10, 11, 13, 12, 14, 15 };

var bandSeries = new BandDataSeries();
bandSeries.Append(x, upper, lower);

var bandRenderable = new BandRenderableSeries
{
    DataSeries = bandSeries,
    FillColor = new ChartColor(50, 205, 50, 80), // Lime green, semi-transparent
    StrokeColorUpper = new ChartColor(34, 139, 34), // Forest green
    StrokeColorLower = new ChartColor(34, 139, 34),
    StrokeThickness = 2
};

var chart = new Chart();
chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Sample" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Value" });
chart.RenderableSeries.Add(bandRenderable);
chart.Save("confidence_band.png");
```

=== "Python"
```python
from chartexa import Chart

x = [0, 1, 2, 3, 4, 5, 6]
mean = [10, 12, 13, 15, 14, 16, 17]
upper = [12, 14, 15, 17, 16, 18, 19]
lower = [8, 10, 11, 13, 12, 14, 15]

chart = (
    Chart(width=800, height=400)
    .band(x, upper, lower,
          fill="#32CD3280",           # Lime green, 50% opacity
          stroke_upper="#228B22",
          stroke_lower="#228B22",
          thickness=2)
    .x_axis(title="Sample")
    .y_axis(title="Value")
    .background("#F0FFF0")
    .save("confidence_band.png")
)
```

### Example 2: Financial Spread (Bid/Ask)

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;

// Bid/Ask spread visualization
double[] time = { 0, 1, 2, 3, 4, 5, 6 };
double[] bid = { 101.2, 101.5, 101.7, 101.6, 101.9, 102.0, 102.2 };
double[] ask = { 101.8, 102.0, 102.2, 102.1, 102.3, 102.5, 102.7 };

var bandSeries = new BandDataSeries();
bandSeries.Append(time, ask, bid);

var bandRenderable = new BandRenderableSeries
{
    DataSeries = bandSeries,
    FillColor = new ChartColor(30, 144, 255, 60), // Dodger blue, semi-transparent
    StrokeColorUpper = new ChartColor(0, 191, 255), // Deep sky blue
    StrokeColorLower = new ChartColor(220, 20, 60), // Crimson
    StrokeThickness = 2
};

var chart = new Chart();
chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Time (min)" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Price ($)" });
chart.RenderableSeries.Add(bandRenderable);
chart.Save("bidask_band.png");
```

=== "Python"
```python
from chartexa import Chart

time = [0, 1, 2, 3, 4, 5, 6]
bid = [101.2, 101.5, 101.7, 101.6, 101.9, 102.0, 102.2]
ask = [101.8, 102.0, 102.2, 102.1, 102.3, 102.5, 102.7]

chart = (
    Chart(width=800, height=400)
    .band(time, ask, bid,
          fill="#1E90FF60",           # Dodger blue, 40% opacity
          stroke_upper="#00BFFF",
          stroke_lower="#DC143C",
          thickness=2)
    .x_axis(title="Time (min)")
    .y_axis(title="Price ($)")
    .background("#E6F7FF")
    .save("bidask_band.png")
)
```

### Example 3: Real-Time Streaming Band

!!! example "Real-Time Streaming"
    === "C#"
    ```csharp
    using Chartexa.Core.Axes;
    using Chartexa.Data.Series;
    using Chartexa.Core.RenderableSeries;
    using Chartexa.Core.Chart;

    // Simulate real-time sensor range update
    var bandSeries = new BandDataSeries();

    var chart = new Chart();
    chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Time (s)" });
    chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Sensor Value" });

    var bandRenderable = new BandRenderableSeries
    {
        DataSeries = bandSeries,
        FillColor = new ChartColor(255, 105, 180, 80), // Hot pink, semi-transparent
        StrokeColorUpper = new ChartColor(255, 20, 147),
        StrokeColorLower = new ChartColor(75, 0, 130),
        StrokeThickness = 2
    };

    chart.RenderableSeries.Add(bandRenderable);

    // Streaming loop (pseudo-code)
    for (int t = 0; t < 100; t++)
    {
        double upper = 50 + 10 * Math.Sin(t * 0.1);
        double lower = 40 + 10 * Math.Sin(t * 0.1 - 0.5);
        bandSeries.Append(new double[] { t }, new double[] { upper }, new double[] { lower });
        chart.Refresh();
    }
    ```

    === "Python"
    ```python
    from chartexa import Chart
    import numpy as np

    chart = (
        Chart(width=800, height=400)
        .x_axis(title="Time (s)")
        .y_axis(title="Sensor Value")
        .background("#FFF0F5")
    )

    # Streaming simulation
    x = []
    upper = []
    lower = []
    for t in range(100):
        x.append(t)
        upper.append(50 + 10 * np.sin(t * 0.1))
        lower.append(40 + 10 * np.sin(t * 0.1 - 0.5))
        chart.band(x, upper, lower,
                   fill="#FF69B480",
                   stroke_upper="#FF1493",
                   stroke_lower="#4B0082",
                   thickness=2)
        chart.refresh()
    chart.save("streaming_band.png")
    ```

---

## Performance Notes

- Band Series rendering is highly optimized for large datasets, especially with the DirectX 12 backend.
- Filling the band area is GPU-accelerated; typical performance is >1 million points per second on modern hardware.
- Minimal overhead compared to two line series; fill rendering is batched.
- Python integration leverages .NET runtime for native performance.

!!! tip "Performance Tip"
    Use DirectX 12 backend for real-time streaming or datasets exceeding 100K points. Skia and WPF backends are suitable for smaller datasets or static charts.

---

## When to Use

- Visualizing uncertainty, confidence intervals, or error margins.
- Showing minimum/maximum or high/low ranges (e.g., temperature, financial spread).
- Comparing two related datasets and highlighting the area between them.
- Displaying real-time sensor ranges or variability.
- Any scenario where the area between two curves conveys meaningful information.

---

## Related

- [FastLineRenderableSeries](fast-line-series.md)
- [ScatterRenderableSeries](scatter-series.md)
- [Axis Ranging](../axes/axis-ranging.md)
- [ThemeEngine](../theming/theme-engine.md)

---

> **Last updated:** 2024-06-10 14:37 UTC | **Status:** draft