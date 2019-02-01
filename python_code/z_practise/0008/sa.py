# 先读取文件创建两张表(两个dict)，记录老师的 id:name
with open('records/course.txt',encoding='utf8') as f :
    courses = f.read().splitlines()[1:]

with open('records/teacher.txt',encoding='utf8') as f :
    teachers = f.read().splitlines()[1:]

courseDict = {}

for course in courses:
    if not course.strip():
        continue

    parts = course.split(';')
    courseId = parts[0]
    courseName = parts[1]
    courseDict[courseId] = courseName

teacherDict = {}
for teacher in teachers:
    if not teacher.strip():
        continue

    parts = teacher.split(';')
    teacherId = parts[0]
    teacherName = parts[4]
    teacherDict[teacherId] = teacherName


# 根据老师教学记录表， 将里面的id替换为 名字
with open('records/teacher_course.txt') as f :
    teacher_courses = f.read().splitlines()[1:]



with open('ret.txt','w',encoding='utf8') as f :
    for tc in teacher_courses:
        if not tc.strip():
            continue

        parts = tc.split(';')
        teacherId = parts[0]
        courseId = parts[1]

        if (teacherId not in teacherDict) or (courseId not in courseDict):
            print(f'skip record {tc}')

        ret = f"{teacherDict[teacherId]:10} : {courseDict[courseId]}"

        print(ret)

        f.write(ret+'\n')


