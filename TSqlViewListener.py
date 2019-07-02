from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TSqlParser import TSqlParser
    from .TSqlParserVisitor import TSqlParserVisitor
else:
    from TSqlParser import TSqlParser
    from TSqlParserListener import TSqlParserListener
import uast

class TSqlViewListener(TSqlParserListener):

    sqlFile = ""
    uastTree = None
    currentParent = None
    currentNode = None
    parentStack = []

    # Enter a parse tree produced by TSqlParser#tsql_file.
    def enterTsql_file(self, ctx:TSqlParser.Tsql_fileContext):
        self.uastTree = uast.Node()
        self.uastTree.internalType = "sql:File"
        self.uastTree.roles.append(uast.Role.FILE)
        self.uastTree.token = self.sqlFile
        self.currentParent = self.uastTree
        elementCtx = ctx.getChild(1)
        elementCtx = ctx.getChild(1)
        if isinstance(elementCtx, TSqlParser.BatchContext):
            body = uast.Node()
            body.roles.append(uast.Role.BODY)
            body.internalType = "sql:Body"
            self.uastTree.children.append(body)
            self.parentStack.append(self.currentParent)
            self.currentParent = body
        else:
            print("Somehow the first child wasn't a BATCH element")

    # Enter a parse tree produced by TSqlParser#alter_view.
    def enterAlter_view(self, ctx:TSqlParser.Alter_viewContext):
        node = uast.Node()
        node.internalType = "sql:AlterView"
        node.roles.append(uast.Role.ALTER)
        self.currentParent.children.append(node)
        self.parentStack.append(self.currentParent)
        for i in range(ctx.getChildCount()):
            elementCtx = ctx.getChild(i)
            if isinstance(elementCtx, TSqlParser.Simple_nameContext):
                name = uast.Node()
                name.internalType = "sql:Name"
                name.roles.append(uast.Role.NAME)
                name.token = elementCtx.getText()
                node.children.append(name)
            if isinstance(elementCtx, TSqlParser.Column_name_listContext):
                for i in range(elementCtx.getChildCount()):
                    childCtx = elementCtx.getChild(i)
                    if isinstance(childCtx, TSqlParser.IdContext):
                        id = uast.Node()
                        id.internalType = "sql:Id"
                        id.roles.append(uast.Role.IDENTIFIER)
                        id.properties["type"] = "coolumn"
                        id.token = childCtx.getText()
                        name.children.append(id)

    # Exit a parse tree produced by TSqlParser#alter_view.
    def exitAlter_view(self, ctx:TSqlParser.Alter_viewContext):
        self.currentParent = self.parentStack.pop()

    # Enter a parse tree produced by TSqlParser#use_statement.
    def enterUse_statement(self, ctx:TSqlParser.Use_statementContext):
        node = uast.Node()
        node.internalType = "sql:Use"
        node.token = ctx.getChild(1).getText()
        node.roles.append(uast.Role.DIRECTIVE)
        self.currentParent.children.append(node)

    # Enter a parse tree produced by TSqlParser#go_statement.
    def enterGo_statement(self, ctx:TSqlParser.Go_statementContext):
        node = uast.Node()
        node.internalType = "sql:GO"
        node.token = "GO"
        node.roles.append(uast.Role.DIRECTIVE)
        self.currentParent.children.append(node)

    # Enter a parse tree produced by TSqlParser#set_env_val.
    def enterSet_env_val(self, ctx:TSqlParser.Set_env_valContext):
        t = {"SETQUOTED" : "QUOTED_IDENTIFIER", "SETANSI_N" : "ANSI_NULLS", "SETANSI_P" : "ANSI_PADDING", "SETANSI_W" : "ANSI_WARNINGS", "SETIDENTI" : "IDENTITY_INSERT"}
        token = t.get(ctx.getChild(0).getText()[:9])
        suffix = "ON" if ctx.getChild(0).getText().replace(";","").endswith("ON") else "OFF"
        node = uast.Node()
        node.internalType = "sql:SetEnvVal"
        node.token = "SET {0} {1}".format(token, suffix)
        node.roles.append(uast.Role.DIRECTIVE)
        self.currentParent.children.append(node)

    # Enter a parse tree produced by TSqlParser#query_specification.
    def enterQuery_specification(self, ctx:TSqlParser.Query_specificationContext):
        node = uast.Node()
        node.internalType = "sql:Query"
        node.token = "SELECT"
        node.roles.append(uast.Role.READ)
        
        self.currentParent.children.append(node)
        self.parentStack.append(self.currentParent)
        self.currentParent = node
        for i in range(ctx.getChildCount()):
            elementCtx = ctx.getChild(i)
            if elementCtx.getText() == "ALL":
                keywordNode = uast.Node()
                keywordNode.internalType = "sql:ALLkeyword"
                keywordNode.token = "ALL"
                keywordNode.roles.append(uast.Role.PRIMITIVE)
                self.currentParent.children.append(keywordNode)
            if elementCtx.getText() == "DISTINCT":
                keywordNode = uast.Node()
                keywordNode.internalType = "sql:Distinctkeyword"
                keywordNode.token = "DISTINCT"
                keywordNode.roles.append(uast.Role.PRIMITIVE)
                self.currentParent.children.append(keywordNode)

    # Exit a parse tree produced by TSqlParser#query_specification.
    def exitQuery_specification(self, ctx:TSqlParser.Query_specificationContext):
        self.currentParent = self.parentStack.pop()

    # Enter a parse tree produced by TSqlParser#column_elem.
    def enterColumn_elem(self, ctx:TSqlParser.Column_elemContext):
        node = uast.Node()
        self.currentNode = node
        node.internalType = "sql:Column"
        node.roles.append(uast.Role.IDENTIFIER)
        for i in range(ctx.getChildCount()):
            elementCtx = ctx.getChild(i)
            if isinstance(elementCtx, TSqlParser.Table_nameContext):
                node.roles.append(uast.Role.QUALIFIED)
                node.properties["Qualifier"] = elementCtx.getText()
            if isinstance(elementCtx, TSqlParser.As_column_aliasContext):
                node.properties["Alias"] = elementCtx.getChild(1).getText()
            if isinstance(elementCtx, TSqlParser.IdContext):
                node.token = elementCtx.getText()
        self.currentParent.children.append(node)

    # Exit a parse tree produced by TSqlParser#Column_elemContext.
    def exitColumn_elemContext(self, ctx:TSqlParser.Column_elemContext):
        self.currentNode = None

    # Enter a parse tree produced by TSqlParser#expression_elem.
    def enterExpression_elem(self, ctx:TSqlParser.Expression_elemContext):
        node = uast.Node()
        self.currentNode = node
        node.internalType = "sql:Expression"
        node.roles.append(uast.Role.EXPRESSION)
        for i in range(ctx.getChildCount()):
            elementCtx = ctx.getChild(i)
            if isinstance(elementCtx, TSqlParser.As_column_aliasContext):
                node.properties["Alias"] = elementCtx.getChild(1).getText()
            if isinstance(elementCtx, TSqlParser.Column_aliasContext):
                node.properties["Alias"] = elementCtx.getChild(0).getText()
        self.currentParent.children.append(node)
        self.parentStack.append(self.currentParent)
        self.currentParent = node

    # Exit a parse tree produced by TSqlParser#expression_elem.
    def exitExpression_elem(self, ctx:TSqlParser.Expression_elemContext):
        self.currentParent = self.parentStack.pop()

    # Enter a parse tree produced by TSqlParser#asterisk.
    def enterAsterisk(self, ctx:TSqlParser.AsteriskContext):
        node = uast.Node()
        node.internalType = "sql:Asterisk"
        node.token = "*"
        node.roles.append(uast.Role.PRIMITIVE)
        for i in range(ctx.getChildCount()):
            elementCtx = ctx.getChild(i)
            if isinstance(elementCtx, TSqlParser.Table_nameContext):
                node.roles.append(uast.Role.QUALIFIED)
                node.properties["Qualifier"] = elementCtx.getText()
        self.currentParent.children.append(node)

    # Enter a parse tree produced by TSqlParser#SCALAR_FUNCTION.
    def enterSCALAR_FUNCTION(self, ctx:TSqlParser.SCALAR_FUNCTIONContext):
        node = uast.Node()
        node.internalType = "sql:ScalarFunction"
        node.token = ctx.getChild(0).getText()
        node.roles.append(uast.Role.FUNCTION)

        self.currentParent.children.append(node)
        self.parentStack.append(self.currentParent)
        self.currentParent = node

    # Exit a parse tree produced by TSqlParser#SCALAR_FUNCTION.
    def exitSCALAR_FUNCTION(self, ctx:TSqlParser.SCALAR_FUNCTIONContext):
        self.currentParent = self.parentStack.pop()
        self.currentNode = self.currentParent

    # Enter a parse tree produced by TSqlParser#ISNULL.
    def enterISNULL(self, ctx:TSqlParser.ISNULLContext):
        node = uast.Node()
        node.internalType = "sql:ScalarFunction"
        node.token = "IsNull"
        node.roles.append(uast.Role.FUNCTION)

        self.currentParent.children.append(node)
        self.parentStack.append(self.currentParent)
        self.currentParent = node

    # Exit a parse tree produced by TSqlParser#ISNULL.
    def exitISNULL(self, ctx:TSqlParser.ISNULLContext):
        self.currentParent = self.parentStack.pop()
        self.currentNode = self.currentParent

    # Enter a parse tree produced by TSqlParser#expression.
    def enterExpression(self, ctx:TSqlParser.ExpressionContext):
        if isinstance(ctx, TSqlParser.Function_callContext):
            pass
        elif isinstance(ctx.getChild(0), TSqlParser.Full_column_nameContext):
            # print("In Full Column Name Context {0} of {1}".format(ctx.getText(), self.currentParent.internalType))
            node = uast.Node()
            node.internalType = "sql:Column"
            node.roles.append(uast.Role.IDENTIFIER)
            for i in range(ctx.getChild(0).getChildCount()):
                elementCtx = ctx.getChild(0).getChild(i)
                if isinstance(elementCtx, TSqlParser.Table_nameContext):
                    node.roles.append(uast.Role.QUALIFIED)
                    node.properties["Qualifier"] = elementCtx.getText()
                else:
                    node.token = elementCtx.getText()
            self.currentParent.children.append(node)
        elif isinstance(ctx.getChild(0), TSqlParser.Primitive_expressionContext):
            node = uast.Node()
            node.internalType = "sql:Primitive"
            node.token = ctx.getChild(0).getText()
            node.roles.append(uast.Role.PRIMITIVE)
            self.currentParent.children.append(node)

    # Enter a parse tree produced by TSqlParser#full_column_name.
    def enterFull_column_name(self, ctx:TSqlParser.Full_column_nameContext):
        pass

    # Enter a parse tree produced by TSqlParser#case_expression.
    def enterCase_expression(self, ctx:TSqlParser.Case_expressionContext):
        node = uast.Node()
        node.internalType = "sql:Case"
        node.roles.append(uast.Role.SWITCH)
        self.currentParent.children.append(node)
        self.parentStack.append(self.currentParent)
        self.currentParent = node

    # Exit a parse tree produced by TSqlParser#case_expression.
    def exitCase_expression(self, ctx:TSqlParser.Case_expressionContext):
        self.currentParent = self.parentStack.pop()
        self.currentNode = self.currentParent

    # Enter a parse tree produced by TSqlParser#switch_section.
    def enterSwitch_section(self, ctx:TSqlParser.Switch_sectionContext):
        node = uast.Node()
        node.internalType = "sql:When"
        node.roles.append(uast.Role.CASE)
        self.currentParent.children.append(node)
        self.parentStack.append(self.currentParent)
        self.currentParent = node

    # Exit a parse tree produced by TSqlParser#switch_section.
    def exitSwitch_section(self, ctx:TSqlParser.Switch_sectionContext):
        self.currentParent = self.parentStack.pop()
        self.currentNode = self.currentParent

    # Enter a parse tree produced by TSqlParser#switch_search_condition_section.
    def enterSwitch_search_condition_section(self, ctx:TSqlParser.Switch_search_condition_sectionContext):
        node = uast.Node()
        node.internalType = "sql:When"
        node.roles.append(uast.Role.CASE)
        self.currentParent.children.append(node)
        self.parentStack.append(self.currentParent)
        self.currentParent = node

    # Exit a parse tree produced by TSqlParser#switch_search_condition_section.
    def exitSwitch_search_condition_section(self, ctx:TSqlParser.Switch_search_condition_sectionContext):
        self.currentParent = self.parentStack.pop()
        self.currentNode = self.currentParent

    # Enter a parse tree produced by TSqlParser#aggregate_windowed_function.
    def enterAggregate_windowed_function(self, ctx:TSqlParser.Aggregate_windowed_functionContext):
        node = uast.Node()
        node.token = ctx.getChild(0).getText()
        node.internalType = "sql:Aggregate"
        node.roles.append(uast.Role.AGGREGATE)
        self.currentParent.children.append(node)
        self.parentStack.append(self.currentParent)
        self.currentParent = node

    # Exit a parse tree produced by TSqlParser#aggregate_windowed_function.
    def exitAggregate_windowed_function(self, ctx:TSqlParser.Aggregate_windowed_functionContext):
        self.currentParent = self.parentStack.pop()
        self.currentNode = self.currentParent

    # Enter a parse tree produced by TSqlParser#full_table_name.
    def enterFull_table_name(self, ctx:TSqlParser.Full_table_nameContext):
        if self.currentParent.internalType == "sql:TableSource":
            node = uast.Node()
            node.internalType = "sql:Table"
            node.roles.append(uast.Role.DATASOURCE)
            if ctx.server != None:
                node.token = "{0}.{1}.{2}.{3}".format(ctx.server.getText(), ctx.database.getText(), ctx.schema.getText(), ctx.table.getText())
            elif ctx.server == None and ctx.database != None:
                node.token = "{0}.{1}.{2}".format(ctx.database.getText(), ctx.schema.getText(), ctx.table.getText())
            else:
                node.token = "{0}.{1}".format(ctx.schema.getText(), ctx.table.getText())
                
            self.currentParent.children.append(node)

    # Enter a parse tree produced by TSqlParser#table_name.
    def enterTable_name(self, ctx:TSqlParser.Table_nameContext):
        if self.currentParent.internalType == "sql:TableSource":
            node = uast.Node()
            node.internalType = "sql:Table"
            node.roles.append(uast.Role.DATASOURCE)
            if ctx.database != None and ctx.schema != None:
                node.token = "{0}.{1}.{2}".format(ctx.database.getText(), ctx.schema.getText(), ctx.table.getText())
            elif ctx.database == None and ctx.schema != None:
                node.token = "{0}.{1}".format(ctx.schema.getText(), ctx.table.getText())
            else:
                node.token = "{0}".format(ctx.getText())
                
            self.currentParent.children.append(node)

    # Enter a parse tree produced by TSqlParser#table_sources.
    def enterTable_sources(self, ctx:TSqlParser.Table_sourcesContext):
        node = uast.Node()
        node.internalType = "sql:From"
        node.roles.append(uast.Role.DATASOURCE)
        self.currentParent.children.append(node)
        self.parentStack.append(self.currentParent)
        self.currentParent = node

    # Exit a parse tree produced by TSqlParser#table_sources.
    def exitTable_sources(self, ctx:TSqlParser.Table_sourcesContext):
        self.currentParent = self.parentStack.pop()
        self.currentNode = self.currentParent

    # Enter a parse tree produced by TSqlParser#table_source_item.
    def enterTable_source_item(self, ctx:TSqlParser.Table_source_itemContext):
        node = uast.Node()
        if isinstance(ctx.getChild(0), TSqlParser.Table_name_with_hintContext):
            node.internalType = "sql:TableSource"
        elif isinstance(ctx.getChild(0), TSqlParser.Full_table_nameContext):
            node.internalType = "sql:TableSource"
        elif isinstance(ctx.getChild(0), TSqlParser.Rowset_functionContext):
            node.internalType = "sql:RowsetSource"
        elif isinstance(ctx.getChild(0), TSqlParser.Derived_tableContext):
            node.internalType = "sql:DerivedTable"
        node.roles.append(uast.Role.DATASOURCE)
        for i in range(ctx.getChildCount()):
            elementCtx = ctx.getChild(i)
            if isinstance(elementCtx, TSqlParser.As_table_aliasContext):
                node.properties["Alias"] = elementCtx.getChild(0).getText() if elementCtx.getChild(0).getText() != "AS" else elementCtx.getChild(1).getText()
                node.roles.append(uast.Role.QUALIFIED)
        self.currentParent.children.append(node)
        self.parentStack.append(self.currentParent)
        self.currentParent = node

    # Exit a parse tree produced by TSqlParser#table_source_item.
    def exitTable_source_item(self, ctx:TSqlParser.Table_source_itemContext):
        self.currentParent = self.parentStack.pop()
        self.currentNode = self.currentParent

    # Enter a parse tree produced by TSqlParser#join_clause.
    def enterJoin_clause(self, ctx:TSqlParser.Join_clauseContext):
        node = uast.Node()
        node.internalType = "sql:Join"
        node.roles.append(uast.Role.JOINCLAUSE)
        token = "JOIN"
        if ctx.INNER() != None:
            node.token = "INNER {}".format(token)
        outer = " OUTER" if ctx.OUTER() != None else ""
        if ctx.join_type != None:
            node.token = "{0}{1} {2}".format(ctx.join_type, outer, token)
        self.currentParent.children.append(node)
        self.parentStack.append(self.currentParent)
        self.currentParent = node

    # Exit a parse tree produced by TSqlParser#join_clause.
    def exitJoin_clause(self, ctx:TSqlParser.Join_clauseContext):
        self.currentParent = self.parentStack.pop()
        self.currentNode = self.currentParent

    # Enter a parse tree produced by TSqlParser#predicate.
    def enterPredicate(self, ctx:TSqlParser.PredicateContext):
        node = uast.Node()
        if self.currentParent.internalType == "sql:Join":
            node.internalType = "sql:OnCondition"
        if self.currentParent.internalType == "sql:Query":
            node.internalType = "sql:WhereCondition"
        node.roles.append(uast.Role.CONDITION)
        self.currentParent.children.append(node)
        self.parentStack.append(self.currentParent)
        self.currentParent = node

    # Exit a parse tree produced by TSqlParser#predicate.
    def exitPredicate(self, ctx:TSqlParser.PredicateContext):
        self.currentParent = self.parentStack.pop()
        self.currentNode = self.currentParent

    # Enter a parse tree produced by TSqlParser#comparison_operator.
    def enterComparison_operator(self, ctx:TSqlParser.Comparison_operatorContext):
        node = uast.Node()
        node.internalType = "sql:ComparisonOperator"
        operator = ctx.getText()
        node.token = operator
        node.roles.append(uast.Role.OPERATOR)
        if operator == "=":
            node.roles.append(uast.Role.EQUAL)
        elif operator == "<":
            node.roles.append(uast.Role.LESS_THAN)
        elif operator == ">":
            node.roles.append(uast.Role.GREATER_THAN)
        elif operator == "<=":
            node.roles.append(uast.Role.LESS_THAN_OR_EQUAL)
        elif operator == ">=":
            node.roles.append(uast.Role.GREATER_THAN_OR_EQUAL)
        elif operator == "<>" or operator == "!=":
            node.roles.append(uast.Role.NOT)
            node.roles.append(uast.Role.EQUAL)
        elif operator == "IN":
            node.roles.append(uast.Role.CONTAINS)
        self.currentParent.children.append(node)
