import importlib
import sys

def run_day(day_number):
    try:
        # Import the day's module dynamically
        day_module = importlib.import_module(f"aoc2024.day{day_number}.day{day_number}")
        
        # Run both stars
        print(f"Day {day_number}:")
        print(f"Star 1: {day_module.star1()}")
        print(f"Star 2: {day_module.star2()}")
        
    except ModuleNotFoundError:
        print(f"Day {day_number} not found!")
    except AttributeError as e:
        print(f"Error running day {day_number}: {e}")
        print("Make sure the day's module has star1() and star2() functions")

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <day_number>")
        print("Example: python main.py 1")
        return

    try:
        day = int(sys.argv[1])
        if day < 1 or day > 25:
            print("Day must be between 1 and 25")
            return
        run_day(day)
    except ValueError:
        print("Day must be a number")

if __name__ == "__main__":
    main()
