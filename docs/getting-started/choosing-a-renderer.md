---
title: "Choosing a Renderer"
section: "getting-started"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Choosing a Renderer

## Summary

Chartexa supports multiple rendering backends. Select the one that matches your deployment target and performance requirements.

---

## Renderer Comparison

| Renderer | Platform | GPU Accel | Best For |
|---|---|---|---|
| **DirectX 12** | Windows 10+ | Yes | Real-time dashboards, millions of points, desktop apps |
| **Skia** | Windows, Linux, macOS | CPU | Cross-platform CLI tools, server-side rendering, CI pipelines |
| **WPF** | Windows (desktop) | Partial | XAML-based desktop applications with data binding |
| **Web (HTML/Canvas)** | Any browser | N/A | Interactive HTML exports, Jupyter notebooks |

---

## DirectX 12

The DirectX 12 renderer is the highest-performance option. It uses GPU compute shaders for data processing and SDF (Signed Distance Field) text rendering for crisp labels at any resolution.

=== "C#"

    `csharp
    using Chartexa.Rendering.DirectX12;

    var renderer = new Dx12ChartRenderer();
    surface.Renderer = renderer;
    `

=== "Python"

    `python
    # The Python wrapper auto-selects the best available renderer.
    # DirectX 12 is used on Windows when a compatible GPU is detected.
    import chartexa as cx
    chart = cx.Chart()  # Auto-selects DX12 on Windows
    `

!!! warning "Windows Only"
    DirectX 12 requires Windows 10 version 1903 or later and a DirectX 12 capable GPU.

---

## Skia

Skia is a cross-platform 2D graphics library. It runs on Windows, Linux, and macOS without GPU requirements.

=== "C#"

    `csharp
    using Chartexa.Rendering.Skia;

    var renderer = new SkiaChartRenderer();
    surface.Renderer = renderer;
    `

=== "Python"

    `python
    # Skia is used automatically on Linux/macOS or when no GPU is available.
    import chartexa as cx
    chart = cx.Chart()  # Falls back to Skia on Linux
    `

---

## WPF

The WPF renderer integrates with XAML data binding, styles, and the WPF visual tree. Use it for desktop applications built with Windows Presentation Foundation.

`csharp
using Chartexa.WPF;

// In XAML: <cx:ChartexaChart x:Name="chart" />
// The WPF control handles rendering internally.
`

---

## Web (HTML/Canvas)

The web renderer exports charts as self-contained HTML files with Canvas-based rendering and optional interactivity (zoom, pan, crosshair, tooltips).

`python
import chartexa as cx

chart = (
    cx.Chart()
    .line([1, 2, 3], [10, 20, 15])
    .zoom_pan()
    .crosshair()
    .tooltips()
)

chart.save_html("interactive.html")
`

---

## Decision Guide

`mermaid
graph TD
    A[What platform?] -->|Windows desktop| B{Need real-time?}
    A -->|Linux / macOS| C[Skia]
    A -->|Web / Jupyter| D[Web HTML/Canvas]
    B -->|Yes, millions of pts| E[DirectX 12]
    B -->|No, static charts| F{WPF app?}
    F -->|Yes| G[WPF]
    F -->|No| C
`

---

## Related

- [DirectX 12 Setup](../rendering/directx12/setup.md) -- detailed DX12 configuration
- [Skia Setup](../rendering/skia/setup.md) -- Skia renderer setup
- [GPU Acceleration](../performance/gpu-acceleration.md) -- performance tuning

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
