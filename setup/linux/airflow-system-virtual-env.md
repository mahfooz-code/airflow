# Remove python2
sudo apt purge -y python2.7-minimal

# You already have Python3 but don't care about the version 
sudo ln -s /usr/bin/python3 /usr/bin/python

# Same for pip
sudo apt install -y python3-pip
sudo ln -s /usr/bin/pip3 /usr/bin/pip

# Confirm the new version of Python: 3
python --version

export AIRFLOW_HOME=/e/workflow/airflow
AIRFLOW_VERSION=2.2.3
PYTHON_VERSION="$(python --version|cut -d " " -f2|cut -d "." -f 1-2)"

# For example: 3.6
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

# For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.2.3/constraints-3.6.txt
pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

# The Standalone command will initialise the database, make a user,
# and start all components for you.
airflow standalone