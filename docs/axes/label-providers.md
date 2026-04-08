---
title: "Label Providers"
section: "axes"
last_updated: "2024-06-13 14:45 UTC"
status: draft
---

# Label Providers

## Summary

**Chartexa** is a high-performance charting engine built in C# with a DirectX 12 renderer, designed for real-time and large-scale data visualization, with seamless Python integration.

Label Providers in Chartexa control how axis tick labels are formatted and displayed. The `ILabelProvider` interface and its implementations, such as `NumericLabelProvider`, allow you to customize axis label formatting for numeric, date/time, or categorical axes. Use label providers to display values with custom units, precision, currency symbols, or localized formats.

---

## Installation

### .NET (NuGet)

```bash
dotnet add package Chartexa.Core
```

### Python (PyPI)

```bash
pip install chartexa
```

---

## Quick Start

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Core.LabelProviders;

// Create a NumericAxis with custom label formatting (e.g., 2 decimal places)
var axis = new NumericAxis
{
    AxisTitle = "Price (USD)",
    LabelProvider = new NumericLabelProvider("F2") // Format: 2 decimals
};
```

=== "Python"

```python
from chartexa import Chart, NumericAxis, NumericLabelProvider

# Create a NumericAxis with custom label formatting (e.g., 2 decimal places)
axis = NumericAxis(
    axis_title="Price (USD)",
    label_provider=NumericLabelProvider("F2")  # Format: 2 decimals
)

chart = (
    Chart(width=600, height=400)
    .add_axis(axis, position="left")
    .line([0, 1, 2], [10.123, 12.345, 14.567])
    .show()
)
```

---

## Concepts

Label Providers determine how axis values are converted to text for display. By default, axes use standard formatting, but you can supply a custom label provider to control the appearance of tick labels. For example, you might want to:

- Show numeric values with fixed decimal precision
- Display currency symbols or units
- Format date/time axes in a specific locale
- Add thousands separators or scientific notation

Label Providers implement the `ILabelProvider` interface, which defines methods for formatting and parsing axis values. Chartexa includes built-in providers for numeric and date/time axes, and you can create your own for specialized needs.

Use a label provider when you need precise control over how axis labels appear, especially for financial, scientific, or internationalized applications.

---

## Basic Usage

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Core.LabelProviders;
using Chartexa.Data.Series;
using Chartexa.Rendering;

// Create a NumericLabelProvider with currency formatting
var currencyLabelProvider = new NumericLabelProvider("$#,##0.00");

// Create a NumericAxis using the custom label provider
var yAxis = new NumericAxis
{
    Id = "Y",
    AxisTitle = "Revenue",
    LabelProvider = currencyLabelProvider
};

// Create sample data
var xAxis = new NumericAxis { Id = "X", AxisTitle = "Quarter" };
var dataSeries = new XyDataSeries();
dataSeries.Append(new[] { 1, 2, 3, 4 }, new[] { 12000.5, 15000.75, 17000.2, 21000.9 });

// Create a chart and add axes and series
var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(new FastLineRenderableSeries { DataSeries = dataSeries });
chart.Render();
```

=== "Python"

```python
from chartexa import Chart, NumericAxis, NumericLabelProvider

# Create a NumericLabelProvider with currency formatting
currency_label_provider = NumericLabelProvider("$#,##0.00")

# Create axes
x_axis = NumericAxis(axis_title="Quarter")
y_axis = NumericAxis(axis_title="Revenue", label_provider=currency_label_provider)

# Sample data
quarters = [1, 2, 3, 4]
revenue = [12000.5, 15000.75, 17000.2, 21000.9]

# Create chart
chart = (
    Chart(width=600, height=400)
    .add_axis(x_axis, position="bottom")
    .add_axis(y_axis, position="left")
    .line(quarters, revenue, stroke="#228B22", thickness=2)
    .background("#F5F5F5")
    .show()
)
```

---

## Configuration

| Property         | Type                  | Default      | Description                                                    |
|------------------|----------------------|--------------|----------------------------------------------------------------|
| `LabelProvider`  | `ILabelProvider`     | Built-in     | The provider used to format axis labels.                       |
| `FormatString`   | `string`             | `"G"`        | Format string for numeric/date values (e.g., `"F2"`, `"$#,##0.00"`). |
| `Culture`        | `CultureInfo`        | System locale| Optional locale for formatting (C# only).                      |

### Built-in Label Providers

| Provider                | Description                                      |
|-------------------------|--------------------------------------------------|
| `NumericLabelProvider`  | Formats numeric values using a specified format.  |
| `DateTimeLabelProvider` | Formats date/time values for DateTime axes.       |
| `CategoryLabelProvider` | Formats categorical axis labels.                  |

---

## Examples

### Example 1: Scientific Notation for Axis Labels

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Core.LabelProviders;
using Chartexa.Data.Series;

// Use scientific notation for axis labels
var sciLabelProvider = new NumericLabelProvider("E2");

var yAxis = new NumericAxis
{
    AxisTitle = "Concentration",
    LabelProvider = sciLabelProvider
};

var xAxis = new NumericAxis { AxisTitle = "Sample #" };
var dataSeries = new XyDataSeries();
dataSeries.Append(new[] { 1, 2, 3 }, new[] { 0.000123, 0.000456, 0.000789 });

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(new FastLineRenderableSeries { DataSeries = dataSeries });
chart.Render();
```

=== "Python"

```python
from chartexa import Chart, NumericAxis, NumericLabelProvider

# Use scientific notation for axis labels
sci_label_provider = NumericLabelProvider("E2")

y_axis = NumericAxis(axis_title="Concentration", label_provider=sci_label_provider)
x_axis = NumericAxis(axis_title="Sample #")

samples = [1, 2, 3]
concentration = [0.000123, 0.000456, 0.000789]

chart = (
    Chart(width=500, height=300)
    .add_axis(x_axis, position="bottom")
    .add_axis(y_axis, position="left")
    .line(samples, concentration, stroke="#8B0000", thickness=2)
    .show()
)
```

### Example 2: Custom Date Formatting

=== "C#"

```csharp
using Chartexa.Core.Axes;
using Chartexa.Core.LabelProviders;
using Chartexa.Data.Series;

// Custom date format for DateTime axis
var dateLabelProvider = new DateTimeLabelProvider("MMM yyyy");

var xAxis = new DateTimeAxis
{
    AxisTitle = "Month",
    LabelProvider = dateLabelProvider
};

var yAxis = new NumericAxis { AxisTitle = "Visitors" };
var dataSeries = new XyDataSeries<DateTime, double>();
dataSeries.Append(
    new[] { new DateTime(2023, 1, 1), new DateTime(2023, 2, 1), new DateTime(2023, 3, 1) },
    new[] { 1200, 1350, 1600 }
);

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(new FastLineRenderableSeries { DataSeries = dataSeries });
chart.Render();
```

=== "Python"

```python
from chartexa import Chart, DateTimeAxis, DateTimeLabelProvider, NumericAxis

# Custom date format for DateTime axis
date_label_provider = DateTimeLabelProvider("MMM yyyy")

x_axis = DateTimeAxis(axis_title="Month", label_provider=date_label_provider)
y_axis = NumericAxis(axis_title="Visitors")

months = ["2023-01-01", "2023-02-01", "2023-03-01"]
visitors = [1200, 1350, 1600]

chart = (
    Chart(width=600, height=350)
    .add_axis(x_axis, position="bottom")
    .add_axis(y_axis, position="left")
    .line(months, visitors, stroke="#4169E1", thickness=2)
    .show()
)
```

### Example 3: Localized Number Formatting

=== "C#"

```csharp
using System.Globalization;
using Chartexa.Core.Axes;
using Chartexa.Core.LabelProviders;

// Use German locale for number formatting
var germanLabelProvider = new NumericLabelProvider("N2", new CultureInfo("de-DE"));

var yAxis = new NumericAxis
{
    AxisTitle = "Umsatz (€)",
    LabelProvider = germanLabelProvider
};

var xAxis = new NumericAxis { AxisTitle = "Monat" };
var dataSeries = new XyDataSeries();
dataSeries.Append(new[] { 1, 2, 3 }, new[] { 12345.67, 23456.78, 34567.89 });

var chart = new Chart();
chart.Axes.Add(xAxis);
chart.Axes.Add(yAxis);
chart.Series.Add(new FastLineRenderableSeries { DataSeries = dataSeries });
chart.Render();
```

=== "Python"

```python
from chartexa import Chart, NumericAxis, NumericLabelProvider

# Localized number formatting (German locale)
german_label_provider = NumericLabelProvider("N2", locale="de_DE")

y_axis = NumericAxis(axis_title="Umsatz (€)", label_provider=german_label_provider)
x_axis = NumericAxis(axis_title="Monat")

months = [1, 2, 3]
sales = [12345.67, 23456.78, 34567.89]

chart = (
    Chart(width=500, height=300)
    .add_axis(x_axis, position="bottom")
    .add_axis(y_axis, position="left")
    .line(months, sales, stroke="#FF8C00", thickness=2)
    .show()
)
```

---

## Performance Notes

Label Providers operate on axis tick values and are lightweight, with negligible performance impact even for charts with thousands of ticks. Custom label providers with complex formatting (e.g., locale-aware date parsing) may incur minor overhead, but this is insignificant compared to rendering and data processing.

!!! tip "Performance Tip"
    Use built-in label providers for best performance. Custom providers should avoid expensive operations in the formatting method.

---

## When to Use

- You need axis labels with custom numeric formatting (decimals, currency, scientific notation)
- You want to localize axis labels for international users
- You require custom date/time formats for time-series charts
- You need to display units, symbols, or prefixes in axis labels
- You want to implement domain-specific label formatting (e.g., engineering, finance)

---

## Related

- [NumericAxis](numeric-axis.md)
- [DateTimeAxis](datetime-axis.md)
- [Axis Ranging](axis-ranging.md)
- [Custom Axis Titles](axis-titles.md)

---

> **Last updated:** 2024-06-13 14:45 UTC | **Status:** draft