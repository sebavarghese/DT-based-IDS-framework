#!/bin/bash
#!/bin/bash
service openvswitch-switch start
ovs-vsctl set-manager ptcp:6640
cd src
mn -c
python init.py
python run.py
