"""
Standalone Generator for Subaru: Symmetrical AWD Multi-Plate Clutch & X-Mode AI
Project ID: 47
Tech Stack: Center Differential Hydraulic Clamping, Snow Slip Lockup ML
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 47 (Subaru S-AWD X-Mode)...")
    render_single_project("47")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
