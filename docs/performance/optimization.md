---
title: "Performance Optimization"
section: "performance"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Performance Optimization

## Summary

Chartexa is designed for high-performance charting. The .NET engine handles rendering with GPU acceleration (DirectX 12) and optimised data structures. The Python wrapper provides utilities for efficient data transfer and downsampling.

---

## Key Strategies

### 1. Downsampling

Reduce the number of rendered points while preserving visual shape:

```python
from chartexa import lttb_downsample, minmax_downsample, auto_downsample

# LTTB (Largest Triangle Three Buckets) -- best for line charts
x_ds, y_ds = lttb_downsample(x, y, target_points=5000)

# MinMax -- preserves peaks and valleys
x_ds, y_ds = minmax_downsample(x, y, target_points=5000)

# Auto -- selects the best algorithm based on chart type
x_ds, y_ds = auto_downsample(x, y)
```

### 2. Batch Updates

Defer rendering until all series are added:

```python
with chart.begin_update():
    for i in range(100):
        chart.line(x[i], y[i])
    # Single render at exit
```

### 3. Fast Append

Use `fast_append_xy()` for efficient data transfer to .NET arrays:

```python
from chartexa import fast_append_xy

fast_append_xy(data_series, x_numpy_array, y_numpy_array)
```

### 4. FIFO Buffer

For real-time scrolling charts with fixed-size windows:

```python
from chartexa import FifoBuffer

buffer = FifoBuffer(capacity=10000)
buffer.append(x_value, y_value)
```

### 5. NumPy Interop

Use numpy arrays for zero-copy data transfer:

```python
from chartexa import numpy_to_net_array, net_array_to_numpy

net_arr = numpy_to_net_array(numpy_array)
numpy_arr = net_array_to_numpy(net_array)
```

---

## Performance Guidelines

| Data Size | Strategy |
|---|---|
| < 10,000 points | No optimisation needed |
| 10,000 -- 100,000 | Consider downsampling |
| 100,000 -- 1,000,000 | Use LTTB downsampling + batch updates |
| > 1,000,000 | Use DirectX 12 renderer + LTTB + FIFO buffer |

---

## Related

- [GPU Acceleration](gpu-acceleration.md)
- [Large Datasets](large-datasets.md)
- [Benchmarks](benchmarks.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
