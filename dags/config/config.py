import os
import boto3
from botocore.client import Config

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# CHROME_DRIVER_PATH = os.path.join(ROOT_DIR,"lib/selenium/chromedriver'")

class SSI_API_CONFIG:
    CONSUMER_ID = "a7a664018a9e4114a1a5812838a91e6b"
    CONSUMER_SECRET = "468fc69fe1654ff6b3f46937f954b010"
    PRIVATE_KEY = "PFJTQUtleVZhbHVlPjxNb2R1bHVzPjEzVWUyVTVJRFZxc2JyZjR6ZHJwVGpvVm8wb250cUVrUU5Hd2x1ZXd4VTk0TjducFZsMFRqN2NOQlhDTUYxQ2VlTlJYc1dTT1VMWGFvOTBEY1FzRFNpeCtpNk1uQzBjOVNiQXVXVXIwMjNuRkhsaVRhNVdnUG4zaXZ4dE1CVDIzYVhLTDV4Sk8yUFpRTVB1RG9lR09ENXVWL2VySGZNaitlcGtVcnpnVHJwMD08L01vZHVsdXM+PEV4cG9uZW50PkFRQUI8L0V4cG9uZW50PjxQPjJLOXJlK3c2Q0gyL3V3Vi9GTjhNOFBXQVVsM1NRUWl3dDNISmlWNGhacllLY2JuWS9mUHRmSjdBRDk5MTU2cC9zc0RjaVpkY0VsME0yM0l1aExKalB3PT08L1A+PFE+L295c3o1ZE92RnA5V2lSeldIRk5rTFNZYUJWdzQxSUFPbkJxZFd6K3VZTEpYZTZ6aVFWS01RdytQazNCWnlLelRVMHdoNUoxUTYzZ2RpODRWTUdqSXc9PTwvUT48RFA+S3JEbERGVk9XYjNzdUh3c3ZYLzBuTVRCczNpb3BBZUNTYUl4Z3M3NDViT1grekFTZ0hZK28vN2krRDJlalRZYVVxMk14Yzc4Wk9IUVZxdjRYa3lISVE9PTwvRFA+PERRPi9QTUVBeUlEcnU1cEpIdVdWNnYzL1RWSlFoMFVXZ0N4azJFRW1YM2ZQcSsxdE84d1g1ZnZHd0JrbGZza2xuMklHZWY3c3EwYWRFL0QvdzE3ZDlZWWF3PT08L0RRPjxJbnZlcnNlUT5hbFU3UTdHMHU5TEt5TzFNcFo0anBvY0U1UUNWZStzUlBBRHZEVFVOT2VxMkpRQTdUanBKM3NTa3hiMFVFQ0oyM0tEcWRpckw5bFhBZjJZUEFqakUrQT09PC9JbnZlcnNlUT48RD5KUG10ako5NWtBa2lsSEd3R2l2YVpCbGx3enNqcTV6bDZ0WFJsMlExbXZiemE2VFZIWVFscWtGQTA5RW55WXlGVmJralA0ZEJRU3FrVmdERTZXNTVacjF6QlBaaVVqQnNoUWhKYmhuVmRHaWZ3b3dMZXNWTnFXZ0FZOTlGWTR4M1A5alBhYWVGejRMM0RzWmVrVFdVTVlmamdYcm5LeGcwSWVmRUtnUkxKQVU9PC9EPjwvUlNBS2V5VmFsdWU+"

class SHAREPOINT_CONFIG:
    SITE_URL = "https://kpimvn.sharepoint.com/sites/dataengineer"
    STOCK_CS01_RELATIVE_URL = "/sites/dataengineer/Shared Documents/Data Warehouse SQL Server/Industry - Stock/CS01"
    CAFEF_RELATIVE_URL = STOCK_CS01_RELATIVE_URL + \
        "/2. Data Warehouse/1. Data Source Layer" + "/cafef"
    CAFEF_HISTORY_PRICE_RELATIVE_URL = CAFEF_RELATIVE_URL + "/History Price"
    CAFEF_HISTORY_PRICE_ARCHIVE_RELATIVE_URL = CAFEF_RELATIVE_URL + "/History Price Archive"
    SSI_RELATIVE_URL = STOCK_CS01_RELATIVE_URL + \
        "/2. Data Warehouse/1. Data Source Layer" + "/ssi"
    USERNAME = "hai.nguyen@kpim.vn"
    PASSWORD = "xxxxxx"

class SQL_SERVER_CONFIG:
    # -- Window CONNECTION_STRING = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=10.10.10.20,1436;DATABASE=dw_stock;UID=etl;PWD=KPIM@#2022;Trusted_Connection=yes;TrustServerCertificate=Yes;"
    # MacOS
    CONNECTION_STRING = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=222.252.14.117;DATABASE=dw_stock;UID=etl;PWD=KPIM#2022;TrustServerCertificate=Yes;"

class MinIO_S3_client:
    s3 = boto3.client('s3',
                    endpoint_url='http://127.0.0.1:9000',
                    aws_access_key_id='khanhlq10',
                    aws_secret_access_key='khanhlq10',
                    config=Config(signature_version='s3v4')
                    )

class MinIO_S3_resource:
    s3 = boto3.resource('s3',
                    endpoint_url='http://127.0.0.1:9000',
                    aws_access_key_id='khanhlq10',
                    aws_secret_access_key='khanhlq10',
                    config=Config(signature_version='s3v4')
                    )