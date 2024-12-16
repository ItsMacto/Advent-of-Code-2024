from aoc2024.utils.utils import read_input

def star1():
    def bfs(number, index, operation, target):
        if operation == '+':
            number += numbers[index]
        elif operation == '*':
            number *= numbers[index]
        
        if number == target:
            return True
        index += 1
        if index == len(numbers):
            return False
        # print(number, index, operation, target)
        return bfs(number, index, '+', target) or bfs(number, index, '*', target)
    
    data = read_input()
    total = 0
    for line in data:
        target, numbers = line.split(":")
        target = int(target)
        numbers = list(int(number) for number in numbers.split(" ")[1:])
        if bfs(numbers[0], 1, '+', target) or bfs(numbers[0], 1, '*', target):
            total += target
    return total

def star2():
    data = read_input()
    total = 0
    return total

if __name__ == '__main__':
    print(star1())
    print(star2())
