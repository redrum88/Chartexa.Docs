---
title: "API Reference"
section: "api-reference"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# API Reference

## Summary

Complete API reference for the Chartexa Python package (`chartexa`). Version 0.2.5.

---

## Core

| Class / Function | Description |
|---|---|
| `Chart(width, height)` | [Chart builder](../python/chart-builder.md) with fluent API |
| `ChartSurface` | Legacy API -- direct .NET surface wrapper |

## Convenience Functions

| Function | Description |
|---|---|
| `line(y, x=None, **kw)` | Create a chart with a single line |
| `scatter(x, y, **kw)` | Single scatter chart |
| `bar(x, y, **kw)` | Single bar chart |
| `column(x, y, **kw)` | Single column chart (alias for bar) |
| `mountain(x, y, **kw)` | Single mountain/area chart |
| `candlestick(x, open, high, low, close, **kw)` | Single candlestick chart |
| `band(x, y_upper, y_lower, **kw)` | Single band chart |
| `heatmap(data, **kw)` | Single heatmap chart |
| `bubble(x, y, sizes, **kw)` | Single bubble chart |
| `pie(values, **kw)` | Single pie chart |
| `donut(values, **kw)` | Single donut chart |

## Axes

| Class | Description |
|---|---|
| `NumericAxis` | Continuous numeric axis (default) |
| `DateTimeAxis` | Time-based axis with date formatting |
| `CategoryAxis` | Discrete label axis |
| `LogarithmicAxis` | Logarithmic scale axis |

## Series Types

### 2D Series

| Class | Description |
|---|---|
| `LineSeries` | Connected line |
| `ScatterSeries` | Unconnected markers |
| `ColumnSeries` | Vertical bars |
| `MountainSeries` | Filled area |
| `BandSeries` | Fill between boundaries |
| `BubbleSeries` | Variable-size markers |
| `CandlestickSeries` | OHLC financial candles |
| `HeatmapSeries` | 2D colour grid |
| `ErrorBarSeries` | Uncertainty indicators |
| `BoxPlotSeries` | Statistical box plots |
| `FanSeries` | Confidence bands |
| `GanttSeries` | Gantt chart bars |
| `ImpulseSeries` | Stem plots |
| `WaterfallSeries` | Waterfall chart |
| `PieSeries` / `DonutSeries` | Proportional segments |

### Stacked Series

| Class | Description |
|---|---|
| `StackedColumnSeries` | Stacked vertical bars |
| `StackedBarSeries` | Stacked horizontal bars |
| `StackedMountainSeries` | Stacked area layers |

### Digital Series

| Class | Description |
|---|---|
| `DigitalLineSeries` | Step-function line |
| `DigitalMountainSeries` | Step-function area |
| `DigitalBandSeries` | Step-function band |

### Polar / Radar

| Class | Description |
|---|---|
| `PolarSeries` | Polar coordinate line |
| `RadarSeries` | Multi-axis radar chart |

### 3D

| Class | Description |
|---|---|
| `XYZSurfaceSeries` | 3D surface mesh |

### Gauges & Widgets

| Class | Description |
|---|---|
| `AngularGaugeSeries` | Circular gauge |
| `LinearGaugeSeries` | Horizontal/vertical gauge |
| `RadialGaugeSeries` | Radial progress |
| `ThermometerSeries` | Temperature display |
| `AlarmWidget` | Alarm indicator |
| `BatteryIndicatorWidget` | Battery level |
| `PowerMeterWidget` | Power consumption |
| `StatusLampWidget` | On/off indicator |

### Scientific Instruments

| Class | Description |
|---|---|
| `OscilloscopeSeries` | Oscilloscope display |
| `SpectrumAnalyzerSeries` | Frequency spectrum |
| `BodePlotSeries` | Frequency response |
| `NyquistPlotSeries` | Nyquist diagram |
| `ConstellationDiagramSeries` | Signal constellation |
| `EyeDiagramSeries` | Eye diagram |
| `RadarSweepSeries` | PPI radar display |
| `CompassSeries` | Compass heading |
| `GpsTrackSeries` | GPS track overlay |

### Audio

| Class | Description |
|---|---|
| `VuMeterSeries` | VU meter display |
| `OctaveBandSeries` | Octave band analyser |
| `SpectrumAnalyzerSeries` | Audio spectrum |
| `SegmentedBarSeries` | Segmented bar display |

### Signal Processing

| Class | Description |
|---|---|
| `BeatVisualizerSeries` | Beat detection display |
| `LissajousSeries` | Lissajous figures |
| `PidControllerSeries` | PID controller response |

## Modifiers (Interaction)

| Class | Description |
|---|---|
| `ZoomPanModifier` | Scroll-zoom and drag-pan |
| `RubberBandZoomModifier` | Rectangle selection zoom |
| `CursorModifier` / `CrosshairModifier` | Mouse-following crosshair |
| `TooltipModifier` | Data value tooltips |
| `DataPointSelectionModifier` | Click to select points |
| `SeriesSelectionModifier` | Click to highlight series |

## Annotations

| Class | Description |
|---|---|
| `HorizontalLineAnnotation` | Horizontal line at Y value |
| `VerticalLineAnnotation` | Vertical line at X value |
| `LineAnnotation` | Arbitrary line between two points |
| `BoxAnnotation` | Rectangle region highlight |
| `TextAnnotation` | Text at data coordinates |
| `EventMarker` | Vertical event marker with label |
| `CircleAnnotation` | Circle at data coordinates |
| `ArrowAnnotation` | Arrow between two points |

## Theming

| Class / Object | Description |
|---|---|
| `ChartTheme` | Custom theme definition |
| `Color` | Colour with hex, RGB, named constructors |
| `ColorCycle` | Auto-cycling colour palette |
| `gradient(start, end, steps)` | Generate colour gradient |
| `MarkerStyle` | Marker shape and size |
| `SeriesStyle` | Series visual style |
| `THEME_PRESETS` | Dict of all 15 built-in themes |

## Layout

| Class / Function | Description |
|---|---|
| `Figure` | Multi-chart figure container |
| `Dashboard` | Absolute-positioned chart layout |
| `subplots(rows, cols)` | Quick grid layout |
| `figure()` | Create an empty Figure |
| `LayoutSize` | Size specification |
| `LayoutConstraints` | Min/max size constraints |
| `SizeMode` | Fixed / proportional |

## Performance

| Class / Function | Description |
|---|---|
| `lttb_downsample(x, y, target)` | LTTB visual downsampling |
| `minmax_downsample(x, y, target)` | Min/max downsampling |
| `auto_downsample(x, y)` | Auto-select algorithm |
| `fast_append_xy(ds, x, y)` | Fast .NET array append |
| `FifoBuffer(capacity)` | Fixed-size sliding window |
| `BatchUpdate(chart)` | Deferred rendering context |
| `DisposableChart` | Auto-cleanup chart |
| `ResourceTracker` | .NET resource tracking |
| `numpy_to_net_array(arr)` | NumPy -> .NET conversion |
| `net_array_to_numpy(arr)` | .NET -> NumPy conversion |

## Data Transforms

| Function | Description |
|---|---|
| `moving_average(data, window)` | Simple moving average |
| `exponential_smoothing(data, alpha)` | Exponential smoothing |
| `bollinger_bands(data, window, std_dev)` | Bollinger bands |
| `derivative(data)` | First derivative |
| `integral(data)` | Cumulative integral |
| `low_pass_filter(data, cutoff)` | Low-pass filter |
| `high_pass_filter(data, cutoff)` | High-pass filter |
| `rolling_min(data, window)` | Rolling minimum |
| `rolling_max(data, window)` | Rolling maximum |
| `rolling_std(data, window)` | Rolling standard deviation |

## Data I/O

| Function | Description |
|---|---|
| `export_csv(recorder, path)` | Export recorded data to CSV |
| `import_csv(path)` | Import data from CSV |
| `export_binary(recorder, path)` | Export to binary format |
| `import_binary(path)` | Import from binary format |

## Jupyter

| Class / Function | Description |
|---|---|
| `ChartWidget` | Interactive notebook widget |
| `NotebookLiveChart` | Streaming chart for notebooks |
| `detect_environment()` | Detect notebook environment |
| `is_notebook()` | Check if running in notebook |
| `is_ipython()` | Check if running in IPython |
| `display_chart(chart)` | Force display chart |
| `auto_configure()` | Auto-setup notebook rendering |
| `setup_colab()` | Configure Google Colab |

## Configuration

| Function | Description |
|---|---|
| `set_defaults(**kw)` | Set session-wide defaults |
| `get_default(key)` | Get a default value |
| `reset_defaults()` | Reset all defaults |

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
