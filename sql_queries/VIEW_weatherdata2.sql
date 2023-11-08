USE weatherdatastream
GO
CREATE VIEW bronze.weatherdata2
AS
SELECT Temperature, Unit, Sky, Time FROM OPENROWSET(
    BULK'0_cc45287b0de04887896f6371c805b117_1.json',
    DATA_SOURCE = 'weatherdatastream',
    FORMAT='CSV',
    PARSER_VERSION='1.0',
    FIELDTERMINATOR='0x0b',
    FIELDQUOTE='0x0b',
    ROWTERMINATOR='0x0a'
)WITH(
    jsondata NVARCHAR(MAX)
)
AS [WEATHERDATA]
CROSS APPLY OPENJSON(jsondata)
WITH(
    Temperature VARCHAR(20),
    Unit VARCHAR(20),
    Sky VARCHAR(20),
    Time VARCHAR(20)
)
GO
SELECT * FROM bronze.weatherdata2