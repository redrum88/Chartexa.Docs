---
title: "Band Series"
section: "chart-types/2d"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Band Series

## Summary

The band series fills the area between two Y boundaries sharing the same X values. Ideal for confidence intervals, tolerance bands, and min/max ranges. Uses `BandRenderableSeries` in the .NET engine.

---

## Quick Start

=== "Python"

    ```python
    import chartexa as cx

    x = [0, 1, 2, 3, 4, 5]
    upper = [30, 35, 28, 40, 32, 38]
    lower = [10, 15, 8, 20, 12, 18]

    chart = cx.Chart().band(x, upper, lower, stroke="#A6E3A1", fill="#A6E3A1")
    chart.save("band.png")
    ```

=== "C#"

    ```csharp
    var upperDs = new XyDataSeries();
    upperDs.Append(x, upper);

    var lowerDs = new XyDataSeries();
    lowerDs.Append(x, lower);

    var rs = new BandRenderableSeries
    {
        DataSeries = upperDs,
        LowerSeries = lowerDs,
        Stroke = new ChartColor(166, 227, 161),
        Fill = new ChartColor(80, 166, 227, 161)
    };
    ```

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `stroke` | str / tuple | auto | Boundary line colour |
| `fill` | str / tuple | auto | Fill colour |
| `thickness` | float | `1.0` | Boundary line width |

---

## When to Use

- Confidence intervals (mean +/- std)
- Temperature high/low ranges
- Bollinger bands in finance
- Tolerance zones in engineering

---

## Related

- [Mountain Series](mountain-series.md) -- fill from line to baseline
- [Fan Series](error-bar-series.md) -- multiple confidence bands
- [Error Bar Series](error-bar-series.md) -- discrete error indicators

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
