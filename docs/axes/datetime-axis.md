---
title: "DateTime Axis"
section: "axes"
last_updated: "2024-06-10 18:45 UTC"
status: draft
---

# DateTime Axis

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `DateTimeAxis` provides temporal axis support for charts, automatically generating date/time ticks, formatting labels, and handling time-based data. Use it to visualize data indexed by timestamps, such as financial prices, sensor logs, or event timelines.

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
using Chartexa.Rendering.Series;
using System;

var xAxis = new DateTimeAxis
{
    Id = "X",
    AxisTitle = "Timestamp"
};

var yAxis = new NumericAxis
{
    Id = "Y",
    AxisTitle = "Temperature (°C)"
};

var timestamps = new DateTime[]
{
    new DateTime(2024, 6, 10, 8, 0, 0),
    new DateTime(2024, 6, 10, 9, 0, 0),
    new DateTime(2024, 6, 10, 10, 0, 0)
};
var temperatures = new double[] { 22.5, 24.1, 23.8 };

var dataSeries = new XyDataSeries<DateTime, double>();
dataSeries.Append(timestamps, temperatures);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(255, 99, 71), // Tomato
    StrokeThickness = 2
};
```

=== "Python"

```python
from datetime import datetime
from chartexa import Chart

timestamps = [
    datetime(2024, 6, 10, 8, 0),
    datetime(2024, 6, 10, 9, 0),
    datetime(2024, 6, 10, 10, 0)
]
temperatures = [22.5, 24.1, 23.8]

chart = (
    Chart(width=600, height=300)
    .datetime_axis("bottom", title="Timestamp")
    .numeric_axis("left", title="Temperature (°C)")
    .line(timestamps, temperatures, stroke="#FF6347", thickness=2)
    .save("temperature_timeseries.png")
)
```

---

## Concepts

The `DateTimeAxis` is designed for visualizing data indexed by time. It automatically determines suitable tick intervals (seconds, minutes, hours, days, months, years) based on the data range and zoom level, ensuring readable and meaningful axis labels.

Use `DateTimeAxis` when your X or Y values represent timestamps, such as in financial charts, sensor logs, or event-driven data. The axis handles date formatting, tick spacing, and label rotation, making it easy to present time-based information without manual configuration.

Unlike numeric axes, `DateTimeAxis` understands calendar boundaries, leap years, and daylight saving time, ensuring accurate representation of temporal data.

---

## Basic Usage

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.Series;
using System;

var xAxis = new DateTimeAxis
{
    Id = "Time",
    AxisTitle = "Date",
    LabelFormat = "yyyy-MM-dd HH:mm",
    MajorTickInterval = TimeSpan.FromHours(1),
    MinorTickInterval = TimeSpan.FromMinutes(15),
    AutoRange = true
};

var yAxis = new NumericAxis
{
    Id = "Value",
    AxisTitle = "Sensor Reading"
};

var timestamps = new DateTime[]
{
    new DateTime(2024, 6, 10, 8, 0, 0),
    new DateTime(2024, 6, 10, 8, 30, 0),
    new DateTime(2024, 6, 10, 9, 0, 0),
    new DateTime(2024, 6, 10, 9, 30, 0),
    new DateTime(2024, 6, 10, 10, 0, 0)
};
var readings = new double[] { 10.2, 11.5, 12.1, 11.8, 12.3 };

var dataSeries = new XyDataSeries<DateTime, double>();
dataSeries.Append(timestamps, readings);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(34, 139, 34), // Forest green
    StrokeThickness = 2
};

// Add axes and series to chart (not shown)
```

=== "Python"

```python
from datetime import datetime
from chartexa import Chart

timestamps = [
    datetime(2024, 6, 10, 8, 0),
    datetime(2024, 6, 10, 8, 30),
    datetime(2024, 6, 10, 9, 0),
    datetime(2024, 6, 10, 9, 30),
    datetime(2024, 6, 10, 10, 0)
]
readings = [10.2, 11.5, 12.1, 11.8, 12.3]

chart = (
    Chart(width=700, height=350)
    .datetime_axis("bottom", title="Date", label_format="%Y-%m-%d %H:%M", major_tick_interval="1h", minor_tick_interval="15m", autorange=True)
    .numeric_axis("left", title="Sensor Reading")
    .line(timestamps, readings, stroke="#228B22", thickness=2)
    .save("sensor_readings.png")
)
```

---

## Configuration

| Property           | Type                | Default         | Description                                                      |
|--------------------|---------------------|-----------------|------------------------------------------------------------------|
| `Id`               | string              | `"X"`           | Unique axis identifier.                                          |
| `AxisTitle`        | string              | `""`            | Axis title shown on chart.                                       |
| `LabelFormat`      | string              | `"yyyy-MM-dd"`  | Date/time format for axis labels.                                |
| `MajorTickInterval`| TimeSpan            | Auto            | Interval between major ticks (auto if not set).                  |
| `MinorTickInterval`| TimeSpan            | Auto            | Interval between minor ticks (auto if not set).                  |
| `AutoRange`        | bool                | `true`          | Automatically adjusts axis range to fit data.                    |
| `ShowGridLines`    | bool                | `true`          | Displays grid lines for ticks.                                   |
| `LabelRotation`    | double              | `0`             | Rotates axis labels by given degrees.                            |
| `TickLabelStyle`   | AxisLabelStyle      | Default         | Customizes font, color, and size of tick labels.                 |
| `MinDate`          | DateTime?           | None            | Minimum date/time shown on axis.                                 |
| `MaxDate`          | DateTime?           | None            | Maximum date/time shown on axis.                                 |

!!! tip "Date Formatting"
    Use `LabelFormat` to customize how dates appear on the axis. C# uses .NET date format strings; Python uses `strftime` codes.

---

## Examples

### Example 1: Financial OHLC Chart

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.Series;
using System;

var xAxis = new DateTimeAxis
{
    Id = "Time",
    AxisTitle = "Date",
    LabelFormat = "MMM dd",
    AutoRange = true
};

var yAxis = new NumericAxis
{
    Id = "Price",
    AxisTitle = "Closing Price ($)"
};

var dates = new DateTime[]
{
    new DateTime(2024, 6, 3),
    new DateTime(2024, 6, 4),
    new DateTime(2024, 6, 5),
    new DateTime(2024, 6, 6),
    new DateTime(2024, 6, 7)
};
var closes = new double[] { 101.5, 102.8, 100.9, 104.2, 103.7 };

var dataSeries = new XyDataSeries<DateTime, double>();
dataSeries.Append(dates, closes);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(70, 130, 180), // Steel blue
    StrokeThickness = 2
};
```

=== "Python"

```python
from datetime import datetime
from chartexa import Chart

dates = [
    datetime(2024, 6, 3),
    datetime(2024, 6, 4),
    datetime(2024, 6, 5),
    datetime(2024, 6, 6),
    datetime(2024, 6, 7)
]
closes = [101.5, 102.8, 100.9, 104.2, 103.7]

chart = (
    Chart(width=800, height=400)
    .datetime_axis("bottom", title="Date", label_format="%b %d")
    .numeric_axis("left", title="Closing Price ($)")
    .line(dates, closes, stroke="#4682B4", thickness=2)
    .save("ohlc_close.png")
)
```

### Example 2: Real-Time Streaming Data

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.Series;
using System;
using System.Threading;

var xAxis = new DateTimeAxis { Id = "Time", AxisTitle = "Timestamp" };
var yAxis = new NumericAxis { Id = "Value", AxisTitle = "Reading" };

var dataSeries = new XyDataSeries<DateTime, double>();

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(255, 165, 0), // Orange
    StrokeThickness = 2
};

// Simulate streaming
for (int i = 0; i < 10; i++)
{
    var now = DateTime.Now;
    var value = Math.Sin(i / 2.0) * 10 + 50;
    dataSeries.Append(now, value);
    Thread.Sleep(500); // Simulate real-time update
}
```

=== "Python"

```python
import time
from datetime import datetime
from chartexa import Chart

timestamps = []
values = []

for i in range(10):
    timestamps.append(datetime.now())
    values.append(50 + 10 * __import__('math').sin(i / 2.0))
    time.sleep(0.5)

chart = (
    Chart(width=600, height=300)
    .datetime_axis("bottom", title="Timestamp")
    .numeric_axis("left", title="Reading")
    .line(timestamps, values, stroke="#FFA500", thickness=2)
    .save("streaming_data.png")
)
```

### Example 3: Custom Tick Intervals and Label Rotation

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.Series;
using System;

var xAxis = new DateTimeAxis
{
    Id = "Time",
    AxisTitle = "Hour",
    LabelFormat = "HH:mm",
    MajorTickInterval = TimeSpan.FromHours(1),
    MinorTickInterval = TimeSpan.FromMinutes(30),
    LabelRotation = 45
};

var yAxis = new NumericAxis { Id = "Value", AxisTitle = "Usage" };

var times = new DateTime[]
{
    new DateTime(2024, 6, 10, 8, 0),
    new DateTime(2024, 6, 10, 9, 0),
    new DateTime(2024, 6, 10, 10, 0),
    new DateTime(2024, 6, 10, 11, 0)
};
var usage = new double[] { 120, 135, 128, 140 };

var dataSeries = new XyDataSeries<DateTime, double>();
dataSeries.Append(times, usage);

var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(0, 191, 255), // Deep sky blue
    StrokeThickness = 2
};
```

=== "Python"

```python
from datetime import datetime
from chartexa import Chart

times = [
    datetime(2024, 6, 10, 8, 0),
    datetime(2024, 6, 10, 9, 0),
    datetime(2024, 6, 10, 10, 0),
    datetime(2024, 6, 10, 11, 0)
]
usage = [120, 135, 128, 140]

chart = (
    Chart(width=700, height=350)
    .datetime_axis("bottom", title="Hour", label_format="%H:%M", major_tick_interval="1h", minor_tick_interval="30m", label_rotation=45)
    .numeric_axis("left", title="Usage")
    .line(times, usage, stroke="#00BFFF", thickness=2)
    .save("hourly_usage.png")
)
```

---

## Performance Notes

The `DateTimeAxis` is optimized for large time series datasets. Tick generation and label formatting are performed efficiently, even for millions of points. The DirectX 12 renderer ensures smooth interaction and redraws, regardless of axis complexity.

- Tick calculation is O(1) per visible range change.
- Label formatting leverages cached templates for minimal overhead.
- Rendering performance is unaffected by axis type; bottlenecks depend on data series size.

!!! tip "Performance Tip"
    For datasets exceeding 1 million points, use `DirectX12RenderContext` for best axis and series rendering performance.

!!! note
    Python integration requires the .NET 10 Runtime for full DateTime support.

---

## When to Use

- Visualizing time series data (financial, sensor, log, event).
- Displaying OHLC/candlestick charts indexed by date.
- Plotting real-time streaming values with timestamps.
- Comparing values across calendar intervals (days, weeks, months).
- Any scenario where axis values represent temporal information.

---

## Related

- [Numeric Axis](numeric-axis.md)
- [Axis Ranging](axis-ranging.md)
- [OHLC Data Series](../data-series/ohlc-data-series.md)
- [FastLineRenderableSeries](../chart-types/fast-line-renderable-series.md)

---

> **Last updated:** 2024-06-10 18:45 UTC | **Status:** draft