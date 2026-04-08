---
title: "Data Sources Overview"
section: "data/data-sources"
last_updated: "2026-06-10 14:00 UTC"
status: published
---

# Data Sources Overview

## Summary

Chartexa provides 40+ data source classes for connecting to real-time data feeds. Data sources abstract the connection, parsing, and buffering of incoming data, feeding it directly into chart series.

---

## Data Source Categories

| Category | Sources | Use Case |
|---|---|---|
| **Network** | MQTT, WebSocket, REST, gRPC | Cloud / IoT data feeds |
| **Serial** | Serial port, GPS NMEA | Hardware interfaces |
| **Audio** | Audio capture, FFT | Sound analysis |
| **System** | CPU, memory, process, Docker | System monitoring |
| **Financial** | Market data, candle aggregation | Trading systems |
| **Hardware** | GPIO, ADC, sensors | Embedded / IoT |
| **Automotive** | OBD-II, CAN bus | Vehicle telemetry |
| **Science** | SDR (Software Defined Radio) | RF analysis |
| **Simulation** | Flight sim, racing sim, game engine | Simulator data |

---

## Architecture

`mermaid
graph LR
    A[External Source] --> B[DataSource]
    B --> C[DataSourceBridge]
    C --> D[Chart Series]
    B --> E[DataRecorder]
    E --> F[CSV / Binary file]
`

All data sources extend `DataSource` and emit data through `DataSourceChannel` objects. The `DataSourceManager` handles lifecycle and connects sources to chart series via `DataSourceBridge`.

---

## Related

- [MQTT](network/mqtt.md)
- [WebSocket](network/websocket.md)
- [Serial Port](hardware/serial.md)
- [Market Data](financial/market-data.md)

---

> **Last updated:** 2026-06-10 14:00 UTC | **Status:** published
