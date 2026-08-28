"""
Standalone Generator for Ducati: MotoGP 6-Axis IMU Lean Angle Telemetry & Slide Control
Project ID: 36
Tech Stack: 6-Axis Inertial IMU Telemetry, Anti-Wheelie & Slide Control ML
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 36 (Ducati Lean Dynamics)...")
    render_single_project("36")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
