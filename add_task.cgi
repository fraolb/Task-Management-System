#!"c:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI;
use DBI;

my $cgi = CGI->new;
print $cgi->header;

my $name = $cgi->param('name');
my $description = $cgi->param('description');
my $due_date = $cgi->param('due_date');
my $status = $cgi->param('status');

my $dbh = DBI->connect("dbi:SQLite:dbname=tasks.db", "", "", { RaiseError => 1, AutoCommit => 1 }) or die $DBI::errstr;

my $sth = $dbh->prepare("INSERT INTO tasks (name, description, due_date, status) VALUES (?, ?, ?, ?)");
$sth->execute($name, $description, $due_date, $status) or die $dbh->errstr;

print "<h1>Task Added Successfully</h1>";
print "<a href='/task_form.html'>Go back to Tasks</a>";

$dbh->disconnect;
