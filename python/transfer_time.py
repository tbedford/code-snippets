# Python 2.7

fs = 1 # 1 in TBs
rate = 10 # in Mbps

print "Time to transfer a %d TB file at %d Mbps" % (fs, rate) 

fs = fs * 1000000000000 * 8 # convert to bits
rate = rate * 1000000 # convert to bps

time = fs / rate # in seconds

print "Transfer time in seconds:", time
print "Transfer time in minutes:", time / 60 
print "Transfer time in hours:", time / (60 * 60)
print "Transfer time in days:", time / (60 * 60 * 24)

