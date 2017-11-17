# Imports
import csv


class Task:
    def __init__(self, date, first_name, last_name, task_name,
                 time_elapsed, notes=None):
        self.date = date
        self.first_name = first_name
        self.last_name = last_name
        self.task_name = task_name
        self.time_elapsed = time_elapsed
        self.notes = notes

        self.fields = [
            'first_name',
            'last_name',
            'time_elapsed',
            'date',
            'task_name',
            'notes'
        ]

    def __str__(self):
        '''Returns task in string format'''
        str_format = (
                'Date: {}\n'
                'Task Name: {}\n'
                'First Name: {}\n'
                'Last Name: {}\n'
                'Time Spent: {}\n'
                'Notes: {}\n'
                )
        return str_format.format(self.date, self.task_name,
                                 self.first_name, self.last_name,
                                 self.time_elapsed, self.notes)

    def save(self):
        '''Saves to file'''
        with open('work_logs.csv', 'a', newline='') as log:
            write = csv.DictWriter(log, fieldnames=self.fields)
            write.writerow({
                'first_name': self.first_name,
                'last_name': self.last_name,
                'task_name': self.task_name,
                'time_elapsed': self.time_elapsed,
                'notes': self.notes,
                'date': self.date
                })
