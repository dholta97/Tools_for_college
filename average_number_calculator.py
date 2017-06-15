y = int(input("Enter a mnumber, or type -1 to quit: "))
sum1 = 0
cnt = 0

while y != -1:
    sum1 = sum1 + y
    cnt = cnt + 1
    y = int(input("Enter another number: "))
    
print ("The average of those %d numbers is %.4f" %(cnt,(sum1 / cnt)))

    


