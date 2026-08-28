"""
Standalone Generator for Stellantis South America: E100 Bio-Ethanol Cold-Start AI
Project ID: 49
Tech Stack: Heated Fuel Rail Injector Pulse, Stoichiometric Lambda ML
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 49 (Bio-Ethanol E100 Engine)...")
    render_single_project("49")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
