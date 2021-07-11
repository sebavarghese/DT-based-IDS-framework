# DigitalTwin-SIEM-integration

**Installation**

Installation steps for the whole implementation with Docker Compose is as follows: 
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
4. The script is trying to import the Dsiem dashboard to Kibana. This may take a few minutes. Until Kibana is up and running, error messages are shown. This is normal. Example error message:
    ```
    curl: (22) The requested URL returned error: 503 Service Unavailable
    cannot connect to localhost:5601, will retry in 5 sec ..
    ```
5.  Once the project is ready, access kibana and ids in browser.
    Kibana port 5601 , ids (url comes on console) port 8888
    
The Project is up and running. If you want to start it a second time you simply have to navigate to deployments/docker and run `docker-compose up`.

**Data collection**

Once the docker compose is up, 8 xterm consoles will pop up on the terminal (2 for s1, 2 for plc1, 1 for plc2, 1 for plc3, 1 for hmi and 1 for attacker node)
To trigger data collection, run the following command on hmi terminal
```
python trigger.py <x>
```
Here x corresponds to the minutes for which data (process measuremnets) needs to be collected. For examples, if data needs to be collected for 2 hours, enter x as 120.

Collected dataset is stored as 'data.csv' in logs folder.

Label the dataset using 'label.py' script.
**Executing attacks**



**Running ML-based IDS**

## Reference
[ARES'20](https://doi.org/10.1145/3407023.3407039)
