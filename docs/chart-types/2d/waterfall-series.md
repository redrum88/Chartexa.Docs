---
title: "Waterfall Series"
section: "chart-types/2d"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Waterfall Series

## Summary

The waterfall series shows how an initial value is affected by a series of positive and negative changes. Commonly used in financial reporting to show revenue bridges and variance analysis.

---

## Quick Start

=== "Python"

    ```python
    import chartexa as cx

    chart = cx.Chart().column(
        [0, 1, 2, 3, 4, 5],
        [100, 20, -15, 30, -10, 125],
        fill="#89B4FA",
        label="P&L Waterfall",
    )
    chart.save("waterfall.png")
    ```

---

## When to Use

- Financial bridge charts (revenue waterfall)
- Variance analysis
- Step-by-step value accumulation

---

## Related

- [Column Series](column-series.md) -- basic vertical bars
- [Stacked Column](stacked-column.md) -- layered bars

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
