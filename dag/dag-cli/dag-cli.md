# list all dags 
    
    airflow dags list 
    docker exec  \
        -it airflow-airflow-worker-1  \
        airflow dags list

**POWERSHELL**

    airflow dags list 
    docker exec  `
        -it airflow-airflow-worker-1  `
        airflow dags list

# Triggering a DAG using the Airflow CLI

    airflow dags trigger dag1

    airflow dags trigger \
        -c '{"supermarket_id": 1}' dag1
    airflow dags trigger \
        --conf '{"supermarket_id": 1}' dag1

