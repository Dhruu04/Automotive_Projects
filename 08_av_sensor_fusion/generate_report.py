"""
Standalone Generator for Autonomous Vehicle Multi-Sensor Navigation Safety & Perception
Project ID: 08
Tech Stack: Multi-Sensor Kalman Filtering, 3D Radar & Camera Fusion
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 08 (Multi-Sensor Navigation Safety)...")
    render_single_project("08")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
