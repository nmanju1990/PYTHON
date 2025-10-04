if __name__ == '__main__':
    #n = int(input("enter a number:").strip())
    n = int(input().strip())

    if 100 >= n >= 1:
        if n%2==1:
            print("Weird")
        elif 2<=n<=5:
            print("Not Weird")
        elif 6<=n<=20:
            print("Weird") 
        else:
            print("Not Weird")    
