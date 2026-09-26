#!/bin/bash

while true
do
    # Agent 1: horizontal movement
    for x in $(seq -4 0.5 4)
    do
        gz service -s /world/competition_world/set_pose \
        --reqtype gz.msgs.Pose \
        --reptype gz.msgs.Boolean \
        --timeout 1000 \
        --req "name: \"moving_obstacle\" position {x: $x y: 4 z: 0.5}" \
        >/dev/null
        sleep 0.2
    done

    for x in $(seq 4 -0.5 -4)
    do
        gz service -s /world/competition_world/set_pose \
        --reqtype gz.msgs.Pose \
        --reptype gz.msgs.Boolean \
        --timeout 1000 \
        --req "name: \"moving_obstacle\" position {x: $x y: 4 z: 0.5}" \
        >/dev/null
        sleep 0.2
    done

    # Agent 2: perpendicular movement
    for y in $(seq -4 0.5 4)
    do
        gz service -s /world/competition_world/set_pose \
        --reqtype gz.msgs.Pose \
        --reptype gz.msgs.Boolean \
        --timeout 1000 \
        --req "name: \"crossing_obstacle\" position {x: 2 y: $y z: 0.5}" \
        >/dev/null
        sleep 0.2
    done

    for y in $(seq 4 -0.5 -4)
    do
        gz service -s /world/competition_world/set_pose \
        --reqtype gz.msgs.Pose \
        --reptype gz.msgs.Boolean \
        --timeout 1000 \
        --req "name: \"crossing_obstacle\" position {x: 2 y: $y z: 0.5}" \
        >/dev/null
        sleep 0.2
    done
done
