---
title: "Installation"
section: "getting-started"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Installation

## Summary

Chartexa is available as a NuGet package for .NET and a PyPI package for Python. The Python wrapper uses [pythonnet](https://github.com/pythonnet/pythonnet) to bridge into the .NET engine, so a compatible .NET runtime is required for both platforms.

---

## Prerequisites

| Requirement | .NET | Python |
|---|---|---|
| Runtime | .NET 10 SDK or later | Python 3.9+ |
| OS | Windows, Linux, macOS | Windows, Linux, macOS |
| GPU (optional) | DirectX 12 capable GPU for hardware-accelerated rendering | Not required (server-side rendering) |

---

## .NET Installation

=== "Package Manager"

    ```powershell
    Install-Package Chartexa.Core
    Install-Package Chartexa.Rendering.DirectX12   # GPU renderer
    Install-Package Chartexa.Rendering.Skia         # Cross-platform renderer
    ```

=== ".NET CLI"

    `ash
    dotnet add package Chartexa.Core
    dotnet add package Chartexa.Rendering.DirectX12
    dotnet add package Chartexa.Rendering.Skia
    ```

=== "PackageReference"

    ```xml
    <PackageReference Include="Chartexa.Core" Version="*" />
    <PackageReference Include="Chartexa.Rendering.DirectX12" Version="*" />
    ```

### Available NuGet Packages

| Package | Description |
|---|---|
| `Chartexa.Core` | Core charting engine, axes, series, annotations |
| `Chartexa.Data` | Data series, OHLC, XY data containers |
| `Chartexa.Rendering.DirectX12` | GPU-accelerated DirectX 12 renderer |
| `Chartexa.Rendering.Skia` | Cross-platform Skia renderer |
| `Chartexa.WPF` | WPF controls and data binding |
| `Chartexa.Python` | Python interop bridge (used internally by PyPI package) |

---

## Python Installation

`ash
pip install chartexa
```

This installs the `chartexa` package along with its dependencies:

| Dependency | Purpose |
|---|---|
| `pythonnet >= 3.0.3` | .NET CLR bridge |
| `clr-loader >= 0.2.6` | CLR hosting |
| `numpy` (optional) | Array interoperability |

### Verify the Installation

```python
import chartexa as cx

print(cx.__version__)  # 0.2.5

# Quick smoke test
cx.line([10, 20, 15, 30, 25]).save("test.png")
```

If the import succeeds and `test.png` appears in your working directory, the installation is complete.

!!! tip ".NET Runtime Required"
    The Python package embeds the Chartexa .NET assemblies but still needs a .NET 10+ runtime installed on the host machine. Download it from [dot.net](https://dot.net/download).

---

## Virtual Environment (Recommended)

=== "venv"

    `ash
    python -m venv .venv
    source .venv/bin/activate      # Linux / macOS
    .venv\Scripts\activate         # Windows
    pip install chartexa
    ```

=== "conda"

    `ash
    conda create -n chartexa python=3.12
    conda activate chartexa
    pip install chartexa
    ```

---

## Jupyter / VS Code Notebooks

Chartexa auto-detects notebook environments and registers MIME renderers on import. No extra configuration is needed:

```python
import chartexa as cx

# This cell renders the chart inline automatically
cx.Chart().line([1, 2, 3, 4], [10, 20, 15, 30])
```

For Google Colab, call `cx.setup_colab()` once at the top of the notebook.

---

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError: chartexa` | Package not installed | `pip install chartexa` |
| `RuntimeError: Unable to find a .NET runtime` | Missing .NET SDK/runtime | Install .NET 10+ from [dot.net](https://dot.net/download) |
| `ImportError: pythonnet` | pythonnet not installed | `pip install pythonnet>=3.0.3` |
| `DllNotFoundException` on Linux | Missing native libs | `sudo apt install libicu-dev libssl-dev` |
| Blank chart in Jupyter | Renderer not initialised | Restart kernel after install |

---

## Related

- [First Chart in Python](first-chart-python.md) -- create your first chart in 5 lines
- [First Chart in C#](first-chart-csharp.md) -- getting started with the .NET API
- [Choosing a Renderer](choosing-a-renderer.md) -- DirectX 12 vs Skia vs WPF

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
