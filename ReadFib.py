import sys

def read_series(filename):
    try:
        with open(filename, mode = "rt", encoding="utf-8") as f:
            return [int(line.strip()) for line in f]
    finally:
        print("closed")
        f.close()
    

def main(filename):
    series = read_series(filename)
    print(series)

if __name__ == "__main__":
    main(sys.argv[1])

