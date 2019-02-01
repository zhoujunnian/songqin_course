
def statmf(students,minage=18):
    print(f'\ncheck those ages >= {minage}' )
    malelist = []
    femalelist = []
    for student in students:
        if student['age'] >= minage:
            if student['gender'] == 'male':
                malelist.append(student['name'])
            elif student['gender'] == 'female':
                femalelist.append(student['name'])

    print('the male students   are %s' % ' '.join(malelist))
    print('the female students are %s' % ' '.join(femalelist))


students = [
    {'age':18,'name':'jcy1', 'gender':'male'},
    {'age':20,'name':'jcy2', 'gender':'female'},
    {'age':18,'name':'jcy3', 'gender':'male'},
    {'age':21,'name':'jcy4', 'gender':'female'},
    {'age':22,'name':'jcy5', 'gender':'male'},
]

statmf(students,20)
# statmf(students,20)