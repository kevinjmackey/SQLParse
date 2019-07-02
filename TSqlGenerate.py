import os
import sys
import pyratemp
from datetime import datetime
from enum import Enum, unique

class SqlElementType(Enum):
    nothing = 0
    tsql_file = 1
    use_statement = 2
    go_statement = 3
    set_statement = 4
    create_view = 5
    alter_view = 6
    select_statement = 7
    select_list = 8
    expression_elem = 9
    column_elem = 10

class SqlElement:
    parentElement = None
    level = 0
    elementType = SqlElementType.nothing
    text = ""
    leftText = ""
    rightText = ""
    children = []

class TSqlGenerate:
    astRoot = None
    outputFile = None


    def generateSQL(self, _sqlElement):
        d = {}
