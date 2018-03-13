import sys

msg = 'hello world'
f = open('file.txt','r')

d = dict()

for line in f:
    print(line)
    for word in line.split():
        print(word)
        d[word] = d.setdefault(word,0)+1

    for word, count in sorted(d.items(), key=lambda x: x[1]):
        print('{} {}'.format(count, word))


f.close



