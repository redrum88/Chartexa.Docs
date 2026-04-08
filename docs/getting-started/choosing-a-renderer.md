---
title: "Choosing a Renderer"
section: "getting-started"
last_updated: "2024-06-13 15:42 UTC"
status: draft
---

# Choosing a Renderer

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

Chartexa supports four rendering backends: DirectX 12, Skia, WPF, and Web. Each renderer offers unique capabilities and trade-offs for performance, platform compatibility, and visual fidelity. Selecting the appropriate renderer is essential for achieving optimal results in your application, whether you target desktop, cross-platform, or web environments.

---

## Installation

### .NET (NuGet)

```bash
dotnet add package Chartexa.Core
dotnet add package Chartexa.DirectX12
dotnet add package Chartexa.Skia
dotnet add package Chartexa.Wpf
dotnet add package Chartexa.Web
```

### Python (PyPI)

```bash
pip install chartexa
```

!!! note
    Some renderers require additional dependencies:
    - DirectX 12: Windows 10+, .NET 10 Runtime, DirectX 12-capable GPU
    - WPF: Windows only, .NET Desktop Runtime
    - Skia: Cross-platform, no special requirements
    - Web: Requires Chartexa Web server or integration with web frameworks

---

## Quick Start

### C#

=== "C#"
```csharp
using Chartexa.Core;
using Chartexa.Core.Renderers;
using Chartexa.Data.Series;
using Chartexa.Core.Axes;

// Choose renderer backend
var renderer = new DirectX12RenderContext(); // Or SkiaRenderContext, WpfRenderContext, WebRenderContext

// Create chart
var chart = new Chart
{
    Width = 800,
    Height = 400,
    RenderContext = renderer
};

// Add axes
chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Time (s)" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Value" });

// Add data series
var dataSeries = new XyDataSeries();
dataSeries.Append(
    new double[] { 0, 1, 2, 3, 4 },
    new double[] { 10, 15, 13, 17, 20 }
);

chart.Series.Add(new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(34, 139, 34), // Forest Green
    StrokeThickness = 2
});

// Render chart
chart.Render();
```

### Python

=== "Python"
```python
from chartexa import Chart

# Choose renderer backend: "directx12", "skia", "wpf", "web"
chart = (
    Chart(width=800, height=400, renderer="skia")
    .line([0, 1, 2, 3, 4], [10, 15, 13, 17, 20], stroke="#228B22", thickness=2)
    .x_axis(title="Time (s)")
    .y_axis(title="Value")
    .save("output.png")
)
```

---

## Concepts

Chartexa's rendering system abstracts the drawing of charts from the underlying platform. The renderer determines how visual elements are drawn, how efficiently large datasets are handled, and which environments are supported.

- **DirectX 12**: Hardware-accelerated, optimized for real-time and high-volume data visualization on Windows. Ideal for scientific, financial, or industrial applications requiring maximum performance.
- **Skia**: Cross-platform 2D graphics engine. Suitable for desktop and server environments where portability is important, with good performance and visual quality.
- **WPF**: Windows Presentation Foundation integration for seamless embedding in .NET desktop apps. Leverages WPF's UI features but is limited to Windows.
- **Web**: Enables rendering charts in browsers via WebAssembly or server-side image generation. Best for web dashboards and remote visualization.

Choosing a renderer affects performance, compatibility, and integration options. Chartexa allows you to switch renderers with minimal code changes, making it flexible for diverse deployment scenarios.

---

## Basic Usage

### C#

=== "C#"
```csharp
using Chartexa.Core;
using Chartexa.Core.Renderers;
using Chartexa.Data.Series;
using Chartexa.Core.Axes;

// Select renderer based on your environment
IRenderContext renderer = new SkiaRenderContext(); // For cross-platform
//IRenderContext renderer = new DirectX12RenderContext(); // For Windows, high performance

var chart = new Chart
{
    Width = 600,
    Height = 300,
    RenderContext = renderer
};

// Configure axes
chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Sample #" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Measurement" });

// Prepare data
var xData = new double[] { 1, 2, 3, 4, 5, 6 };
var yData = new double[] { 5.2, 6.1, 7.3, 6.8, 7.0, 7.5 };
var series = new XyDataSeries();
series.Append(xData, yData);

// Add line series
chart.Series.Add(new FastLineRenderableSeries
{
    DataSeries = series,
    StrokeColor = new ChartColor(70, 130, 180), // Steel blue
    StrokeThickness = 2
});

// Render chart (to file or window, depending on renderer)
chart.Render();
```

### Python

=== "Python"
```python
from chartexa import Chart

# Use Skia for cross-platform, DirectX12 for Windows
chart = (
    Chart(width=600, height=300, renderer="skia")
    .line([1, 2, 3, 4, 5, 6], [5.2, 6.1, 7.3, 6.8, 7.0, 7.5], stroke="#4682B4", thickness=2)
    .x_axis(title="Sample #")
    .y_axis(title="Measurement")
    .save("measurement.png")
)
```

---

## Configuration

Chartexa exposes renderer selection via the `RenderContext` property (C#) or `renderer` argument (Python). Each renderer has specific configuration options:

| Renderer      | Platform      | Property/Arg           | Default | Description                                         |
|---------------|--------------|------------------------|---------|-----------------------------------------------------|
| DirectX 12    | Windows 10+  | `DirectX12RenderContext` / `"directx12"` | None    | Hardware-accelerated, best for large datasets       |
| Skia          | All          | `SkiaRenderContext` / `"skia"`           | `"skia"`| Cross-platform, good performance                    |
| WPF           | Windows      | `WpfRenderContext` / `"wpf"`             | None    | Integrates with WPF UI                              |
| Web           | Web/Server   | `WebRenderContext` / `"web"`             | None    | For browser-based or remote rendering               |

Additional configuration options per renderer:

| Option              | Renderer(s)      | Type      | Default   | Description                                   |
|---------------------|------------------|-----------|-----------|-----------------------------------------------|
| `GpuDeviceId`       | DirectX12        | int       | 0         | Selects GPU device for rendering              |
| `Antialiasing`      | Skia, DirectX12  | bool      | true      | Enables/disables antialiasing                 |
| `OutputFormat`      | Web, Skia        | string    | "png"     | Output image format ("png", "svg", "jpg")     |
| `WindowHandle`      | WPF              | object    | None      | Embeds chart in WPF window                    |

---

## Examples

### Example 1: Real-Time Data Visualization (DirectX 12)

=== "C#"
```csharp
using Chartexa.Core;
using Chartexa.Core.Renderers;
using Chartexa.Data.Series;
using Chartexa.Core.Axes;

// Use DirectX12 for high-performance streaming
var renderer = new DirectX12RenderContext();

var chart = new Chart
{
    Width = 1200,
    Height = 600,
    RenderContext = renderer
};

chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Timestamp" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Sensor Value" });

var series = new XyDataSeries();
chart.Series.Add(new FastLineRenderableSeries
{
    DataSeries = series,
    StrokeColor = new ChartColor(255, 69, 0), // OrangeRed
    StrokeThickness = 2
});

// Simulate streaming
for (int i = 0; i < 100000; i++)
{
    series.Append(i, Math.Sin(i * 0.001) * 100);
}
chart.Render();
```

=== "Python"
```python
from chartexa import Chart
import numpy as np

# Use DirectX12 for large datasets (Windows only)
x = np.arange(0, 100000)
y = np.sin(x * 0.001) * 100

chart = (
    Chart(width=1200, height=600, renderer="directx12")
    .line(x, y, stroke="#FF4500", thickness=2)
    .x_axis(title="Timestamp")
    .y_axis(title="Sensor Value")
    .save("streaming.png")
)
```

### Example 2: Cross-Platform Export (Skia)

=== "C#"
```csharp
using Chartexa.Core;
using Chartexa.Core.Renderers;
using Chartexa.Data.Series;
using Chartexa.Core.Axes;

// Use Skia for PNG/SVG export on any OS
var renderer = new SkiaRenderContext { OutputFormat = "svg" };

var chart = new Chart
{
    Width = 800,
    Height = 400,
    RenderContext = renderer
};

chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Category" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Score" });

var series = new XyDataSeries();
series.Append(
    new double[] { 1, 2, 3, 4 },
    new double[] { 80, 85, 90, 95 }
);

chart.Series.Add(new FastColumnRenderableSeries
{
    DataSeries = series,
    FillColor = new ChartColor(30, 144, 255) // Dodger Blue
});

chart.Render("scores.svg");
```

=== "Python"
```python
from chartexa import Chart

# Skia renderer for SVG export
chart = (
    Chart(width=800, height=400, renderer="skia", output_format="svg")
    .column([1, 2, 3, 4], [80, 85, 90, 95], fill="#1E90FF")
    .x_axis(title="Category")
    .y_axis(title="Score")
    .save("scores.svg")
)
```

### Example 3: Embedding in WPF Application

=== "C#"
```csharp
using Chartexa.Core;
using Chartexa.Core.Renderers;
using Chartexa.Data.Series;
using Chartexa.Core.Axes;

// WPF integration (Windows desktop apps)
var renderer = new WpfRenderContext { WindowHandle = myWpfWindow };

var chart = new Chart
{
    Width = 400,
    Height = 300,
    RenderContext = renderer
};

chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Day" });
chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Temperature (°C)" });

var series = new XyDataSeries();
series.Append(
    new double[] { 1, 2, 3, 4, 5, 6, 7 },
    new double[] { 22, 24, 21, 23, 25, 26, 24 }
);

chart.Series.Add(new FastLineRenderableSeries
{
    DataSeries = series,
    StrokeColor = new ChartColor(255, 215, 0), // Gold
    StrokeThickness = 2
});

chart.Render();
```

!!! note
    WPF renderer is only available for .NET desktop applications on Windows.

---

## Performance Notes

- **DirectX 12**: Achieves >1,000,000 points at 60 FPS on modern GPUs. Best for real-time, interactive charts and large datasets.
- **Skia**: Handles up to 500,000 points efficiently; suitable for batch exports and cross-platform apps.
- **WPF**: Performance depends on WPF's rendering pipeline; ideal for UI integration but not for massive datasets.
- **Web**: Performance varies by client/browser; recommended for moderate datasets and interactive dashboards.

!!! tip "Performance Tip"
    Use DirectX 12 for datasets exceeding 100,000 points or when real-time interactivity is required.

!!! warning
    DirectX 12 renderer requires a compatible GPU and Windows 10 or later.

---

## When to Use

- **DirectX 12**
    - Scientific, financial, or industrial applications on Windows
    - Real-time streaming and large datasets
    - Maximum hardware acceleration
- **Skia**
    - Cross-platform desktop/server apps
    - Exporting charts to PNG/SVG
    - Moderate datasets, batch processing
- **WPF**
    - Embedding charts in Windows desktop UI
    - Integration with WPF controls and events
    - Small to medium datasets
- **Web**
    - Browser-based dashboards and remote visualization
    - Interactive web apps
    - Lightweight server-side rendering

---

## Related

- [Rendering Backends Comparison](../rendering/rendering-backends.md)
- [Axis Configuration](../axes/axis-configuration.md)
- [Exporting Charts](../export/exporting-charts.md)

---

> **Last updated:** 2024-06-13 15:42 UTC | **Status:** draft