---
title: "DateTime Axis"
section: "axes"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# DateTime Axis

## Summary

The DateTime axis formats tick labels as dates and times. Accepts Unix timestamps, Python `datetime` objects, or numeric epoch values as X data.

---

## Quick Start

=== "Python"

    `python
    import chartexa as cx
    from datetime import datetime, timedelta

    base = datetime(2026, 1, 1)
    x = [(base + timedelta(days=i)).timestamp() for i in range(30)]
    y = [20 + i * 0.5 for i in range(30)]

    chart = (
        cx.Chart()
        .line(x, y, stroke="#89B4FA")
        .x_axis(type="datetime", title="Date", date_format="MMM dd")
        .y_axis(title="Temperature (C)")
    )
    chart.save("datetime_axis.png")
    `

=== "C#"

    `csharp
    var xAxis = new DateTimeAxis
    {
        AxisTitle = "Date",
        DateFormat = "MMM dd"
    };
    `

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `date_format` | str | `None` | .NET date format string (e.g. `"yyyy-MM-dd"`, `"HH:mm:ss"`) |

---

## Related

- [Axes Overview](overview.md)
- [Numeric Axis](numeric-axis.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
