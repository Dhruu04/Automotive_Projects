"""
Standalone Generator for Brembo: Carbon-Ceramic Matrix (CCM) Brake Rotor Thermal Wear
Project ID: 34
Tech Stack: Acoustic Micro-Fracture Sensing, Rotor Carbon Oxidation ML
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 34 (Brembo Carbon Brakes)...")
    render_single_project("34")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
