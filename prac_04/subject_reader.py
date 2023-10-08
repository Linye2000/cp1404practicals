"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"

def main():
    data = get_data()
    print(data)
    display_info(data)

def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data = []  # Create an empty list to store data
    for line in input_file:
        #print(line)  # See what a line looks like
        #print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        #print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        #print(parts)  # See if that worked
        #print("----------")
        data.append(parts)  # Add the processed part to the data list
    input_file.close()
    return data  # Returns a list containing data

def display_info(data):
    for subject_info in data:
        subject_code, lecturer, num_students = subject_info
        print(f"{subject_code} is taught by {lecturer} and has {num_students} students")


main()