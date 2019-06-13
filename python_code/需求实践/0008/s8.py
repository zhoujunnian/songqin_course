# coding=utf8
# 分别根据 老师、课程文件产生 两个字典 courseDict 、 teacherDict
import pprint
with open('records/course.txt') as f:
    courses = f.read().splitlines()[1:]
    courseDict = {}
    for one in courses:
        parts = one.split(';')
        courseId = parts[0]
        courseName = parts[1]
        courseDict[courseId] =  courseName

with open('records/teacher.txt') as f:
    teachers = f.read().splitlines()[1:]
    teacherDict = {}
    for one in teachers:
        parts = one.split(';')
        tId = parts[0]
        tName = parts[4]
        teacherDict[tId] =  tName

# 根据 老师 授课 文件 ，读取信息，查找 两个字典 获取 老师、课程的名字

outDict = {}
with open('records/teacher_course.txt') as f, open('ret.txt','w') as fw:
    teacher_course = f.read().splitlines()[1:]

    for one in teacher_course:
        teacherId,courseId = one.split(';')

        if (teacherId not in teacherDict)  or (courseId not in courseDict):
            continue

        teacherName = teacherDict[teacherId]
        courseName = courseDict[courseId]
        ret = '{}:{}'.format(teacherName, courseName)

        if teacherName not in outDict:
            outDict[teacherName]  = [courseName]
        else:
            outDict[teacherName].append(courseName)


        # fw.write(ret +'\n')

# pprint.pprint(outDict)

for key,value in outDict.items():
    print key
    for one in value:
        print '     ' + one

    print '-----------------------\n'

