#groupPickerBasic.py
import random
from sys import argv

script, filename = argv

file = open(filename)
list = file.read()
students = 0

for line in list:
    print line
    students += 1

print students
#
# picked = []
#
# studList = []
# for n in xrange(0,students):
#     studList.append(n)
#
# for x in xrange(0, students):
#     cont = True
#     clean = 0
#     for z in xrange(0,len(picked)):
#         if x == picked[z]:
#             cont = False
#     while cont == True:
#         clean = 0
#         rand = random.randrange(0,len(studList))
#         for y in xrange(0,len(picked)):
#             if rand == picked[y] or rand == x:
#                 clean += 1
#         if clean < 1:
#             picked.append(x)
#             picked.append(rand)
#             print "%s and %s" %(x, rand)
#             cont = False
#             break
