---
title: "OHLC Data Series"
section: "data/data-series"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# OHLC Data Series

## Summary

`OhlcDataSeries` stores Open, High, Low, Close financial data. Used by the candlestick series for OHLC chart rendering.

---

## Usage

=== "Python"

    ```python
    import chartexa as cx

    chart = cx.Chart().candlestick(
        x=[0, 1, 2],
        open=[100, 105, 102],
        high=[110, 108, 107],
        low=[98, 101, 99],
        close=[105, 102, 106],
    )
    # OhlcDataSeries is created internally via DataSeriesFactory
    ```

=== "C#"

    ```csharp
    var ds = DataSeriesFactory.CreateOhlcSeries(x, open, high, low, close);
    ```

---

## Related

- [XY Data Series](xy-data-series.md)
- [Candlestick Series](../../chart-types/2d/candlestick-series.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
