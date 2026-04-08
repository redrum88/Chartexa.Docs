---
title: "Digital Signal Series"
section: "chart-types/2d"
last_updated: "2024-06-11 16:45 UTC"
status: draft
---

# Digital Signal Series

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `DigitalSignalSeries` provides a specialized renderable series for visualizing digital signals, such as logic analyzer traces, binary data streams, and step-like signals. It renders data as horizontal steps, emphasizing transitions between discrete states. Use this series to plot digital waveforms, binary sensor outputs, or any signal with abrupt state changes.

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

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (ms)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "State" };

// Prepare digital signal data
double[] time = { 0, 1, 2, 3, 4, 5, 6, 7 };
int[] state = { 0, 1, 1, 0, 0, 1, 0, 1 };

// Create data series
var digitalData = new DigitalDataSeries();
digitalData.Append(time, state);

// Create digital signal series
var digitalSeries = new DigitalSignalSeries
{
    DataSeries = digitalData,
    StrokeColor = new ChartColor(0, 200, 0), // Green
    StrokeThickness = 2
};

// Add to chart (assuming chart object exists)
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(digitalSeries);
```

=== "Python"

```python
from chartexa import Chart

# Digital signal data: time and state
time = [0, 1, 2, 3, 4, 5, 6, 7]
state = [0, 1, 1, 0, 0, 1, 0, 1]

chart = (
    Chart(width=600, height=300)
    .digital(time, state, stroke="#00C800", thickness=2)
    .x_axis(title="Time (ms)")
    .y_axis(title="State", min=0, max=1)
    .background("#222")
    .save("digital_signal.png")
)
```

---

## Concepts

The Digital Signal Series is designed for visualizing signals with discrete states, such as binary or multi-level digital waveforms. Unlike line or scatter plots, it draws horizontal segments for each state, with vertical transitions at each change point. This style is ideal for representing logic analyzer outputs, digital communication signals, or any system where the signal jumps abruptly between defined levels.

Use `DigitalSignalSeries` when you need to emphasize the timing and duration of each state, rather than interpolating between values. It is particularly useful for debugging hardware interfaces, visualizing digital protocols, and monitoring binary sensor data.

The series supports both binary (0/1) and multi-level signals, and can be customized for color, thickness, and step rendering style.

---

## Basic Usage

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.Series;

// Example: Visualizing a digital sensor output

// Time in milliseconds
double[] time = { 0, 10, 20, 30, 40, 50, 60, 70 };
// Sensor state: 0 = OFF, 1 = ON
int[] sensorState = { 0, 0, 1, 1, 0, 1, 1, 0 };

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (ms)", AutoRange = true };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Sensor State", Min = 0, Max = 1 };

// Create digital data series
var digitalData = new DigitalDataSeries();
digitalData.Append(time, sensorState);

// Configure digital signal series
var digitalSeries = new DigitalSignalSeries
{
    DataSeries = digitalData,
    StrokeColor = new ChartColor(255, 140, 0), // Orange
    StrokeThickness = 3,
    StepStyle = StepStyle.Horizontal
};

// Add to chart
chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(digitalSeries);
```

=== "Python"

```python
from chartexa import Chart

# Example: Binary sensor output
time = [0, 10, 20, 30, 40, 50, 60, 70]
sensor_state = [0, 0, 1, 1, 0, 1, 1, 0]

chart = (
    Chart(width=700, height=250)
    .digital(time, sensor_state, stroke="#FF8C00", thickness=3, step="horizontal")
    .x_axis(title="Time (ms)")
    .y_axis(title="Sensor State", min=0, max=1)
    .background("#282828")
    .show()
)
```

---

## Configuration

| Property      | Type           | Default      | Description                                                  |
|---------------|----------------|--------------|--------------------------------------------------------------|
| DataSeries    | DigitalDataSeries | (required) | The data series containing time and state values             |
| StrokeColor   | ChartColor     | #00C800      | Color of the digital signal line                             |
| StrokeThickness | int          | 2            | Line thickness in pixels                                     |
| StepStyle     | StepStyle      | Horizontal   | Step rendering style: `Horizontal`, `Vertical`, `Both`       |
| ShowMarkers   | bool           | false        | Whether to display markers at transition points              |
| MarkerColor   | ChartColor     | #FFFFFF      | Color of markers (if enabled)                                |
| MarkerSize    | int            | 5            | Size of markers in pixels                                    |
| AntiAliasing  | bool           | true         | Enables anti-aliased rendering                               |

!!! tip "StepStyle Options"
    - `Horizontal`: Draws horizontal steps with vertical transitions at state changes (default).
    - `Vertical`: Draws vertical steps, useful for pulse-style signals.
    - `Both`: Combines horizontal and vertical transitions for more explicit state changes.

---

## Examples

### Example 1: Multi-Level Digital Signal

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.Series;

// Multi-level digital signal (e.g., UART voltage states)
double[] time = { 0, 5, 10, 15, 20, 25, 30, 35 };
int[] voltage = { 0, 1, 2, 2, 1, 0, 1, 2 };

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (us)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Voltage Level", Min = 0, Max = 2 };

// Create data series
var digitalData = new DigitalDataSeries();
digitalData.Append(time, voltage);

// Create digital signal series
var digitalSeries = new DigitalSignalSeries
{
    DataSeries = digitalData,
    StrokeColor = new ChartColor(70, 130, 180), // Steel blue
    StrokeThickness = 2,
    StepStyle = StepStyle.Both
};

chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(digitalSeries);
```

=== "Python"

```python
from chartexa import Chart

# Multi-level digital signal (UART voltage states)
time = [0, 5, 10, 15, 20, 25, 30, 35]
voltage = [0, 1, 2, 2, 1, 0, 1, 2]

chart = (
    Chart(width=600, height=300)
    .digital(time, voltage, stroke="#4682B4", thickness=2, step="both")
    .x_axis(title="Time (us)")
    .y_axis(title="Voltage Level", min=0, max=2)
    .background("#1C1C1E")
    .save("multi_level_digital.png")
)
```

### Example 2: Logic Analyzer Trace with Markers

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Rendering.Series;

// Logic analyzer data
double[] time = { 0, 2, 4, 6, 8, 10, 12, 14 };
int[] logic = { 0, 1, 0, 1, 1, 0, 1, 0 };

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (ns)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Logic State", Min = 0, Max = 1 };

// Create data series
var digitalData = new DigitalDataSeries();
digitalData.Append(time, logic);

// Create digital signal series with markers
var digitalSeries = new DigitalSignalSeries
{
    DataSeries = digitalData,
    StrokeColor = new ChartColor(255, 0, 0), // Red
    StrokeThickness = 2,
    ShowMarkers = true,
    MarkerColor = new ChartColor(255, 255, 255), // White
    MarkerSize = 6
};

chart.XAxes.Add(xAxis);
chart.YAxes.Add(yAxis);
chart.RenderableSeries.Add(digitalSeries);
```

=== "Python"

```python
from chartexa import Chart

# Logic analyzer trace with markers
time = [0, 2, 4, 6, 8, 10, 12, 14]
logic = [0, 1, 0, 1, 1, 0, 1, 0]

chart = (
    Chart(width=650, height=250)
    .digital(time, logic, stroke="#FF0000", thickness=2, show_markers=True, marker_color="#FFF", marker_size=6)
    .x_axis(title="Time (ns)")
    .y_axis(title="Logic State", min=0, max=1)
    .background("#232323")
    .show()
)
```

### Example 3: Real-Time Streaming Digital Signal

!!! example "Real-Time Streaming"

    === "C#"

    ```csharp
    using Chartexa.Core.Axes;
    using Chartexa.Data.Series;
    using Chartexa.Rendering.Series;

    // Assume digitalData and digitalSeries are already created and added to chart

    // Simulate streaming digital data
    double currentTime = 0;
    int currentState = 0;

    for (int i = 0; i < 100; i++)
    {
        currentTime += 1;
        // Toggle state randomly
        currentState = (currentState + (new Random().Next(2))) % 2;
        digitalData.Append(currentTime, currentState);
        chart.Refresh(); // Update chart in real-time
        System.Threading.Thread.Sleep(10); // Simulate data arrival
    }
    ```

    === "Python"

    ```python
    from chartexa import Chart
    import time
    import random

    chart = Chart(width=600, height=200)
    times = []
    states = []

    for i in range(100):
        times.append(i)
        states.append(random.randint(0, 1))
        chart.digital(times, states, stroke="#00C800", thickness=2)
        chart.show(block=False)
        time.sleep(0.01)
    ```

---

## Performance Notes

The Digital Signal Series is optimized for rendering large datasets with rapid state transitions. The DirectX 12 backend can efficiently display signals with hundreds of thousands of points, maintaining interactive frame rates.

- Rendering is O(N) with respect to the number of transitions.
- Step rendering avoids unnecessary interpolation, reducing GPU workload.
- Marker rendering may impact performance for very large datasets; disable `ShowMarkers` for best throughput.
- Python integration leverages .NET runtime for high-performance rendering.

!!! tip "Performance Tip"
    For real-time streaming or logic analyzer traces exceeding 500K points, use the DirectX 12 backend and avoid marker rendering.

---

## When to Use

- Visualizing digital signals from hardware (logic analyzers, microcontrollers)
- Displaying binary sensor outputs or switch states
- Monitoring communication protocols (UART, SPI, I2C, CAN)
- Plotting binary or multi-level digital data streams
- Debugging timing and transitions in digital systems
- Representing pulse-width modulation (PWM) or clock signals

---

## Related

- [FastLineRenderableSeries](./line-series.md)
- [Column Series](./column-series.md)
- [Axis Ranging](../axes/axis-ranging.md)
- [OHLC Data Series](../data-series/ohlc-data-series.md)

---

> **Last updated:** 2024-06-11 16:45 UTC | **Status:** draft