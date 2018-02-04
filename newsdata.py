#!/usr/bin/env python 2
import psycopg2

DBNAME = "news"


db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# query1 - Find the three most popular articles

c.execute(
    "SELECT title, count(*) as hits \
    FROM articles \
    JOIN log on '/article/' || articles.slug = log.path \
    GROUP BY title \
    ORDER BY hits desc \
    LIMIT 3")

query1 = c.fetchall()

print("\nThe three most popular articles are:")
for i in query1:
    title = i[0]
    hits = i[1]
    print(" - '%s' : %s views" % (title, str(hits)))

# query2 - Find the most popular authors

c.execute(
    "SELECT authors.name, COUNT(*) as hits \
    FROM articles \
    JOIN authors on articles.author = authors.id \
    JOIN log on '/article/' || articles.slug = log.path \
	GROUP BY authors.name \
    ORDER BY hits desc")

query2 = c.fetchall()

print("\nThe most popular authors are:")

for i in query2:
    author = i[0]
    hits = i[1]
    print(" - %s : %s views" % (author, str(hits)))

# query3 - Find the days with more than 1% of request errors

c.execute(
    "SELECT * FROM \
    (SELECT hitstotal.daily, \
    ROUND(cast((100*errortotal.errors) as numeric) \
    / cast(hitstotal.hits as numeric), 2) \
    as errorperc FROM \
    (SELECT date(time) AS daily, COUNT(*) as hits \
    FROM log \
    GROUP BY daily) \
    as hitstotal \
    INNER JOIN \
    (SELECT date(time) as daily, COUNT(*) as errors \
    FROM log \
    WHERE status LIKE '%404%' \
    GROUP BY daily) \
    as errortotal  \
    ON hitstotal.daily = errortotal.daily) \
    as total \
    WHERE errorperc > 1.0")

query3 = c.fetchall()

print("\nThe days with the more than 1% request errors are:")

for i in query3:
    date = i[0]
    errorperc = i[1]
    print(" - %s : %s%% errors" % (date.strftime('%A %B %d, %Y'),
          str(round(errorperc, 1))))
