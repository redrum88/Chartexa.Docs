---
title: "Heatmap Series"
section: "chart-types/2d"
last_updated: "2024-06-12 16:22 UTC"
status: draft
---

# Heatmap Series

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `HeatmapSeries` visualizes two-dimensional scalar data as a color-coded grid, mapping values to colors via configurable palettes (e.g., Viridis, Plasma). Use it to display spatial distributions, intensity maps, or correlation matrices.

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
using Chartexa.ChartTypes;
using Chartexa.Palettes;

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Longitude" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Latitude" };

// Generate sample data: 2D Gaussian
int width = 100, height = 80;
double[,] data = new double[width, height];
for (int x = 0; x < width; x++)
    for (int y = 0; y < height; y++)
        data[x, y] = Math.Exp(-((x - 50) * (x - 50) + (y - 40) * (y - 40)) / 800.0);

// Create heatmap series
var heatmapSeries = new HeatmapSeries
{
    Data = data,
    XAxis = xAxis,
    YAxis = yAxis,
    Palette = Colormap.Viridis,
    MinValue = 0,
    MaxValue = 1
};

// Add to chart
var chart = new Chart();
chart.AddAxis(xAxis);
chart.AddAxis(yAxis);
chart.AddSeries(heatmapSeries);
chart.Show();
```

=== "Python"

```python
import numpy as np
from chartexa import Chart

# Generate 2D Gaussian data
width, height = 100, 80
x = np.arange(width)
y = np.arange(height)
X, Y = np.meshgrid(x, y)
data = np.exp(-((X - 50)**2 + (Y - 40)**2) / 800.0)

# Create heatmap chart
chart = (
    Chart(width=800, height=600)
    .heatmap(data, palette="viridis", min_value=0, max_value=1)
    .x_axis(title="Longitude")
    .y_axis(title="Latitude")
    .save("heatmap_quickstart.png")
)
```

---

## Concepts

The `HeatmapSeries` renders a rectangular grid of cells, each colored according to its value using a colormap palette. This approach is ideal for visualizing spatial patterns, intensity distributions, or relationships in matrix data. 

Heatmaps are commonly used in scientific, engineering, and financial domains to display temperature maps, correlation matrices, population densities, and more. Chartexa's heatmap supports high-resolution grids, real-time updates, and customizable palettes for clear interpretation.

The palette maps numeric values to colors, allowing you to emphasize gradients, thresholds, or outliers. You can configure axis ranges, cell size, and value normalization to suit your dataset.

---

## Basic Usage

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using Chartexa.Palettes;

// Example: Visualize a correlation matrix
double[,] correlation = new double[,]
{
    { 1.0, 0.8, 0.2 },
    { 0.8, 1.0, -0.3 },
    { 0.2, -0.3, 1.0 }
};

var xAxis = new NumericAxis { Id = "X", AxisTitle = "Variable" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Variable" };

var heatmapSeries = new HeatmapSeries
{
    Data = correlation,
    XAxis = xAxis,
    YAxis = yAxis,
    Palette = Colormap.Plasma,
    MinValue = -1,
    MaxValue = 1,
    CellSize = 1.0
};

var chart = new Chart();
chart.AddAxis(xAxis);
chart.AddAxis(yAxis);
chart.AddSeries(heatmapSeries);
chart.Show();
```

=== "Python"

```python
import numpy as np
from chartexa import Chart

# Example: Correlation matrix
correlation = np.array([
    [1.0, 0.8, 0.2],
    [0.8, 1.0, -0.3],
    [0.2, -0.3, 1.0]
])

chart = (
    Chart(width=400, height=400)
    .heatmap(correlation, palette="plasma", min_value=-1, max_value=1, cell_size=1.0)
    .x_axis(title="Variable")
    .y_axis(title="Variable")
    .save("correlation_heatmap.png")
)
```

---

## Configuration

| Property    | Type           | Default    | Description                                                  |
|-------------|----------------|------------|--------------------------------------------------------------|
| `Data`      | `double[,]`    | Required   | 2D array of values to display                                |
| `Palette`   | `Colormap`     | Viridis    | Color mapping palette (Viridis, Plasma, etc.)                |
| `MinValue`  | `double`       | Auto       | Minimum value for color normalization                        |
| `MaxValue`  | `double`       | Auto       | Maximum value for color normalization                        |
| `CellSize`  | `double`       | 1.0        | Size of each cell in axis units                              |
| `XAxis`     | `Axis`         | Required   | X axis object                                                |
| `YAxis`     | `Axis`         | Required   | Y axis object                                                |
| `Opacity`   | `double`       | 1.0        | Opacity of the heatmap layer (0.0-1.0)                       |
| `ShowLegend`| `bool`         | true       | Display color legend beside the chart                        |
| `Interpolate`| `bool`        | false      | Smooth color transitions between cells                       |

!!! tip "Palette Selection"
    Chartexa supports built-in palettes: Viridis, Plasma, Inferno, Magma, and custom palettes via `Colormap.Custom`.

!!! warning
    The `Data` array must be rectangular (all rows same length), and non-empty.

---

## Examples

### Example 1: Real-Time Sensor Data

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using Chartexa.Palettes;

// Simulate live temperature grid
int width = 50, height = 50;
double[,] tempGrid = new double[width, height];
Random rand = new Random();
for (int x = 0; x < width; x++)
    for (int y = 0; y < height; y++)
        tempGrid[x, y] = 20 + 10 * Math.Sin(x / 8.0) * Math.Cos(y / 8.0) + rand.NextDouble();

var xAxis = new NumericAxis { Id = "X", AxisTitle = "X Position" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Y Position" };

var heatmapSeries = new HeatmapSeries
{
    Data = tempGrid,
    XAxis = xAxis,
    YAxis = yAxis,
    Palette = Colormap.Inferno,
    MinValue = 15,
    MaxValue = 35,
    CellSize = 1.0
};

var chart = new Chart();
chart.AddAxis(xAxis);
chart.AddAxis(yAxis);
chart.AddSeries(heatmapSeries);
chart.Show();
```

=== "Python"

```python
import numpy as np
from chartexa import Chart

# Simulate live temperature grid
width, height = 50, 50
x = np.arange(width)
y = np.arange(height)
X, Y = np.meshgrid(x, y)
temp_grid = 20 + 10 * np.sin(X / 8.0) * np.cos(Y / 8.0) + np.random.rand(width, height)

chart = (
    Chart(width=600, height=600)
    .heatmap(temp_grid, palette="inferno", min_value=15, max_value=35)
    .x_axis(title="X Position")
    .y_axis(title="Y Position")
    .save("sensor_heatmap.png")
)
```

### Example 2: Population Density Map

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using Chartexa.Palettes;

// Example: Population density (synthetic)
int width = 120, height = 80;
double[,] density = new double[width, height];
for (int x = 0; x < width; x++)
    for (int y = 0; y < height; y++)
        density[x, y] = 1000 * Math.Exp(-((x - 60) * (x - 60) + (y - 40) * (y - 40)) / 900.0);

var xAxis = new NumericAxis { Id = "X", AxisTitle = "Longitude" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Latitude" };

var heatmapSeries = new HeatmapSeries
{
    Data = density,
    XAxis = xAxis,
    YAxis = yAxis,
    Palette = Colormap.Magma,
    MinValue = 0,
    MaxValue = 1000,
    CellSize = 0.5
};

var chart = new Chart();
chart.AddAxis(xAxis);
chart.AddAxis(yAxis);
chart.AddSeries(heatmapSeries);
chart.Show();
```

=== "Python"

```python
import numpy as np
from chartexa import Chart

# Synthetic population density
width, height = 120, 80
x = np.arange(width)
y = np.arange(height)
X, Y = np.meshgrid(x, y)
density = 1000 * np.exp(-((X - 60)**2 + (Y - 40)**2) / 900.0)

chart = (
    Chart(width=900, height=600)
    .heatmap(density, palette="magma", min_value=0, max_value=1000, cell_size=0.5)
    .x_axis(title="Longitude")
    .y_axis(title="Latitude")
    .save("population_density_heatmap.png")
)
```

### Example 3: Custom Palette

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using Chartexa.Palettes;

// Custom palette: blue to red
var customPalette = Colormap.Custom(new[]
{
    new ChartColor(0, 0, 255),   // Blue
    new ChartColor(255, 0, 0)    // Red
});

double[,] values = new double[,] { { 0, 1 }, { 1, 0 } };

var xAxis = new NumericAxis { Id = "X", AxisTitle = "A" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "B" };

var heatmapSeries = new HeatmapSeries
{
    Data = values,
    XAxis = xAxis,
    YAxis = yAxis,
    Palette = customPalette,
    MinValue = 0,
    MaxValue = 1
};

var chart = new Chart();
chart.AddAxis(xAxis);
chart.AddAxis(yAxis);
chart.AddSeries(heatmapSeries);
chart.Show();
```

=== "Python"

```python
import numpy as np
from chartexa import Chart

# Custom palette: blue to red
custom_palette = [(0, 0, 255), (255, 0, 0)]  # RGB tuples

values = np.array([[0, 1], [1, 0]])

chart = (
    Chart(width=300, height=300)
    .heatmap(values, palette=custom_palette, min_value=0, max_value=1)
    .x_axis(title="A")
    .y_axis(title="B")
    .save("custom_palette_heatmap.png")
)
```

---

## Performance Notes

Chartexa's DirectX 12 renderer efficiently handles large heatmaps (up to 10 million cells) with minimal latency. GPU acceleration ensures real-time updates for streaming or interactive data. 

- Rendering speed is proportional to grid size; typical 1000x1000 heatmaps render in under 50ms on modern GPUs.
- Python integration leverages .NET runtime for hardware acceleration.
- Memory usage scales with grid dimensions; consider downsampling for extremely large datasets.

!!! tip "Performance Tip"
    For grids larger than 2000x2000, use DirectX12RenderContext and disable interpolation for maximum throughput.

!!! note
    Python requires the .NET 10 Runtime to be installed for hardware-accelerated rendering.

---

## When to Use

- Visualizing spatial distributions (e.g., temperature, population, intensity)
- Displaying correlation matrices or confusion matrices
- Mapping sensor arrays or hardware outputs
- Showing density plots or occupancy grids
- Highlighting outliers or gradients in 2D data

---

## Related

- [FastLineRenderableSeries](./line-series.md)
- [NumericAxis](../axes/numeric-axis.md)
- [Colormap Palettes](../theming/palettes.md)

---

> **Last updated:** 2024-06-12 16:22 UTC | **Status:** draft