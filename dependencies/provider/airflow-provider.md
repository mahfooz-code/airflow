# list all provides

    airflow providers list

# on docker

    docker exec -it <airflow-webserver> \
        airflow providers list

    docker exec -it airflow-airflow-webserver-1 \
        airflow providers list

# installing airflow providers

    pip install \
        apache-airflow-providers-http==2.0.0
    
    docker exec -it <airflow-webserver> \
        pip install \
        apache-airflow-providers-http==2.0.0
    
    docker exec -it airflow-airflow-webserver-1 \
        pip install \
        apache-airflow-providers-http==2.0.0
     