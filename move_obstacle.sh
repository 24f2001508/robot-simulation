#!/bin/bash

# Dynamic obstacle settings
MIN_X=-4
MAX_X=4
STEP=0.5
DELAY=0.2
Y=4
Z=0.5

while true
do
    for x in $(seq $MIN_X $STEP $MAX_X)
    do
        gz service -s /world/competition_world/set_pose \
        --reqtype gz.msgs.Pose \
        --reptype gz.msgs.Boolean \
        --timeout 1000 \
        --req "name: \"moving_obstacle\" position {x: $x y: $Y z: $Z}" \
        >/dev/null

        sleep $DELAY
    done

    for x in $(seq $MAX_X -$STEP $MIN_X)
    do
        gz service -s /world/competition_world/set_pose \
        --reqtype gz.msgs.Pose \
        --reptype gz.msgs.Boolean \
        --timeout 1000 \
        --req "name: \"moving_obstacle\" position {x: $x y: $Y z: $Z}" \
        >/dev/null

        sleep $DELAY
    done
done
