---
title: "First Chart in C#"
section: "getting-started"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# First Chart in C#

## Summary

Create your first Chartexa chart in C# using the core API. Build a chart surface, add axes, create a data series, attach a renderable series, and export to an image file.

---

## Quick Start

`csharp
using Chartexa.Core;
using Chartexa.Core.Axes;
using Chartexa.Core.Series;
using Chartexa.Data.Series;

// 1. Create the chart surface
var surface = new ChartSurface { Width = 1200, Height = 600 };

// 2. Add axes
surface.XAxes.Add(new NumericAxis { AxisTitle = "Sample" });
surface.YAxes.Add(new NumericAxis { AxisTitle = "Value" });

// 3. Create data
var dataSeries = new XyDataSeries();
dataSeries.Append(new double[] { 0, 1, 2, 3, 4 },
                  new double[] { 28.3, 29.1, 30.5, 31.2, 29.8 });

// 4. Create a renderable series
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    Stroke = new ChartColor(243, 139, 168),   // Catppuccin Mocha red
    StrokeThickness = 2
};
surface.RenderableSeries.Add(lineSeries);

// 5. Export
surface.RenderToFile("first_chart.png");
`

---

## Concepts

The C# API is built around four key objects:

| Object | Role |
|---|---|
| `ChartSurface` | The canvas that holds everything |
| `NumericAxis` / `DateTimeAxis` / `CategoryAxis` / `LogarithmicAxis` | Define the coordinate space |
| `XyDataSeries` / `OhlcDataSeries` | Hold the raw data |
| `FastLineRenderableSeries` / `XyScatterRenderableSeries` / etc. | Define how data is drawn |

Data and rendering are separated: a `DataSeries` can be shared across multiple renderable series, and renderable series can be swapped without changing the data.

---

## Multiple Series

`csharp
var sin = new XyDataSeries();
var cos = new XyDataSeries();

for (int i = 0; i < 100; i++)
{
    double x = i * 0.1;
    sin.Append(x, Math.Sin(x));
    cos.Append(x, Math.Cos(x));
}

surface.RenderableSeries.Add(new FastLineRenderableSeries
{
    DataSeries = sin,
    Stroke = new ChartColor(243, 139, 168),
    StrokeThickness = 2
});

surface.RenderableSeries.Add(new FastLineRenderableSeries
{
    DataSeries = cos,
    Stroke = new ChartColor(137, 180, 250),
    StrokeThickness = 2
});
`

---

## Theming

`csharp
using Chartexa.Core.Theming;

var theme = ThemeManager.GetTheme("catppuccin_mocha");
surface.ApplyTheme(theme);
`

Available presets: `dark`, `light`, `catppuccin_mocha`, `catppuccin_latte`, `catppuccin_frappe`, `catppuccin_macchiato`, `github_dark`, `github_light`, `dracula`, `nord`, `solarized_dark`, `solarized_light`, `minimal`, `scientific`.

---

## WPF Integration

For desktop applications, use the WPF control:

`xml
<Window xmlns:cx="clr-namespace:Chartexa.WPF;assembly=Chartexa.WPF">
    <cx:ChartexaChart x:Name="chartControl" />
</Window>
`

`csharp
chartControl.Surface.XAxes.Add(new NumericAxis());
chartControl.Surface.YAxes.Add(new NumericAxis());
// Add series as above
`

---

## Related

- [First Chart in Python](first-chart-python.md) -- the equivalent Python walkthrough
- [Choosing a Renderer](choosing-a-renderer.md) -- DirectX 12 vs Skia vs WPF trade-offs
- [Line Series](../chart-types/2d/line-series.md) -- full line series configuration

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
