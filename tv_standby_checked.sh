#!/usr/bin/env bash

filename=./.alarm

if [ -f $filename ]; then
    echo 'found alarm cannot set tv to standby'
else
    echo 'no alarm setting tv to standby'
    echo standby 0.0.0.0 | cec-client -s -d 1
fi