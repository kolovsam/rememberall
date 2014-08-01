# http://stackoverflow.com/questions/1781571/how-to-concatenate-two-dictionaries-to-create-a-new-one-in-python

d1 = {1:2, 3:4}
d2 = {5:6, 7:9}
d3 = {10:8, 13:22}

# slowest method: concatenate the items and call dict on the resulting list
d4 = dict(d1.items() + d2.items() + d3.items())

# ************************************************************************ #
# fastest method: explit the dict constructor to the hilt, then one update
d4 = dict(d1, **d2)
d4.update(d3)
# ************************************************************************ #

# middle method: a loop of update calls on an initially-empty dict
d4 = {}
for d in (d1, d2, d3):
    d4.update(d)

# middle method 2
d4 = dict(d1)
for d in (d2, d3):
    d4.update(d)
