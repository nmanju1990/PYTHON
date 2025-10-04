n = int(input("No of records to enter => "))
records = []

# take input
for _ in range(n):
    name = input("Enter Name  => ")
    score = float(input("Enter Score => "))
    records.append([name, score])

print(records) 
#  => [['Man', 24.0], ['jk', 25.0]]

#  => [
#      ['Man', 24.0], 
#      ['jk', 25.0]
#     ]

#print( records[0][0])
#print( records[0][1])
#print( records[1][0])
#print( records[1][1])
# for name, score in records:
#     print(name, score)

for n, s in records:
    print(n, s)

# find unique scores and sort them
scores = []
for _, s in records:
    if s not in scores:
        scores.append(s)
scores.sort()
print(scores)

second_lowest = scores[1]   # 2nd lowest score

# collect names with that score
names = []
for name, s in records:
    if s == second_lowest:
        names.append(name)
print(names)       

for name in sorted(names):
    print(name)
