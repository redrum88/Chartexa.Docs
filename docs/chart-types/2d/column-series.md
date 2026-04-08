---
title: "Column Series"
section: "chart-types/2d"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Column Series

## Summary

The column series renders vertical bars. Supports grouped and baseline-offset bars. `chart.bar()` is an alias for `chart.column()`. Uses `FastColumnRenderableSeries` in the .NET engine.

---

## Quick Start

=== "Python"

    `python
    import chartexa as cx

    chart = cx.Chart().column(
        [0, 1, 2, 3, 4],
        [50, 80, 45, 90, 65],
        fill="#A6E3A1",
    )
    chart.save("columns.png")
    `

=== "C#"

    `csharp
    var ds = new XyDataSeries();
    ds.Append(new double[] { 0, 1, 2, 3, 4 },
              new double[] { 50, 80, 45, 90, 65 });

    var rs = new FastColumnRenderableSeries
    {
        DataSeries = ds,
        Fill = new ChartColor(166, 227, 161),
        BarWidthFraction = 0.7
    };
    surface.RenderableSeries.Add(rs);
    `

---

## Configuration

| Property | Type | Default | Description |
|---|---|---|---|
| `fill` | str / tuple | auto | Bar fill colour |
| `stroke` | str / tuple | `None` | Bar outline colour |
| `thickness` | float | `1.0` | Outline stroke width |
| `bar_width` | float | `0.7` | Fraction of available space (0.0 -- 1.0) |
| `baseline` | float | `0.0` | Y-value for the bar baseline |
| `group_index` | int | `0` | Index within grouped bars |
| `group_count` | int | `1` | Total number of groups |

---

## Examples

### Grouped Bars

`python
import chartexa as cx

categories = [0, 1, 2, 3]

chart = (
    cx.Chart(width=1000, height=500)
    .column(categories, [50, 80, 45, 90], fill="#F38BA8", group_index=0, group_count=3, label="Q1")
    .column(categories, [60, 70, 55, 85], fill="#89B4FA", group_index=1, group_count=3, label="Q2")
    .column(categories, [70, 65, 60, 95], fill="#A6E3A1", group_index=2, group_count=3, label="Q3")
    .x_axis(type="category", labels=["Product A", "Product B", "Product C", "Product D"])
    .y_axis(title="Revenue (k)")
    .legend()
)
chart.save("grouped_bars.png")
`

### Negative Values

`python
chart = cx.Chart().column(
    [0, 1, 2, 3, 4],
    [20, -15, 30, -10, 25],
    fill="#CBA6F7",
    baseline=0,
)
chart.save("negative_bars.png")
`

---

## When to Use

- Categorical comparisons (products, regions, time periods)
- Grouped comparisons across categories
- Positive/negative value distribution

---

## Related

- [Stacked Column](stacked-column.md) -- stacked bar chart
- [Mountain Series](mountain-series.md) -- continuous area chart

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
