import importlib
import sys
import os
import traceback

BOILERPLATE = """from aoc2024.utils.utils import read_input

def star1():
    data = read_input()
    total = 0
    return total

def star2():
    data = read_input()
    total = 0
    return total

if __name__ == '__main__':
    print(star1())
    print(star2())
"""

def create_day(day_number):
    # Create the day directory
    day_dir = f"aoc2024/day{day_number}"
    if not os.path.exists(day_dir):
        os.makedirs(day_dir)
        print(f"Created directory: {day_dir}")

    # Create the Python file
    py_file = f"{day_dir}/day{day_number}.py"
    if not os.path.exists(py_file):
        with open(py_file, 'w') as f:
            f.write(BOILERPLATE)
        print(f"Created Python file: {py_file}")

    # Create empty input files
    input_file = f"{day_dir}/input.txt"
    test_file = f"{day_dir}/test.txt"
    
    for file in [input_file, test_file]:
        if not os.path.exists(file):
            with open(file, 'w') as f:
                pass  # Create empty file
            print(f"Created empty file: {file}")

    print(f"\nDay {day_number} setup complete! Files created:")
    print(f"- {py_file}")
    print(f"- {input_file}")
    print(f"- {test_file}")

def run_day(day_number):
    try:
        # Import the day's module dynamically
        day_module = importlib.import_module(f"aoc2024.day{day_number}.day{day_number}")
        
        # Run both stars
        print(f"Day {day_number}:")
        print(f"Star 1: {day_module.star1()}")
        print(f"Star 2: {day_module.star2()}")
        
    except ModuleNotFoundError as e:
        print(f"Error: Day {day_number} not found!")
        print(f"Details: {e}")
        create = input("Would you like to create it? (y/n): ").lower()
        if create == 'y':
            create_day(day_number)
    except AttributeError as e:
        print(f"Error running day {day_number}: {e}")
        print("Make sure the day's module has star1() and star2() functions")
    except Exception as e:
        print(f"\nAn unexpected error occurred while running day {day_number}:")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print("\nFull traceback:")
        print(traceback.format_exc())

def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python main.py <day_number>")
            print("Example: python main.py 1")
            return

        # Validate the input is actually a number
        if not sys.argv[1].isdigit():
            print("Error: Day must be a number")
            print(f"You provided: '{sys.argv[1]}'")
            return

        day = int(sys.argv[1])
        if day < 1 or day > 25:
            print("Error: Day must be between 1 and 25")
            print(f"You provided: {day}")
            return
            
        run_day(day)
        
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print("\nAn unexpected error occurred:")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {str(e)}")
        print("\nFull traceback:")
        print(traceback.format_exc())

if __name__ == "__main__":
    main()
