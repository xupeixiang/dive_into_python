import sys

print 'Dive In'
saveout = sys.stdout
fsock = open('out.log', 'w')
#redirect
sys.stdout = fsock
print 'This message will be logged instead of displayed'
#back
sys.stdout = saveout
fsock.close()