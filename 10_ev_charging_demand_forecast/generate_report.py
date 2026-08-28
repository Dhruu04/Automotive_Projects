"""
Standalone Generator for EV Fast-Charging Station Grid Demand & Queue Optimization
Project ID: 10
Tech Stack: Hourly Demand Forecasting, Off-Peak Pricing Optimization
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 10 (EV Charging Grid & Queue Forecast)...")
    render_single_project("10")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
