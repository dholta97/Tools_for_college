z = str
fg = float
g = 0
yd = float
yt = 0
yp = 0
while z != "c":
    x = float(input("Enter your grade for this assignment: "))
    y = float(input("Enter the weight of this assignment: "))
    z = str(input("Press any key to move on, or c to calculate your final grade: "))
    yd = y / 100
    yp = yp + yd
    g = g + (x*yd)
    

    
if yp == 1:
    gf = g
elif yp != 1:
    gf = g/yp
 

print("You currently have a %.2f in this course." %gf)
