import time
outfile = open('hardlopers.txt', 'w')
hardloper = ''
while hardloper != 'end':
    hardloper = input('Voert u de naam van de harloper in: ')
    if hardloper != 'end':
        outfile.write(time.strftime("%a %d %b %Y") + ', ' + time.strftime("%H:%M:%S") + ', ' + hardloper + '\n')
    else:
        outfile.close()
