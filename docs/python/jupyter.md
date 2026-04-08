---
title: "Jupyter Integration"
section: "python"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Jupyter Integration

## Summary

Chartexa integrates with Jupyter Notebook, JupyterLab, VS Code notebooks, and Google Colab. Charts render inline automatically when returned from a cell.

---

## Quick Start

```python
import chartexa as cx

# Return a Chart from the last expression -- it renders inline
cx.Chart().line([1, 2, 3, 4, 5], [10, 30, 20, 40, 25])
```

No `.show()` call needed. Chartexa registers `_repr_html_` and `_repr_png_` methods that IPython uses automatically.

---

## How It Works

On import, `chartexa` calls `auto_configure()` which:

1. Detects the notebook environment (Jupyter, VS Code, Colab, terminal)
2. Registers MIME type renderers for `text/html` and `image/png`
3. Loads notebook-specific CSS for dark theme compatibility

The detection is transparent -- no manual configuration needed.

---

## Environment Detection

```python
from chartexa import detect_environment, is_notebook, is_ipython

env = detect_environment()
# Returns: NotebookEnvironment.JUPYTER | VS_CODE | COLAB | TERMINAL

if is_notebook():
    print("Running in a notebook")
```

---

## Explicit Display

```python
from chartexa import display_chart

chart = cx.Chart().line([1, 2, 3], [10, 20, 15])
display_chart(chart)  # Force display mid-cell
```

---

## Interactive Charts in Notebooks

Add interactivity modifiers for zoom, pan, and tooltips in the inline HTML:

```python
chart = (
    cx.Chart(width=900, height=400)
    .line([1, 2, 3, 4, 5], [10, 30, 20, 40, 25], label="Sensor A")
    .line([1, 2, 3, 4, 5], [15, 25, 35, 20, 30], label="Sensor B")
    .zoom_pan()
    .crosshair()
    .tooltips()
    .legend()
)

chart  # Interactive HTML renders inline
```

---

## Google Colab

Colab requires a one-time setup call:

```python
import chartexa as cx

cx.setup_colab()  # Installs .NET runtime, configures paths

chart = cx.Chart().line([1, 2, 3], [10, 20, 15])
chart
```

### Colab Runtime Info

```python
from chartexa import detect_colab_runtime, colab_runtime_info

runtime = detect_colab_runtime()  # ColabRuntime.STANDARD | TPU | GPU
info = colab_runtime_info()       # dict with hardware details
```

---

## Live Charts (ChartWidget)

For real-time updating charts in notebooks:

```python
from chartexa import ChartWidget

widget = ChartWidget(width=800, height=400)
widget.display()

# Update data dynamically
import time
for i in range(100):
    widget.update_line([i], [math.sin(i * 0.1)])
    time.sleep(0.05)
```

---

## NotebookLiveChart

For streaming data sources:

```python
from chartexa import NotebookLiveChart

live = NotebookLiveChart(
    width=1000, height=400,
    max_points=500,
    update_interval_ms=50,
)
live.start()

# Push data from another thread or callback
live.append(x_value, y_value)
```

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| Chart not rendering | Restart kernel after `pip install chartexa` |
| Blank output in VS Code | Update the Jupyter extension to latest version |
| Colab import error | Run `cx.setup_colab()` first |
| Low resolution | Set `width` and `height` on the `Chart` constructor |

---

## Related

- [Image Export](image-export.md) -- save charts to files
- [Chart Builder API](chart-builder.md) -- full API reference
- [Getting Started](getting-started.md) -- Python quickstart

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
