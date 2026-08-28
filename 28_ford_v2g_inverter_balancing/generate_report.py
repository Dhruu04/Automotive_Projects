"""
Standalone Generator for Ford Motor Company: Pro Power Onboard Bi-Directional V2G Grid Balancing
Project ID: 28
Tech Stack: Bi-Directional Inverter Phase Synchronization, Harmonic Distortion ML
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 28 (Ford V2G Smart Power)...")
    render_single_project("28")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
