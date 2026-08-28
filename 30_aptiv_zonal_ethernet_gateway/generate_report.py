"""
Standalone Generator for Aptiv / Rivian: Centralized Zonal Vehicle Ethernet Gateway Congestion
Project ID: 30
Tech Stack: Time-Sensitive Networking (TSN) Latency Sizing, Buffer Overflow ML
"""

import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir = os.path.dirname(current_dir)
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from build_all_portfolio import render_single_project, PROJECTS_META

if __name__ == "__main__":
    print(f"Running standalone generation for Project 30 (Aptiv Zonal E/E Network)...")
    render_single_project("30")
    print(f"Successfully generated standalone report at: {os.path.join(current_dir, 'report.html')}")
