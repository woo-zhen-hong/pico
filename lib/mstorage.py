import ujson

class Storage:
    __instance__ = None
    
    @staticmethod
    def getInstance():
        if Storage.__instance__ == None:
            Storage.__instance__ = Storage(filename='/.storage')
        return Storage.__instance__
    
    def __init__(self, filename):
        self.__filename__ = filename
        try:
            with open(self.__filename__, 'r') as f:
                self.__data__ = ujson.loads(f.read())
        except:
            self.__data__ = {}
            
    def get(self, key):
        try:
            return self.__data__[key]
        except KeyError:
            return None
    
    def set(self, key, value):
        self.__data__[key] = value
        self.__save__()
            
            
    def remove(self, key):
        try:
            del self.__data__[key]
            self.__save__()
        except KeyError:
            pass
            
    def __save__(self):
        with open(self.__filename__, 'w') as f:
            f.write(ujson.dumps(self.__data__))
            f.flush()
        