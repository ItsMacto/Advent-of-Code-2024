from collections import Counter

def star1():
    left, right = [], []

    with open('input.txt') as f:
        data = f.read().splitlines()
        for i in data:
            l, r = i.split()
            # print(l, r)
            left.append(int(l))
            right.append(int(r))

    left.sort()
    right.sort()
    total = 0
    for l, r in zip(left,right):
        total += abs(l - r)
        
    return total
    # print(total)
    
def star2():
    left, right = [], []
    
    with open('input.txt') as f:
        data = f.read().splitlines()
        for i in data:
            l, r = i.split()
            left.append(int(l))
            right.append(int(r))
    
    leftCounter, rightCounter = Counter(left), Counter(right)
    
    total = 0 
    for key, val in leftCounter.items():
        total += key * val * rightCounter[key]
        
    return total
    

if __name__ == '__main__':
    print(star1())
    print(star2())
    
    