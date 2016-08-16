from collections import namedtuple
from abc import ABC, abstractmethod
from enum import Enum



"""
corresponds to sql aggregate functions
"""
class AggFunctions(Enum):
    avg = "avg"
    count = "count"
    first = "first"
    last = "last"
    smax = "max"
    smin = "min"
    ssum = "sum"

"""
enum values that corresponds to sql scala functions
"""
class ScalaFunctions(Enum):
    ucase = "ucase"
    lcase = "lcase"
    mid = "mid"
    s_len = "len"
    s_round = "round"
    s_now = "now"
    s_format = "format"

class Ops(Enum):
    eq = "="
    isnot = "is not"
    neg = "!="
    lt = "<"
    gt = ">"
    atmost = "<="
    atleast = ">="
    member = "in"
    
    

#Structure to carry our Inequalities for filter purposes
"""
class that represents an SQL query filter relation such as "id = 23"
"""
class Relation(object):
    def __init__(self,col,op,value):
        self.col = col
        self.op = op
        self.value = value 



"""
Represent a range clause. e.g.where col_name between value1 and value2"
"""
class Range(object):
    def __init__(self,col,min_value,max_value):
        self.col = col
        self.min_value = min_value
        self.max_value = max_value


"""
Represent a join between two tables on t1.col1 t2.col2"
"""
class Join(object):
    def __init__(self,table,ref_table,col,ref_col):
        self.table = table
        self.ref_table = ref_table
        self.col = col
        self.ref_col = ref_col




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

"""
Filter for aggregated columns
"""
class HavingFilter(BaseFilter):
    def __init__(self,ineq):
        self.ineq = ineq

    def unravel(self):
        pass


"""
Base class for query builders"
"""
class AbstractQuery(ABC):
    
    @abstractmethod
    def to_sql(self):
        pass
