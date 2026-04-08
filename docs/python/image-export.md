---
title: "Image Export"
section: "python"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Image Export

## Summary

Chartexa charts can be exported to PNG, JPEG, and interactive HTML. The Python wrapper renders charts server-side using the .NET engine, so no display server or browser is needed for image export.

---

## PNG Export

```python
import chartexa as cx

chart = cx.Chart().line([1, 2, 3, 4], [10, 20, 15, 30])

# Save to file
chart.save("chart.png")

# Get raw bytes (for web APIs, email attachments, etc.)
png_bytes = chart.to_bytes()
```

PNG is the default format. It produces lossless images with transparency support.

---

## JPEG Export

```python
# Save with default quality (90)
chart.save_jpeg("chart.jpg")

# Lower quality for smaller file size
chart.save_jpeg("chart_small.jpg", quality=60)

# Get JPEG bytes
jpeg_bytes = chart.to_bytes(fmt="jpeg", quality=85)
```

---

## HTML Export

### Self-Contained HTML Page

```python
# Save as a complete HTML file
chart.save_html("chart.html")

# With interactivity
chart = (
    cx.Chart()
    .line([1, 2, 3, 4], [10, 20, 15, 30])
    .zoom_pan()
    .crosshair()
    .tooltips()
)
chart.save_html("interactive.html", title="My Dashboard")
```

### HTML String

```python
# Get HTML as a string (for web frameworks)
html = chart.to_html(title="My Chart", interactive=True)

# Embeddable div snippet (no <html>/<head>/<body> wrapper)
div_html = chart.to_html_div()
```

### HTML Options

| Parameter | Type | Default | Description |
|---|---|---|---|
| `title` | str | `"Chartexa Chart"` | HTML page title |
| `interactive` | bool | `True` | Enable zoom/pan/touch |
| `crosshair` | bool | `None` | Show crosshair (auto-detected from modifiers) |
| `container_width` | str | `None` | CSS width (e.g. `"100%"`, `"600px"`) |
| `container_height` | str | `None` | CSS height |

---

## Web Framework Integration

### Flask

```python
from flask import Flask, Response
import chartexa as cx

app = Flask(__name__)

@app.route("/chart.png")
def chart_png():
    chart = cx.Chart().line([1, 2, 3], [10, 20, 15])
    return Response(chart.to_bytes(), mimetype="image/png")

@app.route("/chart")
def chart_html():
    chart = cx.Chart().line([1, 2, 3], [10, 20, 15]).zoom_pan()
    return chart.to_html()
```

### FastAPI

```python
from fastapi import FastAPI
from fastapi.responses import Response
import chartexa as cx

app = FastAPI()

@app.get("/chart.png")
async def chart_png():
    chart = cx.Chart().line([1, 2, 3], [10, 20, 15])
    return Response(content=chart.to_bytes(), media_type="image/png")
```

---

## Resolution and Size

```python
# Set dimensions at construction
chart = cx.Chart(width=1920, height=1080)

# Or modify after creation
chart.width = 2560
chart.height = 1440
chart.save("highres.png")
```

---

## Related

- [Chart Builder API](chart-builder.md) -- full `Chart` class reference
- [Jupyter Integration](jupyter.md) -- inline notebook rendering
- [Web JSON Export](../rendering/web/json-export.md) -- JSON data export

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
