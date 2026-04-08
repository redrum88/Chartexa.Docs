---
title: "XY Data Series"
section: "data/data-series"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# XY Data Series

## Summary

`XyDataSeries` is the primary data container for 2D charts. It stores paired X and Y values as .NET arrays for high-performance access by the rendering engine.

---

## Usage

=== "Python"

    ```python
    # In the Python wrapper, data series are created automatically:
    import chartexa as cx

    chart = cx.Chart().line([1, 2, 3], [10, 20, 15])
    # The .line() method creates an XyDataSeries internally
    ```

=== "C#"

    ```csharp
    var ds = new XyDataSeries();
    ds.Append(new double[] { 1, 2, 3 }, new double[] { 10, 20, 15 });
    ```

---

## Related

- [OHLC Data Series](ohlc-data-series.md)
- [Chart Builder API](../../python/chart-builder.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
