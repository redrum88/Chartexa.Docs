---
title: "Digital Signal"
section: "chart-types/2d"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Digital Signal Series

## Summary

The digital signal series renders data as step functions with no interpolation between points. Ideal for digital logic signals, state machines, and discrete event data. Three variants: digital line, digital mountain, and digital band.

---

## Quick Start

=== "Python"

    `python
    import chartexa as cx

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0]

    chart = cx.Chart().digital_line(x, y, stroke="#A6E3A1", thickness=2)
    chart.save("digital.png")
    `

---

## Variants

### Digital Line

`python
chart.digital_line(x, y, stroke="#A6E3A1")
`

Renders horizontal/vertical steps between data points.

### Digital Mountain

`python
chart.digital_mountain(x, y, stroke="#89B4FA", fill="#89B4FA")
`

Step function with filled area below.

### Digital Band

`python
chart.digital_band(x, y_upper, y_lower, fill="#CBA6F7")
`

Step function with filled area between two boundaries.

---

## When to Use

- Logic analyser traces
- GPIO pin state visualisation
- Protocol decoding (SPI, I2C, UART)
- State machine transitions

---

## Related

- [Line Series](line-series.md) -- interpolated lines
- [Oscilloscope](../instruments/oscilloscope.md) -- real-time waveform display

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
