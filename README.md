#Masoud Nikoofar
######Introduction
This is a simple set of scripts in python which I had written to arrange my movies' filename and TV shows' episodes based on IMDB datasets.
I hope you find it useful.
######Steps
1. Download IMDB dataset files from https://datasets.imdbws.com/ . I downloaded just these files for this project:
* title.basics.tsv.gz
* title.episode.tsv.gz
* title.ratings.tsv.gz

2. Then import them into a database (e.g. I use MySQL)
* Create database and tables
* Import files into tables
* It's a good idea to create some indexes on your tables

3. run the python code in desired directories. For instance, I have a directory named movies which have two files in it as below:
* The Shawshank Redemption
* The Godfather
If I run the bulk_renamer_auto.py script in this directory, it will create a directory named "Unready" and move these two directories in it, because It will find more than one record matching the directory's name for each one, so we have other options:
+ Simply add the movie's year to the directory's name:
* The Shawshank Redemption 1994
* The Godfather 1972
+ run bulk_renamer.py and choose one of the available options 
