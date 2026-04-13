---
title: "Domain Packages Overview"
section: "domains"
last_updated: "2026-04-13 00:00 UTC"
status: published
---

# Domain Packages Overview

## Summary

Chartexa domain packs provide vertical models, synthetic sources, replay-friendly timelines, and adapters for chart consumption.

Domain APIs use the namespace prefix `Chartexa.Domains.*` and package identity `Chartexa.Domains.*`.

---

## Current Domain Pack Matrix

| Domain | NuGet Package | Namespace | Typical Data | Example App |
|---|---|---|---|---|
| GeoSpatial | `Chartexa.Domains.GeoSpatial` | `Chartexa.Domains.GeoSpatial.*` | DEM, LAS/LAZ, GeoTIFF | `TerrainExplorer`, `SurveyExplorer` |
| Industrial | `Chartexa.Domains.Industrial` | `Chartexa.Domains.Industrial.*` | OPC UA, Modbus, MQTT, BACnet | `FactoryDashboard` |
| Finance | `Chartexa.Domains.Finance` | `Chartexa.Domains.Finance.*` | OHLCV, ticks, indicators | `TradingWorkstation` |
| Science | `Chartexa.Domains.Science` | `Chartexa.Domains.Science.*` | HDF5, NetCDF, TDMS | `ScienceLabExplorer` |
| Medical | `Chartexa.Domains.Medical` | `Chartexa.Domains.Medical.*` | EDF and biosignals | `ClinicalSignalReview` |
| Robotics | `Chartexa.Domains.Robotics` | `Chartexa.Domains.Robotics.*` | ROS bag, mission replay | `RobotMissionPlayback` |
| Power | `Chartexa.Domains.Power` | `Chartexa.Domains.Power.*` | PMU, COMTRADE, inverter telemetry | `GridDisturbanceViewer` |
| Imaging | `Chartexa.Domains.Imaging` | `Chartexa.Domains.Imaging.*` | Thermal and multispectral frames | `ThermalInspectionStudio` |
| AEC | `Chartexa.Domains.Aec` | `Chartexa.Domains.Aec.*` | IFC-like scenes, layers, section cuts | `AecSceneExplorer` |
| Simulation | `Chartexa.Domains.Simulation` | `Chartexa.Domains.Simulation.*` | Twin state timelines and replay | `TwinOperationsConsole` |

---

## Installation

```powershell
dotnet add package Chartexa.Core
dotnet add package Chartexa.DataSources
dotnet add package Chartexa.Playback
# Pick one or more domain packs
dotnet add package Chartexa.Domains.Imaging
```

Use `Chartexa.Playback` when you need deterministic replay or timeline scrubbing.

---

## Standard Domain Integration Flow

1. Add one or more `Chartexa.Domains.*` packages.
2. Generate or load domain-native models from a source.
3. Adapt domain models into chart-ready series arrays.
4. Bind adapted arrays to Chartexa series.
5. Add playback/replay for testability and diagnostics.

See [Usage Patterns](usage-patterns.md) for concrete C# examples.

---

## Related

- [Data Sources Overview](../data/data-sources/overview.md)
- [Examples Index](../examples/index.md)
- [API Reference](../api-reference/index.md)

---

> **Last updated:** 2026-04-13 00:00 UTC | **Status:** published
