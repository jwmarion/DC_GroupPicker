#newGroupPicker

import sys, random


with open("studentList.txt") as inp:
    studentList= list(inp.read().splitlines())

inp2 = open("pastGroups.txt", 'a+')
inp2.seek(0)
pastGroups = list(inp2.read().splitlines())
inp.close()
inp2.close()

def checkGroup(group):
    if group[0] == group[1]:
        return False
    else:
        if len(pastGroups) != 0:
            for x in range(len(pastGroups)):
                if group == pastGroups[x]:
                    return False
                else:
                    return True
        else:
            return True


def pickGroup():
    ran = len(studentList)
    r1 = random.randrange(0,ran)
    r2 = random.randrange(0,ran)
    return [studentList[r1],studentList[r2]]

for x in range(len(studentList) / 2):
    while True:
        group = pickGroup()
        t = checkGroup(group)
        if t == True:
            break
    print "Group %i:  %s and %s" %(x +1, group[0], group[1])
    studentList.remove(group[0])
    studentList.remove(group[1])
    pastGroups.append(group)

with open("pastGroups.txt",'a') as app:
    for x in range(len(pastGroups)):
        app.write(str(pastGroups[x]) + "\n")
app.close()
# inp2.write(pastGroups)
# inp2.close()
