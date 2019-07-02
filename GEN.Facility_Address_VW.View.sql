USE [Legacy]
GO
/****** Object:  View [GEN].[Facility_Address_VW]    Script Date: 10/19/2018 12:04:54 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO


CREATE VIEW [GEN].[Facility_Address_VW]
AS
    SELECT [Message_Description] = 'Facility Address'
			,[Soft_Delete_IN] = CASE WHEN [x].[SOURCEDELETED] = 1 THEN 'Y'
								ELSE 'N'
							END
			,[Facility_CD]					= [x].[ORZ_RFRNC_CD]
			,[Address_Type_Key]				= 1
			,[Geographic_Address_KEY]		= 2
			,[Street_Address_1_TX]			= [x].[PLC_ADDR_STREET]
			,[Postal_CD]					= [x].[PLC_ADDR_ZIP]
			,[Country_CD]					= ISNULL([x].[RGN_CTRY_ABBR], [x].[ORZ_CTRY_ALPHA])		--Added ISNULL 3-7-12 
			,[City_NM]						= [x].[RGN_CITY_NM_OF_CZ]
			,[State_Province_CD]            = [x].[RGN_ST_ABBR]
			,[XORZ_DTS_DTTMSP_NB]			= [x].[DTS_DTTMSP]
			,[XORZ_Record_KEY]				= [x].[RECORD_KEY]
			,[Source_Delete_IN]				= [x].[SOURCEDELETED]

			,[Create_ID]					= NULL
			,[Create_TS]					= [dbo].[FormatDateTimeForXML]([x].[DATE], NULL)
			,[Modify_ID]					= NULL
			,[Modify_TS]					= [dbo].[FormatDateTimeForXML]([x].[DATE], NULL)
        FROM [Legacy].[M204_XORZ] [x] WITH (NOLOCK) 
		LEFT JOIN [Legacy].[M204_XORZ_REOCCUR] [r] WITH (NOLOCK) 
			ON [x].[RECORD_KEY] = [r].[XORZ_RECORD_KEY] AND [r].[OCCNO] = 1
        WHERE [x].[RECTYPE] = 'ORZ.BASE'  
			AND [x].[ORZ_TYPE] IN ('TERMINAL','BREAKBULK','RELAY','RAILHEAD','REX SALVAGE STORE','GARAGE','PORT','RELAY NO TERMINAL')		
			AND [x].[ORZ_CLSD_IND] IS NULL
			AND [x].[ORZ_RFRNC_CD] IS NOT NULL
			AND ([x].[RGN_CITY_NM_OF_CZ] IS NOT NULL OR
			     [x].[PLC_ADDR_STREET]  IS NOT NULL OR
				 [x].[PLC_ADDR_ZIP] IS NOT NULL OR
				 [x].[RGN_CTRY_ABBR] IS NOT NULL OR
				 [x].[ORZ_CTRY_ALPHA] IS NOT NULL OR
				 [x].[RGN_ST_ABBR] IS NOT NULL)
			AND (ISNULL([r].[ORZ_HISTORICAL_STATUS],'') <> 'CLOSED'
			OR ISNULL([r].[ORZ_HISTORICAL_STATUS_STDT],'') > GETDATE());


GO
