import sys
from itertools import islice

def fibonacci():
    'Generates one Fibonacci number per call'
    yield 1
    yield 1
    a, b = 1, 1
    while True:
        c = a + b
        yield c
        a, b = b, c

def write_seq(filename, num):
    """ Write a sequence in a file """
    f = open(filename,mode = "wt", encoding="utf-8")
    f.writelines("{0}\n".format(numb) 
            for numb in islice(fibonacci(),num))
    f.close()

if __name__ == "__main__":
    print("calling")
    write_seq(sys.argv[1],int(sys.argv[2]))


