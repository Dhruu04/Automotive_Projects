"""
Standalone Generator for Stellantis: Light Commercial Fleet Euro 7 Real Driving Emissions
Project ID: 19
Tech Stack: Real Driving Emissions (RDE) Telemetry, Catalytic Efficiency
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 19 (Stellantis Euro 7 RDE)...")
    render_single_project("19")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
