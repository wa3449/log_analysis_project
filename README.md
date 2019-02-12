# Project Description
The log reporting tool is a python application that uses information
from a newspaper website database to report on newspaper website user activity.

The log reporting tool creates a text file that includes the result from the
following 3 queries:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Prerequisites
To run the log reporting tool on your local computer, you will need the
following:

1. The first step is to prepare the environment as described in
[Lesson 3 Prepare the software and the data](https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/bc938915-0f7e-4550-a48f-82241ab649e3/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91) of the Log Analysis Project.

2. Clone the remote git repo on your computer.

## Usage
The python application will run from the command line and does not require
any input from the user. The python application connects to the news database
and runs 3 predefined SQL queries, and then writes the query results to the
log_report.txt text file that is located in the same directory from where
the log reporting tool application is run.

1. To run the log reporting tool application, type the following command on the
command line:

```
$ python3 log_reporting_tool
```

2. Once the command completes, you can then view the log_report.txt file for
the query results.
