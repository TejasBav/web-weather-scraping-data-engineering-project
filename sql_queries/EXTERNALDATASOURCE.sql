USE weatherdatastream
GO

CREATE EXTERNAL DATA SOURCE weatherdatastream
WITH(
    LOCATION = 'https://streamingdatastorage2.blob.core.windows.net/output'
)