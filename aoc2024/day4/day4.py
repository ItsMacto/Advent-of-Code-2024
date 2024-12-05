from aoc2024.utils.utils import grid_rotate, read_input

def star1():
    data = read_input()
    total = 0

    # for i in range(4):
        
    for i in range(len(data)):
        for j in range(len(data[1]) - 3):
            if data[i][j] == 'X' and data[i][j+1] == 'M' and data[i][j+2] == 'A' and data[i][j+3] == 'S':
                total += 1
            if data[i][j] == 'S' and data[i][j+1] == 'A' and data[i][j+2] == 'M' and data[i][j+3] == 'X':
                total += 1
    for i in range(len(data) - 3):
        for j in range(len(data[1])):
            if data[i][j] == 'X' and data[i+1][j] == 'M' and data[i+2][j] == 'A' and data[i+3][j] == 'S':
                total += 1
            if data[i][j] == 'S' and data[i+1][j] == 'A' and data[i+2][j] == 'M' and data[i+3][j] == 'X':
                total += 1
            
    for i in range(len(data) - 3):
        for j in range(len(data[1]) - 3):
            if data[i][j] == 'X' and data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S':
                total += 1
            if data[i][j] == 'S' and data[i+1][j+1] == 'A' and data[i+2][j+2] == 'M' and data[i+3][j+3] == 'X':
                total += 1
            if data[i][j+3] == 'X' and data[i+1][j+2] == 'M' and data[i+2][j+1] == 'A' and data[i+3][j] == 'S':
                total += 1
            if data[i][j+3] == 'S' and data[i+1][j+2] == 'A' and data[i+2][j+1] == 'M' and data[i+3][j] == 'X':
                total += 1
    # data = grid_rotate(data)
    # print(total)
    
    return total

    
def star2():
    with open('input.txt') as f:
        data = f.read().splitlines()
        
        
    return
    

if __name__ == '__main__':
    print(star1())
    # print(star2())
    
    