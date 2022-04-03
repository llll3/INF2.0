with open('name.txt', 'r') as f1, open('numbers.txt', 'r') as f2, open('nanu.txt', 'w') as f3:
    for i, j in zip(f1.readlines(), f2.readlines()):
          f3.write(f'{i.strip()}: {j}')
