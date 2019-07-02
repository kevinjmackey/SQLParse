import argparse
import os
import sys
from antlr4 import * 
from FunloadLexer import FunloadLexer 
from FunloadParser import FunloadParser 
from FunloadListener import FunloadListener

class Funload(FunloadListener):

    # Enter a parse tree produced by FunloadParser#identifier.
    def enterIdentifier(self, ctx:FunloadParser.IdentifierContext):
        print('Entering Identifier')
        print(str(ctx.getText()))
    # Enter a parse tree produced by FunloadParser#assignmentStatement.
    def enterAssignmentStatement(self, ctx:FunloadParser.AssignmentStatementContext):
        print('Entering Assignment statement')
        print(str(ctx.getText()))
    # Enter a parse tree produced by FunloadParser#forStatement.
    def enterForStatement(self, ctx:FunloadParser.ForStatementContext):
        print('Entering For statement')
        print(str(ctx.getText()))
    # Enter a parse tree produced by FunloadParser#functionDesignator.
    def enterFunctionDesignator(self, ctx:FunloadParser.FunctionDesignatorContext):
        print('Entering Function designation')
        print(str(ctx.getText()))
    # Enter a parse tree produced by FunloadParser#ifStatement.
    def enterIfStatement(self, ctx:FunloadParser.IfStatementContext):
        print('Entering If statement')
        print(str(ctx.getText()))
    # Enter a parse tree produced by FunloadParser#putStatement.
    def enterPutStatement(self, ctx:FunloadParser.PutStatementContext):
        print('Entering Put statement')
        print(str(ctx.getText()))
    # Enter a parse tree produced by FunloadParser#outputStatement.
    def enterOutputStatement(self, ctx:FunloadParser.OutputStatementContext):
        print('Entering Output statement')
        print(str(ctx.getText()))
    # Enter a parse tree produced by FunloadParser#variable.
    def enterVariable(self, ctx:FunloadParser.VariableContext):
        print('Entering Variable use')
        print(str(ctx.getText()))
    # Enter a parse tree produced by FunloadParser#logicalExpression.
    def enterLogicalExpression(self, ctx:FunloadParser.LogicalExpressionContext):
        print('Entering Logical Expression')
        print(str(ctx.getText()))
    # Enter a parse tree produced by FunloadParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:FunloadParser.ConditionalExpressionContext):
        print('Entering Conditional Expression')
        print(str(ctx.getText()))

def Main(argv): 
    #Script starts here
    input = FileStream(argv[1]) 
    print("Loaded {0}".format(str(argv[1])))
    lexer = FunloadLexer(input) 
    stream = CommonTokenStream(lexer) 
    parser = FunloadParser(stream)
    tree = parser.extract()

    funload = Funload()
    walker = ParseTreeWalker()
    walker.walk(funload, tree)

if __name__ == '__main__': 
    Main(sys.argv) 
