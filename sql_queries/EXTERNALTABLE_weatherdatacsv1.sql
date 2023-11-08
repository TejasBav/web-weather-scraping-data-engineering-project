use weatherdatastream
GO
CREATE EXTERNAL TABLE silver.weatherdatacsv1
WITH(
    DATA_SOURCE=weatherdatastream,
    LOCATION='silver/weatherdata1',
    FILE_FORMAT=CSV_FILES
)
AS
SELECT * FROM bronze.weatherdata1