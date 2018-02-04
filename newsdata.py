#!/usr/bin/env python 2
import psycopg2

DBNAME = "news"


db = psycopg2.connect(database=DBNAME)
c = db.cursor()

# query1 - Find the three most popular articles

c.execute(
    "SELECT title, count(*) as views \
    FROM articles \
        JOIN log on '/article/' || articles.slug = log.path \
    GROUP BY title \
    ORDER BY views desc \
    LIMIT 3")

query1 = c.fetchall()

print("\nThe three most popular articles are:")
for i in query1:
    title = i[0]
    views = i[1]
    print(" - '%s' : %s views" % (title, str(views)))
	
# query2 - Find the most popular authors

c.execute(
    "SELECT authors.name, count(*) as views \
    FROM articles \
        JOIN authors on articles.author = authors.id \
		JOIN log on '/article/' || articles.slug = log.path \
	GROUP BY authors.name \
    ORDER BY views desc")
	
query2 = c.fetchall()

print("\nThe most popular authors are:")

for i in query2:
    author = i[0]
    views = i[1]
    print(" - %s : %s views" % (author, str(views)))
	
# query3 - Find the days with more than 1% request errors

c.execute(
    "SELECT * FROM \
	(SELECT TotalHits.PerDay, \
	ROUND(cast((100*TotalErrors.Errors) as numeric) / cast(TotalHits.Hits as numeric), 2) \
	AS ErrorPercentage FROM \
	(SELECT date(time) AS PerDay, COUNT(*) AS Hits \
	FROM log \
	GROUP BY PerDay) \
	AS TotalHits \
	INNER JOIN \
	(SELECT date(time) AS PerDay, COUNT(*) AS Errors \
	FROM log \
	WHERE status like '%404%' \
	GROUP BY PerDay) \
	AS TotalErrors  \
	ON TotalHits.PerDay = TotalErrors.PerDay) \
	AS Total \
	WHERE ErrorPercentage > 1.0"
	
query2 = c.fetchall()

print("\nThe days with the more than 1% request errors are:")

for i in query3:
    date = i[0]
    ErrorPercentage = i[1]
    print(" - %s : %s%% Errors" % (date, str(round(ErrorPercentage,1))))
