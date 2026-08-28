"""
Standalone Generator for Iveco: Heavy-Duty 700-Bar Hydrogen Fuel Cell Tank & Hydration
Project ID: 40
Tech Stack: 700-Bar Tank Solenoid Purge, PEM Fuel Cell Hydration ML
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 40 (Iveco Hydrogen Freight)...")
    render_single_project("40")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
