# Chartexa Documentation

<div class="hero" markdown>

# Chartexa

**High-Performance, Multi-Backend Charting Engine for .NET and Python**

A modular, renderer-agnostic visualization platform built in C# / .NET 10 â€” designed for financial, scientific, real-time, and industrial applications requiring extreme rendering speed and flexibility.

[Get Started](getting-started/installation.md){ .md-button .md-button--primary }
[View Examples](examples/index.md){ .md-button }
[API Reference](api-reference/index.md){ .md-button }

</div>

---

## What is Chartexa?

Chartexa is a **comprehensive data visualization engine** â€” not a wrapper around an existing renderer, but a ground-up charting platform with a clean separation between data, logic, rendering, and interaction.

It ships as a family of NuGet packages (C#) and a PyPI package (Python), giving you full control over how charts are composed, styled, and rendered.

### Key Capabilities

| Capability | Details |
|---|---|
| **Rendering Backends** | DirectX 12 (GPU-accelerated), SkiaSharp (cross-platform), WPF native, Web/JSON export |
| **Chart Types** | 50+ series types â€” line, scatter, candlestick, heatmap, 3D surface, gauges, instruments, and more |
| **Data Sources** | 40+ built-in data source integrations â€” MQTT, OPC UA, Modbus, serial, audio, GPS, CAN bus, and more |
| **Interaction** | Zoom, pan, rubber-band zoom, crosshair cursor, tooltips, hit testing |
| **Theming** | Token-based theme engine with JSON-serializable definitions and per-widget overrides |
| **Layout** | Dashboard layout engine with grid and absolute positioning, nested containers |
| **Python** | Full Python wrapper with fluent API, Jupyter Notebook support, and image export |
| **Performance** | SIMD coordinate transforms, GPU batching, object pooling, double-buffered swap chain |

### Who is Chartexa for?

- **Financial systems** â€” candlestick, OHLC, real-time streaming, technical indicators
- **Scientific computing** â€” spectrum analyzers, Bode/Nyquist plots, oscilloscopes, heatmaps
- **Industrial & IoT** â€” OPC UA, Modbus, CAN bus, sensor dashboards, PID controllers
- **Real-time analytics** â€” high-frequency data updates, large dataset visualization
- **Audio & Signal Processing** â€” FFT, VU meters, eye diagrams, constellation diagrams

---

## Architecture Overview

Chartexa uses a layered, command-based rendering pipeline. Your code interacts with a high-level API; the engine produces a renderer-neutral description of what to draw; a pluggable backend renders it.

```
User Code â†’ ChartSurface â†’ Axes + Series + Modifiers
          â†’ RenderPipeline â†’ RenderCommand[]
          â†’ Renderer (DirectX 12 / Skia / WPF / Web)
```

Full architecture documentation: [System Overview](architecture/system-overview.md)

---

## Available Packages

### .NET (NuGet)

| Package | Description | Platform |
|---|---|---|
| `Chartexa.Core` | Core engine â€” primitives, math, render protocol, axis/series pipeline | Cross-platform |
| `Chartexa.Axes` | Axis system â€” NumericAxis, DateTimeAxis, CategoryAxis, LogarithmicAxis | Cross-platform |
| `Chartexa.Data` | Data series (XY, OHLC), resampling, downsampling | Cross-platform |
| `Chartexa.DataSources` | 40+ data source adapters (MQTT, OPC UA, Modbus, serial, audio, etc.) | Cross-platform |
| `Chartexa.Rendering` | Render command system, pipeline, coordinate calculators | Cross-platform |
| `Chartexa.Rendering.DirectX` | DirectX 12 GPU-accelerated renderer (Vortice, HLSL shaders, SDF text) | Windows |
| `Chartexa.Rendering.Skia` | SkiaSharp cross-platform renderer | Cross-platform |
| `Chartexa.Rendering.Wpf` | WPF native renderer + `ChartSurface` control | Windows (WPF) |
| `Chartexa.Rendering.Web` | JSON/WebAssembly command export for web frontends | Cross-platform |
| `Chartexa.Modifiers` | Interaction modifiers â€” zoom, pan, cursor, tooltip, rubber-band | Windows (WPF) |
| `Chartexa.Theming` | Token-based theme engine, DPI scaling, palette resolution | Cross-platform |
| `Chartexa.Layout` | Dashboard layout engine â€” grid/absolute positioning, nested containers | Cross-platform |
| `Chartexa.Python` | Python interop bridge (pythonnet) | Cross-platform |

### Python (PyPI)

| Package | Description |
|---|---|
| `chartexa` | Full Python wrapper â€” chart builder, series, axes, modifiers, theming, image export, Jupyter support |

---

## Documentation Structure

```
docs/
â”œâ”€â”€ index.md                          â† You are here
â”‚
â”œâ”€â”€ getting-started/
â”‚   â”œâ”€â”€ installation.md               â† NuGet, PyPI, prerequisites
â”‚   â”œâ”€â”€ first-chart-csharp.md         â† Your first chart in C# / WPF
â”‚   â”œâ”€â”€ first-chart-python.md         â† Your first chart in Python
â”‚   â””â”€â”€ choosing-a-renderer.md        â† DirectX vs. Skia vs. WPF vs. Web
â”‚
â”œâ”€â”€ chart-types/
â”‚   â”œâ”€â”€ 2d/
â”‚   â”‚   â”œâ”€â”€ line-series.md            â† FastLineRenderableSeries
â”‚   â”‚   â”œâ”€â”€ scatter-series.md         â† XyScatterRenderableSeries
â”‚   â”‚   â”œâ”€â”€ column-series.md          â† FastColumnRenderableSeries
â”‚   â”‚   â”œâ”€â”€ mountain-series.md        â† MountainRenderableSeries (area)
â”‚   â”‚   â”œâ”€â”€ band-series.md            â† BandRenderableSeries
â”‚   â”‚   â”œâ”€â”€ bubble-series.md          â† BubbleRenderableSeries
â”‚   â”‚   â”œâ”€â”€ candlestick-series.md     â† FastCandlestickRenderableSeries
â”‚   â”‚   â”œâ”€â”€ heatmap-series.md         â† HeatmapSeries
â”‚   â”‚   â”œâ”€â”€ error-bar-series.md       â† ErrorBarRenderableSeries
â”‚   â”‚   â”œâ”€â”€ stacked-column.md         â† StackedColumnRenderableSeries
â”‚   â”‚   â”œâ”€â”€ stacked-bar.md            â† StackedBarRenderableSeries
â”‚   â”‚   â”œâ”€â”€ stacked-mountain.md       â† StackedMountainRenderableSeries
â”‚   â”‚   â”œâ”€â”€ donut-series.md           â† DonutSeries
â”‚   â”‚   â”œâ”€â”€ waterfall-series.md       â† WaterfallSeries
â”‚   â”‚   â””â”€â”€ digital-signal.md         â† DigitalSignalSeries
â”‚   â”‚
â”‚   â”œâ”€â”€ 3d/
â”‚   â”‚   â””â”€â”€ surface-mesh.md           â† XYZSurfaceSeries (wireframe, solid, heatmap)
â”‚   â”‚
â”‚   â”œâ”€â”€ financial/
â”‚   â”‚   â”œâ”€â”€ candlestick.md
â”‚   â”‚   â””â”€â”€ ohlc-data.md
â”‚   â”‚
â”‚   â”œâ”€â”€ gauges-and-widgets/
â”‚   â”‚   â”œâ”€â”€ angular-gauge.md          â† AngularGaugeSeries
â”‚   â”‚   â”œâ”€â”€ linear-gauge.md           â† LinearGaugeSeries
â”‚   â”‚   â”œâ”€â”€ radial-gauge.md           â† RadialGaugeSeries
â”‚   â”‚   â”œâ”€â”€ thermometer.md            â† ThermometerSeries
â”‚   â”‚   â”œâ”€â”€ vu-meter.md               â† VuMeterSeries
â”‚   â”‚   â”œâ”€â”€ battery-indicator.md      â† BatteryIndicatorWidget
â”‚   â”‚   â”œâ”€â”€ status-lamp.md            â† StatusLampWidget
â”‚   â”‚   â”œâ”€â”€ power-meter.md            â† PowerMeterWidget
â”‚   â”‚   â”œâ”€â”€ numeric-readout.md        â† NumericReadoutWidget
â”‚   â”‚   â”œâ”€â”€ trend-indicator.md        â† TrendIndicatorWidget
â”‚   â”‚   â””â”€â”€ alarm-widget.md           â† AlarmWidget
â”‚   â”‚
â”‚   â””â”€â”€ instruments/
â”‚       â”œâ”€â”€ spectrum-analyzer.md       â† SpectrumAnalyzerSeries
â”‚       â”œâ”€â”€ oscilloscope.md            â† OscilloscopeSeries
â”‚       â”œâ”€â”€ bode-plot.md               â† BodePlotSeries
â”‚       â”œâ”€â”€ nyquist-plot.md            â† NyquistPlotSeries
â”‚       â”œâ”€â”€ constellation-diagram.md   â† ConstellationDiagramSeries
â”‚       â”œâ”€â”€ eye-diagram.md             â† EyeDiagramSeries
â”‚       â”œâ”€â”€ octave-band.md             â† OctaveBandAnalyzerSeries
â”‚       â”œâ”€â”€ correlation-meter.md       â† CorrelationMeterSeries
â”‚       â”œâ”€â”€ radar-sweep.md             â† RadarSweepSeries
â”‚       â”œâ”€â”€ lissajous.md               â† LissajousSeries
â”‚       â”œâ”€â”€ gps-track.md               â† GpsTrackSeries
â”‚       â”œâ”€â”€ compass.md                 â† CompassSeries
â”‚       â””â”€â”€ gforce-diagram.md          â† GForceDiagramSeries
â”‚
â”œâ”€â”€ axis-types/
â”‚   â”œâ”€â”€ overview.md                    â† Axis system architecture
â”‚   â”œâ”€â”€ numeric-axis.md               â† NumericAxis
â”‚   â”œâ”€â”€ datetime-axis.md              â† DateTimeAxis
â”‚   â”œâ”€â”€ category-axis.md              â† CategoryAxis
â”‚   â”œâ”€â”€ logarithmic-axis.md           â† LogarithmicAxis
â”‚   â”œâ”€â”€ tick-providers.md             â† Custom tick generation
â”‚   â”œâ”€â”€ label-providers.md            â† Custom label formatting
â”‚   â”œâ”€â”€ axis-ranging.md               â† AutoRange, VisibleRange, ZoomToFit
â”‚   â”œâ”€â”€ axis-styling.md               â† Gridlines, bands, titles
â”‚   â””â”€â”€ multiple-axes.md              â† Secondary axes, vertical charts
â”‚
â”œâ”€â”€ data/
â”‚   â”œâ”€â”€ data-series/
â”‚   â”‚   â”œâ”€â”€ xy-data-series.md         â† XyDataSeries
â”‚   â”‚   â””â”€â”€ ohlc-data-series.md       â† OhlcDataSeries
â”‚   â”œâ”€â”€ data-sources/
â”‚   â”‚   â”œâ”€â”€ overview.md               â† IDataSource, DataSourceManager
â”‚   â”‚   â”œâ”€â”€ financial/
â”‚   â”‚   â”‚   â”œâ”€â”€ market-data.md        â† MarketDataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ technical-indicators.md â† TechnicalIndicatorsDataSource
â”‚   â”‚   â”‚   â””â”€â”€ portfolio-monitor.md  â† PortfolioMonitorDataSource
â”‚   â”‚   â”œâ”€â”€ network/
â”‚   â”‚   â”‚   â”œâ”€â”€ mqtt.md               â† MqttDataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ opc-ua.md             â† OpcUaDataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ modbus.md             â† ModbusDataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ websocket.md          â† WebSocketDataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ grpc-streaming.md     â† GrpcStreamingDataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ rest-polling.md       â† RestPollingDataSource
â”‚   â”‚   â”‚   â””â”€â”€ timeseries-db.md      â† TimeSeriesDbDataSource (InfluxDB, TimescaleDB)
â”‚   â”‚   â”œâ”€â”€ hardware/
â”‚   â”‚   â”‚   â”œâ”€â”€ serial.md             â† SerialDataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ gpio.md               â† GpioAnalogDataSource, GpioEnvironmentalDataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ scpi.md               â† ScpiDataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ usb-hid.md            â† UsbHidDataSource
â”‚   â”‚   â”‚   â””â”€â”€ thermal-camera.md     â† ThermalCameraDataSource
â”‚   â”‚   â”œâ”€â”€ audio/
â”‚   â”‚   â”‚   â”œâ”€â”€ audio-capture.md      â† AudioCaptureDataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ fft-processor.md      â† FftProcessor
â”‚   â”‚   â”‚   â”œâ”€â”€ midi.md               â† MidiDataSource
â”‚   â”‚   â”‚   â””â”€â”€ acoustic.md           â† AcousticMeasurement
â”‚   â”‚   â”œâ”€â”€ automotive/
â”‚   â”‚   â”‚   â”œâ”€â”€ can-bus.md            â† CanBusDataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ obd2.md              â† Obd2DataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ tpms.md              â† TpmsDataSource
â”‚   â”‚   â”‚   â””â”€â”€ ev-battery.md        â† EvBatteryDataSource
â”‚   â”‚   â”œâ”€â”€ scientific/
â”‚   â”‚   â”‚   â”œâ”€â”€ spectrometer.md       â† SpectrometerDataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ seismometer.md        â† SeismometerDataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ sdr.md               â† SdrDataSource
â”‚   â”‚   â”‚   â””â”€â”€ potentiostat.md       â† PotentiostatDataSource
â”‚   â”‚   â”œâ”€â”€ system/
â”‚   â”‚   â”‚   â”œâ”€â”€ system-monitor.md     â† SystemMonitorDataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ process-monitor.md    â† ProcessMonitorDataSource
â”‚   â”‚   â”‚   â””â”€â”€ docker.md            â† DockerDataSource
â”‚   â”‚   â”œâ”€â”€ simulation/
â”‚   â”‚   â”‚   â”œâ”€â”€ flight-sim.md         â† FlightSimDataSource
â”‚   â”‚   â”‚   â”œâ”€â”€ racing-sim.md         â† RacingSimDataSource
â”‚   â”‚   â”‚   â””â”€â”€ game-engine.md        â† GameEngineDataSource
â”‚   â”‚   â””â”€â”€ input-devices/
â”‚   â”‚       â”œâ”€â”€ gamepad.md            â† GamepadDataSource
â”‚   â”‚       â””â”€â”€ gps-nmea.md           â† GpsNmeaDataSource
â”‚   â”œâ”€â”€ recording-replay.md           â† DataRecordingReplay
â”‚   â””â”€â”€ derived-series.md             â† DerivedComputedSeries
â”‚
â”œâ”€â”€ interaction/
â”‚   â”œâ”€â”€ overview.md                    â† ChartModifier API
â”‚   â”œâ”€â”€ zoom-pan-modifier.md          â† ZoomPanModifier
â”‚   â”œâ”€â”€ rubber-band-zoom.md           â† RubberBandZoomModifier
â”‚   â”œâ”€â”€ cursor-modifier.md            â† CursorModifier (crosshair)
â”‚   â”œâ”€â”€ tooltip-modifier.md           â† TooltipModifier
â”‚   â”œâ”€â”€ modifier-group.md             â† ModifierGroup (composite)
â”‚   â”œâ”€â”€ hit-testing.md                â† HitTestProvider, HitTestResult
â”‚   â””â”€â”€ custom-modifiers.md           â† Extending ChartModifierBase
â”‚
â”œâ”€â”€ rendering/
â”‚   â”œâ”€â”€ overview.md                    â† Render command pipeline
â”‚   â”œâ”€â”€ directx12/
â”‚   â”‚   â”œâ”€â”€ setup.md                  â† DirectX12RenderContext setup
â”‚   â”‚   â”œâ”€â”€ gpu-acceleration.md       â† Swap chain, batching, SIMD
â”‚   â”‚   â”œâ”€â”€ sdf-text.md              â† SDF font atlas text rendering
â”‚   â”‚   â””â”€â”€ profiling.md             â† GpuTimestampQuery, FrameStatistics
â”‚   â”œâ”€â”€ skia/
â”‚   â”‚   â”œâ”€â”€ setup.md                  â† SkiaRenderContext setup
â”‚   â”‚   â””â”€â”€ cross-platform.md        â† Platform support and configuration
â”‚   â”œâ”€â”€ wpf/
â”‚   â”‚   â”œâ”€â”€ setup.md                  â† WpfRenderContext + ChartSurface control
â”‚   â”‚   â”œâ”€â”€ data-binding.md           â† Dependency properties, MVVM
â”‚   â”‚   â””â”€â”€ controls.md              â† ChartSurface properties and usage
â”‚   â”œâ”€â”€ web/
â”‚   â”‚   â””â”€â”€ json-export.md            â† Web/JSON command export
â”‚   â””â”€â”€ render-commands.md            â† RenderCommand types, RenderCommandList, pooling
â”‚
â”œâ”€â”€ theming/
â”‚   â”œâ”€â”€ overview.md                    â† Theme system architecture
â”‚   â”œâ”€â”€ built-in-themes.md            â† Pre-built theme presets
â”‚   â”œâ”€â”€ custom-themes.md              â† ChartTheme, ThemeColors, ThemeTypography, ThemeSpacing, ThemeStroke
â”‚   â”œâ”€â”€ theme-engine.md               â† ThemeEngine â€” token resolution, per-widget overrides
â”‚   â””â”€â”€ dpi-scaling.md                â† DPI-aware rendering
â”‚
â”œâ”€â”€ layout/
â”‚   â”œâ”€â”€ overview.md                    â† Dashboard layout system
â”‚   â”œâ”€â”€ grid-layout.md                â† LayoutType.Grid â€” row/column spanning
â”‚   â”œâ”€â”€ absolute-layout.md            â† LayoutType.Absolute â€” pixel positioning
â”‚   â”œâ”€â”€ nested-layouts.md             â† LayoutContainer nesting
â”‚   â””â”€â”€ dashboard-document.md         â† DashboardLayoutDocument, data binding, serialization
â”‚
â”œâ”€â”€ platforms/
â”‚   â”œâ”€â”€ wpf/
â”‚   â”‚   â”œâ”€â”€ getting-started.md        â† WPF project setup (net10.0-windows)
â”‚   â”‚   â”œâ”€â”€ chart-surface.md          â† ChartSurface control reference
â”‚   â”‚   â””â”€â”€ mvvm.md                   â† MVVM patterns and data binding
â”‚   â”œâ”€â”€ python/
â”‚   â”‚   â”œâ”€â”€ getting-started.md        â† pip install chartexa, .NET runtime
â”‚   â”‚   â”œâ”€â”€ chart-builder.md          â† Fluent Chart API (.line, .scatter, .candlestick, etc.)
â”‚   â”‚   â”œâ”€â”€ image-export.md           â† .save(), .save_jpeg(), .to_bytes()
â”‚   â”‚   â”œâ”€â”€ jupyter.md               â† Jupyter Notebook integration
â”‚   â”‚   â””â”€â”€ api-reference.md         â† Python module reference
â”‚   â””â”€â”€ web/
â”‚       â””â”€â”€ json-integration.md       â† Using Chartexa.Rendering.Web for web frontends
â”‚
â”œâ”€â”€ performance/
â”‚   â”œâ”€â”€ optimization.md               â† General optimization strategies
â”‚   â”œâ”€â”€ gpu-acceleration.md           â† DirectX 12 pipeline, SIMD transforms
â”‚   â”œâ”€â”€ memory.md                     â† Object pooling, render command reuse
â”‚   â”œâ”€â”€ large-datasets.md            â† Resampling, downsampling, streaming
â”‚   â””â”€â”€ benchmarks.md                â† BenchmarkDotNet results and methodology
â”‚
â”œâ”€â”€ examples/
â”‚   â”œâ”€â”€ index.md                       â† Examples overview
â”‚   â”œâ”€â”€ csharp/
â”‚   â”‚   â”œâ”€â”€ real-time-line-chart.md
â”‚   â”‚   â”œâ”€â”€ financial-dashboard.md
â”‚   â”‚   â”œâ”€â”€ multi-series-chart.md
â”‚   â”‚   â”œâ”€â”€ 3d-surface-plot.md
â”‚   â”‚   â”œâ”€â”€ heatmap-visualization.md
â”‚   â”‚   â”œâ”€â”€ instrument-dashboard.md
â”‚   â”‚   â””â”€â”€ iot-sensor-dashboard.md
â”‚   â””â”€â”€ python/
â”‚       â”œâ”€â”€ quick-line-chart.md
â”‚       â”œâ”€â”€ candlestick-chart.md
â”‚       â”œâ”€â”€ scatter-with-tooltips.md
â”‚       â”œâ”€â”€ heatmap.md
â”‚       â””â”€â”€ jupyter-notebook.md
â”‚
â”œâ”€â”€ api-reference/
â”‚   â”œâ”€â”€ index.md                       â† API reference overview
â”‚   â”œâ”€â”€ csharp/
â”‚   â”‚   â”œâ”€â”€ chartexa-core.md
â”‚   â”‚   â”œâ”€â”€ chartexa-axes.md
â”‚   â”‚   â”œâ”€â”€ chartexa-data.md
â”‚   â”‚   â”œâ”€â”€ chartexa-datasources.md
â”‚   â”‚   â”œâ”€â”€ chartexa-rendering.md
â”‚   â”‚   â”œâ”€â”€ chartexa-modifiers.md
â”‚   â”‚   â”œâ”€â”€ chartexa-theming.md
â”‚   â”‚   â””â”€â”€ chartexa-layout.md
â”‚   â””â”€â”€ python/
â”‚       â””â”€â”€ chartexa-python.md
â”‚
â”œâ”€â”€ architecture/
â”‚   â”œâ”€â”€ system-overview.md             â† Layered architecture, component diagram
â”‚   â”œâ”€â”€ rendering-pipeline.md          â† RenderCommand flow, backends
â”‚   â””â”€â”€ coordinate-system.md           â† Data â†” screen coordinate mapping
â”‚
â”œâ”€â”€ migration/
â”‚   â””â”€â”€ from-scichart.md              â† Migration guide from SciChart
â”‚
â””â”€â”€ faq.md
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
| **DirectX 12** | `Chartexa.Rendering.DirectX` | Windows | Maximum GPU performance â€” double-buffered swap chain, SIMD transforms, SDF text, batched draw calls |
| **SkiaSharp** | `Chartexa.Rendering.Skia` | Cross-platform | Flexible software/GPU hybrid â€” ideal for server-side rendering, image export, and cross-platform apps |
| **WPF** | `Chartexa.Rendering.Wpf` | Windows (WPF) | Native WPF integration â€” `DrawingContext` rendering with dependency property support and MVVM |
| **Web** | `Chartexa.Rendering.Web` | Cross-platform | JSON command export â€” feed render commands to a JavaScript/WebAssembly frontend |

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

Chart interaction is handled through the **Modifier API** â€” composable, pluggable behaviors that respond to mouse and touch input.

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

Themes support **per-widget overrides** â€” apply a global theme and selectively customize individual widgets and series.

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

- **DirectX 12** â€” double-buffered swap chain (3 back buffers), per-frame command allocators, root constants (no descriptor heap overhead), draw batch accumulation
- **SIMD** â€” vectorized coordinate transforms for data â†’ screen mapping
- **Object pooling** â€” `RenderCommandPool` and `RenderCommandList` reuse to minimize GC pressure
- **Resampling** â€” built-in data downsampling for large datasets
- **GPU profiling** â€” `GpuTimestampQuery` and `FrameStatistics` for per-frame performance measurement

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

- **User-first** â€” focus on usage patterns and practical scenarios, not internal implementation
- **Example-driven** â€” every feature is demonstrated with working code in both C# and Python
- **Performance-aware** â€” optimization strategies and trade-offs are documented alongside features
- **Consistent** â€” uniform structure, terminology, and code style across all pages

### Writing Style

- Technical, concise, and precise
- No marketing language
- Clear separation of concepts, configuration, and code examples
- Every page follows: **overview â†’ configuration â†’ code example â†’ notes/tips**

### Code Examples

Every documented feature includes:

- **Minimal example** â€” shortest working code
- **Real-world scenario** â€” practical, production-relevant usage
- **C# + Python** â€” side-by-side where the feature is available in both

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

The Chartexa engine is proprietary â€” see the main repository for licensing terms.


---

> **Last synced from source:** 2026-04-08 13:00 UTC
