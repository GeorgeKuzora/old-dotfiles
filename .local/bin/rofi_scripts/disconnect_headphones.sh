#!/bin/bash
if bluetoothctl show | grep -F -q "Powered: yes"; then
    bluetoothctl power off
fi
