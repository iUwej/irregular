from collections import namedtuple



#Structure to carry our Inequalities for filter purposes
Ineq = namedtuple('Ineq',['col','op','value'])

# a representation of  a Join clause
Join = namedtuple('Join',['table1','table2','col1','col2'])

class Where(object):
    def __init__(self,exp):
        self.expression = exp 

class WhereAnd(object):
    def __init__(self,explist = []):

