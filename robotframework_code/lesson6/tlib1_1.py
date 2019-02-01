from  robot.api.deco import  keyword

@keyword('Hello')
def returnlist():
    return [1,2]

def _returnlist2():
    return [1,2]
