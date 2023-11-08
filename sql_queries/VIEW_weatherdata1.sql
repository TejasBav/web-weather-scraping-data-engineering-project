USE weatherdatastream
GO
CREATE VIEW bronze.weatherdata1
AS
SELECT Temperature, Unit, Sky, Time FROM OPENROWSET(
    BULK'0_8a29b826e55a49c79b640836f456f855_1.json',
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
SELECT * FROM bronze.weatherdata1