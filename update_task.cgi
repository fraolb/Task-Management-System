#!"c:\xampp\perl\bin\perl.exe"

use strict;
use warnings;
use CGI;
use DBI;

my $cgi = CGI->new;
print $cgi->header;

my $dbh = DBI->connect("dbi:SQLite:dbname=tasks.db", "", "", { RaiseError => 1, AutoCommit => 1 }) or die $DBI::errstr;

foreach my $param ($cgi->param) {
    if ($param =~ /^task_(\d+)$/) {
        my $task_id = $1;
        my $new_status = $cgi->param($param);
        my $sth = $dbh->prepare("UPDATE tasks SET status = ? WHERE id = ?");
        $sth->execute($new_status, $task_id) or die $dbh->errstr;
    }
}

print "<h1>Tasks Updated Successfully</h1>";
print "<a href='/task_form.html'>Go Back</a>";

$dbh->disconnect;

