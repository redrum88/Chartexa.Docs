---
title: "Donut / Pie Series"
section: "chart-types/2d"
last_updated: "2024-06-13 14:35 UTC"
status: draft
last_updated: "2026-04-08 08:56 UTC"
status: placeholder
---

# Donut / Pie Series

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `DonutSeries` renders pie and donut charts, allowing you to visualize categorical proportions with configurable inner radius. Use it to display distributions, breakdowns, or summary statistics in a visually engaging format.

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
using Chartexa.Core.Chart;
using Chartexa.Core.Series;
using Chartexa.Core.Styles;

// Sample data: Market share by browser
var categories = new[] { "Chrome", "Safari", "Edge", "Firefox", "Other" };
var values = new[] { 63.6, 19.1, 4.6, 2.9, 9.8 };

var donutSeries = new DonutSeries
{
    Categories = categories,
    Values = values,
    InnerRadius = 0.4, // 40% inner radius for donut effect
    SegmentColors = new[]
    {
        new ChartColor(66, 133, 244),   // Chrome blue
        new ChartColor(124, 181, 24),   // Safari green
        new ChartColor(255, 140, 0),    // Edge orange
        new ChartColor(255, 69, 0),     // Firefox red
        new ChartColor(128, 128, 128)   // Other gray
    }
};

var chart = new Chart
{
    Width = 600,
    Height = 400,
    Series = { donutSeries }
};
chart.Save("donut_chart.png");
```

=== "Python"
```python
from chartexa import Chart

categories = ["Chrome", "Safari", "Edge", "Firefox", "Other"]
values = [63.6, 19.1, 4.6, 2.9, 9.8]

chart = (
    Chart(width=600, height=400)
    .donut(
        categories,
        values,
        inner_radius=0.4,
        segment_colors=[
            "#4285F4",  # Chrome blue
            "#7CB514",  # Safari green
            "#FF8C00",  # Edge orange
            "#FF4500",  # Firefox red
            "#808080"   # Other gray
        ]
    )
    .save("donut_chart.png")
)
```

---

## Concepts

The `DonutSeries` visualizes categorical data as segments of a circle, with each segment's angle proportional to its value. By adjusting the `InnerRadius`, you can switch between a classic pie chart (inner radius = 0) and a donut chart (inner radius > 0), providing flexibility in style and emphasis.

Donut and pie charts are ideal for showing parts of a whole, such as market share, budget allocation, or survey results. The donut variant allows for additional information in the center, such as totals or icons, and is often preferred for modern dashboards.

Chartexa's implementation supports custom segment colors, labels, tooltips, and interactive highlighting, making it suitable for both static reporting and dynamic, interactive applications.

---

## Basic Usage

=== "C#"
```csharp
using Chartexa.Core.Chart;
using Chartexa.Core.Series;
using Chartexa.Core.Styles;

// Budget allocation example
var categories = new[] { "R&D", "Marketing", "Operations", "HR", "IT" };
var values = new[] { 25, 30, 20, 15, 10 };

var donutSeries = new DonutSeries
{
    Categories = categories,
    Values = values,
    InnerRadius = 0.3, // 30% donut
    SegmentColors = new[]
    {
        new ChartColor(52, 152, 219),   // R&D blue
        new ChartColor(231, 76, 60),    // Marketing red
        new ChartColor(46, 204, 113),   // Operations green
        new ChartColor(155, 89, 182),   // HR purple
        new ChartColor(241, 196, 15)    // IT yellow
    },
    ShowLabels = true,
    LabelFont = new ChartFont("Segoe UI", 12, ChartFontStyle.Bold),
    LabelColor = new ChartColor(40, 40, 40)
};

var chart = new Chart
{
    Width = 500,
    Height = 500,
    Series = { donutSeries }
};
chart.Save("budget_donut.png");
```

=== "Python"
```python
from chartexa import Chart

categories = ["R&D", "Marketing", "Operations", "HR", "IT"]
values = [25, 30, 20, 15, 10]

chart = (
    Chart(width=500, height=500)
    .donut(
        categories,
        values,
        inner_radius=0.3,
        segment_colors=[
            "#3498DB",  # R&D blue
            "#E74C3C",  # Marketing red
            "#2ECC71",  # Operations green
            "#9B59B6",  # HR purple
            "#F1C40F"   # IT yellow
        ],
        show_labels=True,
        label_font=("Segoe UI", 12, "bold"),
        label_color="#282828"
    )
    .save("budget_donut.png")
)
```

---

## Configuration

| Property        | Type                | Default   | Description                                      |
|-----------------|---------------------|-----------|--------------------------------------------------|
| `Categories`    | string[] / list     | Required  | Category names for each segment                  |
| `Values`        | double[] / list     | Required  | Values for each segment                          |
| `InnerRadius`   | double (0-1)        | 0         | Fractional radius for donut hole (0=pie, 0.5=half)|
| `SegmentColors` | ChartColor[] / list | Auto      | Colors for each segment; auto if not specified   |
| `ShowLabels`    | bool                | true      | Display category/value labels on segments        |
| `LabelFont`     | ChartFont / tuple   | Default   | Font for segment labels                          |
| `LabelColor`    | ChartColor / str    | Auto      | Color for segment labels                         |
| `LabelFormat`   | string              | "{category}: {value}" | Format string for labels                |
| `TooltipEnabled`| bool                | true      | Show tooltips on hover/click                     |
| `ExplodeOffset` | double[] / list     | None      | Offset for each segment (for 'exploded' effect)  |
| `StrokeColor`   | ChartColor / str    | None      | Outline color for segments                       |
| `StrokeThickness`| double             | 1         | Outline thickness                                |

---

## Examples

### Example 1: Survey Results Pie Chart

=== "C#"
```csharp
using Chartexa.Core.Chart;
using Chartexa.Core.Series;

// Survey: Favorite programming language
var categories = new[] { "Python", "C#", "JavaScript", "Java", "Other" };
var values = new[] { 42, 28, 15, 10, 5 };

var pieSeries = new DonutSeries
{
    Categories = categories,
    Values = values,
    InnerRadius = 0, // Pie chart
    ShowLabels = true,
    SegmentColors = new[]
    {
        new ChartColor(53, 132, 228),   // Python blue
        new ChartColor(34, 139, 34),    // C# green
        new ChartColor(255, 215, 0),    // JavaScript yellow
        new ChartColor(255, 87, 34),    // Java orange
        new ChartColor(128, 128, 128)   // Other gray
    }
};

var chart = new Chart
{
    Width = 400,
    Height = 400,
    Series = { pieSeries }
};
chart.Save("survey_pie.png");
```

=== "Python"
```python
from chartexa import Chart

categories = ["Python", "C#", "JavaScript", "Java", "Other"]
values = [42, 28, 15, 10, 5]

chart = (
    Chart(width=400, height=400)
    .pie(
        categories,
        values,
        segment_colors=[
            "#3584E4",  # Python blue
            "#228B22",  # C# green
            "#FFD700",  # JavaScript yellow
            "#FF5722",  # Java orange
            "#808080"   # Other gray
        ],
        show_labels=True
    )
    .save("survey_pie.png")
)
```

### Example 2: Exploded Donut Chart for Sales Breakdown

=== "C#"
```csharp
using Chartexa.Core.Chart;
using Chartexa.Core.Series;
using Chartexa.Core.Styles;

// Sales breakdown by region
var categories = new[] { "North America", "Europe", "Asia", "Other" };
var values = new[] { 120, 95, 80, 30 };
var explode = new[] { 0.1, 0, 0, 0 }; // Explode North America

var donutSeries = new DonutSeries
{
    Categories = categories,
    Values = values,
    InnerRadius = 0.5,
    ExplodeOffset = explode,
    SegmentColors = new[]
    {
        new ChartColor(52, 152, 219),   // NA blue
        new ChartColor(46, 204, 113),   // Europe green
        new ChartColor(231, 76, 60),    // Asia red
        new ChartColor(155, 89, 182)    // Other purple
    }
};

var chart = new Chart
{
    Width = 600,
    Height = 400,
    Series = { donutSeries }
};
chart.Save("sales_donut_exploded.png");
```

=== "Python"
```python
from chartexa import Chart

categories = ["North America", "Europe", "Asia", "Other"]
values = [120, 95, 80, 30]
explode = [0.1, 0, 0, 0]  # Explode North America

chart = (
    Chart(width=600, height=400)
    .donut(
        categories,
        values,
        inner_radius=0.5,
        segment_colors=[
            "#3498DB",  # NA blue
            "#2ECC71",  # Europe green
            "#E74C3C",  # Asia red
            "#9B59B6"   # Other purple
        ],
        explode_offset=explode
    )
    .save("sales_donut_exploded.png")
)
```

### Example 3: Donut Chart with Custom Center Label

=== "C#"
```csharp
using Chartexa.Core.Chart;
using Chartexa.Core.Series;
using Chartexa.Core.Styles;

// Custom center label (requires overlay)
var categories = new[] { "Completed", "In Progress", "Pending" };
var values = new[] { 70, 20, 10 };

var donutSeries = new DonutSeries
{
    Categories = categories,
    Values = values,
    InnerRadius = 0.6,
    SegmentColors = new[]
    {
        new ChartColor(46, 204, 113),   // Completed green
        new ChartColor(241, 196, 15),   // In Progress yellow
        new ChartColor(231, 76, 60)     // Pending red
    },
    ShowLabels = false
};

var chart = new Chart
{
    Width = 400,
    Height = 400,
    Series = { donutSeries },
    CenterOverlay = new ChartTextOverlay
    {
        Text = "100 Tasks",
        Font = new ChartFont("Segoe UI", 18, ChartFontStyle.Bold),
        Color = new ChartColor(40, 40, 40)
    }
};
chart.Save("tasks_donut_center.png");
```

=== "Python"
```python
from chartexa import Chart

categories = ["Completed", "In Progress", "Pending"]
values = [70, 20, 10]

chart = (
    Chart(width=400, height=400)
    .donut(
        categories,
        values,
        inner_radius=0.6,
        segment_colors=[
            "#2ECC71",  # Completed green
            "#F1C40F",  # In Progress yellow
            "#E74C3C"   # Pending red
        ],
        show_labels=False
    )
    .overlay_text(
        "100 Tasks",
        font=("Segoe UI", 18, "bold"),
        color="#282828"
    )
    .save("tasks_donut_center.png")
)
```

---

## Performance Notes

Chartexa's DirectX 12 renderer efficiently handles donut and pie charts with hundreds of segments, maintaining smooth interaction and rendering even with large datasets. Segment rendering is vector-based, ensuring crisp visuals at any resolution.

- Rendering time is typically under 10 ms for charts with up to 100 segments.
- Tooltips and interactive highlighting are GPU-accelerated.
- For charts with thousands of segments, consider disabling labels or tooltips to optimize performance.

!!! tip "Performance Tip"
    Use the DirectX12 backend for interactive dashboards and large segment counts. For static exports or simple charts, Skia and WPF backends are also supported.

---

## When to Use

- Visualizing categorical proportions (market share, budget, survey results)
- Displaying parts of a whole in dashboards or reports
- Highlighting a key segment with exploded or colored effects
- Adding summary or total information in the center (donut charts)
- Comparing distributions across multiple categories

---

## Related

- [Column Series](column-series.md)
- [Stacked Series](stacked-series.md)
- [Legend and Tooltip](../interaction/legend-tooltip.md)
- [Theme Engine](../../theming/theme-engine.md)

---

> **Last updated:** 2024-06-13 14:35 UTC | **Status:** draft
> **Last updated:** 2026-04-08 08:56 UTC | **Status:** Placeholder -- awaiting AI expansion
