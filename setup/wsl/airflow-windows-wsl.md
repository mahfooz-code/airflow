# Remove python2 as you want to use only python v3
    sudo apt purge -y python2.7-minimal

# You already have Python3 but don't care about the version 
    sudo ln -s /usr/bin/python3 /usr/bin/python

# Install pip
    sudo apt install -y python3-pip
    sudo ln -s /usr/bin/pip3 /usr/bin/pip

# Set the airflow home directory and default will be ~/airflow
    export AIRFLOW_HOME=/e/workflow/airflow-wsl

# setting the apache airflow version
    $AIRFLOW_VERSION=2.2.3

# setting version of python which is installed in the system
    PYTHON_VERSION="$(python --version|cut -d " " -f2|cut -d "." -f 1-2)"

# setting correct url which mathcing airflow and python version
    $CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

# install the airflow using corerct version
    pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# Now add the path of airflow

    echo 'PATH=$PATH:$HOME/.local/bin'>>~/.bashrc

# source the .bashrc to reflect PATH variable in current session and it will be releflected automatically in next session.

    source ~/.bashrc   
    . ~/.bashrc   

# standalone mode 

The Standalone command will initialise the database, make a user, and start all components for you.
    
    airflow standalone

# running in proper mode

# Setting up the database

    airflow db check
    airflow config get-value core sql_alchemy_conn

# Running airflow webserver
    airflow webserver

# Running scheduler
    airflow scheduler

