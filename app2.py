# -*- coding: utf-8 -*-
"""
    By Francis
"""
# from optparse import Values
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
s3_data_source_path='s3://frankyego-bucket/Mydata/survey_results_public.csv'
 # copy data path from s3 bucket and copy the file name
s3_data_path_output='s3://frankyego-bucket/data-output' 
#same as s3 bucket but in a different folder
def main():
    spark=SparkSession.builder.appName('YegoDemoApp').getOrCreate()
    all_data=spark.read.csv(s3_data_source_path,header=True)
    print("Total no of records:%s"% all_data.count())
    selected_data=all_data.where((col("Country")=='United States')&(col("WorkWeekHrs")>45))
    print("The number of negineers who who wok more than 45hrs of week in US %s"% selected_data.count())
    selected_data.write.mode("overwrite").parquet(s3_data_path_output)
    print("selected data was successfully saved to S3:%s" % s3_data_path_output)
if __name__=='_main_':
    main()