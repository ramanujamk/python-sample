import sys

for x in [1,2,3,4,5,6,6,7,8,9,10]:
    if x < 5:
        print(x,file = sys.stdout,flush = False)

sys.stdout.flush()