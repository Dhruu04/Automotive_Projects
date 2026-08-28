"""
Standalone Generator for Denso Corporation: EV Heat-Pump Refrigerant Loop & Subcooling COP
Project ID: 26
Tech Stack: Thermodynamic Pressure-Enthalpy Modeling, Expansion Valve Sizing
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 26 (Denso EV Heat Pump)...")
    render_single_project("26")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
