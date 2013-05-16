#!/usr/bin/python
# Example experiment script
# Authors: Ed Schwartz and Thanassis Avgerinos

import csv
import gdata.spreadsheet.text_db
import os
import random
import string
import subprocess
import sys
import time
from multiprocessing import Pool

from subprocess import Popen, PIPE

# Redo entries already in sheet?
redo = False

trials = 20

names = ["ed", "thanassis"]
inputs = reduce(list.__add__, map(lambda n: map(lambda num: {"name": n, "num": num}, xrange(trials)), names))
print inputs

ids = ["name", "num"]
measured = ["time"]

key="0Au4zXzOoce8JdGFjZ0JBVTIxRmgzeEpZN0VFRVktb0E"

from password import user, password

dbname="paper"

client = gdata.spreadsheet.text_db.DatabaseClient(username=user, password=password)

db = client.GetDatabases(spreadsheet_key=key)[0]
tables = db.GetTables(name=dbname)
if len(tables) == 1:
    table = tables[0]
else:
    table = db.CreateTable(dbname, ids + measured)

def timeit(cmd):
    stime = time.time()
    p = subprocess.Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    duration = time.time() - stime
    return_code = p.returncode

    if return_code != 0:
        duration = -1

    return duration, stderr

def run_method(inputs):

    # Check for existing rows
    query_strs = map(lambda column: column + " == \"" + str(inputs[column]) + "\"", ids)
    query_str = string.join(query_strs, " and ")
    #print query_str

    records = table.FindRecords(query_str)

    if redo:
        for row in records:
            row.Delete()
            go = True
    else:
        go = len(records) == 0

    if go:
        runtime, out = timeit("sleep " + str(random.normalvariate(len(inputs["name"]), 1.0)))

        measurements = {"time": runtime}

        m = map(lambda column: (column, str(inputs[column])), ids)
        m = m + map(lambda column: (column, str(measurements[column])), measured)
        d = dict(m)
        #print d

        ## Try a couple times to add the data
        for i in xrange(10):
             try:
                 print "adding", d
                 table.AddRecord(d)
                 break
             except:
                 print "Unexpected error:", sys.exc_info()[0]
                 time.sleep(i*10)

    else:
         # Don't make Google too mad.
         print "Skipping", inputs
         sys.stdout.flush()
         time.sleep(1)

pool = Pool()

pool.map(run_method, inputs)


