---
title: "Chart Builder API"
section: "python"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Chart Builder API

## Summary

The `Chart` class is the primary entry point for creating charts in Python. It uses a fluent (method-chaining) API where every configuration method returns `self`.

---

## Constructor

`python
cx.Chart(width: int = 800, height: int = 600)
`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `width` | `int` | `800` | Chart width in pixels |
| `height` | `int` | `600` | Chart height in pixels |

---

## Series Methods

All series methods return `Chart` for chaining. Common parameters:

| Parameter | Description |
|---|---|
| `stroke` | Line/outline colour (hex string or RGB tuple) |
| `fill` | Fill colour |
| `thickness` | Stroke thickness in pixels |
| `label` | Series name (shown in legend and tooltips) |
| `x_axis_id` | Bind to a specific X axis (multi-axis charts) |
| `y_axis_id` | Bind to a specific Y axis (multi-axis charts) |

### `chart.line(x, y, **kwargs)`

Add a fast line series.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `x` | sequence | *required* | X values |
| `y` | sequence | *required* | Y values |
| `stroke` | str / tuple | `None` | Line colour |
| `thickness` | float | `1.5` | Line width |
| `dash` | str | `None` | `"solid"`, `"dash"`, `"dot"`, `"dash_dot"`, `"dash_dot_dot"` |
| `opacity` | float | `1.0` | 0.0 -- 1.0 |
| `spline` | bool | `False` | Catmull-Rom spline interpolation |
| `spline_segments` | int | `16` | Segments per data point pair |

### `chart.scatter(x, y, **kwargs)`

Add a scatter (XY) series.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `marker` | str | `"circle"` | `"circle"`, `"square"`, `"triangle"`, `"cross"`, `"diamond"`, `"plus"`, `"star"` |
| `size` | float | `8.0` | Marker diameter (px) |
| `fill` | str / tuple | `None` | Marker fill colour |
| `stroke` | str / tuple | `None` | Marker outline colour |
| `stroke_thickness` | float | `1.0` | Outline width |
| `opacity` | float | `1.0` | 0.0 -- 1.0 |

### `chart.column(x, y, **kwargs)` / `chart.bar(x, y, **kwargs)`

Add a column (vertical bar) series. `bar()` is an alias for `column()`.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `fill` | str / tuple | `None` | Bar fill colour |
| `bar_width` | float | `0.7` | Fraction of available space (0.0 -- 1.0) |
| `baseline` | float | `0.0` | Y-value baseline |
| `group_index` | int | `0` | Index within grouped bars |
| `group_count` | int | `1` | Total groups |

### `chart.mountain(x, y, **kwargs)`

Add a mountain (area) series.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `stroke` | str / tuple | `None` | Top-edge line colour |
| `fill` | str / tuple | `None` | Area fill colour |
| `thickness` | float | `1.5` | Stroke width |
| `baseline` | float | `0.0` | Where the fill meets the axis |

### `chart.candlestick(x, open, high, low, close, **kwargs)`

Add a candlestick (OHLC) series.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `bullish_fill` | str / tuple | `None` | Up-candle fill |
| `bearish_fill` | str / tuple | `None` | Down-candle fill |
| `bullish_stroke` | str / tuple | `None` | Up-candle outline |
| `bearish_stroke` | str / tuple | `None` | Down-candle outline |
| `thickness` | float | `1.0` | Wick stroke width |
| `bar_width` | float | `0.7` | Candle width fraction |

### `chart.band(x, y_upper, y_lower, **kwargs)`

Add a band (fill-between) series.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `stroke` | str / tuple | `None` | Boundary line colour |
| `fill` | str / tuple | `None` | Fill colour |
| `thickness` | float | `1.0` | Boundary line width |

### `chart.heatmap(data, **kwargs)`

Add a 2D heatmap.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `data` | 2D sequence | *required* | Row-major values `data[row][col]` |
| `palette` | str | `"thermal"` | `"thermal"`, `"rainbow"`, `"viridis"`, `"inferno"`, `"diverging"` |
| `min_value` | float | `0.0` | Colour scale minimum |
| `max_value` | float | `1.0` | Colour scale maximum |
| `show_grid` | bool | `True` | Draw cell gridlines |

### `chart.bubble(x, y, sizes, **kwargs)`

Add a bubble series.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `sizes` | sequence | *required* | Size values per bubble |
| `min_size` | float | `4.0` | Minimum rendered radius (px) |
| `max_size` | float | `40.0` | Maximum rendered radius (px) |

### `chart.pie(values, **kwargs)` / `chart.donut(values, **kwargs)`

Add a pie or donut chart.

| Parameter | Type | Default | Description |
|---|---|---|---|
| `values` | sequence | *required* | Segment values |
| `labels` | sequence | `None` | Segment labels |
| `colors` | sequence | `None` | Per-segment colours |
| `explode` | sequence | `None` | Indices to pull out |
| `start_angle` | float | `0.0` | Starting angle (degrees) |
| `show_percentage` | bool | `True` | Show % labels |
| `hole_radius` | float | `0.55` | Inner radius (donut only) |

### `chart.stacked_column(x, layers, **kwargs)`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `layers` | sequence of sequences | *required* | Y-values per layer |
| `colors` | sequence | `None` | Per-layer colours |
| `labels` | sequence | `None` | Per-layer labels |
| `stacked_100` | bool | `False` | Normalise to 100% |

### `chart.error_bar(x, y, **kwargs)`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `error_y` | sequence | `None` | Symmetric Y error |
| `error_high` | sequence | `None` | Upper error bound |
| `error_low` | sequence | `None` | Lower error bound |
| `error_x` | sequence | `None` | X error |
| `cap_width` | float | `6.0` | Error bar cap width (px) |

### `chart.box_plot(**kwargs)`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `raw_data` | sequence of sequences | `None` | Raw data (auto-computes quartiles) |
| `x_positions` | sequence | `None` | X positions for each box |
| `minimums` ... `maximums` | sequence | `None` | Pre-computed quartile values |
| `box_width` | float | `0.6` | Box width fraction |
| `outlier_threshold` | float | `1.5` | IQR multiplier for outliers |

### `chart.polar(theta, r, **kwargs)`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `theta` | sequence | *required* | Angle values |
| `r` | sequence | *required* | Radius values |
| `degrees` | bool | `True` | Interpret theta as degrees (vs radians) |
| `max_radius` | float | `0.0` | Fixed max radius (0 = auto) |

### `chart.radar(datasets, **kwargs)`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `datasets` | seq of seq | *required* | One sequence per dataset |
| `category_labels` | sequence | `None` | Spoke labels |
| `dataset_labels` | sequence | `None` | Legend labels |
| `max_value` | float | `0.0` | Fixed max (0 = auto) |

### Additional Series

| Method | Description |
|---|---|
| `chart.impulse()` | Stem / impulse plot |
| `chart.fan()` | Confidence fan bands |
| `chart.gantt()` | Gantt chart |
| `chart.digital_line()` | Step-function line |
| `chart.digital_mountain()` | Step-function area |
| `chart.digital_band()` | Step-function band |

---

## Axis Methods

### `chart.x_axis(**kwargs)` / `chart.y_axis(**kwargs)`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `type` | str | `"numeric"` | `"numeric"`, `"datetime"`, `"category"`, `"log"` |
| `id` | str | `"DefaultXAxis"` | Axis identifier |
| `alignment` | str | `"bottom"` / `"left"` | `"top"`, `"bottom"`, `"left"`, `"right"` |
| `title` | str | `None` | Axis label text |
| `range` | tuple | `None` | Fixed visible range `(min, max)` |
| `grow_by` | float | `0.05` | Extra padding fraction |
| `label_format` | str | `None` | Numeric format string |
| `date_format` | str | `None` | Date format string |
| `labels` | sequence | `None` | Category labels (required for `"category"` type) |
| `label_rotation` | float | `0.0` | Label rotation (degrees) |
| `log_base` | float | `10.0` | Logarithm base (for `"log"` type) |
| `grid_visible` | bool | `True` | Show grid lines |
| `grid_color` | str / tuple | `None` | Grid line colour |
| `grid_thickness` | float | `1.0` | Grid line width |
| `grid_dash` | str | `None` | Grid line dash style |

### `chart.secondary_x_axis(**kwargs)` / `chart.secondary_y_axis(**kwargs)`

Convenience methods that default to `alignment="top"` / `"right"` and `id="SecondaryXAxis"` / `"SecondaryYAxis"`. Accept the same parameters as the primary axis methods.

---

## Appearance Methods

### `chart.background(color)`
Set the chart background colour.

### `chart.theme(theme)`
Apply a theme by name or `ChartTheme` object.

### `chart.title(text, *, font_size=18.0, font_family=None, color=None)`
Set the chart title.

### `chart.subtitle(text, *, font_size=13.0, font_family=None, color=None)`
Set the subtitle (rendered below the title).

### `chart.watermark(text, *, opacity=0.1, rotation=-30.0, font_size=48.0)`
Add a watermark to the chart centre.

---

## Annotation Methods

### `chart.horizontal_line(y, *, color="#FF6432", thickness=1.0, dash="dash", label=None)`
### `chart.vertical_line(x, *, color="#FF6432", thickness=1.0, dash="dash", label=None)`
### `chart.line_annotation(x1, y1, x2, y2, *, color="#FF6432", thickness=1.0, dash=None)`
### `chart.box_annotation(x1, y1, x2, y2, *, fill=None, stroke="#FF6432", thickness=1.0)`
### `chart.annotation(x, y, text, *, color="#E6E6E6", font_size=12.0, rotation=0.0)`
### `chart.event_marker(x, *, text=None, color="#FF6432", thickness=1.5)`

---

## Legend

### `chart.legend(entries=None, *, position="top_right", orientation="vertical", font_size=11.0)`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `entries` | sequence | `None` | `(label, color)` or `(label, color, marker)` tuples. `None` uses series labels. |
| `position` | str | `"top_right"` | `"top_right"`, `"top_left"`, `"bottom_left"`, `"bottom_right"`, `"top_center"`, `"right_center"` |
| `orientation` | str | `"vertical"` | `"vertical"` or `"horizontal"` |

---

## Interactivity Methods

### `chart.zoom_pan(*, zoom_in_factor=0.8, zoom_out_factor=1.25, x_axis_only=False, y_axis_only=False)`
### `chart.rubber_band_zoom(*, min_drag_px=5)`
### `chart.crosshair(*, snap_to_data=False, show_x_line=True, show_y_line=True, color=None, dash_style="dash")`
### `chart.tooltips(*, threshold_px=15.0, mode="single", show_series_name=True, font_size=12.0)`
### `chart.selection(*, mode="data_point", multi_select=True, selection_color="#FF6600")`
### `chart.modifier(mod)`

---

## Output Methods

### `chart.save(path, *, dpi=96)`
Render to PNG file.

### `chart.save_jpeg(path, *, quality=90)`
Render to JPEG file.

### `chart.to_bytes(*, fmt="png", quality=90)`
Return image bytes. `fmt` is `"png"` or `"jpeg"`.

### `chart.show()`
Display inline (Jupyter) or open in browser (terminal).

### `chart.to_html(*, title="Chartexa Chart", interactive=True, crosshair=None)`
Return a self-contained HTML page string.

### `chart.to_html_div(*, interactive=True, crosshair=None)`
Return an embeddable `<div>` snippet.

### `chart.save_html(path, *, title="Chartexa Chart", interactive=True)`
Save as a self-contained HTML file.

---

## Properties

| Property | Type | Access | Description |
|---|---|---|---|
| `chart.width` | int | read/write | Chart width in pixels |
| `chart.height` | int | read/write | Chart height in pixels |
| `chart.modifiers` | list | read-only | Attached modifier instances |

---

## Context Manager

`Chart` supports the context manager protocol for resource cleanup:

`python
with cx.Chart() as chart:
    chart.line(x, y).save("out.png")
# .NET resources released here
`

---

## Batch Updates

`python
with chart.begin_update():
    chart.line(x1, y1)
    chart.line(x2, y2)
    # Single render at exit
`

---

## Related

- [Getting Started](getting-started.md) -- quickstart overview
- [Image Export](image-export.md) -- export format details
- [Jupyter Integration](jupyter.md) -- notebook rendering

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
