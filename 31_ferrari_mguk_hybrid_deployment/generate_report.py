"""
Standalone Generator for Ferrari: Hybrid Supercar MGU-K Energy Recovery & Apex Torque Boost
Project ID: 31
Tech Stack: State-of-Charge Discharge Scheduling, Corner Exit Boost ML
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 31 (Ferrari Hybrid MGU-K)...")
    render_single_project("31")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
