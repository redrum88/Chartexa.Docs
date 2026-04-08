---
title: "Axis Styling"
section: "axes"
last_updated: "2024-06-13 18:22 UTC"
status: draft
---

# Axis Styling

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

Axis styling in Chartexa allows you to customize the appearance of chart axes, including gridlines, axis bands, tick marks, labels, and titles. This feature is essential for creating visually distinct, readable, and informative charts that match your application's theme or highlight specific data ranges.

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
using Chartexa.Core.Chart;
using Chartexa.Data.Series;
using Chartexa.Rendering;

// Create axes with custom styling
var xAxis = new NumericAxis
{
    AxisTitle = "Time (s)",
    TitleFontSize = 16,
    TitleColor = new ChartColor(30, 144, 255), // Dodger blue
    MajorGridLineStyle = new GridLineStyle
    {
        Color = new ChartColor(220, 220, 220),
        Thickness = 1,
        DashArray = new[] { 4, 2 }
    }
};

var yAxis = new NumericAxis
{
    AxisTitle = "Amplitude",
    AxisBandsVisible = true,
    AxisBandColor = new ChartColor(245, 245, 245, 128), // Light gray, semi-transparent
    LabelFontSize = 14,
    LabelColor = new ChartColor(34, 34, 34)
};

// Create chart and add axes
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
```

=== "Python"

```python
from chartexa import Chart

chart = (
    Chart(width=800, height=400)
    .x_axis(
        title="Time (s)",
        title_font_size=16,
        title_color="#1E90FF",  # Dodger blue
        major_grid_color="#DCDCDC",
        major_grid_thickness=1,
        major_grid_dash=[4, 2]
    )
    .y_axis(
        title="Amplitude",
        axis_bands=True,
        axis_band_color="#F5F5F580",  # Light gray, semi-transparent
        label_font_size=14,
        label_color="#222222"
    )
    .line(
        [0, 1, 2, 3, 4], [10, 20, 15, 25, 18],
        stroke="#4682B4", thickness=2
    )
    .save("styled_axis_chart.png")
)
```

---

## Concepts

Axis styling in Chartexa provides granular control over the visual aspects of chart axes. You can customize gridlines, axis bands (alternating background stripes), tick marks, label fonts, colors, and axis titles. These options help improve chart readability, emphasize important data ranges, and align the chart's appearance with your application's branding.

Use axis styling when you need to:

- Highlight specific intervals or ranges with axis bands.
- Improve visual clarity by adjusting gridline styles.
- Match axis label and title fonts/colors to your UI theme.
- Distinguish between multiple axes in composite charts.

Axis styling exists to ensure that charts are not only functional but also visually appealing and accessible, especially when dealing with complex or dense data.

---

## Basic Usage

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Core.Chart;
using Chartexa.Data.Series;

// Configure axis styling
var xAxis = new NumericAxis
{
    AxisTitle = "Frequency (Hz)",
    TitleFontSize = 14,
    TitleColor = new ChartColor(0, 128, 0), // Green
    MajorGridLineStyle = new GridLineStyle
    {
        Color = new ChartColor(211, 211, 211), // Light gray
        Thickness = 1,
        DashArray = new[] { 2, 2 }
    },
    MinorGridLineStyle = new GridLineStyle
    {
        Color = new ChartColor(240, 240, 240),
        Thickness = 1
    },
    AxisBandsVisible = true,
    AxisBandColor = new ChartColor(230, 230, 250, 100) // Lavender, semi-transparent
};

var yAxis = new NumericAxis
{
    AxisTitle = "Power (dB)",
    LabelFontSize = 12,
    LabelColor = new ChartColor(0, 0, 0),
    TickMarkLength = 8,
    TickMarkColor = new ChartColor(0, 128, 128)
};

// Add axes to chart
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);

// Add data series (example)
var dataSeries = new XyDataSeries();
dataSeries.Append(
    new double[] { 100, 200, 300, 400, 500 },
    new double[] { -30, -20, -25, -15, -10 }
);

chart.RenderableSeries.Add(
    new FastLineRenderableSeries
    {
        DataSeries = dataSeries,
        StrokeColor = new ChartColor(70, 130, 180),
        StrokeThickness = 2
    }
);
```

=== "Python"

```python
from chartexa import Chart

chart = (
    Chart(width=600, height=350)
    .x_axis(
        title="Frequency (Hz)",
        title_font_size=14,
        title_color="#008000",  # Green
        major_grid_color="#D3D3D3",
        major_grid_thickness=1,
        major_grid_dash=[2, 2],
        minor_grid_color="#F0F0F0",
        axis_bands=True,
        axis_band_color="#E6E6FA64"  # Lavender, semi-transparent
    )
    .y_axis(
        title="Power (dB)",
        label_font_size=12,
        label_color="#000000",
        tick_length=8,
        tick_color="#008080"
    )
    .line(
        [100, 200, 300, 400, 500], [-30, -20, -25, -15, -10],
        stroke="#4682B4", thickness=2
    )
    .save("axis_styling_basic.png")
)
```

---

## Configuration

| Property              | Type                | Default      | Description                                                |
|-----------------------|---------------------|--------------|------------------------------------------------------------|
| `AxisTitle`           | string              | ""           | Text displayed as the axis title.                          |
| `TitleFontSize`       | int                 | 12           | Font size for the axis title.                              |
| `TitleColor`          | ChartColor / str    | Black        | Color for the axis title text.                             |
| `LabelFontSize`       | int                 | 10           | Font size for axis labels.                                 |
| `LabelColor`          | ChartColor / str    | Black        | Color for axis labels.                                     |
| `MajorGridLineStyle`  | GridLineStyle       | Solid, gray  | Style for major gridlines (color, thickness, dash array).  |
| `MinorGridLineStyle`  | GridLineStyle       | Solid, light | Style for minor gridlines.                                 |
| `AxisBandsVisible`    | bool                | false        | Show alternating axis bands for improved readability.       |
| `AxisBandColor`       | ChartColor / str    | None         | Color for axis bands (with optional alpha for transparency).|
| `TickMarkLength`      | int                 | 6            | Length of tick marks.                                      |
| `TickMarkColor`       | ChartColor / str    | Black        | Color of tick marks.                                       |
| `TickMarkThickness`   | int                 | 1            | Thickness of tick marks.                                   |
| `LabelRotation`       | double              | 0            | Rotation angle for axis labels (degrees).                  |

!!! note
    Python property names use snake_case (e.g., `title_font_size`, `major_grid_color`). Colors can be specified as hex strings or RGBA.

---

## Examples

### Example 1: Highlighting Weekends with Axis Bands

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Core.Chart;
using Chartexa.Data.Series;

// Date axis with axis bands
var xAxis = new DateTimeAxis
{
    AxisTitle = "Date",
    AxisBandsVisible = true,
    AxisBandColor = new ChartColor(255, 228, 181, 80) // Moccasin, semi-transparent
};

var yAxis = new NumericAxis
{
    AxisTitle = "Stock Price ($)",
    LabelFontSize = 13,
    LabelColor = new ChartColor(0, 0, 128)
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);

// Example data
var dates = new DateTime[]
{
    new DateTime(2024, 6, 10),
    new DateTime(2024, 6, 11),
    new DateTime(2024, 6, 12),
    new DateTime(2024, 6, 13),
    new DateTime(2024, 6, 14)
};
var prices = new double[] { 120.5, 122.3, 121.0, 123.8, 124.2 };

var dataSeries = new XyDataSeries<DateTime, double>();
dataSeries.Append(dates, prices);

chart.RenderableSeries.Add(
    new FastLineRenderableSeries
    {
        DataSeries = dataSeries,
        StrokeColor = new ChartColor(34, 139, 34),
        StrokeThickness = 2
    }
);
```

=== "Python"

```python
from datetime import datetime
from chartexa import Chart

dates = [
    datetime(2024, 6, 10),
    datetime(2024, 6, 11),
    datetime(2024, 6, 12),
    datetime(2024, 6, 13),
    datetime(2024, 6, 14)
]
prices = [120.5, 122.3, 121.0, 123.8, 124.2]

chart = (
    Chart(width=700, height=300)
    .x_axis(
        title="Date",
        axis_bands=True,
        axis_band_color="#FFE4B580"  # Moccasin, semi-transparent
    )
    .y_axis(
        title="Stock Price ($)",
        label_font_size=13,
        label_color="#000080"
    )
    .line(dates, prices, stroke="#228B22", thickness=2)
    .save("axis_bands_example.png")
)
```

---

### Example 2: Custom Gridlines and Rotated Labels

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Core.Chart;

// Numeric axis with custom gridlines and label rotation
var xAxis = new NumericAxis
{
    AxisTitle = "Sensor ID",
    MajorGridLineStyle = new GridLineStyle
    {
        Color = new ChartColor(255, 140, 0), // Dark orange
        Thickness = 2,
        DashArray = new[] { 6, 3 }
    },
    LabelFontSize = 12,
    LabelRotation = 45 // Rotate labels for clarity
};

var yAxis = new NumericAxis
{
    AxisTitle = "Temperature (°C)",
    LabelFontSize = 12
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
```

=== "Python"

```python
from chartexa import Chart

chart = (
    Chart(width=600, height=350)
    .x_axis(
        title="Sensor ID",
        major_grid_color="#FF8C00",
        major_grid_thickness=2,
        major_grid_dash=[6, 3],
        label_font_size=12,
        label_rotation=45
    )
    .y_axis(
        title="Temperature (°C)",
        label_font_size=12
    )
    .column(
        [101, 102, 103, 104, 105], [23.5, 24.1, 22.8, 25.0, 23.9],
        fill="#FF8C00"
    )
    .save("rotated_labels_gridlines.png")
)
```

---

### Example 3: Minimalist Axis Styling for Dashboard

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Core.Chart;

// Minimalist axes for dashboard
var xAxis = new NumericAxis
{
    AxisTitle = "",
    MajorGridLineStyle = new GridLineStyle
    {
        Color = new ChartColor(245, 245, 245),
        Thickness = 1
    },
    LabelFontSize = 9,
    LabelColor = new ChartColor(120, 120, 120)
};

var yAxis = new NumericAxis
{
    AxisTitle = "",
    LabelFontSize = 9,
    LabelColor = new ChartColor(120, 120, 120),
    TickMarkLength = 0 // Hide tick marks
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
```

=== "Python"

```python
from chartexa import Chart

chart = (
    Chart(width=400, height=200)
    .x_axis(
        title="",
        major_grid_color="#F5F5F5",
        major_grid_thickness=1,
        label_font_size=9,
        label_color="#787878"
    )
    .y_axis(
        title="",
        label_font_size=9,
        label_color="#787878",
        tick_length=0
    )
    .line([0, 1, 2, 3], [5, 7, 6, 8], stroke="#4682B4", thickness=2)
    .save("minimalist_axis.png")
)
```

---

## Performance Notes

Axis styling has minimal impact on rendering performance, as most styling options (colors, fonts, gridline patterns) are processed efficiently by the DirectX 12 renderer. However, enabling axis bands or using complex dash patterns may slightly increase GPU workload, especially with many axes or large charts.

- Gridlines are drawn using optimized GPU primitives.
- Semi-transparent axis bands may incur additional blending overhead.
- Font rendering for labels and titles is cached for repeated redraws.

!!! tip "Performance Tip"
    For charts with more than 10 axes or frequent real-time updates, avoid excessive use of semi-transparent axis bands and complex dash arrays to maintain maximum frame rates.

---

## When to Use

- When you need to visually distinguish axes in multi-axis charts.
- To improve readability for dense or complex data.
- To match chart appearance to your application's theme.
- To highlight specific intervals (e.g., weekends, thresholds) using axis bands.
- To rotate labels for better fit when axis values are long or overlapping.
- To create minimalist dashboards with subdued axis styling.

---

## Related

- [Axis Ranging](axis-ranging.md)
- [Numeric Axis](numeric-axis.md)
- [DateTime Axis](datetime-axis.md)
- [Theming](../theming/theme-engine.md)

---

> **Last updated:** 2024-06-13 18:22 UTC | **Status:** draft