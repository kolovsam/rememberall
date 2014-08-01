# http://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/

import time

# time.strftime(format)

## 24 hour format ##
print time.strftime("%H:%M:%S")

## 12 hour format ##
print time.strftime("%I:%M:%S")

## mm/dd/yyyy format ##
print time.strftime("%m/%d/%Y")

now = time.strftime("%c")

## date and time
print "Current date and time: " + time.strftime("%c")

## only date
print "Current date: " + time.strftime("%x")

## only time
print "Current time: " + time.strftime("%X")

## use variable
print "Current date and time: %s" % now


