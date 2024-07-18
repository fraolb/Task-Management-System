#!"c:\xampp\perl\bin\perl.exe"

use strict;
use warnings;
use CGI;
use DBI;

my $cgi = CGI->new;
print $cgi->header;

my $dbh = DBI->connect("dbi:SQLite:dbname=tasks.db", "", "", { RaiseError => 1, AutoCommit => 1 }) or die $DBI::errstr;

my $sth = $dbh->prepare("SELECT id, name, status FROM tasks");
$sth->execute();

print "<table border='1'>";
print "<tr><th>Name</th><th>Status</th></tr>";
while (my $row = $sth->fetchrow_hashref) {
    print "<tr>";
    print "<td>" . $cgi->escapeHTML($row->{name}) . "</td>";
    print "<td>";
    print "<select name='task_" . $cgi->escapeHTML($row->{id}) . "'>";
    print "<option value='Pending'" . ($row->{status} eq 'Pending' ? " selected" : "") . ">Pending</option>";
    print "<option value='Completed'" . ($row->{status} eq 'Completed' ? " selected" : "") . ">Completed</option>";
    print "</select>";
    print "</td>";
    print "</tr>";
}
print "</table>";

$dbh->disconnect;

