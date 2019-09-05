the main things I want to work on are
- persistant state
- batch add multiple units (12) before viewing
- multithreading/worker pool
- dumping/cacheing the timetable pages
- with the previous three i should be able to have
    - a worker pool for downloading timetables
    - use a worker pool using beautifulsoup4 for processing the timetables (this frees up selenium to download another page)
- json output
- some metadata about the staleness
- an API
- hosting




Generate new driver
Do a search
Get a list of units
for each unit
	read scrapetime of unit from disk
	append metadata to list items
dump unitlist to terminal
put unitlist in a queue

while there are unititems in the queue

	while (you have collected less than 12 unititems AND there are unititems in the queue
		Collect unititems from the queue (if now - scrapetime is greater than staleness)
	
	tries = 1
	while tries less equal than 3
		try
			remove all units from form
			For each unititem you've collected
				select unititem on form
				add unititem
			
				viewtimetable
				append timetable body, scrapetime to htmllist	
		catch
			closedriver
			sleep 10
			Generate a new driver
			blank search
			tries += 1

closedriver
	
put htmllist in a queue

while there are htmlitems in the queue
	Beautifulsoup htmlitems
	for every htmlitems unittable/tbody/tr (classtime)
		collect all the columns for that row
			append that and htmlitems.scrapetime to listofclasstimes

export listofclasstimes
