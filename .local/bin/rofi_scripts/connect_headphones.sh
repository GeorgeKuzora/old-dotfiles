#!/bin/sh
jbl_650="88:D0:39:10:4A:0B"
jbl_sink="bluez_output.88_D0_39_10_4A_0B.a2dp-sink"

bluetoothctl power on
bluetoothctl connect $jbl_650
sleep 1
pactl set-default-sink $jbl_sink
