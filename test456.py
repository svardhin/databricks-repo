df = spark.read.format("csv").load("dbfs:/FileStore/tables/test.csv")
display(df)
