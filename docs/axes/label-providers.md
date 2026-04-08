---
title: "Label Providers"
section: "axes"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Label Providers

## Summary

Label providers control how tick values are formatted as text. By default, numeric axes use standard number formatting and date axes use date/time formatting.

---

## Built-in Formatting

=== "Python"

    ```python
    # Numeric format
    chart.x_axis(label_format="0.00")       # 2 decimal places
    chart.x_axis(label_format="#,##0")       # Thousands separator
    chart.x_axis(label_format="0.0%")       # Percentage

    # Date format
    chart.x_axis(type="datetime", date_format="yyyy-MM-dd")
    chart.x_axis(type="datetime", date_format="HH:mm:ss")
    ```

=== "C#"

    ```csharp
    var axis = new NumericAxis { LabelFormat = "#,##0.00" };
    var dateAxis = new DateTimeAxis { DateFormat = "dd MMM yyyy" };
    ```

---

## Related

- [Tick Providers](tick-providers.md)
- [Axes Overview](overview.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
