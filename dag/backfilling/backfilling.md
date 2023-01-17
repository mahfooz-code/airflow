# back-filling
Schedule intervals become even more powerful when combined with the 
concept of back-filling, which allows you to execute a new DAG for 
historical schedule intervals that occurred in the past.

This feature allows you to easily create (or backfill ) new data sets 
with historical data simply by running your DAG for these past schedule 
intervals.


# running backfilling 

    airflow dags backfill tutorial \
        --start-date 2015-06-01 \
        --end-date 2015-06-07

