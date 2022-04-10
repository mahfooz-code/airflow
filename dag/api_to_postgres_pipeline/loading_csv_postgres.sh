
export PGPASSWORD="postgres"
psql -h localhost \
    -p 5432 \
    -U postgres \
    -d postgres \
    -f /d/development/POC/workflow/api-postgres-pipeline/loading_csv_postgres.sql