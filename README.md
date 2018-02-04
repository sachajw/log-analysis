# **Project 3: Log Analysis**

**by Sacha Wharton**

## **About**
This is the third project in the Udacity Full Stack Web Developer Nanodegree. The PostgreSQL database provided is a newspaper website's backend and contains newspaper articles, as well as the web server log for the site. The program I have written runs from the command line and does not require any input from the user. It connects to the database, uses SQL queries to analyse the log data, and prints out the answers to a set of questions about the site's user activity in human readable format.

The following questions are answered:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## **Required Libraries and Dependencies**

Python 2.x (The Python executable should be in your default path, which the Python installer sets.)
Vagrant
Virtual Box

## **Main Project Contents**

The project contains the following files:
- ****newsdata.py**** - main Python script to run
- ****output.txt**** - the output of running newsdata.py

## **How to Run Project**

- Install Oracle Virtualbox from [here](https://www.virtualbox.org/wiki/Downloads)
- Install Vagrant from [here](https://www.vagrantup.com/downloads.html)
- Use this link to configure and run the virtual machine     [here](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0)
- Download the data from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) and copy the ****newsdata.sql**** file into the Vagrant directory
- Run ****psql -d news -f newsdata.sql**** (this will connect to the PostgreSQL server and create the database with all the relevant tables and data)
- Copy ****newsdata.py**** to the Vagrant folder
- Navigate to the Vagrant folder on the virtual machine
- Run ****python newsdata.py****

## **Extra Credit Description**

In the results printed for Question 3, my code converts the date from the timestamp format to one that uses a combination of words (day of the week and month) and numerals, so as to make it easier for users to understand. Adding the day of the week to this printed result could help to highlight error patterns (for example, if a larger percentage of errors consistently occurred on specific weekdays).

## **Miscellaneous**
I based the README based on this template [forum](https://discussions.udacity.com/t/readme-files-in-project-1/23524)
