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


def new_task():
    '''Records each input for new tasks'''
    clear_screen()
    # first name input
    first_name = input('What is your first name?\n> ')
    clear_screen()
    # last name input
    last_name = input('What is your last name?\n> ')
    clear_screen()
    # task input
    task_name = input('What is the task?\n> ')
    clear_screen()
    # time elapsed and check validity
    time_elapsed = None
    while not time_elapsed:
        try:
            time_elapsed = int(input('Minutes spent on task?\n> '))
        except ValueError:
            print('Not a valid entry.')
            continue
    clear_screen()
    # notes input
    notes = input('Enter any additional notes.\n> ')
    clear_screen()
    # date of entry
    date = datetime.datetime.today().strftime(date_format)
    task = Task(date,
                first_name,
                last_name,
                task_name,
                str(time_elapsed),
                notes)
    # save entry
    task.save()
    return task


def start():
    '''Creates csv file if it doesn't exist'''
    try:
        with open('work_logs.csv', 'x') as file:
            write = csv.DictWriter(file, fieldnames=fields)
            write.writeheader()
        input('Welome to Work Logs! Press any key to begin.')
        task = new_task()
        clear_screen()
        print('Task has been added!\n')
        print(task)
        input('\nPress any key to continue.')
    except FileExistsError:
        pass


def menu():
    '''Initial menu when running the program'''
    while True:
        print('Make a selection (1, 2 or 3):')
        print('1: Search\n'
              '2: Log New Task\n'
              '3: Quit\n')
        selected_menu = input('> ')
        if selected_menu == '3':
            clear_screen()
            quit()
        elif selected_menu == '2':
            clear_screen()
            task = new_task()
            print('Task has been added!\n')
            print(task)
            input('\nPress any key to continue')
            clear_screen()
        elif selected_menu == '1':
            clear_screen()
            search_menu()
        else:
            clear_screen()
            print('Not a valid selection. Please choose 1, 2 or 3')
            continue


def search_menu():
    '''menu to search items'''
    search = Search()
    while True:
        print('How would you like to search?\n'
              '1: Exact Date\n'
              '2: Exact input\n'
              '3: Input pattern\n'
              '4: Exact minutes elapsed\n'
              '5: Return to main menu\n')
        selected_menu = input('> ')
        if selected_menu == '1':
            search.exact_date()
        elif selected_menu == '2':
            search.exact_input()
        elif selected_menu == '3':
            search.input_pattern()
        elif selected_menu == '4':
            search.exact_minutes()
        elif selected_menu == '5':
            clear_screen()
            menu()
        else:
            clear_screen()
            print('Not a valid selection. Please try again.')
            continue


if __name__ == '__main__':
    start()
    menu()
