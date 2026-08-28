"""
Standalone Generator for Bosch Group: ESP/ABS Hydraulic Brake Modulator Wear Diagnostics
Project ID: 15
Tech Stack: Hydraulic Transient Modeling, Solenoid Valve Diagnostics
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 15 (Bosch ABS Hydraulics)...")
    render_single_project("15")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
