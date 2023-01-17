# install postgres provider
    pip install apache-airflow-providers-postgres

# creating postgres connection

# creating httpSensor connection

# loading the data into table
    export PGPASSWORD="postgres"
    psql -h localhost \
    -p 5432 \
    -U postgres \
    -d postgres \
    -f /d/development/POC/workflow/api-postgres-pipeline/loading_csv_postgres.sql
