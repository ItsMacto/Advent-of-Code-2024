

def star1():
    with open('input.txt') as f:
        data = f.read().splitlines()

    data = [list(map(int, x.split())) for x in data]
    total = 0

    for report in data:
        # print(report)
        safe = True
        if report[0] < report[1]:
            for i in range(1, len(report)):
                diff = report[i] - report[i-1]
                if diff > 3 or diff < 1:
                    safe = False
                    break
        else:
            for i in range(1, len(report)):
                diff = report[i-1] - report[i]
                if diff > 3 or diff < 1:
                    safe = False
                    break
        if safe:
            # print('safe')
            total += 1
        
    return total

    
def star2():
    with open('test.txt') as f:
        data = f.read().splitlines()

    data = [list(map(int, x.split())) for x in data]
    total = 0
    updated = []
    for report in data:
        print(report)
        safe = True
        if report[0] < report[1]:
            for i in range(1, len(report)):
                diff = report[i] - report[i-1]
                if diff > 3 or diff < 1:
                    safe = False
                    report.pop(i - 1)
                    updated.append(report)
                    break

                    
        else:
            for i in range(1, len(report)):
                diff = report[i-1] - report[i]
                if diff > 3 or diff < 1:
                    safe = False
                    report.pop(i - 1)
                    updated.append(report)
                    break
        if safe:
            print('safe', safe)
            total += 1
            
            
    for report in updated:
        # print(report)
        safe = True
        if report[0] < report[1]:
            for i in range(1, len(report)):
                diff = report[i] - report[i-1]
                if diff > 3 or diff < 1:
                    safe = False
                    # report.pop(i - 1)
                    # updated.append(report)
                    break

                    
        else:
            for i in range(1, len(report)):
                diff = report[i-1] - report[i]
                if diff > 3 or diff < 1:
                    safe = False
                    # report.pop(i - 1)
                    # updated.append(report)
                    break
        if safe:
            print('safe', safe)
            total += 1

    return total
    

if __name__ == '__main__':
    print(star1())
    print(star2())
    
    