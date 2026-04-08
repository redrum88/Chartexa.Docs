---
title: "Candlestick Series"
section: "chart-types/2d"
last_updated: "2024-06-10 15:42 UTC"
status: draft
---

# Candlestick Series

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

The `FastCandlestickRenderableSeries` displays OHLC (Open, High, Low, Close) candlestick charts, commonly used for financial and trading applications. This series visualizes price movements over time, providing insight into market trends and volatility.

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
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;

// Sample OHLC data
double[] dates = { 20240601, 20240602, 20240603, 20240604 };
double[] open = { 101.2, 102.5, 103.0, 104.1 };
double[] high = { 103.0, 104.2, 105.0, 106.5 };
double[] low = { 100.8, 101.7, 102.8, 103.9 };
double[] close = { 102.8, 103.9, 104.7, 106.0 };

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Date" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Price (USD)" };

// Create OHLC data series
var ohlcSeries = new OhlcDataSeries();
ohlcSeries.Append(dates, open, high, low, close);

// Create candlestick renderable series
var candleSeries = new FastCandlestickRenderableSeries
{
    DataSeries = ohlcSeries,
    UpFill = new ChartColor(34, 139, 34),       // Green for up
    DownFill = new ChartColor(220, 20, 60),     // Red for down
    StrokeThickness = 1.5
};

// Create chart and add series
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(candleSeries);
```

=== "Python"
```python
from chartexa import Chart

# Sample OHLC data
dates = [20240601, 20240602, 20240603, 20240604]
open = [101.2, 102.5, 103.0, 104.1]
high = [103.0, 104.2, 105.0, 106.5]
low = [100.8, 101.7, 102.8, 103.9]
close = [102.8, 103.9, 104.7, 106.0]

chart = (
    Chart(width=800, height=400)
    .candlestick(
        x=dates,
        open=open,
        high=high,
        low=low,
        close=close,
        up_fill="#228B22",     # Green for up
        down_fill="#DC143C",   # Red for down
        thickness=1.5
    )
    .axis_x(title="Date")
    .axis_y(title="Price (USD)")
    .background("#F5F5F5")
    .save("candlestick_quickstart.png")
)
```

---

## Concepts

Candlestick charts are essential for visualizing price action in financial markets. Each candlestick represents a single time period (e.g., day, hour) and displays four key values: open, high, low, and close. The body of the candlestick shows the range between open and close, while the "wicks" indicate the high and low.

Use `FastCandlestickRenderableSeries` when you need to analyze trends, reversals, and volatility in trading data. The candlestick format is preferred over line or column charts for its ability to convey more information per data point, including directionality and magnitude of price changes.

Chartexa's candlestick series is optimized for large datasets and real-time updates, making it suitable for live trading dashboards and historical analysis.

---

## Basic Usage

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;

// Example: Visualizing weekly stock prices

double[] dates = { 20240603, 20240604, 20240605, 20240606, 20240607 };
double[] open = { 120.5, 121.3, 122.0, 123.1, 124.0 };
double[] high = { 123.0, 124.2, 125.0, 126.5, 127.2 };
double[] low = { 119.8, 120.7, 121.8, 122.9, 123.5 };
double[] close = { 122.8, 123.9, 124.7, 126.0, 126.8 };

var xAxis = new NumericAxis { Id = "X", AxisTitle = "Date" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Stock Price (USD)" };

var ohlcSeries = new OhlcDataSeries();
ohlcSeries.Append(dates, open, high, low, close);

var candleSeries = new FastCandlestickRenderableSeries
{
    DataSeries = ohlcSeries,
    UpFill = new ChartColor(0, 128, 0),        // Green
    DownFill = new ChartColor(255, 0, 0),      // Red
    StrokeThickness = 2,
    WickThickness = 1
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(candleSeries);

// Optionally export or display chart
chart.SaveToFile("weekly_stock_candlestick.png");
```

=== "Python"
```python
from chartexa import Chart

dates = [20240603, 20240604, 20240605, 20240606, 20240607]
open = [120.5, 121.3, 122.0, 123.1, 124.0]
high = [123.0, 124.2, 125.0, 126.5, 127.2]
low = [119.8, 120.7, 121.8, 122.9, 123.5]
close = [122.8, 123.9, 124.7, 126.0, 126.8]

chart = (
    Chart(width=900, height=500)
    .candlestick(
        x=dates,
        open=open,
        high=high,
        low=low,
        close=close,
        up_fill="#008000",      # Green
        down_fill="#FF0000",    # Red
        thickness=2,
        wick_thickness=1
    )
    .axis_x(title="Date")
    .axis_y(title="Stock Price (USD)")
    .background("#FFFFFF")
    .save("weekly_stock_candlestick.png")
)
```

---

## Configuration

| Property        | Type           | Default         | Description                                              |
|-----------------|----------------|-----------------|----------------------------------------------------------|
| `UpFill`        | ChartColor     | Green           | Fill color for upward (close > open) candles             |
| `DownFill`      | ChartColor     | Red             | Fill color for downward (close < open) candles           |
| `StrokeColor`   | ChartColor     | Black           | Outline color for candle bodies                          |
| `StrokeThickness`| double        | 1.0             | Thickness of candle body outline                         |
| `WickColor`     | ChartColor     | Black           | Color for candle wicks                                   |
| `WickThickness` | double         | 1.0             | Thickness of candle wicks                                |
| `DataSeries`    | OhlcDataSeries | (required)      | OHLC data source                                         |
| `Opacity`       | double         | 1.0             | Opacity of candle fills (0.0-1.0)                        |
| `AutoRange`     | bool           | true            | Automatically fit axis range to data                     |

!!! warning
    The `OhlcDataSeries.Append()` method requires all input arrays (`x`, `open`, `high`, `low`, `close`) to have equal length.

---

## Examples

### Example 1: Visualizing Intraday Forex Data

=== "C#"
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;
using Chartexa.Core.RenderableSeries;
using Chartexa.Core.Chart;

// EUR/USD hourly prices
double[] hours = { 9, 10, 11, 12, 13, 14 };
double[] open = { 1.086, 1.088, 1.090, 1.092, 1.091, 1.089 };
double[] high = { 1.089, 1.091, 1.093, 1.094, 1.092, 1.090 };
double[] low = { 1.085, 1.087, 1.089, 1.090, 1.088, 1.087 };
double[] close = { 1.088, 1.090, 1.092, 1.091, 1.089, 1.088 };

var xAxis = new NumericAxis { Id = "X", AxisTitle = "Hour (UTC)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "EUR/USD" };

var ohlcSeries = new OhlcDataSeries();
ohlcSeries.Append(hours, open, high, low, close);

var candleSeries = new FastCandlestickRenderableSeries
{
    DataSeries = ohlcSeries,
    UpFill = new ChartColor(0, 200, 0),
    DownFill = new ChartColor(200, 0, 0),
    StrokeThickness = 1,
    WickThickness = 1
};

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.RenderableSeries.Add(candleSeries);
chart.SaveToFile("intraday_forex_candlestick.png");
```

=== "Python"
```python
from chartexa import Chart

hours = [9, 10, 11, 12, 13, 14]
open = [1.086, 1.088, 1.090, 1.092, 1.091, 1.089]
high = [1.089, 1.091, 1.093, 1.094, 1.092, 1.090]
low = [1.085, 1.087, 1.089, 1.090, 1.088, 1.087]
close = [1.088, 1.090, 1.092, 1.091, 1.089, 1.088]

chart = (
    Chart(width=700, height=350)
    .candlestick(
        x=hours,
        open=open,
        high=high,
        low=low,
        close=close,
        up_fill="#00C800",
        down_fill="#C80000",
        thickness=1,
        wick_thickness=1
    )
    .axis_x(title="Hour (UTC)")
    .axis_y(title="EUR/USD")
    .background("#F0F8FF")
    .save("intraday_forex_candlestick.png")
)
```

### Example 2: Real-Time Streaming Candlestick Chart

!!! example "Real-Time Streaming"
    === "C#"
    ```csharp
    using Chartexa.Core.Axes;
    using Chartexa.Data.Series;
    using Chartexa.Core.RenderableSeries;
    using Chartexa.Core.Chart;

    // Simulate streaming OHLC data
    var ohlcSeries = new OhlcDataSeries();
    var candleSeries = new FastCandlestickRenderableSeries
    {
        DataSeries = ohlcSeries,
        UpFill = new ChartColor(50, 205, 50),
        DownFill = new ChartColor(255, 69, 0),
        StrokeThickness = 1
    };

    var chart = new Chart();
    chart.Axes.Add(new NumericAxis { Id = "X", AxisTitle = "Time (s)" });
    chart.Axes.Add(new NumericAxis { Id = "Y", AxisTitle = "Price" });
    chart.RenderableSeries.Add(candleSeries);

    // Streaming loop (pseudo-code)
    for (int t = 0; t < 100; t++)
    {
        double open = GetOpen(t);
        double high = GetHigh(t);
        double low = GetLow(t);
        double close = GetClose(t);
        ohlcSeries.Append(new double[] { t }, new double[] { open }, new double[] { high }, new double[] { low }, new double[] { close });
        chart.Refresh();
    }
    ```
    === "Python"
    ```python
    from chartexa import Chart
    import time

    chart = Chart(width=800, height=400)
    chart.axis_x(title="Time (s)")
    chart.axis_y(title="Price")

    # Initial empty lists
    times, open, high, low, close = [], [], [], [], []

    for t in range(100):
        times.append(t)
        open.append(get_open(t))
        high.append(get_high(t))
        low.append(get_low(t))
        close.append(get_close(t))
        chart.candlestick(
            x=times,
            open=open,
            high=high,
            low=low,
            close=close,
            up_fill="#32CD32",
            down_fill="#FF4500",
            thickness=1
        )
        chart.refresh()
        time.sleep(0.05)
    ```

---

## Performance Notes

Chartexa's `FastCandlestickRenderableSeries` leverages DirectX 12 for hardware-accelerated rendering, enabling smooth visualization of datasets with hundreds of thousands of candlesticks. Rendering performance remains consistent even with frequent real-time updates.

- Rendering 100,000 candlesticks: ~60 FPS on modern GPUs
- Python integration uses .NET runtime and DirectX backend for maximum throughput
- Memory usage scales linearly with data size; avoid storing redundant OHLC arrays

!!! tip "Performance Tip"
    Use the DirectX12 renderer for live trading dashboards or historical datasets exceeding 50,000 candlesticks.

!!! note
    Python requires the .NET 10 Runtime to be installed for DirectX 12 support.

---

## When to Use

- Visualizing financial time series (stocks, forex, crypto)
- Building trading dashboards with real-time price updates
- Analyzing historical price action for technical analysis
- Comparing price volatility across multiple assets
- Displaying OHLC data with clear up/down color coding

---

## Related

- [OhlcDataSeries](../../data-series/ohlc-data-series.md)
- [NumericAxis](../../axes/numeric-axis.md)
- [Column Series](column-series.md)
- [Line Series](line-series.md)

---

> **Last updated:** 2024-06-10 15:42 UTC | **Status:** draft