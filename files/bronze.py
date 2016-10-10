f = open('input.txt','r')
f1 = open('output.txt','w')
for line in f.readlines():
    f1.write(line)

f.close()
f1.close()
