"""
Standalone Generator for Toyota Motor Corp: Stamping Press Vibration & Kaizen Sheet Metal AI
Project ID: 21
Tech Stack: Micro-Vibration Peak Wave Analysis, Die Wear Classification
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 21 (Toyota Lean Stamping AI)...")
    render_single_project("21")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
