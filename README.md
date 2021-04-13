# The Philosophy Data Project - Stats App

This repo contains the Heroku app used on the Philosophy Data Project [website](http://philosophydata.com) to provide basic stats on philosophers in the corpus. The app uses a set of pickled files created by the Philosophy Data Project [data processing notebooks](https://github.com/kcalizadeh/PDP_data_processing). Each of these contains a dictionary with the different stats and is then drawn upon as needed by the primary app. 

The stats that the app provides are:
- Titles of all texts in the searched category
- Average word length
- Average sentence length
- Word frequency chart
- Bigram frequency chart
- Number of unique words out of total words

The repo contains:
- one stats.py file that constitutes the main app
- one stats_functions.py file that contains the menus and dropdown lists for the app
- a folder containing all the pickled dictionaries
- various necessary files to run the app through Heroku (procfiles, requirements, etc.)

