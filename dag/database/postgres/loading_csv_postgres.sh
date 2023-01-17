export PGPASSWORD="postgres"
psql -h localhost \
  -p 5432 \
  -U postgres \
  -d postgres \
  -f loading_csv_postgres.sql