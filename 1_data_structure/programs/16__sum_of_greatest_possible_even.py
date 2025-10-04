a=int(input("enter a number:"))
b=int(input("enter b number:"))
list_k =[]
list_sum =[]

for x in range (1,b+1):
    if b % x == 0:
        #print(x)
         list_k.append(x)
print(list_k)    

#print(list_k)
# loop through the list
for k in list_k:
    #print(k)
    a_new= a * k
    b_new = b/k
    
    sum= a_new + b_new
    print(f"new a {a_new} new b {b_new}, Sum of both {sum}")
    list_sum.append(sum)

# loop through the list
for s in list_sum:
    #print(s)
    if s % 2 == 0:
        print(f"Even{s}")
        largest=s
        if (s >largest):
            largest= s

print (f"largest even no is {largest}")

