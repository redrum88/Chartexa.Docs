---
title: "Logarithmic Axis"
section: "axes"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Logarithmic Axis

## Summary

The logarithmic axis maps values on a logarithmic scale. Ideal for data spanning several orders of magnitude (frequency response, decibel scales, exponential growth).

---

## Quick Start

=== "Python"

    `python
    import chartexa as cx

    x = [1, 10, 100, 1000, 10000]
    y = [0, -3, -6, -12, -20]

    chart = (
        cx.Chart()
        .line(x, y, stroke="#CBA6F7")
        .x_axis(type="log", title="Frequency (Hz)", log_base=10)
        .y_axis(title="Gain (dB)")
    )
    chart.save("log_axis.png")
    `

=== "C#"

    `csharp
    var xAxis = new LogarithmicAxis
    {
        AxisTitle = "Frequency (Hz)",
        LogBase = 10
    };
    `

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `log_base` | float | `10.0` | Logarithm base (e.g. 10, 2, `e`) |

---

## When to Use

- Frequency response (Bode plots)
- Decibel scales
- Exponential growth or decay
- Power spectra

---

## Related

- [Axes Overview](overview.md)
- [Bode Plot](../chart-types/instruments/bode-plot.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
