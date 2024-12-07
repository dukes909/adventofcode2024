
# Day 1 Part 2s Historian Hysteria
list1 = []
list2 = []
list1_min = 0
list2_min = 0
distance = 0
sum = 0
with  open("c:/Users/bopalko.LAFAYETTE/Desktop/Python/advent of code 2024/day 1/day1-1.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
        linesplit = line.split()
        list1.append(linesplit[0])
        list2.append(linesplit[1])

for i in list1:
    countitem = list2.count(i)
    print(i, countitem)
    sum += int(i) * int(countitem)

print(sum)
  


#while list1:
#    list1_min = int(min(list1))
#    list2_min = int(min(list2))
#    distance = abs(list1_min - list2_min)
#    print(str(list1_min) + " " + str(list2_min) + " " + str(distance))
#    sum += distance
#    list1.remove(str(list1_min))
#    list2.remove(str(list2_min))

#print(sum)
