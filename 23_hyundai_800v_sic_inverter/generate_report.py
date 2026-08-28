"""
Standalone Generator for Hyundai Motor Group: 800V E-GMP Silicon Carbide Inverter Thermal Loss
Project ID: 23
Tech Stack: High-Frequency Switching Loss Regression, SiC MOSFET Modeling
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 23 (Hyundai 800V Inverter)...")
    render_single_project("23")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
