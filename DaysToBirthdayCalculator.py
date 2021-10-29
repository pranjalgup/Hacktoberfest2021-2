'''''
You are here: Home / Basics / Date and Time in Python
Date and Time in Python
Author: PFB Staff Writer
Last Updated: August 27, 2020
Date and Time in Python
In my last post about datetime & time modules in Python, I mostly used the strftime(format) method to print out the dates and times.
In this post, I will show you how you can do it without that by just using datetime.datetime.now().
 
The second part of the post is about the the timedelta class, in which we can see the difference between two date, time, or datetime instances to microsecond resolution.
Date and Time Script
The last example is a short script for counting how many days there is left for any given date (birthday in this example).
'''''

import datetime
now = datetime.datetime.now()
print "-" * 25
print now
print now.year
print now.month
print now.day
print now.hour
print now.minute
print now.second

print "-" * 25
print "1 week ago was it: ", now - datetime.timedelta(weeks=1)
print "100 days ago was: ", now - datetime.timedelta(days=100)
print "1 week from now is it: ",  now + datetime.timedelta(weeks=1)
print "In 1000 days from now is it: ", now + datetime.timedelta(days=1000)

print "-" * 25
birthday = datetime.datetime(2012,11,04)

print "Birthday in ... ", birthday - now
print "-" * 25


'''''
You should see an output simimlar to this:
-------------------------
2012-10-03 16:04:56.703758
2012
10
3
16
4
56
-------------------------
The date and time one week ago from now was:  2012-09-26 16:04:56.703758
100 days ago was:  2012-06-25 16:04:56.703758
One week from now is it:  2012-10-10 16:04:56.703758
In 1000 days from now is it:  2015-06-30 16:04:56.703758
-------------------------
Birthday in ...  31 days, 7:55:03.296242
-------------------------
'''''
