
import numpy as np
q = []
correct_count = 0
for i in range(5):
  x = np.random.randint(3, 20)
  y = np.random.randint(6, 15)
  answer = int(input(str(x) + ' + ' + str(y) + ' = '))
  q.append([x, y, answer, x + y == answer])
  if answer == x + y:
    correct_count += 1
    print('Correct! {}/{}\n'.format(correct_count, i+1))
  else:
    print('Incorrect! {}/{}\n'.format(correct_count, i+1))

for i in q:
  print(i)
