---
title: "Theme Engine"
section: "theming"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Theme Engine

## Summary

The theme engine resolves theme names to `ChartTheme` objects and applies theme properties to all chart elements. Themes are resolved via `resolve_theme()` which accepts either a string preset name or a `ChartTheme` instance.

---

## Resolution Order

1. If `theme` is a `ChartTheme` instance, use it directly
2. If `theme` is a string, look it up in `THEME_PRESETS`
3. If not found, return `None` (no theme applied)

---

## Preset Registry

```python
from chartexa import THEME_PRESETS

# List all available presets
for name in THEME_PRESETS:
    print(name)
```

---

## Related

- [Theming Overview](overview.md)
- [Custom Themes](custom-themes.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
