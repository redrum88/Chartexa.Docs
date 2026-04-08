---
title: "Waterfall Series"
section: "chart-types/2d"
last_updated: "2024-06-10 15:35 UTC"
status: draft
---

# Waterfall Series

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The Waterfall Series (`WaterfallRenderableSeries`) provides a time-frequency waterfall display, commonly used in audio, RF, and scientific applications to visualize spectral evolution over time. It renders a sequence of horizontal slices (spectra) as colored bands, stacking them vertically to show changes in frequency content across time.

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
using Chartexa.Rendering;

// Create axes
var xAxis = new NumericAxis { Id = "Freq", AxisTitle = "Frequency (Hz)" };
var yAxis = new NumericAxis { Id = "Time", AxisTitle = "Time (s)" };

// Create waterfall data: 100 time slices, 512 frequency bins
var waterfallData = new WaterfallDataSeries
{
    FrequencyBins = Enumerable.Range(0, 512).Select(i => i * 10.0).ToArray(), // 0-5110 Hz
    TimeStamps = Enumerable.Range(0, 100).Select(i => i * 0.1).ToArray(),     // 0-9.9 s
    Amplitudes = GenerateSpectrogram(100, 512) // Returns double[100,512]
};

// Create waterfall series
var waterfallSeries = new WaterfallRenderableSeries
{
    DataSeries = waterfallData,
    ColorMap = ColorMaps.Viridis,
    Opacity = 0.95
};

// Add to chart
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(waterfallSeries);
chart.Render();
```

=== "Python"
```python
from chartexa import Chart, colormap
import numpy as np

# Generate waterfall data: 100 time slices, 512 frequency bins
freq_bins = np.arange(0, 512) * 10.0  # 0-5110 Hz
time_stamps = np.arange(0, 100) * 0.1 # 0-9.9 s
amplitudes = np.random.normal(loc=0, scale=1, size=(100, 512)) + np.sin(np.linspace(0, 20, 512))[None,:]

chart = (
    Chart(width=900, height=600)
    .waterfall(
        freq_bins=freq_bins,
        time_stamps=time_stamps,
        amplitudes=amplitudes,
        colormap=colormap.viridis,
        opacity=0.95
    )
    .x_axis(title="Frequency (Hz)")
    .y_axis(title="Time (s)")
    .save("waterfall.png")
)
```

---

## Concepts

The waterfall series is a specialized visualization for time-frequency data, where each row represents a spectrum at a specific timestamp. The chart stacks these spectra vertically, using color to encode amplitude or power at each frequency bin. This approach is widely used in signal processing, audio analysis, RF monitoring, and scientific instrumentation.

Waterfall charts are ideal for visualizing how spectral content evolves over time, such as tracking frequency shifts, transient signals, or periodic patterns. Unlike heatmaps, waterfall displays emphasize the temporal ordering and allow for real-time streaming updates.

Chartexa's waterfall series is optimized for large datasets, supporting thousands of time slices and high-resolution frequency bins, with GPU-accelerated rendering for smooth interaction.

---

## Basic Usage

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using Chartexa.Rendering;
using System.Linq;

// Generate frequency bins and time stamps
double[] freqBins = Enumerable.Range(0, 256).Select(i => i * 20.0).ToArray(); // 0-5110 Hz
double[] timeStamps = Enumerable.Range(0, 50).Select(i => i * 0.2).ToArray(); // 0-9.8 s

// Generate amplitudes: shape [50, 256]
double[,] amplitudes = new double[50, 256];
for (int t = 0; t < 50; t++)
{
    for (int f = 0; f < 256; f++)
    {
        amplitudes[t, f] = Math.Sin(0.01 * f * t) + 0.5 * Math.Cos(0.05 * f) + 0.2 * t;
    }
}

// Create WaterfallDataSeries
var waterfallData = new WaterfallDataSeries
{
    FrequencyBins = freqBins,
    TimeStamps = timeStamps,
    Amplitudes = amplitudes
};

// Configure WaterfallRenderableSeries
var waterfallSeries = new WaterfallRenderableSeries
{
    DataSeries = waterfallData,
    ColorMap = ColorMaps.Inferno,
    Opacity = 0.85,
    SliceThickness = 2,
    ShowGridLines = true
};

// Setup chart
var chart = new Chart();
chart.Axes.Add(new NumericAxis { Id = "Freq", AxisTitle = "Frequency (Hz)" });
chart.Axes.Add(new NumericAxis { Id = "Time", AxisTitle = "Time (s)" });
chart.Series.Add(waterfallSeries);
chart.Render();
```

=== "Python"
```python
from chartexa import Chart, colormap
import numpy as np

freq_bins = np.linspace(0, 5000, 256)
time_stamps = np.linspace(0, 10, 50)
amplitudes = np.zeros((50, 256))

for t in range(50):
    amplitudes[t] = np.sin(0.01 * freq_bins * t) + 0.5 * np.cos(0.05 * freq_bins) + 0.2 * t

chart = (
    Chart(width=800, height=500)
    .waterfall(
        freq_bins=freq_bins,
        time_stamps=time_stamps,
        amplitudes=amplitudes,
        colormap=colormap.inferno,
        opacity=0.85,
        slice_thickness=2,
        show_grid=True
    )
    .x_axis(title="Frequency (Hz)")
    .y_axis(title="Time (s)")
    .save("waterfall_basic.png")
)
```

---

## Configuration

| Property         | Type           | Default     | Description                                                        |
|------------------|----------------|-------------|--------------------------------------------------------------------|
| `DataSeries`     | WaterfallDataSeries | Required    | The time-frequency data to display                                 |
| `ColorMap`       | ColorMap       | Viridis     | Color mapping for amplitude values                                 |
| `Opacity`        | double         | 1.0         | Transparency of waterfall slices (0.0-1.0)                         |
| `SliceThickness` | int            | 1           | Vertical pixel thickness of each time slice                        |
| `ShowGridLines`  | bool           | false       | Display grid lines between slices                                  |
| `ZOffset`        | double         | 0.0         | Depth offset for 3D-like rendering (if enabled)                    |
| `AutoRange`      | bool           | true        | Automatically fit axes to data                                     |
| `HighlightSlice` | int?           | null        | Index of slice to highlight                                        |
| `LegendLabel`    | string         | "Waterfall" | Label for legend                                                   |

!!! note
    Python keyword arguments match C# property names, but use snake_case (e.g., `slice_thickness`, `show_grid`).

---

## Examples

### Example 1: Audio Spectrogram Visualization

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using System.IO;

// Load audio spectrogram data from CSV
var freqBins = File.ReadAllLines("audio_freq_bins.csv").Select(double.Parse).ToArray();
var timeStamps = File.ReadAllLines("audio_time_stamps.csv").Select(double.Parse).ToArray();
var amplitudes = LoadMatrixFromCsv("audio_spectrogram.csv"); // double[,]

// Create waterfall series
var waterfallData = new WaterfallDataSeries
{
    FrequencyBins = freqBins,
    TimeStamps = timeStamps,
    Amplitudes = amplitudes
};

var waterfallSeries = new WaterfallRenderableSeries
{
    DataSeries = waterfallData,
    ColorMap = ColorMaps.Magma,
    Opacity = 0.9,
    SliceThickness = 3
};

var chart = new Chart();
chart.Axes.Add(new NumericAxis { Id = "Freq", AxisTitle = "Frequency (Hz)" });
chart.Axes.Add(new NumericAxis { Id = "Time", AxisTitle = "Time (s)" });
chart.Series.Add(waterfallSeries);
chart.Render();
```

=== "Python"
```python
from chartexa import Chart, colormap
import numpy as np

freq_bins = np.loadtxt("audio_freq_bins.csv")
time_stamps = np.loadtxt("audio_time_stamps.csv")
amplitudes = np.loadtxt("audio_spectrogram.csv")

chart = (
    Chart(width=1000, height=600)
    .waterfall(
        freq_bins=freq_bins,
        time_stamps=time_stamps,
        amplitudes=amplitudes,
        colormap=colormap.magma,
        opacity=0.9,
        slice_thickness=3
    )
    .x_axis(title="Frequency (Hz)")
    .y_axis(title="Time (s)")
    .save("audio_waterfall.png")
)
```

### Example 2: Real-Time RF Spectrum Monitoring

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;
using System.Threading.Tasks;

// Simulate real-time streaming
var freqBins = Enumerable.Range(0, 1024).Select(i => i * 1.0).ToArray(); // 0-1023 MHz
var timeStamps = new List<double>();
var amplitudes = new List<double[]>();

var chart = new Chart();
var waterfallData = new WaterfallDataSeries
{
    FrequencyBins = freqBins,
    TimeStamps = new double[0],
    Amplitudes = new double[0, 1024]
};
var waterfallSeries = new WaterfallRenderableSeries
{
    DataSeries = waterfallData,
    ColorMap = ColorMaps.Turbo,
    Opacity = 0.95
};
chart.Axes.Add(new NumericAxis { Id = "Freq", AxisTitle = "Frequency (MHz)" });
chart.Axes.Add(new NumericAxis { Id = "Time", AxisTitle = "Time (s)" });
chart.Series.Add(waterfallSeries);
chart.Render();

Task.Run(async () =>
{
    for (int t = 0; t < 200; t++)
    {
        double[] spectrum = AcquireRfSpectrum(freqBins); // Simulated
        timeStamps.Add(t * 0.05);
        amplitudes.Add(spectrum);
        waterfallData.TimeStamps = timeStamps.ToArray();
        waterfallData.Amplitudes = To2DArray(amplitudes);
        chart.Update();
        await Task.Delay(50);
    }
});
```

=== "Python"
```python
from chartexa import Chart, colormap
import numpy as np
import time

freq_bins = np.arange(0, 1024)
time_stamps = []
amplitudes = []

chart = (
    Chart(width=1200, height=700)
    .waterfall(
        freq_bins=freq_bins,
        time_stamps=[],
        amplitudes=np.empty((0, 1024)),
        colormap=colormap.turbo,
        opacity=0.95
    )
    .x_axis(title="Frequency (MHz)")
    .y_axis(title="Time (s)")
    .show()  # Interactive window
)

for t in range(200):
    spectrum = np.random.normal(loc=0, scale=1, size=1024) + np.sin(freq_bins * 0.01 * t)
    time_stamps.append(t * 0.05)
    amplitudes.append(spectrum)
    chart.update_waterfall(
        time_stamps=np.array(time_stamps),
        amplitudes=np.vstack(amplitudes)
    )
    time.sleep(0.05)
```

### Example 3: Highlighting a Specific Time Slice

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.ChartTypes;

// ... (setup as above)
var waterfallSeries = new WaterfallRenderableSeries
{
    DataSeries = waterfallData,
    ColorMap = ColorMaps.Viridis,
    HighlightSlice = 25 // Highlights the 25th time slice
};
```

=== "Python"
```python
chart = (
    Chart(width=800, height=400)
    .waterfall(
        freq_bins=freq_bins,
        time_stamps=time_stamps,
        amplitudes=amplitudes,
        colormap=colormap.viridis,
        highlight_slice=25
    )
    .x_axis(title="Frequency (Hz)")
    .y_axis(title="Time (s)")
    .save("highlighted_slice.png")
)
```

---

## Performance Notes

Chartexa's waterfall series leverages GPU acceleration via DirectX 12 for rendering large spectrograms. Typical performance benchmarks:

- Rendering 10,000 time slices × 2,048 frequency bins: < 30 ms per frame on modern GPUs
- Real-time streaming updates: supports > 100 FPS for datasets up to 2 million points
- Python integration uses native .NET backend; ensure .NET 10 Runtime is installed for optimal performance

!!! tip "Performance Tip"
    Use the DirectX12 renderer for datasets exceeding 100K points. For static or small datasets, Skia backend may suffice.

!!! warning
    WaterfallDataSeries requires amplitude arrays of shape `[num_time_slices, num_freq_bins]`. Mismatched dimensions will throw an error.

---

## When to Use

- Visualizing audio spectrograms or frequency evolution over time
- RF spectrum monitoring and signal analysis
- Scientific instrumentation (e.g., seismic, EEG, radar)
- Real-time streaming of time-frequency data
- Detecting transient events, frequency shifts, or periodic patterns

---

## Related

- [Heatmap Series](./heatmap-series.md)
- [FastLine Series](./fastline-series.md)
- [Axis Ranging](../axes/axis-ranging.md)
- [DirectX12 Renderer](../rendering/directx12.md)

---

> **Last updated:** 2024-06-10 15:35 UTC | **Status:** draft