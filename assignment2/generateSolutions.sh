#!/bin/bash

function runQuery() {
    sqlite3 $1 < $2.sql > $2.txt
}

runQuery "reuters.db" "select"
runQuery "reuters.db" "select_project"
runQuery "reuters.db" "union"
#sqlite3 reuters.db < select.sql > select.txt
#sqlite3 reuters.db < select_project.sql > select_project.txt

