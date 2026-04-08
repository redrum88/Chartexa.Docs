---
title: "Large Datasets"
section: "performance"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Large Datasets

## Summary

Chartexa can render millions of data points per series. This page covers strategies for working with large datasets efficiently in Python.

---

## Downsampling Algorithms

### LTTB (Largest Triangle Three Buckets)

The gold standard for visual downsampling. Preserves the visual shape of the data while reducing point count:

```python
from chartexa import lttb_downsample

# Reduce 1 million points to 5000
x_ds, y_ds = lttb_downsample(x, y, target_points=5000)
chart = cx.Chart().line(x_ds, y_ds)
```

### MinMax

Preserves exact peaks and valleys. Each bucket outputs the min and max values:

```python
from chartexa import minmax_downsample

x_ds, y_ds = minmax_downsample(x, y, target_points=5000)
```

### Auto Downsample

Automatically selects the best algorithm:

```python
from chartexa import auto_downsample

x_ds, y_ds = auto_downsample(x, y)
```

---

## FIFO Buffer for Streaming Data

For real-time charts with a sliding window:

```python
from chartexa import FifoBuffer

buffer = FifoBuffer(capacity=50000)

# In a data callback
def on_data(x, y):
    buffer.append(x, y)
    # Oldest points are automatically dropped when capacity is exceeded
```

---

## Related

- [Performance Optimization](optimization.md)
- [GPU Acceleration](gpu-acceleration.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
