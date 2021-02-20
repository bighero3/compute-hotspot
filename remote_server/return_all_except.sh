#!/bin/bash

# Usage: ./return_all_except.sh <the uid of the instane> <server and location to be returned to>
# must be run from ~
# assumes that permissions for scp have been properly set up

ls files/$1 | grep -v $1 | xargs -I{} scp {} $2:

rm -rf files/$1
