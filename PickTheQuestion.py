import csv
import random


while True:
    x = int(input('Number of questions printed: '))
    if x <= 0:
        print('Go perform your testing stuff somewhere else')
    with open('questions_list.csv', newline='') as cf:
        question_reader = csv.reader(cf)
        m = list(question_reader)
        repeat = []
        while x > len(repeat):
            z = m[random.randint(1, len(m))]
            if z in repeat:
                continue
            else:
                repeat.append(z)

            print('Q',z[0],':',z[1],'\n ')
    l = input('More questions? (y/n): ')
    if l == 'n':
        break
    elif l == 'y':
        continue
