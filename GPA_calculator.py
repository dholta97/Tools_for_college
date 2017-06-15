
cred = float
cred = 0
z = str
GPA = float
qpts = float
gpts = float
total_qpts = 0

while z != "quit":
    x = str(input("Enter your grade for your class: ")) 
    y = float(input("Enter the credits for this class: "))
    if x == "A":
        gpts = 4
    elif x == "B":
        gpts = 3
    elif x ==  "C":
        gpts = 2
    elif x == "A-":
        gpts = 3.7
    elif x == "B+":
        gpts = 3.33
    elif x ==  "C+":
        gpts = 2.3
    elif x == "D":
        gpts = 1
    elif x == "B-":
        gpts = 2.7
    elif x ==  "C-":
        gpts = 1.7
    elif x == "D+":
        gpts = 1.3
    elif x ==  "D-":
        gpts = .7

    qpts = gpts * y
    total_qpts = total_qpts + qpts
    cred = cred + y
    GPA  = (total_qpts)/cred
    z = str(input("Type quit to Exit: "))

print ("You are enrolled in %d credits. Your GPA for this semester will be %.4f " %(cred, GPA))
