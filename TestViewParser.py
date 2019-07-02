import argparse
import os
import sys
import json
from antlr4 import * 
from TSqlLexer import TSqlLexer 
from TSqlParser import TSqlParser 
# from TSqlParserListener import TSqlParserListener
from TSqlViewListener import TSqlViewListener

def Main(argv): 
    inputFile = "GEN.Facility_Address_VW.View.sql"
    # if str(argv[1]).lower().endswith(".sql"):
    #     inputFile = str(argv[1])
    input = FileStream(inputFile) 
    lexer = TSqlLexer(input) 
    stream = CommonTokenStream(lexer) 
    print("Loaded {0}".format(inputFile))
    parser = TSqlParser(stream)
    tree = parser.tsql_file()
    print("{0} parsed".format(inputFile))
    
    # astPrinter = AstPrinter()
    # astPrinter.print(tree)

    print("Listening to {0}...".format(inputFile))

    listener = TSqlViewListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # visitor = TSqlViewVisitor()
    # visitor.sqlFile = "GEN.Facility_Address_VW.View.sql" #str(argv[1])
    # visitor.visit(tree)

    # with open("ParsedView.txt", "w") as fout:
    #     fout.write(listener.uastTree.ToString())
    with open("ParsedView.json", "w") as fout:
        fout.write(json.dumps(json.loads(listener.uastTree.ToString()), indent=4))
    # print("Internal Type: {}".format(visitor.currentParent.InternalType()))
    # print("Token: {}".format(visitor.currentParent.Token()))
    # print("Visitor Properties: {}".format(visitor.currentParent.Properties()))
    # print("Visitor Roles: {}".format(visitor.currentParent.Roles()))
    # print("{0} visited".format(str(argv[1])))
    # TSqlListener = TSqlParserListener()
    # walker = ParseTreeWalker()
    # walker.walk(TSqlListener, tree)

if __name__ == '__main__': 
    Main(sys.argv) 