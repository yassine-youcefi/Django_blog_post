import logging
clean_data = []

with open('test.txt','r') as F:
    data=F.readlines()
    print(data)
    for x in data:
        if x != '\n':
            clean_data.append(x)
        file_content = list(filter(''.__ne__ , clean_data))
    print(clean_data)
    print(file_content)

    with open('test_2.txt','w') as F:
        for line in file_content:
            F.writelines(line)
    print('ok')