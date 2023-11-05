"""
Prac_07 project
"""


class Project:
    """Creates class"""

    def __init__(self, name="", start_date_str="", priority=0, cost_estimate=0, completion_percentage=0):
        """Initialise project"""
        self.name = name
        self.start_date_str = start_date_str
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

        # Parsing the start date
        day, month, year = start_date_str.split("/")
        self.start_date = datetime(int(year), int(month), int(day))

    def __repr__(self):
        """repr of project info"""
        return f"{self.name}\t{self.start_date_str}\t{self.priority}\t${self.cost_estimate:.2f}\t{self.completion_percentage}%"

    def __str__(self):
        """String of project info"""
        return (f"{self.name}, start: {self.start_date_str}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Sort by priority (ascending) and start date (ascending)"""
        if self.priority != other.priority:
            return self.priority < other.priority
        else:
            return self.start_date < other.start_date

    def is_completed(self):
        """return True if percentage is 100"""
        return self.completion_percentage == 100