"""
Standalone Generator for Magna International: Smart eAxle Active Torque Vectoring & Disconnect
Project ID: 29
Tech Stack: Dog-Clutch Engagement Shock Minimization, Torque Vectoring ML
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 29 (Magna Smart eAxle)...")
    render_single_project("29")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
