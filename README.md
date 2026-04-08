# Chartexa Documentation

<div class="hero" markdown>

# Chartexa

**High-Performance, Multi-Backend Charting Engine for .NET and Python**

A modular, renderer-agnostic visualization platform built in C# / .NET 10 — designed for financial, scientific, real-time, and industrial applications requiring extreme rendering speed and flexibility.

[Get Started](getting-started/installation.md){ .md-button .md-button--primary }
[View Examples](examples/index.md){ .md-button }
[API Reference](api-reference/index.md){ .md-button }

</div>

---

## What is Chartexa?

Chartexa is a **comprehensive data visualization engine** — not a wrapper around an existing renderer, but a ground-up charting platform with a clean separation between data, logic, rendering, and interaction.

It ships as a family of NuGet packages (C#) and a PyPI package (Python), giving you full control over how charts are composed, styled, and rendered.

### Key Capabilities

| Capability | Details |
|---|---|
| **Rendering Backends** | DirectX 12 (GPU-accelerated), SkiaSharp (cross-platform), WPF native, Web/JSON export |
| **Chart Types** | 50+ series types — line, scatter, candlestick, heatmap, 3D surface, gauges, instruments, and more |
| **Data Sources** | 40+ built-in data source integrations — MQTT, OPC UA, Modbus, serial, audio, GPS, CAN bus, and more |
| **Interaction** | Zoom, pan, rubber-band zoom, crosshair cursor, tooltips, hit testing |
| **Theming** | Token-based theme engine with JSON-serializable definitions and per-widget overrides |
| **Layout** | Dashboard layout engine with grid and absolute positioning, nested containers |
| **Python** | Full Python wrapper with fluent API, Jupyter Notebook support, and image export |
| **Performance** | SIMD coordinate transforms, GPU batching, object pooling, double-buffered swap chain |

### Who is Chartexa for?

- **Financial systems** — candlestick, OHLC, real-time streaming, technical indicators
- **Scientific computing** — spectrum analyzers, Bode/Nyquist plots, oscilloscopes, heatmaps
- **Industrial & IoT** — OPC UA, Modbus, CAN bus, sensor dashboards, PID controllers
- **Real-time analytics** — high-frequency data updates, large dataset visualization
- **Audio & Signal Processing** — FFT, VU meters, eye diagrams, constellation diagrams

---

## Architecture Overview

Chartexa uses a layered, command-based rendering pipeline. Your code interacts with a high-level API; the engine produces a renderer-neutral description of what to draw; a pluggable backend renders it.

```
User Code → ChartSurface → Axes + Series + Modifiers
          → RenderPipeline → RenderCommand[]
          → Renderer (DirectX 12 / Skia / WPF / Web)
```

Full architecture documentation: [System Overview](architecture/system-overview.md)

---

## Available Packages

### .NET (NuGet)

| Package | Description | Platform |
|---|---|---|
| `Chartexa.Core` | Core engine — primitives, math, render protocol, axis/series pipeline | Cross-platform |
| `Chartexa.Axes` | Axis system — NumericAxis, DateTimeAxis, CategoryAxis, LogarithmicAxis | Cross-platform |
| `Chartexa.Data` | Data series (XY, OHLC), resampling, downsampling | Cross-platform |
| `Chartexa.DataSources` | 40+ data source adapters (MQTT, OPC UA, Modbus, serial, audio, etc.) | Cross-platform |
| `Chartexa.Rendering` | Render command system, pipeline, coordinate calculators | Cross-platform |
| `Chartexa.Rendering.DirectX` | DirectX 12 GPU-accelerated renderer (Vortice, HLSL shaders, SDF text) | Windows |
| `Chartexa.Rendering.Skia` | SkiaSharp cross-platform renderer | Cross-platform |
| `Chartexa.Rendering.Wpf` | WPF native renderer + `ChartSurface` control | Windows (WPF) |
| `Chartexa.Rendering.Web` | JSON/WebAssembly command export for web frontends | Cross-platform |
| `Chartexa.Modifiers` | Interaction modifiers — zoom, pan, cursor, tooltip, rubber-band | Windows (WPF) |
| `Chartexa.Theming` | Token-based theme engine, DPI scaling, palette resolution | Cross-platform |
| `Chartexa.Layout` | Dashboard layout engine — grid/absolute positioning, nested containers | Cross-platform |
| `Chartexa.Python` | Python interop bridge (pythonnet) | Cross-platform |

### Python (PyPI)

| Package | Description |
|---|---|
| `chartexa` | Full Python wrapper — chart builder, series, axes, modifiers, theming, image export, Jupyter support |

---

## Documentation Structure

```
docs/
├── index.md                          ← You are here
│
├── getting-started/
│   ├── installation.md               ← NuGet, PyPI, prerequisites
│   ├── first-chart-csharp.md         ← Your first chart in C# / WPF
│   ├── first-chart-python.md         ← Your first chart in Python
│   └── choosing-a-renderer.md        ← DirectX vs. Skia vs. WPF vs. Web
│
├── chart-types/
│   ├── 2d/
│   │   ├── line-series.md            ← FastLineRenderableSeries
│   │   ├── scatter-series.md         ← XyScatterRenderableSeries
│   │   ├── column-series.md          ← FastColumnRenderableSeries
│   │   ├── mountain-series.md        ← MountainRenderableSeries (area)
│   │   ├── band-series.md            ← BandRenderableSeries
│   │   ├── bubble-series.md          ← BubbleRenderableSeries
│   │   ├── candlestick-series.md     ← FastCandlestickRenderableSeries
│   │   ├── heatmap-series.md         ← HeatmapSeries
│   │   ├── error-bar-series.md       ← ErrorBarRenderableSeries
│   │   ├── stacked-column.md         ← StackedColumnRenderableSeries
│   │   ├── stacked-bar.md            ← StackedBarRenderableSeries
│   │   ├── stacked-mountain.md       ← StackedMountainRenderableSeries
│   │   ├── donut-series.md           ← DonutSeries
│   │   ├── waterfall-series.md       ← WaterfallSeries
│   │   └── digital-signal.md         ← DigitalSignalSeries
│   │
│   ├── 3d/
│   │   └── surface-mesh.md           ← XYZSurfaceSeries (wireframe, solid, heatmap)
│   │
│   ├── financial/
│   │   ├── candlestick.md
│   │   └── ohlc-data.md
│   │
│   ├── gauges-and-widgets/
│   │   ├── angular-gauge.md          ← AngularGaugeSeries
│   │   ├── linear-gauge.md           ← LinearGaugeSeries
│   │   ├── radial-gauge.md           ← RadialGaugeSeries
│   │   ├── thermometer.md            ← ThermometerSeries
│   │   ├── vu-meter.md               ← VuMeterSeries
│   │   ├── battery-indicator.md      ← BatteryIndicatorWidget
│   │   ├── status-lamp.md            ← StatusLampWidget
│   │   ├── power-meter.md            ← PowerMeterWidget
│   │   ├── numeric-readout.md        ← NumericReadoutWidget
│   │   ├── trend-indicator.md        ← TrendIndicatorWidget
│   │   └── alarm-widget.md           ← AlarmWidget
│   │
│   └── instruments/
│       ├── spectrum-analyzer.md       ← SpectrumAnalyzerSeries
│       ├── oscilloscope.md            ← OscilloscopeSeries
│       ├── bode-plot.md               ← BodePlotSeries
│       ├── nyquist-plot.md            ← NyquistPlotSeries
│       ├── constellation-diagram.md   ← ConstellationDiagramSeries
│       ├── eye-diagram.md             ← EyeDiagramSeries
│       ├── octave-band.md             ← OctaveBandAnalyzerSeries
│       ├── correlation-meter.md       ← CorrelationMeterSeries
│       ├── radar-sweep.md             ← RadarSweepSeries
│       ├── lissajous.md               ← LissajousSeries
│       ├── gps-track.md               ← GpsTrackSeries
│       ├── compass.md                 ← CompassSeries
│       └── gforce-diagram.md          ← GForceDiagramSeries
│
├── axis-types/
│   ├── overview.md                    ← Axis system architecture
│   ├── numeric-axis.md               ← NumericAxis
│   ├── datetime-axis.md              ← DateTimeAxis
│   ├── category-axis.md              ← CategoryAxis
│   ├── logarithmic-axis.md           ← LogarithmicAxis
│   ├── tick-providers.md             ← Custom tick generation
│   ├── label-providers.md            ← Custom label formatting
│   ├── axis-ranging.md               ← AutoRange, VisibleRange, ZoomToFit
│   ├── axis-styling.md               ← Gridlines, bands, titles
│   └── multiple-axes.md              ← Secondary axes, vertical charts
│
├── data/
│   ├── data-series/
│   │   ├── xy-data-series.md         ← XyDataSeries
│   │   └── ohlc-data-series.md       ← OhlcDataSeries
│   ├── data-sources/
│   │   ├── overview.md               ← IDataSource, DataSourceManager
│   │   ├── financial/
│   │   │   ├── market-data.md        ← MarketDataSource
│   │   │   ├── technical-indicators.md ← TechnicalIndicatorsDataSource
│   │   │   └── portfolio-monitor.md  ← PortfolioMonitorDataSource
│   │   ├── network/
│   │   │   ├── mqtt.md               ← MqttDataSource
│   │   │   ├── opc-ua.md             ← OpcUaDataSource
│   │   │   ├── modbus.md             ← ModbusDataSource
│   │   │   ├── websocket.md          ← WebSocketDataSource
│   │   │   ├── grpc-streaming.md     ← GrpcStreamingDataSource
│   │   │   ├── rest-polling.md       ← RestPollingDataSource
│   │   │   └── timeseries-db.md      ← TimeSeriesDbDataSource (InfluxDB, TimescaleDB)
│   │   ├── hardware/
│   │   │   ├── serial.md             ← SerialDataSource
│   │   │   ├── gpio.md               ← GpioAnalogDataSource, GpioEnvironmentalDataSource
│   │   │   ├── scpi.md               ← ScpiDataSource
│   │   │   ├── usb-hid.md            ← UsbHidDataSource
│   │   │   └── thermal-camera.md     ← ThermalCameraDataSource
│   │   ├── audio/
│   │   │   ├── audio-capture.md      ← AudioCaptureDataSource
│   │   │   ├── fft-processor.md      ← FftProcessor
│   │   │   ├── midi.md               ← MidiDataSource
│   │   │   └── acoustic.md           ← AcousticMeasurement
│   │   ├── automotive/
│   │   │   ├── can-bus.md            ← CanBusDataSource
│   │   │   ├── obd2.md              ← Obd2DataSource
│   │   │   ├── tpms.md              ← TpmsDataSource
│   │   │   └── ev-battery.md        ← EvBatteryDataSource
│   │   ├── scientific/
│   │   │   ├── spectrometer.md       ← SpectrometerDataSource
│   │   │   ├── seismometer.md        ← SeismometerDataSource
│   │   │   ├── sdr.md               ← SdrDataSource
│   │   │   └── potentiostat.md       ← PotentiostatDataSource
│   │   ├── system/
│   │   │   ├── system-monitor.md     ← SystemMonitorDataSource
│   │   │   ├── process-monitor.md    ← ProcessMonitorDataSource
│   │   │   └── docker.md            ← DockerDataSource
│   │   ├── simulation/
│   │   │   ├── flight-sim.md         ← FlightSimDataSource
│   │   │   ├── racing-sim.md         ← RacingSimDataSource
│   │   │   └── game-engine.md        ← GameEngineDataSource
│   │   └── input-devices/
│   │       ├── gamepad.md            ← GamepadDataSource
│   │       └── gps-nmea.md           ← GpsNmeaDataSource
│   ├── recording-replay.md           ← DataRecordingReplay
│   └── derived-series.md             ← DerivedComputedSeries
│
├── interaction/
│   ├── overview.md                    ← ChartModifier API
│   ├── zoom-pan-modifier.md          ← ZoomPanModifier
│   ├── rubber-band-zoom.md           ← RubberBandZoomModifier
│   ├── cursor-modifier.md            ← CursorModifier (crosshair)
│   ├── tooltip-modifier.md           ← TooltipModifier
│   ├── modifier-group.md             ← ModifierGroup (composite)
│   ├── hit-testing.md                ← HitTestProvider, HitTestResult
│   └── custom-modifiers.md           ← Extending ChartModifierBase
│
├── rendering/
│   ├── overview.md                    ← Render command pipeline
│   ├── directx12/
│   │   ├── setup.md                  ← DirectX12RenderContext setup
│   │   ├── gpu-acceleration.md       ← Swap chain, batching, SIMD
│   │   ├── sdf-text.md              ← SDF font atlas text rendering
│   │   └── profiling.md             ← GpuTimestampQuery, FrameStatistics
│   ├── skia/
│   │   ├── setup.md                  ← SkiaRenderContext setup
│   │   └── cross-platform.md        ← Platform support and configuration
│   ├── wpf/
│   │   ├── setup.md                  ← WpfRenderContext + ChartSurface control
│   │   ├── data-binding.md           ← Dependency properties, MVVM
│   │   └── controls.md              ← ChartSurface properties and usage
│   ├── web/
│   │   └── json-export.md            ← Web/JSON command export
│   └── render-commands.md            ← RenderCommand types, RenderCommandList, pooling
│
├── theming/
│   ├── overview.md                    ← Theme system architecture
│   ├── built-in-themes.md            ← Pre-built theme presets
│   ├── custom-themes.md              ← ChartTheme, ThemeColors, ThemeTypography, ThemeSpacing, ThemeStroke
│   ├── theme-engine.md               ← ThemeEngine — token resolution, per-widget overrides
│   └── dpi-scaling.md                ← DPI-aware rendering
│
├── layout/
│   ├── overview.md                    ← Dashboard layout system
│   ├── grid-layout.md                ← LayoutType.Grid — row/column spanning
│   ├── absolute-layout.md            ← LayoutType.Absolute — pixel positioning
│   ├── nested-layouts.md             ← LayoutContainer nesting
│   └── dashboard-document.md         ← DashboardLayoutDocument, data binding, serialization
│
├── platforms/
│   ├── wpf/
│   │   ├── getting-started.md        ← WPF project setup (net10.0-windows)
│   │   ├── chart-surface.md          ← ChartSurface control reference
│   │   └── mvvm.md                   ← MVVM patterns and data binding
│   ├── python/
│   │   ├── getting-started.md        ← pip install chartexa, .NET runtime
│   │   ├── chart-builder.md          ← Fluent Chart API (.line, .scatter, .candlestick, etc.)
│   │   ├── image-export.md           ← .save(), .save_jpeg(), .to_bytes()
│   │   ├── jupyter.md               ← Jupyter Notebook integration
│   │   └── api-reference.md         ← Python module reference
│   └── web/
│       └── json-integration.md       ← Using Chartexa.Rendering.Web for web frontends
│
├── performance/
│   ├── optimization.md               ← General optimization strategies
│   ├── gpu-acceleration.md           ← DirectX 12 pipeline, SIMD transforms
│   ├── memory.md                     ← Object pooling, render command reuse
│   ├── large-datasets.md            ← Resampling, downsampling, streaming
│   └── benchmarks.md                ← BenchmarkDotNet results and methodology
│
├── examples/
│   ├── index.md                       ← Examples overview
│   ├── csharp/
│   │   ├── real-time-line-chart.md
│   │   ├── financial-dashboard.md
│   │   ├── multi-series-chart.md
│   │   ├── 3d-surface-plot.md
│   │   ├── heatmap-visualization.md
│   │   ├── instrument-dashboard.md
│   │   └── iot-sensor-dashboard.md
│   └── python/
│       ├── quick-line-chart.md
│       ├── candlestick-chart.md
│       ├── scatter-with-tooltips.md
│       ├── heatmap.md
│       └── jupyter-notebook.md
│
├── api-reference/
│   ├── index.md                       ← API reference overview
│   ├── csharp/
│   │   ├── chartexa-core.md
│   │   ├── chartexa-axes.md
│   │   ├── chartexa-data.md
│   │   ├── chartexa-datasources.md
│   │   ├── chartexa-rendering.md
│   │   ├── chartexa-modifiers.md
│   │   ├── chartexa-theming.md
│   │   └── chartexa-layout.md
│   └── python/
│       └── chartexa-python.md
│
├── architecture/
│   ├── system-overview.md             ← Layered architecture, component diagram
│   ├── rendering-pipeline.md          ← RenderCommand flow, backends
│   └── coordinate-system.md           ← Data ↔ screen coordinate mapping
│
├── migration/
│   └── from-scichart.md              ← Migration guide from SciChart
│
└── faq.md
```

---

## Quick Start

### C# / WPF

**1. Install NuGet packages**

```bash
dotnet add package Chartexa.Core
dotnet add package Chartexa.Data
dotnet add package Chartexa.Rendering.Wpf
dotnet add package Chartexa.Modifiers
```

**2. Add the ChartSurface control**

```xml
<Window xmlns:chartexa="clr-namespace:Chartexa.Rendering.Wpf.Controls;assembly=Chartexa.Rendering.Wpf">
    <chartexa:ChartSurface x:Name="Chart" />
</Window>
```

**3. Create your first chart**

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;

// Add axes
Chart.XAxes.Add(new NumericAxis { Id = "X" });
Chart.YAxes.Add(new NumericAxis { Id = "Y" });

// Add data
var series = new XyDataSeries();
series.Append(new[] { 0.0, 1.0, 2.0, 3.0, 4.0 }, new[] { 0.0, 3.5, 7.2, 4.8, 9.1 });

// Add a line series
Chart.Series.Add(new FastLineRenderableSeries { DataSeries = series });

// Add zoom/pan interaction
Chart.RootModifier = new ModifierGroup(
    new ZoomPanModifier(),
    new CursorModifier()
);

Chart.InvalidateChart();
```

Full tutorial: [First Chart in C#](getting-started/first-chart-csharp.md)

---

### Python

**1. Install**

```bash
pip install chartexa
```

> Requires the [.NET 10 Runtime](https://dotnet.microsoft.com/download).

**2. Create a chart**

```python
from chartexa import Chart

chart = (
    Chart(width=800, height=400)
    .line([0, 1, 2, 3, 4], [0, 3.5, 7.2, 4.8, 9.1], stroke="#4682B4", thickness=2)
    .background("#1C1C1E")
    .save("my_chart.png")
)
```

**3. Financial chart**

```python
from chartexa import Chart

chart = (
    Chart(width=1000, height=500)
    .candlestick(dates, opens, highs, lows, closes)
    .save("candlestick.png")
)
```

Full tutorial: [First Chart in Python](getting-started/first-chart-python.md)

---

## Chart Types at a Glance

### 2D Series

| Series | Class | Description |
|---|---|---|
| Line | `FastLineRenderableSeries` | High-performance line chart with optional spline interpolation |
| Scatter | `XyScatterRenderableSeries` | XY scatter plot with configurable markers |
| Column | `FastColumnRenderableSeries` | Vertical bar/column chart |
| Mountain | `MountainRenderableSeries` | Filled area chart |
| Band | `BandRenderableSeries` | Upper/lower bound ribbon |
| Bubble | `BubbleRenderableSeries` | Bubble chart with variable radius |
| Candlestick | `FastCandlestickRenderableSeries` | OHLC candlestick for financial data |
| Heatmap | `HeatmapSeries` | 2D heatmap with colormap palette |
| Error Bars | `ErrorBarRenderableSeries` | Error bar visualization |
| Stacked Column | `StackedColumnRenderableSeries` | Multi-layer stacked columns |
| Stacked Mountain | `StackedMountainRenderableSeries` | Stacked area chart |
| Donut | `DonutSeries` | Pie/donut chart |
| Waterfall | `WaterfallSeries` | Time-frequency waterfall display |
| Digital Signal | `DigitalSignalSeries` | Step/digital signal plot |

### 3D Series

| Series | Class | Description |
|---|---|---|
| Surface Mesh | `XYZSurfaceSeries` | 3D surface with wireframe, solid, and heatmap render modes |

### Gauges & Widgets

| Widget | Class | Description |
|---|---|---|
| Angular Gauge | `AngularGaugeSeries` | Circular gauge indicator |
| Linear Gauge | `LinearGaugeSeries` | Linear gauge bar |
| Radial Gauge | `RadialGaugeSeries` | Radial gauge display |
| Thermometer | `ThermometerSeries` | Thermometer widget |
| VU Meter | `VuMeterSeries` | Audio VU meter |
| Battery | `BatteryIndicatorWidget` | Battery level indicator |
| Status Lamp | `StatusLampWidget` | LED/lamp indicator |
| Power Meter | `PowerMeterWidget` | Power meter display |
| Numeric Readout | `NumericReadoutWidget` | Numeric value display |
| Trend Indicator | `TrendIndicatorWidget` | Directional trend arrow |
| Alarm | `AlarmWidget` | Alarm/alert indicator |

### Scientific Instruments

| Instrument | Class | Description |
|---|---|---|
| Spectrum Analyzer | `SpectrumAnalyzerSeries` | Frequency spectrum display |
| Oscilloscope | `OscilloscopeSeries` | Waveform oscilloscope |
| Bode Plot | `BodePlotSeries` | Bode magnitude diagram |
| Nyquist Plot | `NyquistPlotSeries` | Nyquist stability plot |
| Constellation | `ConstellationDiagramSeries` | IQ constellation (digital comms) |
| Eye Diagram | `EyeDiagramSeries` | Signal integrity eye diagram |
| Radar Sweep | `RadarSweepSeries` | Polar radar sweep |
| Lissajous | `LissajousSeries` | Lissajous curve display |
| GPS Track | `GpsTrackSeries` | GPS trajectory visualization |
| Compass | `CompassSeries` | Heading compass display |

---

## Rendering Backends

Chartexa supports multiple rendering backends. Choose the one that fits your application requirements.

| Backend | Package | Platform | Use Case |
|---|---|---|---|
| **DirectX 12** | `Chartexa.Rendering.DirectX` | Windows | Maximum GPU performance — double-buffered swap chain, SIMD transforms, SDF text, batched draw calls |
| **SkiaSharp** | `Chartexa.Rendering.Skia` | Cross-platform | Flexible software/GPU hybrid — ideal for server-side rendering, image export, and cross-platform apps |
| **WPF** | `Chartexa.Rendering.Wpf` | Windows (WPF) | Native WPF integration — `DrawingContext` rendering with dependency property support and MVVM |
| **Web** | `Chartexa.Rendering.Web` | Cross-platform | JSON command export — feed render commands to a JavaScript/WebAssembly frontend |

See [Choosing a Renderer](getting-started/choosing-a-renderer.md) for a detailed comparison.

---

## Data Sources

Chartexa includes 40+ built-in data source adapters organized by domain. Each data source implements the `IDataSource` interface and can be managed by the `DataSourceManager`.

| Domain | Sources | Examples |
|---|---|---|
| **Financial** | Market data, technical indicators, portfolio | `MarketDataSource`, `TechnicalIndicatorsDataSource` |
| **Network** | MQTT, OPC UA, Modbus, WebSocket, gRPC, REST, time-series DB | `MqttDataSource`, `OpcUaDataSource`, `ModbusDataSource` |
| **Hardware** | Serial, GPIO, SCPI, USB HID, thermal camera | `SerialDataSource`, `ScpiDataSource` |
| **Audio** | Audio capture, FFT, MIDI, acoustic measurement | `AudioCaptureDataSource`, `FftProcessor` |
| **Automotive** | CAN bus, OBD-II, TPMS, EV battery | `CanBusDataSource`, `Obd2DataSource` |
| **Scientific** | Spectrometer, seismometer, SDR, potentiostat | `SpectrometerDataSource`, `SdrDataSource` |
| **System** | CPU/memory/disk, process metrics, Docker | `SystemMonitorDataSource`, `DockerDataSource` |
| **Simulation** | Flight sim, racing sim, game engine | `FlightSimDataSource`, `RacingSimDataSource` |

See [Data Sources Overview](data/data-sources/overview.md) for the full list and configuration guides.

---

## Interaction System

Chart interaction is handled through the **Modifier API** — composable, pluggable behaviors that respond to mouse and touch input.

| Modifier | Class | Description |
|---|---|---|
| Zoom & Pan | `ZoomPanModifier` | Click-drag to pan, scroll to zoom |
| Rubber Band Zoom | `RubberBandZoomModifier` | Drag a rectangle to zoom into a region |
| Crosshair | `CursorModifier` | Crosshair cursor with real-time coordinate display |
| Tooltip | `TooltipModifier` | Tooltip on hover showing data point values |
| Group | `ModifierGroup` | Combine multiple modifiers on one chart |

```csharp
Chart.RootModifier = new ModifierGroup(
    new ZoomPanModifier(),
    new RubberBandZoomModifier(),
    new CursorModifier(),
    new TooltipModifier()
);
```

See [Interaction Overview](interaction/overview.md) for full configuration and custom modifier development.

---

## Theming

Chartexa uses a **token-based theming system** with JSON-serializable theme definitions.

```csharp
var theme = new ChartTheme
{
    Colors = new ThemeColors
    {
        Background = "#1C1C1E",
        Foreground = "#FFFFFF",
        Accent = "#4A90D9",
        Grid = "#2C2C2E"
    },
    Typography = new ThemeTypography
    {
        FontFamily = "Segoe UI",
        BaseSize = 12
    }
};
```

Themes support **per-widget overrides** — apply a global theme and selectively customize individual widgets and series.

See [Theming Overview](theming/overview.md) for complete configuration reference.

---

## Dashboard Layouts

The layout engine lets you compose multi-chart dashboards with grid or absolute positioning.

```csharp
var dashboard = new DashboardLayoutDocument
{
    Root = new LayoutContainer
    {
        Type = LayoutType.Grid,
        Columns = 3,
        Rows = 2,
        Children = { /* LayoutItem definitions */ }
    }
};
```

See [Layout Overview](layout/overview.md) for grid spans, nested containers, and data source binding.

---

## Performance

Chartexa is engineered for performance at every layer:

- **DirectX 12** — double-buffered swap chain (3 back buffers), per-frame command allocators, root constants (no descriptor heap overhead), draw batch accumulation
- **SIMD** — vectorized coordinate transforms for data → screen mapping
- **Object pooling** — `RenderCommandPool` and `RenderCommandList` reuse to minimize GC pressure
- **Resampling** — built-in data downsampling for large datasets
- **GPU profiling** — `GpuTimestampQuery` and `FrameStatistics` for per-frame performance measurement

See [Performance Guide](performance/optimization.md) and [Benchmarks](performance/benchmarks.md) for tuning strategies and results.

---

## Building from Source

### Prerequisites

- [.NET 10 SDK](https://dotnet.microsoft.com/download)
- Windows (required for WPF and DirectX renderer development)

### Commands

```bash
# Build all projects
dotnet build

# Run tests
dotnet test

# Run WPF demo
dotnet run --project examples/WpfDemo

# Run benchmarks
dotnet run --project benchmarks/Chartexa.Benchmarks -c Release
```

---

## Documentation Standards

### Principles

- **User-first** — focus on usage patterns and practical scenarios, not internal implementation
- **Example-driven** — every feature is demonstrated with working code in both C# and Python
- **Performance-aware** — optimization strategies and trade-offs are documented alongside features
- **Consistent** — uniform structure, terminology, and code style across all pages

### Writing Style

- Technical, concise, and precise
- No marketing language
- Clear separation of concepts, configuration, and code examples
- Every page follows: **overview → configuration → code example → notes/tips**

### Code Examples

Every documented feature includes:

- **Minimal example** — shortest working code
- **Real-world scenario** — practical, production-relevant usage
- **C# + Python** — side-by-side where the feature is available in both

---

## MkDocs Configuration

This documentation site is built with [MkDocs](https://www.mkdocs.org/) and [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/).

Key features:

- Hierarchical section navigation
- Full-text search
- Dark / light mode toggle
- Syntax-highlighted code blocks with copy button
- Tabbed code examples (C# / Python)
- Admonitions (notes, warnings, tips)
- Version selector (future)

---

## Contribution Policy

Contributions are welcome for:

- Examples and tutorials
- Documentation clarity and corrections
- Translations

Restrictions:

- Do not expose internal engine implementation details
- Do not include reverse-engineered or decompiled content

---

## License

Chartexa documentation is licensed under [MIT](https://opensource.org/licenses/MIT).

The Chartexa engine is proprietary — see the main repository for licensing terms.
