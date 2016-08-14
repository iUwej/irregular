
from collections import namedtuple

"""
class that correspond to a SQL table
"""
class Table(object):
    def __init__(self,name,cols=[]):
        self.name = name
        self.columns = cols

    def add_column(self,col):
        self.columns.append(col)

"""
class that represents a generic SQL column
"""
class Column(object):
    def __init__(self,name,table,dtype):
        self.name = name
        #i thought this might be nessary
        # but then again each table has a list of columns
        self.table = table
        self.data_type = dtype        

"""
class that represents a foreign key relation in a table
"""
class ForeignKeyColumn(Column):
    def __init__(self,name,table,dtype,other_column):
        super().__init__(name,table,dtype)
        self.foreign_column = other_column

"""
a class that represents a primary key column in  a table
"""
class PrimaryKeyColumn(Column):
    def __init__(self,name,table,dtype):
        super().__init__(name,table,dtype)

"""
 a class representing a column that will be aggregated in the 
query
"""
class AggregateColumn(Column):
    def __init__(self,name,table,dtype,func):
        super().__init__(name,table,dtype)
        self.func = func
