alpine-valley-snow-report
=========================

A python script to pull snow report data from alpinevalleyresort.com

Example DEBUG output (otherwise returns a dictionary with all the same data):

```
$ python snow_report.py

###
# Alpine Valley Ski Report Snow Report
###
Data retrieved at 2014-12-29 17:46:00.475070
Status: Open
Status full: OPEN:Monday 12/29/14
Hours: 9am - 10pm
Trail Status: 20 / 20
Lift Status: 8 / 12
Snow base: 15"
Snow yesterday: 0.00"
Currently: Cloudy
Condition Description: Cooling temperatures have turned a wet corn like granular snow into a frozen granular snow.  This frozen granular snow will be very fine in consistency after the groomers tillers mix it up, and will be a very loose like sugar.  Ease of skiing will vary between 4-6.

###
# Trail Status
###
Mohawk: Open
Valley View: Open
First Adventure: Open
First Tracks: Open
Halfway: Open
Shelter: Open
Northwest Pass: Open
Timber Trail: Open
E-Z Pass: Open
Strawberry: Open
Cut Throat: Open
Lodge: Open
East Pass: Open
Alpine: Open
Broadway: Open
Big Thunder: Open
Raspberry: Open
Timber Gulch: Open
Soft Landings: Open
E-Z-Does-it: Open

###
# Lift Status
###
Triple - Lodge Chair: Closed
Quad - Valley Flyer: Open
Double - Valley View Chair: Closed
Quad- Super Glide: Open
Triple - Mohawk Chair: Open
Adding chairlifts as needed: Open
Triple - First Adventure Chair: Open
Conveyer #1: Closed
Conveyer #3: Open
Conveyer #2: Open
Quad - E-Z Rider: Open
Conveyer #4: Closed
```
