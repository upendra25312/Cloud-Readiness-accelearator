# Monitoring Tool Integration Guide

**Version**: 1.0 | **Task**: 10.2 | **Requirements**: 10.2, 15.2

---

## Overview

This guide covers extracting performance metrics from monitoring tools to populate infrastructure profiling and readiness scoring templates.

---

## Splunk Integration

### Performance Metrics Queries

**CPU Utilization (30-day)**:
```spl
index=os_metrics sourcetype=cpu host=* 
| timechart span=1h avg(cpu_percent) as avg_cpu, perc95(cpu_percent) as p95_cpu, max(cpu_percent) as peak_cpu by host
| stats avg(avg_cpu) as avg, perc95(p95_cpu) as p95, max(peak_cpu) as peak by host
```

**Memory Utilization (30-day)**:
```spl
index=os_metrics sourcetype=memory host=*
| timechart span=1h avg(mem_percent) as avg_mem by host
| stats avg(avg_mem) as avg, max(avg_mem) as peak by host
```

**Disk I/O (30-day)**:
```spl
index=os_metrics sourcetype=disk host=*
| timechart span=1h avg(disk_iops) as avg_iops, avg(disk_latency_ms) as avg_latency by host
| stats avg(avg_iops) as avg_iops, max(avg_iops) as peak_iops, avg(avg_latency) as avg_latency by host
```

### Export: Splunk REST API or CSV export from saved searches

---

## Datadog Integration

### API Queries

**CPU Metrics**:
```
GET /api/v1/query?query=avg:system.cpu.user{*} by {host}&from={30d_ago}&to={now}
```

**Memory Metrics**:
```
GET /api/v1/query?query=avg:system.mem.pct_usable{*} by {host}&from={30d_ago}&to={now}
```

### Export: Datadog API (JSON), Dashboard CSV export

---

## New Relic Integration

### NRQL Queries

**CPU Utilization**:
```sql
SELECT average(cpuPercent), max(cpuPercent), percentile(cpuPercent, 95) 
FROM SystemSample SINCE 30 days ago FACET hostname
```

**Memory Utilization**:
```sql
SELECT average(memoryUsedPercent), max(memoryUsedPercent) 
FROM SystemSample SINCE 30 days ago FACET hostname
```

### Export: New Relic API (JSON), Dashboard CSV export

---

## Azure Monitor / SCOM Integration

### Azure Monitor (Log Analytics):
```kql
Perf
| where TimeGenerated > ago(30d)
| where ObjectName == "Processor" and CounterName == "% Processor Time"
| summarize avg(CounterValue), max(CounterValue), percentile(CounterValue, 95) by Computer
```

### SCOM: Export performance reports via SCOM Reporting

---

## Data Mapping to Accelerator Templates

| Monitoring Metric | Template Field | Unit | Collection Period |
|------------------|---------------|------|-------------------|
| CPU utilization (avg) | Average CPU % | % | 30 days minimum |
| CPU utilization (peak) | Peak CPU % | % | 30 days minimum |
| CPU utilization (p95) | 95th Percentile CPU % | % | 30 days minimum |
| Memory utilization (avg) | Average Memory % | % | 30 days minimum |
| Disk IOPS (avg) | Average IOPS | IOPS | 30 days minimum |
| Disk latency (avg) | Average Latency | ms | 30 days minimum |
| Network throughput (avg) | Average Network | Mbps | 30 days minimum |

---

## Data Quality Requirements

- Minimum 30 days of continuous data
- Collection interval: 5 minutes or less
- Coverage: >95% of in-scope servers
- Validate against known peak periods (month-end, quarter-end)
- Flag any gaps >4 hours in collection data

---

*Guide Version 1.0 — Cloud Readiness Accelerator Framework*
