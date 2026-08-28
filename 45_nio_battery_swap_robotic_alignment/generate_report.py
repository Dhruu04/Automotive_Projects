"""
Standalone Generator for NIO: Power Swap Station 4.0 3-Minute Robotic Alignment AI
Project ID: 45
Tech Stack: 3D Machine Vision Bolt Alignment, Automated Pack Health Telemetry
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 45 (NIO Power Swap 4.0)...")
    render_single_project("45")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
