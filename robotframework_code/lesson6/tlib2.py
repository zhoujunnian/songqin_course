from robot.api import logger

class SubLibrary:
    def returnint(self):
        return 3

    def _returnint2(self):
        return 4



class SubLibrary2:
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def printaddr(self):
        logger.console('host:%s,ip:%s' % (self.host,self.port))


class tlib2:
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def printaddr(self):
        logger.console('host:%s,ip:%s' % (self.host,self.port))


