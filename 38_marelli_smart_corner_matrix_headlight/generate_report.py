"""
Standalone Generator for Marelli: Smart Corner Matrix Laser-LED Headlight Thermal Sizing
Project ID: 38
Tech Stack: Thermal Junction Dissipation, Pixel Glare Sizing ML
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 38 (Marelli Matrix Lighting)...")
    render_single_project("38")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
