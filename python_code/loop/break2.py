nba_ages = [
    ('Mike Jordan',19),
    ('Jason Kid',18),
    ('Korby Briant',16),
    ('Lebron James',26),
    ('Korby Briant4',16),
    ('Korby Briant5',16),
    ('Korby Briant6',16),
    ('Korby Briant7',16),
    ('Korby Briant7', 16),
    ('Korby Briant8',16),
    ('Korby Briant9',16),
    ('Korby Briantk',16)
]


idx = 0
while True:
    current = nba_ages[idx]
    name = current[0]
    age  = current[1]
    print(name, age)
    if name == 'Lebron James':
        print('!!!!!!!!!! 找到了, james年龄是 %d' % age)
        break
    idx += 1