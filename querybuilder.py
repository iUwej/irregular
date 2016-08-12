from collections import namedtuple



#Structure to carry our Inequalities for filter purposes
Ineq = namedtuple('Ineq',['col','op','value'])

"""
Represent a range clause. e.g.where col_name between value1 and value2"
"""
Range = namedtuple('Range',['col','inital_value','final_value'])

"""
Represent a join between two tables on t1.col1 t2.col2"
"""
Join = namedtuple('Join',['table1','table2','col1','col2'])

"""
Represents an in clause in SQL for a col that matches any
of the value in the set
"""
In = namedtuple('In',['col','values'])


"""
Class that represents a simple SQL where clause, basic filter class
"""
class Where(object):
    def __init__(self,exp):
        self.expression = exp 
"""
A Class that holds a list of inequalities. Filter clause for records
matching all conditions
"""
class WhereAnd(object):
    def __init__(self,explist = []):
        self.expressions = explist

"""
A class that holds a list of inequalities. Represents a filter clause
for records that match any of the conditions
"""
class WhereOr(object):
    def __init__(self,explist = []):
        self.expressions = explist


