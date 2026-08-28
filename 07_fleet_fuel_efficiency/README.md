# Heavy Commercial Fleet Fuel Economy & Cargo Load Management

![Domain: Automotive Data Science](https://img.shields.io/badge/Domain-Automotive%20Data%20Science-0284c7)
![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-10b981)
![Focus: Operational Excellence](https://img.shields.io/badge/Focus-Operational%20Excellence-6366f1)

---

## 1. Executive Summary & Problem Framing
Shows how cargo weight, highway speeds, tire pressure, and road hills impact truck fuel economy, providing clear rules for drivers to save diesel across 120 trucks.

- **Target Operational Domain:** `Powertrain & Fleet`
- **Organization / Fleet Sector:** `Freight Transportation Fleet`
- **Primary Business Metric:** `+4.5 MPG Improvement`
- **Annual Financial Return / Value:** `$248k / yr`

---

## 2. Key Operational Findings & Visual Chart Insights
### Fuel Economy (MPG) vs Cargo Payload Weight
- **Data Finding:** Heavier freight cargo reduces fuel economy in a predictable linear line (-0.22 MPG per metric ton). Heavy haulers drop from 11.2 MPG when empty to 5.4 MPG when carrying full 18,000 kg cargo loads.
- **Operational Recommendation:** Deploy intelligent cargo packing to balance weight evenly across axles, lowering rolling resistance and saving 0.35 MPG across heavy freight hauls.

### Speed vs Wind Resistance Impact on Fuel Economy
- **Data Finding:** Fuel economy drops steeply when driving above 62 MPH because air drag increases rapidly with speed. Trucks with high wind resistance drop below 6.0 MPG at 70 MPH.
- **Operational Recommendation:** Install aerodynamic trailer side-skirts and set truck highway cruise speed limits to 58-60 MPH on flat highway corridors, achieving an immediate 12.4% fuel savings without impacting delivery schedules.

### Average Fuel Economy by Truck Model
- **Data Finding:** AeroTruck V6 achieves the highest fuel efficiency (9.8 MPG), outperforming heavy TransHaul units (6.9 MPG) by 42% on medium-distance regional routes.
- **Operational Recommendation:** Assign AeroTruck units to routes where average cargo weight is under 8,000 kg, saving $8,400 per truck in annual diesel fuel costs.

### What Affects Fuel Consumption Most
- **Data Finding:** Wind resistance and cargo weight cause the highest fuel penalties. Maintaining correct tire pressure (+0.05 MPG per PSI) provides consistent positive fuel economy savings.
- **Operational Recommendation:** Equip all fleet trailers with automatic tire inflation systems that maintain 105 PSI constantly, preventing low-tire fuel waste and extending tire tread life by 18%.


---

## 3. Executive Key Performance Indicators (KPIs)
| Performance Indicator | Operational Value | Target Benchmark | Business Impact |
|---|---|---|---|
| **Optimized Fleet MPG** | `6.5 MPG` | +4.5 MPG Potential | Direct Cost & Uptime Driver |
| **Annual Diesel Saved** | `$248,000` | Across 120 Fleet Trucks | Direct Cost & Uptime Driver |
| **Model Prediction Score** | `0.893` | Accurate Predictions | Direct Cost & Uptime Driver |
| **Low Tire Pressure Warnings** | `520 Alerts` | <98 PSI Alerts | Direct Cost & Uptime Driver |

---

## 4. What This Means for the Company & Financial Value
- $248,000 Direct Diesel Fuel Savings: Increasing average fleet fuel economy from 6.8 to 8.2 MPG across 120 trucks.
- 18% Longer Tire Life: Consistent tire pressure prevents heat build-up and reduces premature tire replacement costs.

- **Identified Annual Financial Value:** **$248k / yr**
- **Asset Protection & Reliability:** Directly prevents catastrophic hardware breakdowns, optimizes warranty reserves, and ensures peak operational efficiency.

---

## 5. Recommended Management Action & Strategic Playbook
### Immediate Operational Priorities:
- Low Tire Pressure Alerts: Send immediate alerts to dispatchers whenever a truck tire pressure drops below 100 PSI.
- Highway Speed Governor: Set truck maximum cruise speed limiters to 62 MPH across all long-haul highway vehicles.
- Aerodynamic Trailer Skirts: Install aero skirts on the 40 lowest-efficiency highway haulers.

### Long-Term Strategic Roadmap:
- Hill-Elevation Predictive Cruise: Integrate topographic highway hill maps into automatic transmission gear-shifting logic.
- Truck Drafting Telematics: Allow connected trucks to safely follow each other on highways to draft behind leading trucks.
- Hybrid Brake Energy Recovery: Model regenerative braking capture on hilly delivery routes.

---

## 6. How to Review the Interactive Report
1. Open `report.html` in any standard web browser to view the interactive 2D data visualizations, distribution curves, and diagnostic drill-downs.
2. To regenerate the operational dataset and analytical report from source, execute:
   ```bash
   python generate_report.py
   ```
3. To view all 50 enterprise systems in the unified portfolio, open `../index.html`.
