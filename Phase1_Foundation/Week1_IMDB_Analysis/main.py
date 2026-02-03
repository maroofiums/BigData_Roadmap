import os

# Base folder for Week 1
base_dir = "Week1_BigData_Pandas"

# Day-wise folder names
days = [
    "Day1_BigData_Introduction",
    "Day2_BigData_Vs_DataTypes",
    "Day3_Pandas_Basics",
    "Day4_Pandas_Selection_Filtering",
    "Day5_Pandas_Grouping_Aggregations",
    "Day6_Data_Visualization",
    "Day7_MiniProject_IMDB_Analysis"
]

# README template
readme_template = """# {day_name}

## Overview
Write your notes and summary here.

## Topics Learned
- Topic 1
- Topic 2
- Topic 3

## Practice / Exercises
Describe your practice tasks.

## Mini Project (if any)
Describe the mini project tasks or exercises.

## Tips
- Note 1
- Note 2
"""

# Create base folder
os.makedirs(base_dir, exist_ok=True)

# Create day folders with README.md
for day in days:
    day_path = os.path.join(base_dir, day)
    os.makedirs(day_path, exist_ok=True)
    
    # Create README.md inside each day folder
    readme_path = os.path.join(day_path, "README.md")
    with open(readme_path, "w") as f:
        f.write(readme_template.format(day_name=day))

print(f"Week 1 folders with README.md created successfully in '{base_dir}'")
