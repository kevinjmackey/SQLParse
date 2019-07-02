USE [Legacy];
GO

/****** Object:  View [EQP].[Carrier_VW]    Script Date: 8/13/2018 4:32:03 PM ******/
SET ANSI_NULLS ON;
GO

SET QUOTED_IDENTIFIER ON;
GO



/* ========================================================================================================   
   Author:		 
   Create date:     
   Description:	Processes /OPS/RTES/Load_Carrier messages   
   ========================================================================================================   
   
   Versioned 05/18/2017: Reshmi - IBF_CNTRCT_REF_NBR column was moved from REOCCUR table to BASE table.
              
   ========================================================================================================*/




ALTER VIEW [EQP].[Carrier_VW]
AS
SELECT DISTINCT [IBF_SCAC_CD]                                                                        AS [SCAC_CD]
      ,[IBF_NM]                                                                             AS [Carrier_NM]
      ,[DATE]                                                                               AS [Create_TS]
      ,NULL                                                                                 AS [Create_ID]
      ,[dbo].[ConvertimeToUTC]([dbo].[FormatDateTimeForXML]([I].[DATE], [I].[TIME]), 'EST') AS [Modify_TS]
      ,NULL                                                                                 AS [Modify_ID]
      ,[I].[PROCEDURE]                                                                      AS [Source_Create_ID]
      ,[I].[PROCEDURE]                                                                      AS [Source_Modify_ID]
      ,'ETL'                                                                                AS [System_ID]
      ,[I].[IBF_EDI_BL_IND]                                                                 AS [EDI_Bill_Of_Lading_CD]
      ,[I].[IBF_EDI_TRACING_IND]                                                            AS [EDI_Tracking_IN]
      ,[I].[IBF_CNTRCT_REF_NBR]                                                             AS [Special_Quote_Reference_NB]
      ,NULL                                                                                 AS [Car_Location_Msg_Time_Zone_CD]
      ,NULL                                                                                 AS [Country_CD]
      ,[I].[DTS_DTTMSP]                                                                     AS [IBF_DTS_DTTMSP_NB]
      ,[I].[RECORD_KEY]                                                                     AS [IBF_Record_KEY]
      ,[I].[USER]                                                                           AS [M204_Create_ID]
      ,[I].[DATE]                                                                           AS [M204_Create_TS]
      ,[I].[USER]                                                                           AS [M204_Modify_ID]
      ,[dbo].[ConvertimeToUTC]([dbo].[FormatDateTimeForXML]([I].[DATE], [I].[TIME]), 'EST') AS [M204_Modify_TS]
      ,[Other]                                                                              AS [Other_Transportation_Mode_IN]
      ,[Rail]                                                                               AS [Rail_IN]
      ,[Ship]                                                                               AS [Ship_IN]
      ,NULL                                                                                 AS [Create_User_ID]
      ,NULL                                                                                 AS [Modify_User_ID]
      ,[I].[SOURCEDELETED]                                                                  AS [Source_Delete_IN]
FROM [Legacy].[M204_IBF] AS [I]
    JOIN
    (
        SELECT [IBF_RECORD_KEY]
              ,ISNULL(MAX(   CASE [IBF_TRVL_MODE]
                                 WHEN 'OTHER' THEN
                                     'Y'
                             END
                         )
                     ,'N'
                     ) AS [Other]
              ,ISNULL(MAX(   CASE [IBF_TRVL_MODE]
                                 WHEN 'RAIL' THEN
                                     'Y'
                             END
                         )
                     ,'N'
                     ) AS [Rail]
              ,ISNULL(MAX(   CASE [IBF_TRVL_MODE]
                                 WHEN 'SHIP' THEN
                                     'Y'
                             END
                         )
                     ,'N'
                     ) AS [Ship]
        FROM [Legacy].[M204_IBF_REOCCUR]
        GROUP BY
            [IBF_RECORD_KEY]
    )                    AS [Ir]
    ON [I].[RECORD_KEY] = [Ir].[IBF_RECORD_KEY]
WHERE [I].[RECTYPE] = 'Carrier';















GO


