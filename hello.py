import sys

def readfile(filename):
    with open(filename, mode = "r", encoding='utf-8') as f:
        for line in f.readlines():
            sys.stdout.write(line)

    
  
def main(filename):
    readfile(filename)

try:
    if __name__ == '__main__':
        main(sys.argv[1])
except IndexError:
    sys.stderr.write("no parameters passed")

except FileNotFoundError as e:
    sys.stderr.write("File {} not found".format(e.filename))
  

