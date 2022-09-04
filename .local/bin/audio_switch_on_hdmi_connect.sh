#!/bin/bash
hdmi_sink="alsa_output.pci-0000_04_00.1.hdmi-stereo"

pactl set-default-sink $hdmi_sink
