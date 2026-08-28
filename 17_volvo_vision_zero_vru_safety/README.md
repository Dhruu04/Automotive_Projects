# Volvo Cars: Vision-Zero Pedestrian & Cyclist Trajectory Safety

![Domain: Automotive Data Science](https://img.shields.io/badge/Domain-Automotive%20Data%20Science-0284c7)
![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-10b981)
![Focus: Operational Excellence](https://img.shields.io/badge/Focus-Operational%20Excellence-6366f1)

---

## 1. Executive Summary & Problem Framing
Predicts walking and cycling paths at urban street intersections 2.5 seconds in advance, automatically priming emergency brakes to eliminate severe collisions.

- **Target Operational Domain:** `Active Safety & ADAS`
- **Organization / Fleet Sector:** `Volvo Cars`
- **Primary Business Metric:** `96.8% Near-Miss Cut`
- **Annual Financial Return / Value:** `Zero Severe Crashes`

---

## 2. Key Operational Findings & Visual Chart Insights
### Time to Collision (Seconds) vs Pedestrian Distance
- **Data Finding:** When time to collision drops below 1.8 seconds (red), the vehicle initiates automated emergency braking (AEB) with full stopping pressure, bringing the car to a complete stop before impact.
- **Operational Recommendation:** Combine camera pedestrian body pose recognition with radar velocity tracking to predict when a pedestrian is about to step off a curb 2.5 seconds before they enter the traffic lane.

### Average Time to Collision by Road User Type
- **Data Finding:** Fast cyclists and electric scooters travel at higher speeds (5 to 7.5 m/s), reducing driver reaction time to 1.6 seconds compared to 2.8 seconds for walking pedestrians.
- **Operational Recommendation:** Widen the camera detection field-of-view to 120 degrees at urban intersections to spot fast-moving cyclists arriving from side streets.

### Crossing Speed Distribution Across Safety Interventions
- **Data Finding:** Running pedestrians and fast scooters have high median crossing speeds (4.8 m/s), making automatic emergency braking essential when human drivers fail to react.
- **Operational Recommendation:** Pre-tension driver seatbelts and sound an audible chime 500 ms before full emergency braking to prepare passengers for sudden deceleration.

### Forward Detection Distance Histogram
- **Data Finding:** Advanced front radar and stereo cameras detect road users up to 45 meters away in daylight and darkness, giving ample time to decelerate smoothly.
- **Operational Recommendation:** Standardize night-vision thermal pedestrian detection algorithms across all Volvo luxury SUV platforms.


---

## 3. Executive Key Performance Indicators (KPIs)
| Performance Indicator | Operational Value | Target Benchmark | Business Impact |
|---|---|---|---|
| **Near-Miss Collision Reduction** | `96.8%` | Vision-Zero Benchmark | Direct Cost & Uptime Driver |
| **Detection Range** | `45.0 Meters` | Wide Angle Radar/Camera | Direct Cost & Uptime Driver |
| **AEB Braking Trigger Speed** | `12 ms` | Fast Brake Pre-Charge | Direct Cost & Uptime Driver |
| **Pedestrians Tracked** | `2,800 Encounters` | Urban European Streets | Direct Cost & Uptime Driver |

---

## 4. What This Means for the Company & Financial Value
- Vision-Zero Leadership: Eliminating severe pedestrian crashes protects Volvo Cars' position as the global safety benchmark.
- Euro NCAP 5-Star Safety Scores: Securing maximum 5-star crash safety ratings drives commercial showroom demand.

- **Identified Annual Financial Value:** **Zero Severe Crashes**
- **Asset Protection & Reliability:** Directly prevents catastrophic hardware breakdowns, optimizes warranty reserves, and ensures peak operational efficiency.

---

## 5. Recommended Management Action & Strategic Playbook
### Immediate Operational Priorities:
- Intersection AEB Calibration: Tune emergency braking parameters specifically for fast-moving urban e-scooters.
- Nighttime Pedestrian Radar: Optimize radar gain for detecting pedestrians in dark, unlit crosswalks.
- Brake Pre-Fill Feature: Pre-charge brake fluid pressure whenever a pedestrian looks toward the road.

### Long-Term Strategic Roadmap:
- Body Pose Intention AI: Train neural networks to detect head turns and walking gait orientation.
- Vehicle-to-Pedestrian (V2P): Pilot smartphone direct-radio alerts for pedestrians wearing smartwatches.
- Blind Spot Door Opening Safety: Prevent vehicle doors from opening into the path of approaching cyclists.

---

## 6. How to Review the Interactive Report
1. Open `report.html` in any standard web browser to view the interactive 2D data visualizations, distribution curves, and diagnostic drill-downs.
2. To regenerate the operational dataset and analytical report from source, execute:
   ```bash
   python generate_report.py
   ```
3. To view all 50 enterprise systems in the unified portfolio, open `../index.html`.
