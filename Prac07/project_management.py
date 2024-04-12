import csv
from datetime import datetime

from project import Project

def load_projects(filename):
    """Load projects from a CSV file and return a list of Project objects."""
    projects = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip the header row
        for row in reader:
            name, start_date_str, priority, cost_estimate, completion_percentage = row
            start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
            projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
    return projects

def save_projects(projects, filename):
    """Save projects to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(["Name", "Start Date", "Priority", "Cost Estimate", "Completion Percentage"])
        for project in projects:
            writer.writerow([project.name, project.start_date.strftime("%d/%m/%Y"), project.priority,
                             project.cost_estimate, project.completion_percentage])

def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete_projects = [project for project in projects if project.completion_percentage < 100]
    completed_projects = [project for project in projects if project.completion_percentage == 100]
    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda x: x.priority):
        print(f"  {project}")
    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda x: x.priority):
        print(f"  {project}")

def filter_projects_by_date(projects, filter_date):
    """Filter projects that start after a given date."""
    filtered_projects = [project for project in projects if project.start_date > filter_date]
    for project in sorted(filtered_projects, key=lambda x: x.start_date):
        print(f"  {project}")

def add_project(projects):
    """Add a new project to the list."""
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yyyy): ")
    start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
    print("New project added successfully.")

def update_project(projects):
    """Update an existing project's completion percentage and/or priority."""
    print("Current projects:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    index = int(input("Project choice: "))
    project = projects[index]
    new_completion_percentage = input("New Percentage: ")
    if new_completion_percentage:
        project.completion_percentage = int(new_completion_percentage)
    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)
    print(f"{index} {project} updated successfully.")

def main():
    """Main function to manage projects."""
    projects = load_projects('projects.txt')
    print(f"Welcome to Pythonic Project Management\nLoaded {len(projects)} projects from projects.txt")
    while True
