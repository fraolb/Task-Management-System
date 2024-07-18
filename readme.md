# Task Management System

This is a simple web-based Task Management System using Perl and SQLite. Users can create new tasks, view existing tasks, and update the status of tasks.

## Prerequisites

- XAMPP (or any other web server that supports CGI and Perl)
- Perl
- DBI and DBD::SQLite Perl modules

## Installation

1. **Install XAMPP:**
   Download and install XAMPP from [Apache Friends](https://www.apachefriends.org/index.html).

2. **Install Perl:**
   Perl comes pre-installed on most Unix-like systems. On Windows, you can use Strawberry Perl or the Perl that comes with XAMPP.

3. **Install DBI and DBD::SQLite modules:**
   Open a terminal or command prompt and run:

   ```sh
   cpan DBI
   cpan DBD::SQLite
   ```

4. **Setup the Database:**
   Create an SQLite database named `tasks.db` and set up the `tasks` table by running the `setup_db.cgi` script:

   ```sh
   perl setup_db.cgi
   ```

5. **Configure CGI in XAMPP:**
   Ensure that CGI is enabled in XAMPP. Edit the `httpd.conf` file in the XAMPP `apache` directory and make sure the following lines are uncommented:

   ```sh
   LoadModule cgi_module modules/mod_cgi.so
   AddHandler cgi-script .cgi .pl
   ```

6. **Place CGI Scripts:**
   Place your CGI scripts (`add_task.cgi`, `update_task.cgi`, `view_tasks.cgi`, `setup_db.cgi`) in the `cgi-bin` directory of your XAMPP installation (typically found at `C:\xampp\cgi-bin` on Windows).

7. **HTML Form:**
   Place your HTML form file (`task_form.html`) in the `htdocs` directory of your XAMPP installation (typically found at `C:\xampp\htdocs` on Windows).

## Files

- **task_form.html:**
  This is the HTML form for creating new tasks and viewing/updating existing tasks.
- **add_task.cgi:**
  This CGI script handles the form submission for adding a new task to the database.

- **update_task.cgi:**
  This CGI script handles updating the status of existing tasks.

- **view_tasks.cgi:**
  This CGI script fetches and displays existing tasks from the database.

- **setup_db.cgi:**
  This CGI script sets up the SQLite database and creates the `tasks` table.

## Usage

1. **Add New Task:**
   Open your web browser and navigate to `http://localhost/task_form.html`. Fill out the form and submit to add a new task.

2. **View Existing Tasks:**
   Existing tasks are displayed in the same form at `http://localhost/task_form.html`.

3. **Update Task Status:**
   Update the status of tasks using the dropdowns and click the "Update Tasks" button.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
