infile = open('hardlopers.txt', 'r')
lines = infile.readlines()
infile.close()

for line in lines:
    kaartinfo = line.split(',')
    print('De hardloper: ' + kaartinfo[2].strip() + ' liept in : ' + kaartinfo[1].strip() + ' ' + kaartinfo[0].strip())
