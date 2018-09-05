
domain = open('domain.txt', 'r+')
result = open('result.txt', 'w+')

for line in domain:
    result.write('www.%s' % line)
    result.write('*.%s' % line)
    result.write(line)
