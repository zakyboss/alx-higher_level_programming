#!/usr/bin/python3
print(', '.join('{:02}'.format(i*10+j)
    for i in range(10) for j in range(i+1,10)),end='/n')
