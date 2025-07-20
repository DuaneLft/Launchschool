forenames = ['Ken', 'Lynn', 'Pat',' Nancy']
surenames = ['Camp', 'Blake', 'Flanagan', 'Short']
index = 0
while index < len(forenames):
    if index >= len(surenames):# surnames might be shorter
        break
    forename = forenames[index]
    surename = surenames[index]
    print(f'{forename} {surename}')
    index += 1

zipped_names = zip(forenames, surenames)
for forename, surename in zipped_names:
    print(f'{forename} {surename}')
    