from tmpHumDb import TmpHumDb

tmpHumDb = TmpHumDb(
    hostStr="localhost",  # Or your cloud host
    dbPort=5432,
    dbStr="postgres",
    uNameStr="postgres",
    dbPassStr="Password@12345"
)
tmpHumDb.insertData(30, 55, "s1")
print("Data insertion testing complete...")
