# Remove python2 as you want to use only python v3
    sudo apt purge -y python2.7-minimal

# You already have Python3 but don't care about the version 
    sudo ln -s /usr/bin/python3 /usr/bin/python

# Install pip
    sudo apt install -y python3-pip
    sudo ln -s /usr/bin/pip3 /usr/bin/pip

# Set the airflow home directory
    export AIRFLOW_HOME=~/airflow

# setting the apache airflow version
    AIRFLOW_VERSION=2.2.3


# Running airflow webserver
    airflow webserver

# Running scheduler
    airflow scheduler

