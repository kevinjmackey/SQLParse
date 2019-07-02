# Generated from TSqlParser.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TSqlParser import TSqlParser
else:
    from TSqlParser import TSqlParser

# This class defines a complete generic visitor for a parse tree produced by TSqlParser.

class TSqlParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TSqlParser#tsql_file.
    def visitTsql_file(self, ctx:TSqlParser.Tsql_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#batch.
    def visitBatch(self, ctx:TSqlParser.BatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#sql_clauses.
    def visitSql_clauses(self, ctx:TSqlParser.Sql_clausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#sql_clause.
    def visitSql_clause(self, ctx:TSqlParser.Sql_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#dml_clause.
    def visitDml_clause(self, ctx:TSqlParser.Dml_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#ddl_clause.
    def visitDdl_clause(self, ctx:TSqlParser.Ddl_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#backup_statement.
    def visitBackup_statement(self, ctx:TSqlParser.Backup_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#cfl_statement.
    def visitCfl_statement(self, ctx:TSqlParser.Cfl_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#block_statement.
    def visitBlock_statement(self, ctx:TSqlParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#break_statement.
    def visitBreak_statement(self, ctx:TSqlParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#continue_statement.
    def visitContinue_statement(self, ctx:TSqlParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#goto_statement.
    def visitGoto_statement(self, ctx:TSqlParser.Goto_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#return_statement.
    def visitReturn_statement(self, ctx:TSqlParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#if_statement.
    def visitIf_statement(self, ctx:TSqlParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#throw_statement.
    def visitThrow_statement(self, ctx:TSqlParser.Throw_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#throw_error_number.
    def visitThrow_error_number(self, ctx:TSqlParser.Throw_error_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#throw_message.
    def visitThrow_message(self, ctx:TSqlParser.Throw_messageContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#throw_state.
    def visitThrow_state(self, ctx:TSqlParser.Throw_stateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#try_catch_statement.
    def visitTry_catch_statement(self, ctx:TSqlParser.Try_catch_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#waitfor_statement.
    def visitWaitfor_statement(self, ctx:TSqlParser.Waitfor_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#while_statement.
    def visitWhile_statement(self, ctx:TSqlParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#print_statement.
    def visitPrint_statement(self, ctx:TSqlParser.Print_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#raiseerror_statement.
    def visitRaiseerror_statement(self, ctx:TSqlParser.Raiseerror_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#empty_statement.
    def visitEmpty_statement(self, ctx:TSqlParser.Empty_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#another_statement.
    def visitAnother_statement(self, ctx:TSqlParser.Another_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_application_role.
    def visitAlter_application_role(self, ctx:TSqlParser.Alter_application_roleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_application_role.
    def visitCreate_application_role(self, ctx:TSqlParser.Create_application_roleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_aggregate.
    def visitDrop_aggregate(self, ctx:TSqlParser.Drop_aggregateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_application_role.
    def visitDrop_application_role(self, ctx:TSqlParser.Drop_application_roleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_assembly.
    def visitAlter_assembly(self, ctx:TSqlParser.Alter_assemblyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_assembly_start.
    def visitAlter_assembly_start(self, ctx:TSqlParser.Alter_assembly_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_assembly_clause.
    def visitAlter_assembly_clause(self, ctx:TSqlParser.Alter_assembly_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_assembly_from_clause.
    def visitAlter_assembly_from_clause(self, ctx:TSqlParser.Alter_assembly_from_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_assembly_from_clause_start.
    def visitAlter_assembly_from_clause_start(self, ctx:TSqlParser.Alter_assembly_from_clause_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_assembly_drop_clause.
    def visitAlter_assembly_drop_clause(self, ctx:TSqlParser.Alter_assembly_drop_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_assembly_drop_multiple_files.
    def visitAlter_assembly_drop_multiple_files(self, ctx:TSqlParser.Alter_assembly_drop_multiple_filesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_assembly_drop.
    def visitAlter_assembly_drop(self, ctx:TSqlParser.Alter_assembly_dropContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_assembly_add_clause.
    def visitAlter_assembly_add_clause(self, ctx:TSqlParser.Alter_assembly_add_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_asssembly_add_clause_start.
    def visitAlter_asssembly_add_clause_start(self, ctx:TSqlParser.Alter_asssembly_add_clause_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_assembly_client_file_clause.
    def visitAlter_assembly_client_file_clause(self, ctx:TSqlParser.Alter_assembly_client_file_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_assembly_file_name.
    def visitAlter_assembly_file_name(self, ctx:TSqlParser.Alter_assembly_file_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_assembly_file_bits.
    def visitAlter_assembly_file_bits(self, ctx:TSqlParser.Alter_assembly_file_bitsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_assembly_as.
    def visitAlter_assembly_as(self, ctx:TSqlParser.Alter_assembly_asContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_assembly_with_clause.
    def visitAlter_assembly_with_clause(self, ctx:TSqlParser.Alter_assembly_with_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_assembly_with.
    def visitAlter_assembly_with(self, ctx:TSqlParser.Alter_assembly_withContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#client_assembly_specifier.
    def visitClient_assembly_specifier(self, ctx:TSqlParser.Client_assembly_specifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#assembly_option.
    def visitAssembly_option(self, ctx:TSqlParser.Assembly_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#network_file_share.
    def visitNetwork_file_share(self, ctx:TSqlParser.Network_file_shareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#network_computer.
    def visitNetwork_computer(self, ctx:TSqlParser.Network_computerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#network_file_start.
    def visitNetwork_file_start(self, ctx:TSqlParser.Network_file_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#file_path.
    def visitFile_path(self, ctx:TSqlParser.File_pathContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#file_directory_path_separator.
    def visitFile_directory_path_separator(self, ctx:TSqlParser.File_directory_path_separatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#local_file.
    def visitLocal_file(self, ctx:TSqlParser.Local_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#local_drive.
    def visitLocal_drive(self, ctx:TSqlParser.Local_driveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#multiple_local_files.
    def visitMultiple_local_files(self, ctx:TSqlParser.Multiple_local_filesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#multiple_local_file_start.
    def visitMultiple_local_file_start(self, ctx:TSqlParser.Multiple_local_file_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_assembly.
    def visitCreate_assembly(self, ctx:TSqlParser.Create_assemblyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_assembly.
    def visitDrop_assembly(self, ctx:TSqlParser.Drop_assemblyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_asymmetric_key.
    def visitAlter_asymmetric_key(self, ctx:TSqlParser.Alter_asymmetric_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_asymmetric_key_start.
    def visitAlter_asymmetric_key_start(self, ctx:TSqlParser.Alter_asymmetric_key_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#asymmetric_key_option.
    def visitAsymmetric_key_option(self, ctx:TSqlParser.Asymmetric_key_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#asymmetric_key_option_start.
    def visitAsymmetric_key_option_start(self, ctx:TSqlParser.Asymmetric_key_option_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#asymmetric_key_password_change_option.
    def visitAsymmetric_key_password_change_option(self, ctx:TSqlParser.Asymmetric_key_password_change_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_asymmetric_key.
    def visitCreate_asymmetric_key(self, ctx:TSqlParser.Create_asymmetric_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_asymmetric_key.
    def visitDrop_asymmetric_key(self, ctx:TSqlParser.Drop_asymmetric_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_authorization.
    def visitAlter_authorization(self, ctx:TSqlParser.Alter_authorizationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#authorization_grantee.
    def visitAuthorization_grantee(self, ctx:TSqlParser.Authorization_granteeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#entity_to.
    def visitEntity_to(self, ctx:TSqlParser.Entity_toContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#colon_colon.
    def visitColon_colon(self, ctx:TSqlParser.Colon_colonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_authorization_start.
    def visitAlter_authorization_start(self, ctx:TSqlParser.Alter_authorization_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_authorization_for_sql_database.
    def visitAlter_authorization_for_sql_database(self, ctx:TSqlParser.Alter_authorization_for_sql_databaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_authorization_for_azure_dw.
    def visitAlter_authorization_for_azure_dw(self, ctx:TSqlParser.Alter_authorization_for_azure_dwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_authorization_for_parallel_dw.
    def visitAlter_authorization_for_parallel_dw(self, ctx:TSqlParser.Alter_authorization_for_parallel_dwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#class_type.
    def visitClass_type(self, ctx:TSqlParser.Class_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#class_type_for_sql_database.
    def visitClass_type_for_sql_database(self, ctx:TSqlParser.Class_type_for_sql_databaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#class_type_for_azure_dw.
    def visitClass_type_for_azure_dw(self, ctx:TSqlParser.Class_type_for_azure_dwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#class_type_for_parallel_dw.
    def visitClass_type_for_parallel_dw(self, ctx:TSqlParser.Class_type_for_parallel_dwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_availability_group.
    def visitDrop_availability_group(self, ctx:TSqlParser.Drop_availability_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_availability_group.
    def visitAlter_availability_group(self, ctx:TSqlParser.Alter_availability_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_availability_group_start.
    def visitAlter_availability_group_start(self, ctx:TSqlParser.Alter_availability_group_startContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_availability_group_options.
    def visitAlter_availability_group_options(self, ctx:TSqlParser.Alter_availability_group_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_or_alter_broker_priority.
    def visitCreate_or_alter_broker_priority(self, ctx:TSqlParser.Create_or_alter_broker_priorityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_broker_priority.
    def visitDrop_broker_priority(self, ctx:TSqlParser.Drop_broker_priorityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_certificate.
    def visitAlter_certificate(self, ctx:TSqlParser.Alter_certificateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_column_encryption_key.
    def visitAlter_column_encryption_key(self, ctx:TSqlParser.Alter_column_encryption_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_column_encryption_key.
    def visitCreate_column_encryption_key(self, ctx:TSqlParser.Create_column_encryption_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_certificate.
    def visitDrop_certificate(self, ctx:TSqlParser.Drop_certificateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_column_encryption_key.
    def visitDrop_column_encryption_key(self, ctx:TSqlParser.Drop_column_encryption_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_column_master_key.
    def visitDrop_column_master_key(self, ctx:TSqlParser.Drop_column_master_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_contract.
    def visitDrop_contract(self, ctx:TSqlParser.Drop_contractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_credential.
    def visitDrop_credential(self, ctx:TSqlParser.Drop_credentialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_cryptograhic_provider.
    def visitDrop_cryptograhic_provider(self, ctx:TSqlParser.Drop_cryptograhic_providerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_database.
    def visitDrop_database(self, ctx:TSqlParser.Drop_databaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_database_audit_specification.
    def visitDrop_database_audit_specification(self, ctx:TSqlParser.Drop_database_audit_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_database_scoped_credential.
    def visitDrop_database_scoped_credential(self, ctx:TSqlParser.Drop_database_scoped_credentialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_default.
    def visitDrop_default(self, ctx:TSqlParser.Drop_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_endpoint.
    def visitDrop_endpoint(self, ctx:TSqlParser.Drop_endpointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_external_data_source.
    def visitDrop_external_data_source(self, ctx:TSqlParser.Drop_external_data_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_external_file_format.
    def visitDrop_external_file_format(self, ctx:TSqlParser.Drop_external_file_formatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_external_library.
    def visitDrop_external_library(self, ctx:TSqlParser.Drop_external_libraryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_external_resource_pool.
    def visitDrop_external_resource_pool(self, ctx:TSqlParser.Drop_external_resource_poolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_external_table.
    def visitDrop_external_table(self, ctx:TSqlParser.Drop_external_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_event_notifications.
    def visitDrop_event_notifications(self, ctx:TSqlParser.Drop_event_notificationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_event_session.
    def visitDrop_event_session(self, ctx:TSqlParser.Drop_event_sessionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_fulltext_catalog.
    def visitDrop_fulltext_catalog(self, ctx:TSqlParser.Drop_fulltext_catalogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_fulltext_index.
    def visitDrop_fulltext_index(self, ctx:TSqlParser.Drop_fulltext_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_fulltext_stoplist.
    def visitDrop_fulltext_stoplist(self, ctx:TSqlParser.Drop_fulltext_stoplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_login.
    def visitDrop_login(self, ctx:TSqlParser.Drop_loginContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_master_key.
    def visitDrop_master_key(self, ctx:TSqlParser.Drop_master_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_message_type.
    def visitDrop_message_type(self, ctx:TSqlParser.Drop_message_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_partition_function.
    def visitDrop_partition_function(self, ctx:TSqlParser.Drop_partition_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_partition_scheme.
    def visitDrop_partition_scheme(self, ctx:TSqlParser.Drop_partition_schemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_queue.
    def visitDrop_queue(self, ctx:TSqlParser.Drop_queueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_remote_service_binding.
    def visitDrop_remote_service_binding(self, ctx:TSqlParser.Drop_remote_service_bindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_resource_pool.
    def visitDrop_resource_pool(self, ctx:TSqlParser.Drop_resource_poolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_db_role.
    def visitDrop_db_role(self, ctx:TSqlParser.Drop_db_roleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_route.
    def visitDrop_route(self, ctx:TSqlParser.Drop_routeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_rule.
    def visitDrop_rule(self, ctx:TSqlParser.Drop_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_schema.
    def visitDrop_schema(self, ctx:TSqlParser.Drop_schemaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_search_property_list.
    def visitDrop_search_property_list(self, ctx:TSqlParser.Drop_search_property_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_security_policy.
    def visitDrop_security_policy(self, ctx:TSqlParser.Drop_security_policyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_sequence.
    def visitDrop_sequence(self, ctx:TSqlParser.Drop_sequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_server_audit.
    def visitDrop_server_audit(self, ctx:TSqlParser.Drop_server_auditContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_server_audit_specification.
    def visitDrop_server_audit_specification(self, ctx:TSqlParser.Drop_server_audit_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_server_role.
    def visitDrop_server_role(self, ctx:TSqlParser.Drop_server_roleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_service.
    def visitDrop_service(self, ctx:TSqlParser.Drop_serviceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_signature.
    def visitDrop_signature(self, ctx:TSqlParser.Drop_signatureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_statistics_name_azure_dw_and_pdw.
    def visitDrop_statistics_name_azure_dw_and_pdw(self, ctx:TSqlParser.Drop_statistics_name_azure_dw_and_pdwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_symmetric_key.
    def visitDrop_symmetric_key(self, ctx:TSqlParser.Drop_symmetric_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_synonym.
    def visitDrop_synonym(self, ctx:TSqlParser.Drop_synonymContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_user.
    def visitDrop_user(self, ctx:TSqlParser.Drop_userContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_workload_group.
    def visitDrop_workload_group(self, ctx:TSqlParser.Drop_workload_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_xml_schema_collection.
    def visitDrop_xml_schema_collection(self, ctx:TSqlParser.Drop_xml_schema_collectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#disable_trigger.
    def visitDisable_trigger(self, ctx:TSqlParser.Disable_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#enable_trigger.
    def visitEnable_trigger(self, ctx:TSqlParser.Enable_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#lock_table.
    def visitLock_table(self, ctx:TSqlParser.Lock_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#truncate_table.
    def visitTruncate_table(self, ctx:TSqlParser.Truncate_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_column_master_key.
    def visitCreate_column_master_key(self, ctx:TSqlParser.Create_column_master_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_credential.
    def visitAlter_credential(self, ctx:TSqlParser.Alter_credentialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_credential.
    def visitCreate_credential(self, ctx:TSqlParser.Create_credentialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_cryptographic_provider.
    def visitAlter_cryptographic_provider(self, ctx:TSqlParser.Alter_cryptographic_providerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_cryptographic_provider.
    def visitCreate_cryptographic_provider(self, ctx:TSqlParser.Create_cryptographic_providerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_event_notification.
    def visitCreate_event_notification(self, ctx:TSqlParser.Create_event_notificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_or_alter_event_session.
    def visitCreate_or_alter_event_session(self, ctx:TSqlParser.Create_or_alter_event_sessionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#event_session_predicate_expression.
    def visitEvent_session_predicate_expression(self, ctx:TSqlParser.Event_session_predicate_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#event_session_predicate_factor.
    def visitEvent_session_predicate_factor(self, ctx:TSqlParser.Event_session_predicate_factorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#event_session_predicate_leaf.
    def visitEvent_session_predicate_leaf(self, ctx:TSqlParser.Event_session_predicate_leafContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_external_data_source.
    def visitAlter_external_data_source(self, ctx:TSqlParser.Alter_external_data_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_external_library.
    def visitAlter_external_library(self, ctx:TSqlParser.Alter_external_libraryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_external_library.
    def visitCreate_external_library(self, ctx:TSqlParser.Create_external_libraryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_external_resource_pool.
    def visitAlter_external_resource_pool(self, ctx:TSqlParser.Alter_external_resource_poolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_external_resource_pool.
    def visitCreate_external_resource_pool(self, ctx:TSqlParser.Create_external_resource_poolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_fulltext_catalog.
    def visitAlter_fulltext_catalog(self, ctx:TSqlParser.Alter_fulltext_catalogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_fulltext_catalog.
    def visitCreate_fulltext_catalog(self, ctx:TSqlParser.Create_fulltext_catalogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_fulltext_stoplist.
    def visitAlter_fulltext_stoplist(self, ctx:TSqlParser.Alter_fulltext_stoplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_fulltext_stoplist.
    def visitCreate_fulltext_stoplist(self, ctx:TSqlParser.Create_fulltext_stoplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_login_sql_server.
    def visitAlter_login_sql_server(self, ctx:TSqlParser.Alter_login_sql_serverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_login_sql_server.
    def visitCreate_login_sql_server(self, ctx:TSqlParser.Create_login_sql_serverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_login_azure_sql.
    def visitAlter_login_azure_sql(self, ctx:TSqlParser.Alter_login_azure_sqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_login_azure_sql.
    def visitCreate_login_azure_sql(self, ctx:TSqlParser.Create_login_azure_sqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_login_azure_sql_dw_and_pdw.
    def visitAlter_login_azure_sql_dw_and_pdw(self, ctx:TSqlParser.Alter_login_azure_sql_dw_and_pdwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_login_pdw.
    def visitCreate_login_pdw(self, ctx:TSqlParser.Create_login_pdwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_master_key_sql_server.
    def visitAlter_master_key_sql_server(self, ctx:TSqlParser.Alter_master_key_sql_serverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_master_key_sql_server.
    def visitCreate_master_key_sql_server(self, ctx:TSqlParser.Create_master_key_sql_serverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_master_key_azure_sql.
    def visitAlter_master_key_azure_sql(self, ctx:TSqlParser.Alter_master_key_azure_sqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_master_key_azure_sql.
    def visitCreate_master_key_azure_sql(self, ctx:TSqlParser.Create_master_key_azure_sqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_message_type.
    def visitAlter_message_type(self, ctx:TSqlParser.Alter_message_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_partition_function.
    def visitAlter_partition_function(self, ctx:TSqlParser.Alter_partition_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_partition_scheme.
    def visitAlter_partition_scheme(self, ctx:TSqlParser.Alter_partition_schemeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_remote_service_binding.
    def visitAlter_remote_service_binding(self, ctx:TSqlParser.Alter_remote_service_bindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_remote_service_binding.
    def visitCreate_remote_service_binding(self, ctx:TSqlParser.Create_remote_service_bindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_resource_pool.
    def visitCreate_resource_pool(self, ctx:TSqlParser.Create_resource_poolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_resource_governor.
    def visitAlter_resource_governor(self, ctx:TSqlParser.Alter_resource_governorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_db_role.
    def visitAlter_db_role(self, ctx:TSqlParser.Alter_db_roleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_db_role.
    def visitCreate_db_role(self, ctx:TSqlParser.Create_db_roleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_route.
    def visitCreate_route(self, ctx:TSqlParser.Create_routeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_rule.
    def visitCreate_rule(self, ctx:TSqlParser.Create_ruleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_schema_sql.
    def visitAlter_schema_sql(self, ctx:TSqlParser.Alter_schema_sqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_schema.
    def visitCreate_schema(self, ctx:TSqlParser.Create_schemaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_schema_azure_sql_dw_and_pdw.
    def visitCreate_schema_azure_sql_dw_and_pdw(self, ctx:TSqlParser.Create_schema_azure_sql_dw_and_pdwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_schema_azure_sql_dw_and_pdw.
    def visitAlter_schema_azure_sql_dw_and_pdw(self, ctx:TSqlParser.Alter_schema_azure_sql_dw_and_pdwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_search_property_list.
    def visitCreate_search_property_list(self, ctx:TSqlParser.Create_search_property_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_security_policy.
    def visitCreate_security_policy(self, ctx:TSqlParser.Create_security_policyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_sequence.
    def visitAlter_sequence(self, ctx:TSqlParser.Alter_sequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_sequence.
    def visitCreate_sequence(self, ctx:TSqlParser.Create_sequenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_server_audit.
    def visitAlter_server_audit(self, ctx:TSqlParser.Alter_server_auditContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_server_audit.
    def visitCreate_server_audit(self, ctx:TSqlParser.Create_server_auditContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_server_audit_specification.
    def visitAlter_server_audit_specification(self, ctx:TSqlParser.Alter_server_audit_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_server_audit_specification.
    def visitCreate_server_audit_specification(self, ctx:TSqlParser.Create_server_audit_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_server_configuration.
    def visitAlter_server_configuration(self, ctx:TSqlParser.Alter_server_configurationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_server_role.
    def visitAlter_server_role(self, ctx:TSqlParser.Alter_server_roleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_server_role.
    def visitCreate_server_role(self, ctx:TSqlParser.Create_server_roleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_server_role_pdw.
    def visitAlter_server_role_pdw(self, ctx:TSqlParser.Alter_server_role_pdwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_service.
    def visitAlter_service(self, ctx:TSqlParser.Alter_serviceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_service.
    def visitCreate_service(self, ctx:TSqlParser.Create_serviceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_service_master_key.
    def visitAlter_service_master_key(self, ctx:TSqlParser.Alter_service_master_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_symmetric_key.
    def visitAlter_symmetric_key(self, ctx:TSqlParser.Alter_symmetric_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_symmetric_key.
    def visitCreate_symmetric_key(self, ctx:TSqlParser.Create_symmetric_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_synonym.
    def visitCreate_synonym(self, ctx:TSqlParser.Create_synonymContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_user.
    def visitAlter_user(self, ctx:TSqlParser.Alter_userContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_user.
    def visitCreate_user(self, ctx:TSqlParser.Create_userContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_user_azure_sql_dw.
    def visitCreate_user_azure_sql_dw(self, ctx:TSqlParser.Create_user_azure_sql_dwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_user_azure_sql.
    def visitAlter_user_azure_sql(self, ctx:TSqlParser.Alter_user_azure_sqlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_workload_group.
    def visitAlter_workload_group(self, ctx:TSqlParser.Alter_workload_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_workload_group.
    def visitCreate_workload_group(self, ctx:TSqlParser.Create_workload_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_xml_schema_collection.
    def visitCreate_xml_schema_collection(self, ctx:TSqlParser.Create_xml_schema_collectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_queue.
    def visitCreate_queue(self, ctx:TSqlParser.Create_queueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#queue_settings.
    def visitQueue_settings(self, ctx:TSqlParser.Queue_settingsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_queue.
    def visitAlter_queue(self, ctx:TSqlParser.Alter_queueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#queue_action.
    def visitQueue_action(self, ctx:TSqlParser.Queue_actionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#queue_rebuild_options.
    def visitQueue_rebuild_options(self, ctx:TSqlParser.Queue_rebuild_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_contract.
    def visitCreate_contract(self, ctx:TSqlParser.Create_contractContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#conversation_statement.
    def visitConversation_statement(self, ctx:TSqlParser.Conversation_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#message_statement.
    def visitMessage_statement(self, ctx:TSqlParser.Message_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#merge_statement.
    def visitMerge_statement(self, ctx:TSqlParser.Merge_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#merge_matched.
    def visitMerge_matched(self, ctx:TSqlParser.Merge_matchedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#merge_not_matched.
    def visitMerge_not_matched(self, ctx:TSqlParser.Merge_not_matchedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#delete_statement.
    def visitDelete_statement(self, ctx:TSqlParser.Delete_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#delete_statement_from.
    def visitDelete_statement_from(self, ctx:TSqlParser.Delete_statement_fromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#insert_statement.
    def visitInsert_statement(self, ctx:TSqlParser.Insert_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#insert_statement_value.
    def visitInsert_statement_value(self, ctx:TSqlParser.Insert_statement_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#receive_statement.
    def visitReceive_statement(self, ctx:TSqlParser.Receive_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#select_statement.
    def visitSelect_statement(self, ctx:TSqlParser.Select_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#time.
    def visitTime(self, ctx:TSqlParser.TimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#update_statement.
    def visitUpdate_statement(self, ctx:TSqlParser.Update_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#output_clause.
    def visitOutput_clause(self, ctx:TSqlParser.Output_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#output_dml_list_elem.
    def visitOutput_dml_list_elem(self, ctx:TSqlParser.Output_dml_list_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#output_column_name.
    def visitOutput_column_name(self, ctx:TSqlParser.Output_column_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_database.
    def visitCreate_database(self, ctx:TSqlParser.Create_databaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_index.
    def visitCreate_index(self, ctx:TSqlParser.Create_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_or_alter_procedure.
    def visitCreate_or_alter_procedure(self, ctx:TSqlParser.Create_or_alter_procedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_or_alter_trigger.
    def visitCreate_or_alter_trigger(self, ctx:TSqlParser.Create_or_alter_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_or_alter_dml_trigger.
    def visitCreate_or_alter_dml_trigger(self, ctx:TSqlParser.Create_or_alter_dml_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#dml_trigger_option.
    def visitDml_trigger_option(self, ctx:TSqlParser.Dml_trigger_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#dml_trigger_operation.
    def visitDml_trigger_operation(self, ctx:TSqlParser.Dml_trigger_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_or_alter_ddl_trigger.
    def visitCreate_or_alter_ddl_trigger(self, ctx:TSqlParser.Create_or_alter_ddl_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#ddl_trigger_operation.
    def visitDdl_trigger_operation(self, ctx:TSqlParser.Ddl_trigger_operationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_or_alter_function.
    def visitCreate_or_alter_function(self, ctx:TSqlParser.Create_or_alter_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#func_body_returns_select.
    def visitFunc_body_returns_select(self, ctx:TSqlParser.Func_body_returns_selectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#func_body_returns_table.
    def visitFunc_body_returns_table(self, ctx:TSqlParser.Func_body_returns_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#func_body_returns_scalar.
    def visitFunc_body_returns_scalar(self, ctx:TSqlParser.Func_body_returns_scalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#procedure_param.
    def visitProcedure_param(self, ctx:TSqlParser.Procedure_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#procedure_option.
    def visitProcedure_option(self, ctx:TSqlParser.Procedure_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#function_option.
    def visitFunction_option(self, ctx:TSqlParser.Function_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_statistics.
    def visitCreate_statistics(self, ctx:TSqlParser.Create_statisticsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#update_statistics.
    def visitUpdate_statistics(self, ctx:TSqlParser.Update_statisticsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_table.
    def visitCreate_table(self, ctx:TSqlParser.Create_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#table_options.
    def visitTable_options(self, ctx:TSqlParser.Table_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_view.
    def visitCreate_view(self, ctx:TSqlParser.Create_viewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#view_attribute.
    def visitView_attribute(self, ctx:TSqlParser.View_attributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_table.
    def visitAlter_table(self, ctx:TSqlParser.Alter_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_view.
    def visitAlter_view(self, ctx:TSqlParser.Alter_viewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_database.
    def visitAlter_database(self, ctx:TSqlParser.Alter_databaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#database_optionspec.
    def visitDatabase_optionspec(self, ctx:TSqlParser.Database_optionspecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#auto_option.
    def visitAuto_option(self, ctx:TSqlParser.Auto_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#change_tracking_option.
    def visitChange_tracking_option(self, ctx:TSqlParser.Change_tracking_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#change_tracking_option_list.
    def visitChange_tracking_option_list(self, ctx:TSqlParser.Change_tracking_option_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#containment_option.
    def visitContainment_option(self, ctx:TSqlParser.Containment_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#cursor_option.
    def visitCursor_option(self, ctx:TSqlParser.Cursor_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#alter_endpoint.
    def visitAlter_endpoint(self, ctx:TSqlParser.Alter_endpointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#database_mirroring_option.
    def visitDatabase_mirroring_option(self, ctx:TSqlParser.Database_mirroring_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#mirroring_set_option.
    def visitMirroring_set_option(self, ctx:TSqlParser.Mirroring_set_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#mirroring_partner.
    def visitMirroring_partner(self, ctx:TSqlParser.Mirroring_partnerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#mirroring_witness.
    def visitMirroring_witness(self, ctx:TSqlParser.Mirroring_witnessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#witness_partner_equal.
    def visitWitness_partner_equal(self, ctx:TSqlParser.Witness_partner_equalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#partner_option.
    def visitPartner_option(self, ctx:TSqlParser.Partner_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#witness_option.
    def visitWitness_option(self, ctx:TSqlParser.Witness_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#witness_server.
    def visitWitness_server(self, ctx:TSqlParser.Witness_serverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#partner_server.
    def visitPartner_server(self, ctx:TSqlParser.Partner_serverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#mirroring_host_port_seperator.
    def visitMirroring_host_port_seperator(self, ctx:TSqlParser.Mirroring_host_port_seperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#partner_server_tcp_prefix.
    def visitPartner_server_tcp_prefix(self, ctx:TSqlParser.Partner_server_tcp_prefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#port_number.
    def visitPort_number(self, ctx:TSqlParser.Port_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#host.
    def visitHost(self, ctx:TSqlParser.HostContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#date_correlation_optimization_option.
    def visitDate_correlation_optimization_option(self, ctx:TSqlParser.Date_correlation_optimization_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#db_encryption_option.
    def visitDb_encryption_option(self, ctx:TSqlParser.Db_encryption_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#db_state_option.
    def visitDb_state_option(self, ctx:TSqlParser.Db_state_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#db_update_option.
    def visitDb_update_option(self, ctx:TSqlParser.Db_update_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#db_user_access_option.
    def visitDb_user_access_option(self, ctx:TSqlParser.Db_user_access_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#delayed_durability_option.
    def visitDelayed_durability_option(self, ctx:TSqlParser.Delayed_durability_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#external_access_option.
    def visitExternal_access_option(self, ctx:TSqlParser.External_access_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#hadr_options.
    def visitHadr_options(self, ctx:TSqlParser.Hadr_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#mixed_page_allocation_option.
    def visitMixed_page_allocation_option(self, ctx:TSqlParser.Mixed_page_allocation_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#parameterization_option.
    def visitParameterization_option(self, ctx:TSqlParser.Parameterization_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#recovery_option.
    def visitRecovery_option(self, ctx:TSqlParser.Recovery_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#service_broker_option.
    def visitService_broker_option(self, ctx:TSqlParser.Service_broker_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#snapshot_option.
    def visitSnapshot_option(self, ctx:TSqlParser.Snapshot_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#sql_option.
    def visitSql_option(self, ctx:TSqlParser.Sql_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#target_recovery_time_option.
    def visitTarget_recovery_time_option(self, ctx:TSqlParser.Target_recovery_time_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#termination.
    def visitTermination(self, ctx:TSqlParser.TerminationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_index.
    def visitDrop_index(self, ctx:TSqlParser.Drop_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_relational_or_xml_or_spatial_index.
    def visitDrop_relational_or_xml_or_spatial_index(self, ctx:TSqlParser.Drop_relational_or_xml_or_spatial_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_backward_compatible_index.
    def visitDrop_backward_compatible_index(self, ctx:TSqlParser.Drop_backward_compatible_indexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_procedure.
    def visitDrop_procedure(self, ctx:TSqlParser.Drop_procedureContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_trigger.
    def visitDrop_trigger(self, ctx:TSqlParser.Drop_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_dml_trigger.
    def visitDrop_dml_trigger(self, ctx:TSqlParser.Drop_dml_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_ddl_trigger.
    def visitDrop_ddl_trigger(self, ctx:TSqlParser.Drop_ddl_triggerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_function.
    def visitDrop_function(self, ctx:TSqlParser.Drop_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_statistics.
    def visitDrop_statistics(self, ctx:TSqlParser.Drop_statisticsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_table.
    def visitDrop_table(self, ctx:TSqlParser.Drop_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_view.
    def visitDrop_view(self, ctx:TSqlParser.Drop_viewContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_type.
    def visitCreate_type(self, ctx:TSqlParser.Create_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#drop_type.
    def visitDrop_type(self, ctx:TSqlParser.Drop_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#rowset_function_limited.
    def visitRowset_function_limited(self, ctx:TSqlParser.Rowset_function_limitedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#openquery.
    def visitOpenquery(self, ctx:TSqlParser.OpenqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#opendatasource.
    def visitOpendatasource(self, ctx:TSqlParser.OpendatasourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#declare_statement.
    def visitDeclare_statement(self, ctx:TSqlParser.Declare_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#cursor_statement.
    def visitCursor_statement(self, ctx:TSqlParser.Cursor_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#backup_database.
    def visitBackup_database(self, ctx:TSqlParser.Backup_databaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#backup_log.
    def visitBackup_log(self, ctx:TSqlParser.Backup_logContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#backup_certificate.
    def visitBackup_certificate(self, ctx:TSqlParser.Backup_certificateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#backup_master_key.
    def visitBackup_master_key(self, ctx:TSqlParser.Backup_master_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#backup_service_master_key.
    def visitBackup_service_master_key(self, ctx:TSqlParser.Backup_service_master_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#execute_statement.
    def visitExecute_statement(self, ctx:TSqlParser.Execute_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#execute_body.
    def visitExecute_body(self, ctx:TSqlParser.Execute_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#execute_statement_arg.
    def visitExecute_statement_arg(self, ctx:TSqlParser.Execute_statement_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#execute_var_string.
    def visitExecute_var_string(self, ctx:TSqlParser.Execute_var_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#security_statement.
    def visitSecurity_statement(self, ctx:TSqlParser.Security_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_certificate.
    def visitCreate_certificate(self, ctx:TSqlParser.Create_certificateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#existing_keys.
    def visitExisting_keys(self, ctx:TSqlParser.Existing_keysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#private_key_options.
    def visitPrivate_key_options(self, ctx:TSqlParser.Private_key_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#generate_new_keys.
    def visitGenerate_new_keys(self, ctx:TSqlParser.Generate_new_keysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#date_options.
    def visitDate_options(self, ctx:TSqlParser.Date_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#open_key.
    def visitOpen_key(self, ctx:TSqlParser.Open_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#close_key.
    def visitClose_key(self, ctx:TSqlParser.Close_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_key.
    def visitCreate_key(self, ctx:TSqlParser.Create_keyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#key_options.
    def visitKey_options(self, ctx:TSqlParser.Key_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#algorithm.
    def visitAlgorithm(self, ctx:TSqlParser.AlgorithmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#encryption_mechanism.
    def visitEncryption_mechanism(self, ctx:TSqlParser.Encryption_mechanismContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#decryption_mechanism.
    def visitDecryption_mechanism(self, ctx:TSqlParser.Decryption_mechanismContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#grant_permission.
    def visitGrant_permission(self, ctx:TSqlParser.Grant_permissionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#set_statement.
    def visitSet_statement(self, ctx:TSqlParser.Set_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#transaction_statement.
    def visitTransaction_statement(self, ctx:TSqlParser.Transaction_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#go_statement.
    def visitGo_statement(self, ctx:TSqlParser.Go_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#use_statement.
    def visitUse_statement(self, ctx:TSqlParser.Use_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#setuser_statement.
    def visitSetuser_statement(self, ctx:TSqlParser.Setuser_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#dbcc_clause.
    def visitDbcc_clause(self, ctx:TSqlParser.Dbcc_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#dbcc_options.
    def visitDbcc_options(self, ctx:TSqlParser.Dbcc_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#execute_clause.
    def visitExecute_clause(self, ctx:TSqlParser.Execute_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#declare_local.
    def visitDeclare_local(self, ctx:TSqlParser.Declare_localContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#table_type_definition.
    def visitTable_type_definition(self, ctx:TSqlParser.Table_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#xml_type_definition.
    def visitXml_type_definition(self, ctx:TSqlParser.Xml_type_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#xml_schema_collection.
    def visitXml_schema_collection(self, ctx:TSqlParser.Xml_schema_collectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#column_def_table_constraints.
    def visitColumn_def_table_constraints(self, ctx:TSqlParser.Column_def_table_constraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#column_def_table_constraint.
    def visitColumn_def_table_constraint(self, ctx:TSqlParser.Column_def_table_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#column_definition.
    def visitColumn_definition(self, ctx:TSqlParser.Column_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#materialized_column_definition.
    def visitMaterialized_column_definition(self, ctx:TSqlParser.Materialized_column_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#column_constraint.
    def visitColumn_constraint(self, ctx:TSqlParser.Column_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#table_constraint.
    def visitTable_constraint(self, ctx:TSqlParser.Table_constraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#on_delete.
    def visitOn_delete(self, ctx:TSqlParser.On_deleteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#on_update.
    def visitOn_update(self, ctx:TSqlParser.On_updateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#index_options.
    def visitIndex_options(self, ctx:TSqlParser.Index_optionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#index_option.
    def visitIndex_option(self, ctx:TSqlParser.Index_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#declare_cursor.
    def visitDeclare_cursor(self, ctx:TSqlParser.Declare_cursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#declare_set_cursor_common.
    def visitDeclare_set_cursor_common(self, ctx:TSqlParser.Declare_set_cursor_commonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#declare_set_cursor_common_partial.
    def visitDeclare_set_cursor_common_partial(self, ctx:TSqlParser.Declare_set_cursor_common_partialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#fetch_cursor.
    def visitFetch_cursor(self, ctx:TSqlParser.Fetch_cursorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#set_special.
    def visitSet_special(self, ctx:TSqlParser.Set_specialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#constant_LOCAL_ID.
    def visitConstant_LOCAL_ID(self, ctx:TSqlParser.Constant_LOCAL_IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#expression.
    def visitExpression(self, ctx:TSqlParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#primitive_expression.
    def visitPrimitive_expression(self, ctx:TSqlParser.Primitive_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#case_expression.
    def visitCase_expression(self, ctx:TSqlParser.Case_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#unary_operator_expression.
    def visitUnary_operator_expression(self, ctx:TSqlParser.Unary_operator_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#bracket_expression.
    def visitBracket_expression(self, ctx:TSqlParser.Bracket_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#constant_expression.
    def visitConstant_expression(self, ctx:TSqlParser.Constant_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#subquery.
    def visitSubquery(self, ctx:TSqlParser.SubqueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#with_expression.
    def visitWith_expression(self, ctx:TSqlParser.With_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#common_table_expression.
    def visitCommon_table_expression(self, ctx:TSqlParser.Common_table_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#update_elem.
    def visitUpdate_elem(self, ctx:TSqlParser.Update_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#search_condition_list.
    def visitSearch_condition_list(self, ctx:TSqlParser.Search_condition_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#search_condition.
    def visitSearch_condition(self, ctx:TSqlParser.Search_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#search_condition_and.
    def visitSearch_condition_and(self, ctx:TSqlParser.Search_condition_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#search_condition_not.
    def visitSearch_condition_not(self, ctx:TSqlParser.Search_condition_notContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#predicate.
    def visitPredicate(self, ctx:TSqlParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#query_expression.
    def visitQuery_expression(self, ctx:TSqlParser.Query_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#sql_union.
    def visitSql_union(self, ctx:TSqlParser.Sql_unionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#query_specification.
    def visitQuery_specification(self, ctx:TSqlParser.Query_specificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#top_clause.
    def visitTop_clause(self, ctx:TSqlParser.Top_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#top_percent.
    def visitTop_percent(self, ctx:TSqlParser.Top_percentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#top_count.
    def visitTop_count(self, ctx:TSqlParser.Top_countContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#order_by_clause.
    def visitOrder_by_clause(self, ctx:TSqlParser.Order_by_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#for_clause.
    def visitFor_clause(self, ctx:TSqlParser.For_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#xml_common_directives.
    def visitXml_common_directives(self, ctx:TSqlParser.Xml_common_directivesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#order_by_expression.
    def visitOrder_by_expression(self, ctx:TSqlParser.Order_by_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#group_by_item.
    def visitGroup_by_item(self, ctx:TSqlParser.Group_by_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#option_clause.
    def visitOption_clause(self, ctx:TSqlParser.Option_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#option.
    def visitOption(self, ctx:TSqlParser.OptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#optimize_for_arg.
    def visitOptimize_for_arg(self, ctx:TSqlParser.Optimize_for_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#select_list.
    def visitSelect_list(self, ctx:TSqlParser.Select_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#udt_method_arguments.
    def visitUdt_method_arguments(self, ctx:TSqlParser.Udt_method_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#asterisk.
    def visitAsterisk(self, ctx:TSqlParser.AsteriskContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#column_elem.
    def visitColumn_elem(self, ctx:TSqlParser.Column_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#udt_elem.
    def visitUdt_elem(self, ctx:TSqlParser.Udt_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#expression_elem.
    def visitExpression_elem(self, ctx:TSqlParser.Expression_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#select_list_elem.
    def visitSelect_list_elem(self, ctx:TSqlParser.Select_list_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#table_sources.
    def visitTable_sources(self, ctx:TSqlParser.Table_sourcesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#table_source.
    def visitTable_source(self, ctx:TSqlParser.Table_sourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#table_source_item_joined.
    def visitTable_source_item_joined(self, ctx:TSqlParser.Table_source_item_joinedContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#table_source_item.
    def visitTable_source_item(self, ctx:TSqlParser.Table_source_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#open_xml.
    def visitOpen_xml(self, ctx:TSqlParser.Open_xmlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#schema_declaration.
    def visitSchema_declaration(self, ctx:TSqlParser.Schema_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#column_declaration.
    def visitColumn_declaration(self, ctx:TSqlParser.Column_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#change_table.
    def visitChange_table(self, ctx:TSqlParser.Change_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#join_part.
    def visitJoin_part(self, ctx:TSqlParser.Join_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#pivot_clause.
    def visitPivot_clause(self, ctx:TSqlParser.Pivot_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#unpivot_clause.
    def visitUnpivot_clause(self, ctx:TSqlParser.Unpivot_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#full_column_name_list.
    def visitFull_column_name_list(self, ctx:TSqlParser.Full_column_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#table_name_with_hint.
    def visitTable_name_with_hint(self, ctx:TSqlParser.Table_name_with_hintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#rowset_function.
    def visitRowset_function(self, ctx:TSqlParser.Rowset_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#bulk_option.
    def visitBulk_option(self, ctx:TSqlParser.Bulk_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#derived_table.
    def visitDerived_table(self, ctx:TSqlParser.Derived_tableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#RANKING_WINDOWED_FUNC.
    def visitRANKING_WINDOWED_FUNC(self, ctx:TSqlParser.RANKING_WINDOWED_FUNCContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#AGGREGATE_WINDOWED_FUNC.
    def visitAGGREGATE_WINDOWED_FUNC(self, ctx:TSqlParser.AGGREGATE_WINDOWED_FUNCContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#ANALYTIC_WINDOWED_FUNC.
    def visitANALYTIC_WINDOWED_FUNC(self, ctx:TSqlParser.ANALYTIC_WINDOWED_FUNCContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#SCALAR_FUNCTION.
    def visitSCALAR_FUNCTION(self, ctx:TSqlParser.SCALAR_FUNCTIONContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#BINARY_CHECKSUM.
    def visitBINARY_CHECKSUM(self, ctx:TSqlParser.BINARY_CHECKSUMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#CAST.
    def visitCAST(self, ctx:TSqlParser.CASTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#CONVERT.
    def visitCONVERT(self, ctx:TSqlParser.CONVERTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#CHECKSUM.
    def visitCHECKSUM(self, ctx:TSqlParser.CHECKSUMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#COALESCE.
    def visitCOALESCE(self, ctx:TSqlParser.COALESCEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#CURRENT_TIMESTAMP.
    def visitCURRENT_TIMESTAMP(self, ctx:TSqlParser.CURRENT_TIMESTAMPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#CURRENT_USER.
    def visitCURRENT_USER(self, ctx:TSqlParser.CURRENT_USERContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#DATEADD.
    def visitDATEADD(self, ctx:TSqlParser.DATEADDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#DATEDIFF.
    def visitDATEDIFF(self, ctx:TSqlParser.DATEDIFFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#DATENAME.
    def visitDATENAME(self, ctx:TSqlParser.DATENAMEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#DATEPART.
    def visitDATEPART(self, ctx:TSqlParser.DATEPARTContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#GETDATE.
    def visitGETDATE(self, ctx:TSqlParser.GETDATEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#GETUTCDATE.
    def visitGETUTCDATE(self, ctx:TSqlParser.GETUTCDATEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#IDENTITY.
    def visitIDENTITY(self, ctx:TSqlParser.IDENTITYContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#MIN_ACTIVE_ROWVERSION.
    def visitMIN_ACTIVE_ROWVERSION(self, ctx:TSqlParser.MIN_ACTIVE_ROWVERSIONContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#NULLIF.
    def visitNULLIF(self, ctx:TSqlParser.NULLIFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#STUFF.
    def visitSTUFF(self, ctx:TSqlParser.STUFFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#SESSION_USER.
    def visitSESSION_USER(self, ctx:TSqlParser.SESSION_USERContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#SYSTEM_USER.
    def visitSYSTEM_USER(self, ctx:TSqlParser.SYSTEM_USERContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#ISNULL.
    def visitISNULL(self, ctx:TSqlParser.ISNULLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#XML_DATA_TYPE_FUNC.
    def visitXML_DATA_TYPE_FUNC(self, ctx:TSqlParser.XML_DATA_TYPE_FUNCContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#xml_data_type_methods.
    def visitXml_data_type_methods(self, ctx:TSqlParser.Xml_data_type_methodsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#value_method.
    def visitValue_method(self, ctx:TSqlParser.Value_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#query_method.
    def visitQuery_method(self, ctx:TSqlParser.Query_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#exist_method.
    def visitExist_method(self, ctx:TSqlParser.Exist_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#modify_method.
    def visitModify_method(self, ctx:TSqlParser.Modify_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#nodes_method.
    def visitNodes_method(self, ctx:TSqlParser.Nodes_methodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#switch_section.
    def visitSwitch_section(self, ctx:TSqlParser.Switch_sectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#switch_search_condition_section.
    def visitSwitch_search_condition_section(self, ctx:TSqlParser.Switch_search_condition_sectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#as_column_alias.
    def visitAs_column_alias(self, ctx:TSqlParser.As_column_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#as_table_alias.
    def visitAs_table_alias(self, ctx:TSqlParser.As_table_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#table_alias.
    def visitTable_alias(self, ctx:TSqlParser.Table_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#with_table_hints.
    def visitWith_table_hints(self, ctx:TSqlParser.With_table_hintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#insert_with_table_hints.
    def visitInsert_with_table_hints(self, ctx:TSqlParser.Insert_with_table_hintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#table_hint.
    def visitTable_hint(self, ctx:TSqlParser.Table_hintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#index_value.
    def visitIndex_value(self, ctx:TSqlParser.Index_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#column_alias_list.
    def visitColumn_alias_list(self, ctx:TSqlParser.Column_alias_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#column_alias.
    def visitColumn_alias(self, ctx:TSqlParser.Column_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#table_value_constructor.
    def visitTable_value_constructor(self, ctx:TSqlParser.Table_value_constructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#expression_list.
    def visitExpression_list(self, ctx:TSqlParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#ranking_windowed_function.
    def visitRanking_windowed_function(self, ctx:TSqlParser.Ranking_windowed_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#aggregate_windowed_function.
    def visitAggregate_windowed_function(self, ctx:TSqlParser.Aggregate_windowed_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#analytic_windowed_function.
    def visitAnalytic_windowed_function(self, ctx:TSqlParser.Analytic_windowed_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#all_distinct_expression.
    def visitAll_distinct_expression(self, ctx:TSqlParser.All_distinct_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#over_clause.
    def visitOver_clause(self, ctx:TSqlParser.Over_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#row_or_range_clause.
    def visitRow_or_range_clause(self, ctx:TSqlParser.Row_or_range_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#window_frame_extent.
    def visitWindow_frame_extent(self, ctx:TSqlParser.Window_frame_extentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#window_frame_bound.
    def visitWindow_frame_bound(self, ctx:TSqlParser.Window_frame_boundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#window_frame_preceding.
    def visitWindow_frame_preceding(self, ctx:TSqlParser.Window_frame_precedingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#window_frame_following.
    def visitWindow_frame_following(self, ctx:TSqlParser.Window_frame_followingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#create_database_option.
    def visitCreate_database_option(self, ctx:TSqlParser.Create_database_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#database_filestream_option.
    def visitDatabase_filestream_option(self, ctx:TSqlParser.Database_filestream_optionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#database_file_spec.
    def visitDatabase_file_spec(self, ctx:TSqlParser.Database_file_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#file_group.
    def visitFile_group(self, ctx:TSqlParser.File_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#file_spec.
    def visitFile_spec(self, ctx:TSqlParser.File_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#entity_name.
    def visitEntity_name(self, ctx:TSqlParser.Entity_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#entity_name_for_azure_dw.
    def visitEntity_name_for_azure_dw(self, ctx:TSqlParser.Entity_name_for_azure_dwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#entity_name_for_parallel_dw.
    def visitEntity_name_for_parallel_dw(self, ctx:TSqlParser.Entity_name_for_parallel_dwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#full_table_name.
    def visitFull_table_name(self, ctx:TSqlParser.Full_table_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#table_name.
    def visitTable_name(self, ctx:TSqlParser.Table_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#simple_name.
    def visitSimple_name(self, ctx:TSqlParser.Simple_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#func_proc_name.
    def visitFunc_proc_name(self, ctx:TSqlParser.Func_proc_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#ddl_object.
    def visitDdl_object(self, ctx:TSqlParser.Ddl_objectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#full_column_name.
    def visitFull_column_name(self, ctx:TSqlParser.Full_column_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#column_name_list_with_order.
    def visitColumn_name_list_with_order(self, ctx:TSqlParser.Column_name_list_with_orderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#column_name_list.
    def visitColumn_name_list(self, ctx:TSqlParser.Column_name_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#cursor_name.
    def visitCursor_name(self, ctx:TSqlParser.Cursor_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#on_off.
    def visitOn_off(self, ctx:TSqlParser.On_offContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#clustered.
    def visitClustered(self, ctx:TSqlParser.ClusteredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#null_notnull.
    def visitNull_notnull(self, ctx:TSqlParser.Null_notnullContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#null_or_default.
    def visitNull_or_default(self, ctx:TSqlParser.Null_or_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#scalar_function_name.
    def visitScalar_function_name(self, ctx:TSqlParser.Scalar_function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#begin_conversation_timer.
    def visitBegin_conversation_timer(self, ctx:TSqlParser.Begin_conversation_timerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#begin_conversation_dialog.
    def visitBegin_conversation_dialog(self, ctx:TSqlParser.Begin_conversation_dialogContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#contract_name.
    def visitContract_name(self, ctx:TSqlParser.Contract_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#service_name.
    def visitService_name(self, ctx:TSqlParser.Service_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#end_conversation.
    def visitEnd_conversation(self, ctx:TSqlParser.End_conversationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#waitfor_conversation.
    def visitWaitfor_conversation(self, ctx:TSqlParser.Waitfor_conversationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#get_conversation.
    def visitGet_conversation(self, ctx:TSqlParser.Get_conversationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#queue_id.
    def visitQueue_id(self, ctx:TSqlParser.Queue_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#send_conversation.
    def visitSend_conversation(self, ctx:TSqlParser.Send_conversationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#data_type.
    def visitData_type(self, ctx:TSqlParser.Data_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#default_value.
    def visitDefault_value(self, ctx:TSqlParser.Default_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#constant.
    def visitConstant(self, ctx:TSqlParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#sign.
    def visitSign(self, ctx:TSqlParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#id.
    def visitId(self, ctx:TSqlParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#simple_id.
    def visitSimple_id(self, ctx:TSqlParser.Simple_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#comparison_operator.
    def visitComparison_operator(self, ctx:TSqlParser.Comparison_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#assignment_operator.
    def visitAssignment_operator(self, ctx:TSqlParser.Assignment_operatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TSqlParser#file_size.
    def visitFile_size(self, ctx:TSqlParser.File_sizeContext):
        return self.visitChildren(ctx)



del TSqlParser