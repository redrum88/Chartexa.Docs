---
title: "Angular Gauge"
section: "chart-types/gauges-and-widgets"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Angular Gauge

## Summary

The angular gauge renders a circular dial with a needle indicator. Suitable for speedometers, pressure gauges, and any single-value display with min/max context. Uses `AngularGaugeSeries` in the .NET engine.

---

## Quick Start

=== "Python"

    ```python
    from chartexa import Chart, AngularGaugeSeries
    # Angular gauge configuration via the series class API
    ```

=== "C#"

    ```csharp
    var gauge = new AngularGaugeSeries
    {
        Value = 72,
        MinValue = 0,
        MaxValue = 100
    };
    surface.RenderableSeries.Add(gauge);
    ```

---

## Related

- [Linear Gauge](linear-gauge.md)
- [Radial Gauge](radial-gauge.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
