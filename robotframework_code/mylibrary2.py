from robot.api import logger
		
class SubLibrary:
    def __init__(self,host,port):
        self.host = host
        self.port = port

    def printaddr(self):
        logger.console('host:%s,ip:%s' % (self.host,self.port))


    def returnint(self):
        return 3

    def _returnint2(self):
        return 4        