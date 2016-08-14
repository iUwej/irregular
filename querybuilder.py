from collections import namedtuple
from abc import ABC, abstractmethod


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
Base class for all Filter clauses, provide a helper method to flatten it to an SQL statement.
Allows for a recursive definition of filter clauses
"""
class BaseFilter(ABC):
    @abstractmethod
    def unravel(self):
        pass
    

"""
Class that represents a simple SQL where clause, basic filter class
"""
class SimpleFilter(BaseFilter):

    def __init__(self,ineq):
        self.expression = ineq

    def unravel(self):
        pass

"""
class that represents a where filter with several inequalities joined by an  "and" clause
"""
class AndFilter(BaseFilter):
    def __init__(self,filters):
        self.filters = filters

    def unravel(self):
        pass


"""
class that represents a filter with several inequalities joined by an "or" clause
"""

class OrFilter(BaseFilter):
    def __init__(self,filters):
        self.filters = filters

    def unravel(self):
        pass
