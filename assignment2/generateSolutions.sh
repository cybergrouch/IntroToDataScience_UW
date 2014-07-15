#!/bin/bash

function runQuery() {
    sqlite3 $1 < $2.sql > $2.txt
}

runQuery "reuters.db" "select"
runQuery "reuters.db" "select_project"
runQuery "reuters.db" "union"
runQuery "reuters.db" "count"
runQuery "reuters.db" "big_documents"
runQuery "reuters.db" "two_words"

