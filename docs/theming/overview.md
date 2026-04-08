---
title: "Theming Overview"
section: "theming"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Theming Overview

## Summary

Chartexa includes 15 built-in theme presets and supports fully custom themes. Themes control background colour, axis styles, grid lines, series colour palette, and text appearance.

---

## Quick Start

```python
import chartexa as cx

chart = cx.Chart().line([1, 2, 3], [10, 20, 15]).theme("catppuccin_mocha")
chart.save("themed.png")
```

---

## Available Presets

| Preset | Description |
|---|---|
| `dark` | Default dark theme |
| `light` | Light theme with dark text |
| `catppuccin_mocha` | Catppuccin Mocha (dark, warm) |
| `catppuccin_latte` | Catppuccin Latte (light) |
| `catppuccin_frappe` | Catppuccin Frappe (mid-dark) |
| `catppuccin_macchiato` | Catppuccin Macchiato (dark) |
| `github_dark` | GitHub Dark theme |
| `github_light` | GitHub Light theme |
| `dracula` | Dracula theme |
| `nord` | Nord theme |
| `solarized_dark` | Solarized Dark |
| `solarized_light` | Solarized Light |
| `minimal` | Minimal, clean design |
| `scientific` | Publication-ready, serif fonts |

---

## Applying Themes

=== "Python"

    ```python
    # By name
    chart.theme("dracula")

    # By ChartTheme object
    from chartexa import ChartTheme
    theme = ChartTheme(
        background="#1E1E2E",
        surface="#313244",
        text="#CDD6F4",
        grid="#45475A",
    )
    chart.theme(theme)
    ```

=== "C#"

    ```csharp
    var theme = ThemeManager.GetTheme("dracula");
    surface.ApplyTheme(theme);
    ```

---

## Related

- [Custom Themes](custom-themes.md) -- create your own theme
- [Theme Engine](theme-engine.md) -- how the theme system works

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
