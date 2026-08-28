"""
Standalone Generator for Porsche AG: Track Dynamics & Active Aero Downforce Optimization
Project ID: 14
Tech Stack: G-G Friction Circle Analysis, Dynamic Wing Load Sizing
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 14 (Porsche Track Dynamics)...")
    render_single_project("14")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
