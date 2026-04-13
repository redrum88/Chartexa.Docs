---
title: "Domain Usage Patterns"
section: "domains"
last_updated: "2026-04-13 00:00 UTC"
status: published
---

# Domain Usage Patterns

This page shows practical usage for the newest domain packs: Imaging, AEC, and Simulation.

## Imaging Domain

Generate synthetic thermal frames and convert them into chartable line data.

```csharp
using Chartexa.Domains.Imaging.Adapters;
using Chartexa.Domains.Imaging.Sources;

var frames = ThermalSource.GenerateTimeSeries(
    frameCount: 120,
    intervalSeconds: 0.5,
    width: 320,
    height: 240);

// Convert one frame to false-color ARGB for image-style visualization.
var falseColor = FalseColorAdapter.MapThermal(frames[0]);

// falseColor.Pixels can be rendered via WriteableBitmap or a custom image layer.
```

Use `ThermalStreamSource` when frames must be emitted in real time.

---

## AEC Domain

Generate a synthetic building scene and create section-cut data for visualization.

```csharp
using Chartexa.Domains.Aec.Adapters;
using Chartexa.Domains.Aec.Sources;

var scene = AecSceneSource.GenerateSynthetic(
    floors: 6,
    gridX: 8,
    gridY: 5,
    seed: 42);

var section = SectionCutAdapter.Compute(
    scene.Elements,
    SectionCutAdapter.SectionPlane.XY,
    position: 7.2);

// section.Segments can be mapped to line series for section overlays.
```

Use `LayerVisibilityAdapter` to filter per discipline (architecture, structural, MEP) before rendering.

---

## Simulation Domain

Create a synthetic twin timeline and adapt telemetry into bounded chart arrays.

```csharp
using Chartexa.Domains.Simulation.Adapters;
using Chartexa.Domains.Simulation.Models;
using Chartexa.Domains.Simulation.Sources;

var scenario = TwinScenarioSource.GenerateSynthetic(
    durationSeconds: 180,
    updateRateHz: 30,
    runtime: SimulationRuntime.Unity,
    seed: 7);

var telemetry = TwinTelemetryAdapter.AdaptTelemetry(
    scenario.Frames,
    maxPoints: 2000);

// telemetry.Time, telemetry.Speed, telemetry.StateOfCharge, etc.
```

Use `TwinReplaySource` for deterministic playback and incident forensics.

---

## Cross-Domain Recommendations

1. Keep domain models immutable once adapted for rendering.
2. Decimate to a maximum point budget before UI binding.
3. Separate source ingestion, adaptation, and chart composition.
4. Record and replay timelines for regression tests.
5. Prefer domain adapters over ad-hoc mapping in UI code.

---

## Related

- [Domain Packages Overview](overview.md)
- [Data Sources Overview](../data/data-sources/overview.md)
- [Performance Optimization](../performance/optimization.md)

---

> **Last updated:** 2026-04-13 00:00 UTC | **Status:** published
