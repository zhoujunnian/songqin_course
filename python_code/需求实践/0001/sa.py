# https://github.com/jcyrss/songqin-testdev/blob/master/python/task/task01.md

def getName(srcStr):
    return srcStr.split('the name is ')[1].split(',')[0]





testcases = [
    ('001 come in, the name is Jack, level 9;', 'Jack'),
    ('02 come in, the name is Clean, level 19;', 'Clean'),
    ('0233 come in, the name is Mike, level 330;', 'Mike'),
    ('A pretty boy come in, the name is Patrick, level 194;', 'Patrick')
]


def test(no, src, expectRet):
    try:
        ret = getName(src)
        if ret == expectRet:
            print('#temp {} pass'.format(no))
        else:
            print('#temp {} fail'.format(no))
    except:
        print('#temp {} fail with exception'.format(no))

    print('\n')


for idx, tc in enumerate(testcases):
    test(idx + 1, tc[0], tc[1])

