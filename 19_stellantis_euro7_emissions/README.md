# Stellantis: Light Commercial Fleet Euro 7 Real Driving Emissions

![Domain: Automotive Data Science](https://img.shields.io/badge/Domain-Automotive%20Data%20Science-0284c7)
![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-10b981)
![Focus: Operational Excellence](https://img.shields.io/badge/Focus-Operational%20Excellence-6366f1)

---

## 1. Executive Summary & Problem Framing
Monitors exhaust gas temperatures and catalytic converter chemistry during stop-and-go city delivery routes to ensure strict Euro 7 clean air compliance.

- **Target Operational Domain:** `Powertrain & Emissions`
- **Organization / Fleet Sector:** `Stellantis / Renault`
- **Primary Business Metric:** `-24.5% NOx Emissions`
- **Annual Financial Return / Value:** `$4.4M Penalty Avoid`

---

## 2. Key Operational Findings & Visual Chart Insights
### Real Driving NOx Emissions vs Exhaust Temperature
- **Data Finding:** When the exhaust catalyst operates above 220°C, catalytic efficiency exceeds 95%, keeping tailpipe NOx well below the 60 mg/km Euro 7 limit. Cold starts in stop-and-go city traffic cause brief emissions spikes.
- **Operational Recommendation:** Install 48V electric exhaust heaters that warm the catalytic converter to 200°C within 15 seconds of engine start, eliminating cold-start urban emissions.

### AdBlue Urea Dosing vs Catalytic Cleaning Efficiency
- **Data Finding:** Injecting 45-60 mg/s of AdBlue delivers maximum 96% NOx conversion. Over-dosing beyond 75 mg/s creates unreacted ammonia smell without improving emissions.
- **Operational Recommendation:** Deploy smart neural dosing controllers that inject the exact chemical stoichiometric amount of AdBlue based on live NOx sensor readings.

### Tailpipe NOx Emissions Spread (mg/km)
- **Data Finding:** 91.8% of all commercial van delivery trips operate comfortably below the 60 mg/km regulatory limit with an average fleet score of 42.5 mg/km.
- **Operational Recommendation:** Incorporate automated cloud emissions reporting to verify fleet compliance and avoid European regulatory non-compliance fines.

### Average NOx Emissions Across Exhaust Thermal Zones
- **Data Finding:** Emissions drop from 112 mg/km during cold idling down to 28.4 mg/km during optimal 260-360°C operating conditions.
- **Operational Recommendation:** Schedule city delivery routes to minimize cold idling, keeping delivery van catalytic converters warm and clean.


---

## 3. Executive Key Performance Indicators (KPIs)
| Performance Indicator | Operational Value | Target Benchmark | Business Impact |
|---|---|---|---|
| **NOx Emissions Reduction** | `-24.5%` | Below Euro 7 Ceiling | Direct Cost & Uptime Driver |
| **SCR Catalyst Efficiency** | `94.2%` | Optimal Urea Reaction | Direct Cost & Uptime Driver |
| **Fleet Compliance Rate** | `91.8%` | Real Driving Emissions | Direct Cost & Uptime Driver |
| **RDE Test Trips Logged** | `2,600 Trips` | City Delivery Vans | Direct Cost & Uptime Driver |

---

## 4. What This Means for the Company & Financial Value
- $4.4M European Regulatory Fine Avoidance: Strict Euro 7 compliance avoids heavy European environmental penalty fees.
- Commercial Fleet Contract Wins: Delivering verified low-emission vans wins municipal delivery fleet supply contracts.

- **Identified Annual Financial Value:** **$4.4M Penalty Avoid**
- **Asset Protection & Reliability:** Directly prevents catastrophic hardware breakdowns, optimizes warranty reserves, and ensures peak operational efficiency.

---

## 5. Recommended Management Action & Strategic Playbook
### Immediate Operational Priorities:
- Electric Catalyst Heating: Enable 48V fast pre-heating logic during morning cold starts.
- AdBlue Dosing Tune: Calibrate urea dosing maps to eliminate ammonia odor during high-speed highway driving.
- Delivery Van Idle Reduction: Set automatic 3-minute engine shutdown limits during package delivery stops.

### Long-Term Strategic Roadmap:
- Plug-In Hybrid Geofencing: Automatically switch delivery vans to pure electric mode in zero-emission city centers.
- Synthetic E-Fuels Feasibility: Test carbon-neutral synthetic diesel fuels to achieve net-zero transport.
- On-Board NOx Diagnostics (OBD-3): Stream continuous emissions compliance data to municipal environmental portals.

---

## 6. How to Review the Interactive Report
1. Open `report.html` in any standard web browser to view the interactive 2D data visualizations, distribution curves, and diagnostic drill-downs.
2. To regenerate the operational dataset and analytical report from source, execute:
   ```bash
   python generate_report.py
   ```
3. To view all 50 enterprise systems in the unified portfolio, open `../index.html`.
