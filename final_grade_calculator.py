c = float(input("Enter your current grade percentage: "))
e = float(input("Ente what grade you want: "))
w = float(input("Enter what your final is worth: "))
cd = c/100
ed = e/100
wd = w/100
f = (ed - (cd*(1-wd))) /wd
fg = f * 100
print ("You need to get a %.2f on your final exam to get a %.2f in the class" %(fg,e))
