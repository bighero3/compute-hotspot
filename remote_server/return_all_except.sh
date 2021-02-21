#!/bin/bash

# Usage: ./return_all_except.sh <the uid of the instance>
# must be run from ~
# assumes that permissions for scp have been properly set up
# assumes that the return_location is alright


# compress the folder except the python scripts
# tar -czf files/$1/$1.tar.gz files/$1 --exclude=*.py

zip -r files/$1/$1.zip files/$1

# return the files to the location stored at ~/return_location
# this assumes that proper permissions have been set up for scp

location=$(cat return_location)

scp -r files/$1/$1.zip $location && rm -rf files/$1
