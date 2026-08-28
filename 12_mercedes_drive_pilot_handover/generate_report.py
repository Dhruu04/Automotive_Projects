"""
Standalone Generator for Mercedes-Benz: Drive Pilot Level 3 Handover & Driver Alertness
Project ID: 12
Tech Stack: Driver Gaze Classification, Transition Time Sizing
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 12 (Mercedes Level 3 Safety)...")
    render_single_project("12")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
