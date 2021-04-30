#!/bin/bash
service openvswitch-switch start
ovs-vsctl set-manager ptcp:6640
cd DigitalTwin-SIEM-integration/src
mn -c
python init.py
python run.py
