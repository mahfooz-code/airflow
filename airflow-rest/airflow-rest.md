# Sending requests to the REST API
ENDPOINT_URL="http://localhost:8080/"

curl -X GET  \
    --user "airflow:airflow" \
    "${ENDPOINT_URL}/api/v1/pools"

