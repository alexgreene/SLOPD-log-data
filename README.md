# SLOPD-log-data

### What is this?
This is a script I wrote on this fine monday to download log files from the San Luis Obispo Police Dpt.

## Why are you pulling data from the SLOPD?
The police log publish on the dpt's website is updated every weekday with the most recent data. The old data, ie. activity from previous days, is lost. While I'm sure the public can probably request older data from the PD, this is much easier and everything is put into a nice CSV format.

### Can I run this on my computer?
YES!

### How can I run this?
- Put the .py file into a folder along with an empty file called 'logfile.csv' and a file called 'update_file.txt' that only has something random typed into it, like 'apppples' or 'cats'. This will be checked against the current police log number, and if it's not the same, the script will update the .csv and thie update_file.txt will be overwritten with the # of the current police log, so make sure you don't type in a number that might accidentally be the # of the current police log!
- in the .py script, update the file paths for these two files, so that they reflect your computer's directories.
- If you don't know how to use the command line, you'll need to learn that first to use the following commands;
- Make sure you have the following python packages installed: lxml, requests, csv, and python-crontab. To install them, first make sure you have pip installed (on OSX: 'sudo easy_install pip'). For each package 'sudo pip install lxml', 'sudo pip install python-crontab', etc, etc.
- Run the script with 'python scrape.py'
- Now you'll want to set up a cron job so that the script collects new data every time the police department updates the log. To do this, type python on the command line to start a new python console. The following command will set up a cron job: 

```>>> from crontab import CronTab```

```>>> cron = CronTab()``` 

```>>> job = cron.new(command='/usr/bin/python /Users/alexg/Documents/data/slo-pd-logs/scrape.py')```  
(but replace the /Users/... with your own file path) 

```>>> job.hour.every(12)```  

> Every 12 hours the script will now run and check if there is new data to be appended to the csv file. If you want to edit the csv, make a copy and work on it elsewhere, as not to disturb the script!  

You can read more about python-crontab here https://pypi.python.org/pypi/python-crontab  
If you have any questions about my script or need any help, get in touch --> alexgrn7@gmail.com or @alexg473

### What am I supposed to do with the data?
Whatever the heck you want. Do some data science, journalism stuff, or make something cool or whatever.

### If I use this do I owe you a life debt?
What??! No, but I'd love to hear what you use the data for.
