#!/usr/bin/env python
#
# log_report_tool.py
# Log Analysis Project for Udacity Full Stack Nanodegree
#
# See README.md file for detailed information on the application
#
#
import psycopg2
import sys


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=news")


def mostPopular3Articles():
    """Query to return the most popular 3 articles."""
    query = """SELECT a.title, count(*)
        FROM log l
        JOIN articles a ON l.path = concat('/article/', a.slug)
        GROUP BY a.title
        ORDER BY count(*) DESC LIMIT 3"""

    db = connect()
    cur = db.cursor()
    cur.execute(query)
    rs = cur.fetchall()

    # Write the report result.
    print("3 most popular articles of all time:")
    print
    for r in rs:
        frs = '"{}" - {} views'.format(r[0], int(r[1]))
        print(frs)
    print
    print

    cur.close()
    db.close()
    return


def mostPopularArticleAuthors():
    """Query to return the most popular article authors."""
    query = """SELECT p.name, count(*)
        FROM log l
        JOIN articles a ON l.path = concat('/article/', a.slug)
        JOIN authors p ON a.author = p.id
        GROUP BY p.name
        ORDER BY count(*) DESC"""

    db = connect()
    cur = db.cursor()
    cur.execute(query)
    rs = cur.fetchall()

    # Write the report result.
    print("Most popular article authors of all time:")
    print
    for r in rs:
        frs = "{} - {} views".format(r[0], int(r[1]))
        print(frs)
    print
    print

    cur.close()
    db.close()
    return


def daysWithErrorRateGT1():
    """Query to return day and error rate where error rate > 1%."""
    query = """WITH dailyRequestErrors AS (
            SELECT date(time) AS rqstDate, count(*) AS rqstErrors
            FROM log
            WHERE status != '200 OK'
            GROUP BY date(time)
            ORDER BY date(time)),
        dailyRequests AS (
            SELECT date(time) AS rqstDate, count(*) AS requests
            FROM log
            GROUP BY date(time)
            ORDER BY date(time)),
        dailyErrorRate AS (
            SELECT TO_CHAR(dailyRequestErrors.rqstDate,'FMMonth DD, YYYY'),
            (dailyRequestErrors.rqstErrors::FLOAT/dailyRequests.requests)
            * 100 AS errorPercent
            FROM dailyRequestErrors
            JOIN dailyRequests
            ON dailyRequestErrors.rqstDate = dailyRequests.rqstDate
            ORDER BY dailyRequestErrors.rqstDate)
        SELECT * from dailyErrorRate where errorPercent > 1"""

    db = connect()
    cur = db.cursor()
    cur.execute(query)
    rs = cur.fetchall()

    # Write the report result.
    print("Days with request error rate greater than 1%:")
    print
    for r in rs:
        frs = "{} - {:02.2f}% errors".format(r[0], float(r[1]))
        print(frs)
    print
    print

    cur.close()
    db.close()
    return


if __name__ == '__main__':
    """Re-direct stdout to file."""
    sys.stdout = open("./log_report.txt", "w")

    """Run reports."""
    mostPopular3Articles()
    mostPopularArticleAuthors()
    daysWithErrorRateGT1()

    """Close the file and re-direct stdout to terminal."""
    sys.stdout.close()
    sys.stdout = sys.__stdout__
