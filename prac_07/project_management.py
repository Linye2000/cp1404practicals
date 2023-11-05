"""
Prac_07 project_management
"""


from project import Project

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""


def load_file(readable_file):
    """Loads inputted file"""
    my_projects = []
    opened_file = open(readable_file, 'r')
    opened_file.readline()
    for line in opened_file:
        parts = line.strip().split('\t')
        my_projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4])))
    opened_file.close()
    return my_projects


def save_to_file(writable_file, my_projects):
    """Saves to inputted file"""
    opened_file = open(writable_file, 'w')
    for i in range(len(my_projects)):
        print(my_projects[i].__repr__(), file=opened_file)


def display_projects(projects):
    """Displays inputted projects"""
    sorted_projects = sorted(projects)
    print("Incomplete projects:")
    for project in sorted_projects:
        if not project.is_completed():
            print(f"  {project}")
    print("Completed projects:")
    for project in sorted_projects:
        if project.is_completed():
            print(f"  {project}")

def update_project(projects):
    """updates one of the inputted projects"""
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    choice = int(input("Project choice: "))
    print(projects[choice])
    new_percentage = int(input("New Percentage: "))
    new_priority = input("New Priority: ")
    projects[choice].completion_percentage = new_percentage
    if new_priority:
        projects[choice].priority = int(new_priority)
    return projects

def add_new_project():
    """Adds new project using return"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date_str = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = int(input("Percent complete: "))
    return Project(name, start_date_str, priority, cost_estimate, completion_percentage)


def main():
    my_projects = []
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "L":
            file = input("FileName: ")
            my_projects = load_file(file)
        elif choice == "S":
            file = input("FileName: ")
            save_to_file(file, my_projects)
        elif choice == "D":
            display_projects(my_projects)
        elif choice == "F":
            display_filtered_projects(my_projects, input("Date "))
        elif choice == "A":
            my_projects.append(add_new_project())
        elif choice == "U":
            my_projects = update_project(my_projects)
        print(MENU)
        choice = input(">>> ").upper()


main()