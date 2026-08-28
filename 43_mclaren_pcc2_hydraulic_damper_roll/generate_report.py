"""
Standalone Generator for McLaren: Proactive Chassis Control II Hydraulic Damper Roll
Project ID: 43
Tech Stack: Interconnected Hydraulic Lines, Dynamic Roll Stiffness ML
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 43 (McLaren Proactive Chassis)...")
    render_single_project("43")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
