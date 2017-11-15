# Imports
import csv
import os
import datetime

from tasks import Task
from search import Search


# Formatting for date
date_format = '%m%d%Y'
# Fields that will be used
fields = [
    'first_name',
    'last_name',
    'time_elapsed',
    'date',
    'task_name',
    'notes'
]


def clear_screen():
    '''Clears the command screen'''
    os.system('cls' if os.name == 'nt' else 'clear')
