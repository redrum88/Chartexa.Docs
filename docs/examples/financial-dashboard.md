---
title: "Financial Dashboard"
section: "examples"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Financial Dashboard

## Summary

A multi-panel financial dashboard with candlestick chart, volume bars, and Bollinger Bands overlay.

---

## Python

```python
import chartexa as cx
from chartexa import subplots, bollinger_bands, moving_average
import random

# Generate synthetic OHLC data
random.seed(42)
n = 100
price = 100.0
x, opens, highs, lows, closes, volumes = [], [], [], [], [], []

for i in range(n):
    o = price
    c = o + random.gauss(0, 2)
    h = max(o, c) + abs(random.gauss(0, 1))
    l = min(o, c) - abs(random.gauss(0, 1))
    x.append(i)
    opens.append(o)
    highs.append(h)
    lows.append(l)
    closes.append(c)
    volumes.append(random.randint(10000, 50000))
    price = c

# Calculate indicators
ma = moving_average(closes, window=20)
upper, middle, lower = bollinger_bands(closes, window=20, std_dev=2)

# Create dashboard
fig = subplots(rows=2, cols=1, width=1400, height=900)

# Top panel: Candlestick + Bollinger Bands
fig[0, 0].candlestick(
    x, opens, highs, lows, closes,
    bullish_fill="#A6E3A1", bearish_fill="#F38BA8",
).line(
    x[19:], upper, stroke="#F9E2AF", thickness=1, dash="dot", label="Upper BB"
).line(
    x[19:], lower, stroke="#F9E2AF", thickness=1, dash="dot", label="Lower BB"
).line(
    x[19:], ma, stroke="#89B4FA", thickness=1.5, label="MA(20)"
).title("Price Action").legend()

# Bottom panel: Volume bars
fig[1, 0].column(
    x, volumes, fill="#94E2D5"
).title("Volume").y_axis(title="Volume")

fig.save("financial_dashboard.png")
```

---

## Related

- [Candlestick Series](../chart-types/2d/candlestick-series.md)
- [Data Transforms](../data/data-sources/financial/technical-indicators.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
