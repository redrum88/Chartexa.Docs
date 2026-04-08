---
title: "Rendering Overview"
section: "rendering"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Rendering Overview

## Summary

Chartexa supports four rendering backends: DirectX 12, Skia, WPF, and Web (HTML/Canvas). The renderer transforms chart data into visual output.

---

## Backend Comparison

| Backend | Platform | GPU | Best For |
|---|---|---|---|
| DirectX 12 | Windows 10+ | Yes | Maximum performance, real-time |
| Skia | Cross-platform | No | Server-side, CI/CD, CLI tools |
| WPF | Windows | Partial | Desktop XAML applications |
| Web | Any browser | No | Interactive HTML, Jupyter |

See [Choosing a Renderer](../getting-started/choosing-a-renderer.md) for detailed guidance.

---

## Related

- [DirectX 12 Setup](directx12/setup.md)
- [Skia Setup](skia/setup.md)
- [WPF Setup](wpf/setup.md)
- [Web JSON Export](web/json-export.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
