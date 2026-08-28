"""
Standalone Generator for Honda Motor Co: e:HEV Dual-Motor Hybrid Torque Blending & Energy Split
Project ID: 25
Tech Stack: Engine Clutch Lockup Dynamics, Motor-Generator Torque Sync
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 25 (Honda e:HEV Powertrain)...")
    render_single_project("25")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
