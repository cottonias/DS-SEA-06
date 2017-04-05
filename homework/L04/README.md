# DS-SEA-06
## General Assembly Data Science class
#### Lesson 4 Answers
##### The first portion of this assignment will be referencing "04_chipotle_MC.py" when giving lines of code for showing work

1. Look at the head and the tail of **chipotle.tsv** in the **data** subdirectory of this repo. Think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)

**Answer** The file represents customer food orders from Chipotle. The columns break out the descriptions for the orders and each row describes a single item that was ordered and the associated details for that item.

2. How many orders do there appear to be?
**Answer** There appears to be 1834 orders.
3. How many lines are in this file?
**Answer** orders go up to 4624, but the count is 4622 (df.describe() see line 13)
4. Which burrito is more popular, steak or chicken?
**Answer** Chicken was more popular (553) than steak (368). See line 19.
5. Do chicken burritos more often have black beans or pinto beans?
**Answer** Black beans (282 vs 105 for pinto beans). See lines 21-28.
6. Make a list of all of the CSV or TSV files in the [our class repo] (https://github.com/ga-students/DS-SEA-3). repo (using a single command). You will be working on your local repo on your laptop.  Think about how wildcard characters can help you with this task.
**Answer** In a Linux/winGW window such as from Git Bash, enter the following command from the root of the dir for the class:
	find . -name "*.tsv" -o -name "*.csv"

Here is the result (note that at least one file has been added by me "test.csv"):

	./data/airlines.csv
	./data/Airline_on_time_west_coast.csv
	./data/bank-additional.csv
	./data/bikeshare.csv
	./data/chipotle.tsv
	./data/citibike_feb2014.csv
	./data/drinks.csv
	./data/drones.csv
	./data/hitters.csv
	./data/icecream.csv
	./data/imdb_1000.csv
	./data/mtcars.csv
	./data/NBA_players_2015.csv
	./data/ozone.csv
	./data/pronto_cycle_share/2015_station_data.csv
	./data/pronto_cycle_share/2015_trip_data.csv
	./data/pronto_cycle_share/2015_weather_data.csv
	./data/rossmann.csv
	./data/rt_critics.csv
	./data/sms.tsv
	./data/stores.csv
	./data/syria.csv
	./data/time_series_train.csv
	./data/titanic.csv
	./data/ufo.csv
	./data/vehicles_test.csv
	./data/vehicles_train.csv
	./data/yelp.csv
	./test.csv

7. Count the approximate number of occurrences of the word "dictionary" (regardless of case) across all files of [our class repo] (https://github.com/ga-students/DS-SEA-3).
**Answer** Use grep to pull out all instances of "dictionary" (only matching -o) (case-insensitive, -i) (-h to pipe results with no filename) from the current dir and subdirectories (-r) and pipe that in to wc and only count words (-w)
	grep -rohi "dictionary" * | wc -w
Result: 90
8. **Optional:** Use the the command line to discover something "interesting" about the Chipotle data. Try using the commands from the "advanced" section!
**Answer** cut -f1,1 chipotle.tsv | sed -n '1!p' | uniq -c

The code above cuts out only the first column which is the order_id (cut) pipes that to clip off the top row "order_id" (sed) and pipes that to count the how many times each number appeared (uniq). This makes it easy to see that most orders were single digit and the largest order was for 23 items (order 926)


