nba_ages = [
    ('Mike Jordan',19),
    ('Jason Kid',18),
    ('Lebron James',26),
    ('Korby Briant',16),
]


def  find_james():
    idx = 0
    while True:
        current = nba_ages[idx]
        name = current[0]
        age  = current[1]
        print(name, age)
        if name == 'Lebron James':
            print('!!!!!!!!!! 找到了, james年龄是 %d' % age)
            return
        idx += 1

    print('函数结尾')

find_james()