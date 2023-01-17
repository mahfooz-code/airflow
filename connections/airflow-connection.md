# Syntax
    
    airflow connections [-h] COMMAND

# list airflow connection

    docker exec  -it airflow-airflow-worker-1 airflow connections list

# Get the connection details
    
    docker exec  \
        -it airflow-airflow-worker-1 \
        airflow connections \
        get postgres_db

