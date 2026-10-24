## Menu-driven launcher to run the practice programs in this repository
import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

## Each entry is (menu label, folder, script file)
PROGRAMS = [
    ("Dijkstra's shortest path", 'Djikstra code', 'djikstra.py'),
    ('Man-Cabbage-Goat-Wolf puzzle', 'Man Cabbage Goat Wolf Puzzle', 'Man_Cabbage_Goat_Wolf_puzzle.py'),
    ('Factorial of a number', 'Program to find factorial', 'factorial.py'),
    ('Tower of Hanoi (3 disks)', 'Tower of Hanoi', 'Hanoi problem.py'),
]

## Prints the menu of available programs
def show_menu():
    print('\n' + format('Python Practice Code', '^60'))
    print(format('', '-<60'))
    for number, (label, _, _) in enumerate(PROGRAMS, start=1):
        print('%d. %s' % (number, label))
    print('q. Quit')

## Runs the chosen program from its own folder so relative paths keep working
def run_program(folder, script):
    folder_path = os.path.join(BASE_DIR, folder)
    print(format('', '-<60'))
    subprocess.run([sys.executable, script], cwd=folder_path)
    print(format('', '-<60'))

def main():
    while True:
        show_menu()
        try:
            choice = input('Choose a program: ').strip().lower()
        except EOFError:
            break
        if choice == 'q':
            break
        if choice.isdigit() and 1 <= int(choice) <= len(PROGRAMS):
            _, folder, script = PROGRAMS[int(choice) - 1]
            run_program(folder, script)
        else:
            print('Invalid choice, please try again.')
    print('Goodbye!')

if __name__ == '__main__':
    main()
