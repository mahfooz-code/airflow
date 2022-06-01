Sensors are special types of operators whose purpose is to wait on some external or internal trigger. These are commonly used to trigger some or all of the DAG, based on the occurrence of some external event. Some common types of sensors are:


1. ExternalTaskSensor waits on another task (in a different DAG) to complete execution.
2. HivePartitionSensor waits for a specific value of partition of hive table to get created.
3. S3KeySensor are used to wait for a specific file or directory to be available on an S3 bucket.



