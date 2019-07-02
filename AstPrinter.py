import os
import sys
from antlr4 import * 
from TSqlParser import TSqlParser 

class AstPrinter:

    ignoringWrappers = True

    def print(self, ctx):
        self.explore(ctx, 0)

    def explore(self, ctx, indentation):
        toBeIgnored = (self.ignoringWrappers
            and ctx.getChildCount() == 1
            and isinstance(ctx.getChild(0), ParserRuleContext))

        if (toBeIgnored == False):
            ruleName = TSqlParser.ruleNames[ctx.getRuleIndex()]
            indent = ""
            for i in range(indentation):
                indent += " "

            print(indent + ruleName + " :" + getattr(ctx, "use", "False"))

        for i in range(ctx.getChildCount()):
            element = ctx.getChild(i)
            if isinstance(element, TSqlParser.Expression_elemContext):
                element.use = "True"
            if isinstance(element, RuleContext):
                self.explore(element, indentation + (0 if toBeIgnored == True else 1))
