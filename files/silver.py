import string


f1 = open('input.txt', 'r')
f2 = open('badwords.txt', 'r')
filedata = f1.read()
baddata = [badword.strip() for badword in f2]

words=[punc.strip(string.punctuation) for punc in filedata.split()]

newwords=[]
for word in words:
    newwords.append(word if word not in baddata else "*"*len(word))

f3 = open('output.txt', 'w')
for line in newwords:
    f3.write(line + ' ')

f1.close()
f2.close()
f3.close()



