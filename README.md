# Project Description
The log reporting tool is a python application that uses information
from a newspaper website database to report on newspaper website user activity.

The log reporting tool creates a text file that includes the result from the
following 3 queries:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Requirements
To run the log reporting tool on your local computer, you will need the
following:

### Install and configure the VM
A Linux-based virtual machine (VM) is used to run an SQL database server and python
application on your computer. This project is using tools called Vagrant
and VirtualBox to install and manage the VM. Use the following URLs to install Vagrant and VirtualBox. (Note: an older version of VirtualBox is used for this project.)

* [Virtual Box 5.1](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* [Vagrant](https://www.vagrantup.com)

Use this [Vagrantfile](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile) to ensure the VM is configured properly. The Vagrantfile should be stored in the vagrant directory.

In the vagrant directory, type **vagrant up** to launch your virtual machine.

Once it is up and running, type **vagrant ssh**. This will log your terminal into the virtual machine, and you'll get a Linux shell prompt.
Change directory to the /vagrant directory by typing **cd /vagrant**.

### Get the log analysis project from Github

Clone the remote git repo for the log analysis project on your computer using the web URL:

```
https://github.com/wa3449/log_analysis_project.git
```
### Create the database schema and load the data needed for the Project

Download the [newsdata.sql](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) file into the log analysis project directory.

Run the following command to load the data: **psql -d news -f newsdata.sql**


## Usage
The python application will run from the command line and does not require
any input from the user. The python application connects to the news database
and runs 3 predefined SQL queries, and then writes the query results to the
log_report.txt text file that is located in the same directory from where
the log reporting tool application is run.

1. From the log analysis project directory, run the log reporting tool application, type the following command on the command line:

```
$ python log_reporting_tool
```

2. Once the command completes, you can then view the log_report.txt file for
the query results.
