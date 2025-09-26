#!/usr/bin/env python3
"""
Verification script to check if TB incidence analysis outputs were generated
"""
import os
import pandas as pd

print("🔍 CHECKING TB INCIDENCE ANALYSIS OUTPUTS")
print("="*50)

# Check if output directory exists
output_dir = "output"
if os.path.exists(output_dir):
    print(f"✅ Output directory found: {output_dir}")
    print(f"   Contents: {os.listdir(output_dir)}")

    # Check for plots directory
    plots_dir = os.path.join(output_dir, "plots")
    if os.path.exists(plots_dir):
        print(f"✅ Plots directory found: {plots_dir}")
        print(f"   Plot files: {os.listdir(plots_dir)}")
    else:
        print(f"❌ Plots directory not found: {plots_dir}")

    # List all files with their sizes
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            filepath = os.path.join(root, file)
            size = os.path.getsize(filepath)
            print(f"   - {filepath} ({size} bytes)")

else:
    print(f"❌ Output directory not found: {output_dir}")
    print("   Checking if files were created elsewhere...")

    # Check root directory for any analysis outputs
    root_files = [f for f in os.listdir('.') if any(f.endswith(ext) for ext in ['.png', '.docx', '.csv'])]
    if root_files:
        print(f"   Found in root directory: {root_files}")
    else:
        print("   No output files found anywhere")

print("\\n🎯 VERIFICATION COMPLETE")
