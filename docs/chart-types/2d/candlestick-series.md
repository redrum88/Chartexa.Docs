---
title: "Candlestick Series"
section: "chart-types/2d"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Candlestick Series

## Summary

The candlestick series renders OHLC (Open, High, Low, Close) financial data as traditional candlestick bars. Bullish and bearish candles are independently coloured. Uses `FastCandlestickRenderableSeries` in the .NET engine.

---

## Quick Start

=== "Python"

    `python
    import chartexa as cx

    chart = cx.Chart(width=1200, height=600).candlestick(
        x=[0, 1, 2, 3, 4, 5, 6, 7],
        open=[100, 105, 102, 108, 106, 110, 107, 112],
        high=[110, 108, 107, 112, 111, 115, 113, 118],
        low=[98, 101, 99, 105, 103, 107, 104, 109],
        close=[105, 102, 106, 110, 109, 112, 111, 116],
        bullish_fill="#A6E3A1",
        bearish_fill="#F38BA8",
    )
    chart.save("candlestick.png")
    `

=== "C#"

    `csharp
    var ds = DataSeriesFactory.CreateOhlcSeries(x, open, high, low, close);

    var rs = new FastCandlestickRenderableSeries
    {
        DataSeries = ds,
        BullishFill = new ChartColor(166, 227, 161),
        BearishFill = new ChartColor(243, 139, 168)
    };
    `

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `bullish_fill` | str / tuple | auto | Up-candle fill |
| `bearish_fill` | str / tuple | auto | Down-candle fill |
| `bullish_stroke` | str / tuple | same as fill | Up-candle outline |
| `bearish_stroke` | str / tuple | same as fill | Down-candle outline |
| `thickness` | float | `1.0` | Wick and outline stroke width |
| `bar_width` | float | `0.7` | Candle width fraction |

---

## When to Use

- Stock price / cryptocurrency charts
- Any OHLC (Open-High-Low-Close) data
- Financial dashboards

---

## Related

- [Column Series](column-series.md) -- single-value bars
- [Market Data Source](../../data/data-sources/financial/market-data.md) -- live market data feed

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
