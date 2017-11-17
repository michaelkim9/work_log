# Imports
import csv
import re
import os

from tasks import Task


def clear_screen():
    '''Clears the command screen'''
    os.system('cls' if os.name == 'nt' else 'clear')


# This class has methods to search based on different parameters
class Search:
    def __init__(self):
        self.results = []
        with open('work_logs.csv', 'r', newline='') as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                self.results.append(row)

    def exact_date(self):
        '''List of tasks by date. Choose a date'''
        count = 1
        print('Please choose from the following dates.')
        for row in self.results:
            print('{}. {}: {}'.format(count, row['date'], row['task_name']))
            count += 1
        selected_date = input('Which date?\n> ')

        clear_screen()
        try:
            selected_date = int(selected_date)
        except ValueError:
            clear_screen()
            print('Not a valid selection\n')
            return self.exact_date()

        if selected_date <= 0:
            clear_screen()
            print('Not a valid selection\n')
            return self.exact_date()
        elif selected_date > count:
            clear_screen()
            print('Not a valid selection\n')
            return self.exact_date()

        try:
            task = Task(self.results[selected_date - 1]['date'],
                        self.results[selected_date - 1]['first_name'],
                        self.results[selected_date - 1]['last_name'],
                        self.results[selected_date - 1]['task_name'],
                        self.results[selected_date - 1]['time_elapsed'],
                        self.results[selected_date - 1]['notes'])
        except IndexError:
            clear_screen()
            print('Not a valid selection\n')
            return self.exact_date()
        clear_screen()
        print(task)
        input('Press any key to continue')
        clear_screen()

    def exact_input(self):
        '''Lists tasks by search term and chooses one'''
        search_string = input('Search task: ').lower()
        input_results = []
        count = 1
        clear_screen()
        for row in self.results:
            if search_string in row['task_name'].lower():
                input_results.append(row)
            elif search_string in row['notes'].lower():
                input_results.append(row)
        if len(input_results) == 0:
            print('{} not found in tasks or notes.'.format(search_string))
            return self.exact_input()
        print('Please choose task to view:')

        for row in input_results:
            print('{}. {}'.format(count, row['task_name']))
            count += 1
        selected_task = input('Which entry would you like to see?\n> ')
        clear_screen()

        try:
            selected_task = int(selected_task)
        except ValueError:
            clear_screen()
            print('Not a valid input, please try again.')
            return self.exact_input()

        try:
            task = Task(input_results[selected_task - 1]['date'],
                        input_results[selected_task - 1]['first_name'],
                        input_results[selected_task - 1]['last_name'],
                        input_results[selected_task - 1]['task_name'],
                        input_results[selected_task - 1]['time_elapsed'],
                        input_results[selected_task - 1]['notes'])
        except IndexError:
            clear_screen()
            print('Not a valid input, please try again.')
            return self.exact_input()

        clear_screen()
        print(task)
        input('Press any key to continue')
        clear_screen()

    def input_pattern(self):
        '''Lists tasks by regular expression input'''
        clear_screen()
        input_results = []
        count = 1
        while True:
            search_pattern = input('Search by RegEx pattern.\n'
                                   'Press "Q" to quit.\n'
                                   'RegEx Pattern > ')
            if search_pattern.upper() == 'Q':
                break

            for row in self.results:
                if (re.search(r'{}'.format(search_pattern), row['task_name'])):
                    input_results.append(row)
                elif (re.search(r'{}'.format(search_pattern), row['notes'])):
                    input_results.append(row)

            if input_results:
                print('Tasks available based on your search pattern:')
                for row in input_results:
                    print('{}. {}'.format(count, row['task_name']))
                    count += 1
                selected_task = input('Which entry would you like to see?\n> ')
                clear_screen()
            else:
                clear_screen()
                print('No matches found for {}'.format(search_pattern))
                break

            try:
                selected_task = int(selected_task)
            except ValueError:
                clear_screen()
                print('Not a valid selection')
                break
            try:
                task = Task(input_results[selected_task - 1]['date'],
                            input_results[selected_task - 1]['first_name'],
                            input_results[selected_task - 1]['last_name'],
                            input_results[selected_task - 1]['task_name'],
                            input_results[selected_task - 1]['time_elapsed'],
                            input_results[selected_task - 1]['notes'])
            except IndexError:
                clear_screen()
                print('Not a valid selection')
                break
            clear_screen()
            print(task)
            break
        input('Press any key to continue')
        clear_screen()
