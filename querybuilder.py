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

    def to_sql(self):
        return "%s %s %s" % (self.col.to_sql(),self.op,self.value) 
        

n
"""
Represent a range clause. e.g.where col_name between value1 and value2"
"""
class Range(object):
    def __init__(self,col,min_value,max_value):
        self.col = col
        self.min_value = min_value
        self.max_value = max_value

    def to_sql(self):
        return "%s between %s and %s" % (self.col.to_sql(),self.min_value,self.max_value)


"""
Represent a join between two tables on t1.col1 t2.col2"
"""
class Join(object):
    def __init__(self,table,ref_table,col,ref_col):
        self.table = table
        self.ref_table = ref_table
        self.col = col
        self.ref_col = ref_col

    def to_sql(self):
        return "join %s on %s.%s = %s.%s" % (self.ref_table,self.ref_col,table.name,self.col.name)
        



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
        #find out the instance of the inequality
        

"""
class that represents a where filter with several inequalities joined by an  "and" clause
"""
class AndFilter(BaseFilter):
    def __init__(self,filters):
        self.filters = filters

    def unravel(self):
        output = [filter.unravel() for filter in self.filters]
        return 'and'.join(output)
            
            
        


"""
class that represents a filter with several inequalities joined by an "or" clause
"""

class OrFilter(BaseFilter):
    def __init__(self,filters):
        self.filters = filters

    def unravel(self):
        output = [filter.unravel() for filter in self.filters]
        return 'or'.join(output)

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

"""
Simple SQl query, all columns are drawn from the same table"
"""
class SimpleQuery(AbstractQuery):
    def __init__(self,table,cols = None,filters= None,group_by= None,order_by = None):
        self.table = table
        #if no cols are specified we shall assume all columns are required
        self.cols = cols if cols else []
        
        self.filters = filters if filters else []
        self.group_by = group_by if group_by else []
        self.order_by = group_by if group_by else []

        def to_sql(self):
            #will have to move this logic into a more generic class
            output = []
            output.append('select')
            #append cols sql code
            cols_count = len(self.cols)
            for i ,col in enumerate(self.cols):
                output.append(col.to_sql())
                if not cols_count == i + 1:
                    output.append(',')
            #unravel the filters and append to the output
            #i believe there's a more optimal solution if i dare scrath the surface
            
            #first flatten or filters into a single 'And' filter
            if self.filters:
                all_filters = AndFilter(self.filters)
                output.append('where')
                output.append(all_filters.unravel())

            #add the group_by sql
            
            
