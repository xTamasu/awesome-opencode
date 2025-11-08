#!/bin/bash
pgpassword=$1
dbname=$2

export PGPASSWORD=$pgpassword

echo "Waiting for PostgreSQL to be ready..."
for i in {1..60};
do
    psql -h localhost -U postgres -d postgres -c "SELECT 1" > /dev/null 2>&1
    if [ $? -eq 0 ]
    then
        echo "PostgreSQL server ready"
        break
    else
        echo "Not ready yet..."
        sleep 1
    fi
done

# Check if database exists, create if it doesn't
db_exists=$(psql -h localhost -U postgres -d postgres -tAc "SELECT 1 FROM pg_database WHERE datname='$dbname'")
if [ "$db_exists" != "1" ]
then
    echo "Creating database $dbname"
    psql -h localhost -U postgres -d postgres -c "CREATE DATABASE \"$dbname\""
else
    echo "Database $dbname already exists"
fi

# Execute any SQL files in the postgres directory
for f in .devcontainer/postgres/*.sql
do
    if [ -f "$f" ] && [ "$f" != ".devcontainer/postgres/setup.sql" ]
    then
        echo "Executing $f"
        psql -h localhost -U postgres -d $dbname -f $f
    fi
done

unset PGPASSWORD

