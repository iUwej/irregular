from sqlalchemy import *
from collections import namedtuple

class Table(object):
    def __init__(self,name,cols=[]):
        self.name = name
        self.columns = cols

    def addColumn(self,col):
        self.columns.append(col)

class Column(object):
    def __init__(self,name,table):
        self.name = name
        #i thought this might be necessary
        # but then again each table has a list of columns
        self.table = table
        

class ForeignKeyColumn(Column):
    def __init__(self,name,table,other_column):
        super(ForeignKeyColumn,self).__init__(name,table)
        self.foreign_column = other_column


class PrimaryKeyColumn(Column):
    def __init__self(self,name,table):
        super(PrimaryKeyColumn,self).__init__(name,table)


