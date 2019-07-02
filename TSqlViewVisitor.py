from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TSqlParser import TSqlParser
    from .TSqlParserVisitor import TSqlParserVisitor
else:
    from TSqlParser import TSqlParser
    from TSqlParserVisitor import TSqlParserVisitor
import uast

class TSqlViewVisitor(TSqlParserVisitor):

    sqlFile = ""
    uastTree = None
    currentParent = None
    parentStack = []

    # Visit a parse tree produced by TSqlParser#tsql_file.
    def visitTsql_file(self, ctx:TSqlParser.Tsql_fileContext):
        uastTree = uast.Node()
        uastTree.internalType = "sql:File"
        uastTree.roles.append(uast.Role.FILE)
        uastTree.token = self.sqlFile
        self.currentParent = uastTree
        elementCtx = ctx.getChild(1)
        elementCtx = ctx.getChild(1)
        if isinstance(elementCtx, TSqlParser.BatchContext):
            body = uast.Node()
            body.roles.append(uast.Role.BODY)
            body.internalType = "sql:Body"
            self.currentParent.children.append(body)
            for i in range(elementCtx.getChildCount()):
                childCtx = elementCtx.getChild(i)
                if isinstance(childCtx, TSqlParser.Sql_clausesContext):
                    self.parentStack.append(self.currentParent)
                    self.currentParent = body
                    self.visitSql_clauses(childCtx)
                    self.currentParent = self.parentStack.pop()
        else:
            print("Somehow the first child wasn't a BATCH element")
            # self.visitChildren(ctx)

    # Visit a parse tree produced by TSqlParser#sql_clauses.
    def visitSql_clauses(self, ctx:TSqlParser.Sql_clausesContext):
        print("Visiting sql_clauses")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by TSqlParser#batch.
    def visitBatch(self, ctx:TSqlParser.BatchContext):
        node = uast.Node()
        node.internalType = "sql:StatementBatch"
        node.roles.append(uast.Role.BLOCK)
        self.currentParent.children.append(node)
        self.parentStack.append(self.currentParent)
        self.currentParent = node
        self.visitChildren(ctx)
        self.currentParent = self.parentStack.pop()

    # Visit a parse tree produced by TSqlParser#alter_view.
    def visitAlter_view(self, ctx:TSqlParser.Alter_viewContext):
        print("In Alter View statement...")
        node = uast.Node()
        node.internalType = "sql:AlterView"
        node.roles.append(uast.Role.ALTER)
        self.currentParent.children.append(node)
        for i in range(ctx.getChildCount()):
            elementCtx = ctx.getChild(i)
            if isinstance(elementCtx, TSqlParser.Simple_nameContext):
                name = uast.Node()
                name.internalType = "sql:Name"
                name.roles.append(uast.Role.NAME)
                name.token = childCtx.getText()
                self.currentParent.children.append(name)
            if isinstance(elementCtx, TSqlParser.Column_name_listContext):
                for i in range(elementCtx.getChildCount()):
                    childCtx = elementCtx.getChild(i)
                    if isinstance(childCtx, TSqlParser.IdContext):
                        id = uast.Node()
                        id.internalType = "sql:Id"
                        id.roles.append(uast.Role.IDENTIFIER)
                        id.properties["type"] = "coolumn"
                        id.token = childCtx.getText()
                        self.currentParent.children.append(id)
                        print("Column Name: {}".format(id.token))

