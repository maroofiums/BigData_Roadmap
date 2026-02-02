import os

# Base project folder
base_dir = "BigData_Roadmap"

# Phase & weeks
phases = {
    "Phase1_Foundation": ["Week1_IMDB_Analysis", "Week2_SQL_Hadoop"],
    "Phase2_Tools_Storage": ["Week3_NoSQL", "Week4_Spark_Basics"],
    "Phase3_Processing_Analytics": ["Week5_Clickstream_Analytics", "Week6_Visualization"],
    "Phase4_Streaming_RealTime": ["Week7_Kafka", "Week8_Spark_Streaming"],
    "Phase5_Cloud_Deployment": ["Week9_Cloud_Basics", "Week10_Dashboards"],
    "Phase6_Advanced_ML": ["Week11_Fraud_Detection", "Week12_TimeSeries"],
    "Phase7_Revision_Portfolio": ["Week13_Revision", "Week14_Portfolio"]
}

# Template content for README.md
readme_template = """# {folder_name}

**Goal / Objective:**  
Write a short description about the purpose of this folder/project.

**Tasks / Notes:**  
- Task 1  
- Task 2  
- Task 3

**References / Links:**  
- Add relevant links, datasets, or tutorials here
"""

# Create base folder
os.makedirs(base_dir, exist_ok=True)

# Loop through phases and weeks to create folders and README
for phase, weeks in phases.items():
    phase_path = os.path.join(base_dir, phase)
    os.makedirs(phase_path, exist_ok=True)
    
    # Create README for phase
    phase_readme_path = os.path.join(phase_path, "README.md")
    with open(phase_readme_path, "w") as f:
        f.write(readme_template.format(folder_name=phase))
    
    for week in weeks:
        week_path = os.path.join(phase_path, week)
        os.makedirs(week_path, exist_ok=True)
        
        # Create README for week
        week_readme_path = os.path.join(week_path, "README.md")
        with open(week_readme_path, "w") as f:
            f.write(readme_template.format(folder_name=week))

# Create Notes folder with README
notes_path = os.path.join(base_dir, "Notes")
os.makedirs(notes_path, exist_ok=True)
notes_readme_path = os.path.join(notes_path, "README.md")
with open(notes_readme_path, "w") as f:
    f.write(readme_template.format(folder_name="Notes"))

print(f"Directory structure with README.md created successfully in '{base_dir}'")
