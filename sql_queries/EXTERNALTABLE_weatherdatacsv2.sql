use weatherdatastream
GO
CREATE EXTERNAL TABLE silver.weatherdatacsv2
WITH(
    DATA_SOURCE=weatherdatastream,
    LOCATION='silver/weatherdata2',
    FILE_FORMAT=CSV_FILES
)
AS
SELECT * FROM bronze.weatherdata2