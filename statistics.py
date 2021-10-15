

class Statistics:
    def __init__(self):
        self.stat={
            'python':0,
            'sql': 0,
            'django': 0,
            'rest': 0,
            'c++': 0,
            'linux': 0,
            'api': 0,
            'http': 0,
            'flask': 0,
            'java': 0,
            'git': 0,
            'javascript': 0,
            'pytest': 0,
            'postgresql': 0,
            'oracle': 0,
            'mysql': 0,
            'mssql': 0
        }

    def go_seek( self, s ):
        n = 0
        try:
            s = s.lower()
            k = self.stat.keys()
            for ki in k:
                i = s.find(ki)
                if i > 0:
                    self.stat[ki] += 1
                    n += 1
        except AttributeError:
            pass
        return n

    def get_stat( self ):
        sorted_tuple = sorted( self.stat.items(), key=lambda x: x[1], reverse=True )
        return sorted_tuple

    def processing(self):
        #count = len( self.stat )

        nMax = self.get_stat()[0][1]

        dic = {}
        for k,v in self.stat.items():
            dic[ k ] = [ v, round(  (v/nMax)*100  )]

        sorted_tuple = sorted(  dic.items(), key=lambda x: x[1][1], reverse=True)

        lst = []
        for k,v in sorted_tuple:
            lst.append( [k,str(v[1])+'%'] )

        return lst