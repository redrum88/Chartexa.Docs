---
title: "Tick Providers"
section: "axes"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Tick Providers

## Summary

Tick providers determine where tick marks and grid lines are placed along an axis. The default tick provider auto-selects nice intervals based on the visible range.

---

## Concepts

Chartexa uses a two-stage tick system:

1. **Major ticks** -- primary divisions with labels and grid lines
2. **Minor ticks** -- subdivisions between major ticks (typically 4-5 per major tick)

The default `AutoTickProvider` selects intervals that produce readable label values (multiples of 1, 2, 5, 10, etc.).

---

## Custom Tick Intervals

=== "C#"

    ```csharp
    var axis = new NumericAxis
    {
        MajorDelta = 10,    // Major tick every 10 units
        MinorDelta = 2,     // Minor tick every 2 units
        AutoTicks = false   // Disable auto-selection
    };
    ```

---

## Related

- [Label Providers](label-providers.md)
- [Axis Styling](axis-styling.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
