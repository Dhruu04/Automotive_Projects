"""
Standalone Generator for Lucid Motors: 900V Wunderbox Motor Stator Copper Loss & COP
Project ID: 44
Tech Stack: Axial-Flux Stator Thermal Modeling, 900V Silicon-Carbide ML
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 44 (Lucid 900V Powertrain)...")
    render_single_project("44")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
