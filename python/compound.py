pv = 200000.00
r = 0.07
t = 20
n = 1

fv = pv * (1 + r/n)**(n*t)
print ("First formula calculates fv to : %.2f" % fv)

fv = pv * (1 + r/n)**(n*1) # Year 1 only
print("Year %d : %.2f" % (1, fv))
for i in range (2, t+1):
    fv = fv * (1 + r/n)**(n*1) # Calculate one year at a time
    print("Year %d : %.2f" % (i, fv))
