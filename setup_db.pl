#!/usr/bin/env perl
use strict;
use warnings;
use DBI;
#use DBD::SQLite;


# Connect to SQLite database
my $dbh = DBI->connect("dbi:SQLite:dbname=tasks.db", "", "", { RaiseError => 1, AutoCommit => 1 }) or die $DBI::errstr;

# Create tasks table
my $sql = qq{
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        status TEXT
    )
};
$dbh->do($sql) or die $dbh->errstr;
print "Database and table created successfully\n";

$dbh->disconnect;
