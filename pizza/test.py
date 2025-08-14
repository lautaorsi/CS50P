import sys
from tabulate import tabulate

table = []
file = open(sys.argv[1], "r")
for line in file:
    table.append(line.split(','))
headers = table[0]
headers[len(headers)-1] = (headers[len(headers)-1]).replace('\n', '')
del table[0]


print(tabulate(table, headers))