#!/bin/sh

if [ -f "./sqlite/database.db" ]
then
	echo "[INFO] Database file found. Running script."
	python app_b.py
else
	echo "[INFO] Database file does not exist. Creating a new one from schema.sql"
	sqlite3 ./sqlite/database.db < schema.sql
	python app_b.py
fi
