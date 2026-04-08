# Chartexa Documentation — AI Expansion Guidelines

> This file instructs AI agents on **how to expand placeholder docs** into full,
> production-quality documentation. It is the single source of truth for style,
> structure, and content rules.

---

## 1. Project Identity

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12
renderer, designed for real-time and large-scale data visualization, with seamless
Python integration.

Use this sentence (or a close variant) as the opening positioning statement in
every top-level page. Subsection pages can omit it.

---

## 2. Audience

Write for **end users** — developers integrating Chartexa into their applications.

- ✅ How to install, configure, and use features
- ✅ Working code examples in C# and Python
- ✅ Performance characteristics and trade-offs
- ❌ Internal engine implementation details
- ❌ Class hierarchy diagrams or dependency graphs
- ❌ Developer/contributor-facing information

---

## 3. Voice & Style

| Rule | Example |
|---|---|
| Technical, concise, precise | "Append data points to the series" — not "You can easily add data" |
| No marketing language | No "blazing fast", "cutting-edge", "revolutionary" |
| Active voice | "The renderer draws…" — not "The drawing is done by…" |
| Second person for instructions | "Add a `NumericAxis` to your chart" |
| Present tense | "The modifier responds to mouse input" |
| No emoji in prose | Section headers and body text are emoji-free |

---

## 4. Page Structure

Every feature page MUST follow this structure. Sections with no content yet should
use an HTML comment placeholder (`<!-- AI: ... -->`), never blank sections.

```markdown
---
title: "Feature Name"
section: "section/path"
last_updated: "YYYY-MM-DD HH:mm UTC"
status: placeholder | draft | published
---

# Feature Name

## Summary
One paragraph: what it is, what class it maps to, why you'd use it.

---

## Installation
NuGet + PyPI install commands.

---

## Quick Start
### C#
Minimal working example (5-15 lines).

### Python
Equivalent minimal example.

---

## Concepts
- What it does
- When to use it
- Why it exists
Key mental model — 2-4 paragraphs max.

---

## Basic Usage
### C#
Detailed usage (10-30 lines) with comments.

### Python
Equivalent.

---

## Configuration
Properties / options table:

| Property | Type | Default | Description |
|----------|------|---------|-------------|

---

## Examples
2-3 real-world scenarios, each with C# and Python.

---

## Performance Notes
Backend-specific performance characteristics. Include numbers where available.

---

## When to Use
Bullet list of scenarios.

---

## Related
Links to related pages.

---

> **Last updated:** YYYY-MM-DD HH:mm UTC | **Status:** placeholder
```

---

## 5. Code Example Rules

### General
- Every feature MUST have both C# and Python examples
- Use `=== "C#"` / `=== "Python"` tabs (Material for MkDocs tabbed syntax)
- Examples must be **copy-pasteable** — include all necessary `using` / `import` statements
- Prefer real-world data over `1, 2, 3` placeholder values
- No `// ...` or `# ...` truncation — show complete examples

### C# Style
```csharp
using Chartexa.Core.Axes;
using Chartexa.Data.Series;

// Create axes
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Time (s)" };
var yAxis = new NumericAxis { Id = "Y", AxisTitle = "Amplitude" };

// Create data
var dataSeries = new XyDataSeries();
dataSeries.Append(xValues, yValues);

// Create renderable series
var lineSeries = new FastLineRenderableSeries
{
    DataSeries = dataSeries,
    StrokeColor = new ChartColor(70, 130, 180),   // Steel blue
    StrokeThickness = 2
};
```

### Python Style
```python
from chartexa import Chart

chart = (
    Chart(width=800, height=400)
    .line(x_values, y_values, stroke="#4682B4", thickness=2)
    .background("#1C1C1E")
    .save("output.png")
)
```

---

## 6. Admonition Usage

Use Material for MkDocs admonitions:

```markdown
!!! tip "Performance Tip"
    Use `DirectX12RenderContext` for datasets exceeding 100K points.

!!! warning
    The `OhlcDataSeries` requires equal-length arrays for all four channels.

!!! note
    Python requires the .NET 10 Runtime to be installed.

!!! example "Real-Time Streaming"
    ```csharp
    // streaming example
    ```
```

---

## 7. Cross-Referencing

Link to other docs pages using relative paths:

```markdown
See [Axis Ranging](../axes/axis-ranging.md) for details on AutoRange.
```

Never use absolute URLs for internal docs links.

---

## 8. Frontmatter

Every page MUST have YAML frontmatter with:

| Field | Required | Description |
|---|---|---|
| `title` | Yes | Page title (used in nav and `<title>`) |
| `section` | Yes | Section path (e.g., `chart-types/2d`) |
| `last_updated` | Yes | ISO timestamp of last content update |
| `status` | Yes | `placeholder`, `draft`, or `published` |

---

## 9. Status Workflow

| Status | Meaning |
|---|---|
| `placeholder` | Generated scaffold — section headers only, no real content |
| `draft` | AI-expanded with content, needs human review |
| `published` | Reviewed and approved for public consumption |

The generation script sets `placeholder`. AI expansion should set `draft`.
Human review sets `published`.

---

## 10. Content Priorities

When expanding docs, prioritize in this order:

1. **Getting Started** — installation, first chart (C# and Python)
2. **Core chart types** — line, scatter, column, candlestick, heatmap
3. **Axes** — numeric, datetime, configuration
4. **Interaction** — zoom/pan, cursor, tooltips
5. **Rendering backends** — DirectX 12, Skia, WPF setup
6. **Data series** — XY, OHLC
7. **Theming** — custom themes, ThemeEngine
8. **Layout** — dashboard composition
9. **Data sources** — expand by domain (network, hardware, audio, etc.)
10. **Gauges, widgets, instruments** — expand last

---

## 11. What NOT to Document

- Private/internal classes or methods
- Build system or CI/CD configuration
- Contributor guidelines (those go in CONTRIBUTING.md, not docs)
- Implementation rationale or design decisions
- Performance benchmarks that haven't been verified
- Features that don't exist yet (no roadmap items in docs)

---

## 12. Tables

Use tables for:
- Property/configuration reference
- Comparison charts (renderer backends, axis types, etc.)
- Package listings

Always include a header row. Align columns with `|---|`.

---

## 13. Images and Diagrams

- Use Mermaid for architecture/flow diagrams (supported by Material)
- Screenshots go in `docs/assets/images/` with descriptive filenames
- Always include alt text
- Prefer SVG over PNG when possible

---

## 14. Timestamps

The `last_updated` frontmatter field tracks when content was last meaningfully
changed. The generation script sets this to the sync time. AI expansion should
update it. Cosmetic/formatting changes should NOT update it.
