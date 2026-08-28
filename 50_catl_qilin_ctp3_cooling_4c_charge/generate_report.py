"""
Standalone Generator for CATL: Qilin CTP 3.0 Cooling Plate Heat Exchange & 4C Charge
Project ID: 50
Tech Stack: Inter-Cell Liquid Cooling Elastic Pad, 4C Fast-Charge Dendrite AI
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 50 (CATL Qilin CTP 3.0)...")
    render_single_project("50")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
