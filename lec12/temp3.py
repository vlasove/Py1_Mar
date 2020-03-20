def is_pifagor(a:int, b:int, c:int) -> bool:
    return a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2+a**2 == b**2

answers = []

with open('problem.txt', 'r') as  fhandler:
    for line in fhandler.readlines():
        line = [int(x) for x in line.strip().split()] #'3 2 1' - > [3,2,1]
        if is_pifagor(line[0], line[1], line[2]):
            answers.append('Yes')
        else:
            answers.append('No')

with open('answer.txt', 'a') as fhandler:
    total ='\n'.join(answers)
    fhandler.write(total)
