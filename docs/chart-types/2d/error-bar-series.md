---
title: "Error Bar Series"
section: "chart-types/2d"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Error Bar Series

## Summary

The error bar series renders uncertainty indicators around data points. Supports symmetric, asymmetric, and bidirectional error bars with configurable cap width.

---

## Quick Start

=== "Python"

    `python
    import chartexa as cx

    chart = cx.Chart().error_bar(
        x=[1, 2, 3, 4, 5],
        y=[20, 35, 28, 42, 31],
        error_y=[3, 5, 2, 4, 3],
        stroke="#F9E2AF",
        thickness=1.5,
        cap_width=8,
    )
    chart.save("error_bars.png")
    `

=== "C#"

    `csharp
    var s = new ErrorBarSeries(x, y)
    {
        ErrorY = errorValues,
        Stroke = new ChartColor(249, 226, 175),
        CapWidth = 8
    };
    `

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `error_y` | sequence | `None` | Symmetric Y error (+/-) |
| `error_high` | sequence | `None` | Upper error bound |
| `error_low` | sequence | `None` | Lower error bound |
| `error_x` | sequence | `None` | X error |
| `stroke` | str / tuple | auto | Bar colour |
| `thickness` | float | `1.5` | Bar stroke width |
| `cap_width` | float | `6.0` | Cap width in pixels |

---

## When to Use

- Scientific measurements with uncertainty
- Survey results with confidence intervals
- Experimental data with error margins

---

## Related

- [Band Series](band-series.md) -- continuous confidence band
- [Box Plot](../chart-types/2d/stacked-column.md) -- statistical distribution summary

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
