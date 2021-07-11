This is the code repository for my master thesis project titled '**Digital Twin based Intrusion Detection for Industrial Control Systems**'. The main contribution of this work is a security framework for ICS that uses a digital twin of an ICS for security monitoring and has an ML-based IDS for intrusion detection. The digital twin solution used in this work is the framework proposed in 'https://dl.acm.org/doi/10.1145/3407023.3407039' and cloned from the authors' github repo: https://github.com/FrauThes/DigitalTwin-SIEM-integration. 

Folders in this repository (README files are further provided separately for different folders)
1) **DigitalTwin-SIEM-integration**: Cloned from https://github.com/FrauThes/DigitalTwin-SIEM-integration.

 _ **Changes made:**_
  (a) Modelling of different process-aware attacks.
  (b) Collecting process measurements & labelling of generated dataset
  (c) Added changes to extend the docker compose framework with a new docker container that will be running ML-based IDS
2) **ML_IDS**: This folder contains Jupyter notebooks for different ML algorithms (Supervised, Stacking) and dataset used to train the models. (FIINNAAL IMPLEMENTATION RUNNING IN IDS???)
3) **Plots:** This folder has plots showing effect of modelled attacks on different process measurements.
4) **siem:** standalone digital twin as a docker container

**_#To run the whole framework in docker, follow the steps below:_**
1) sudo xhost +si:localuser:root  
  //Comments: add root user to the local access control list of xhost on "Docker host", not inside container.
2) From 'DigitalTwin-SIEM-integration/deployments/docker', run the init script using 'sudo sh init.sh'. Give an IP on which elastic search needs to be deployed.
3) Once the project is ready, access kibana and ids in browser.
  Kibana port 5601 , ids (url comes on console) port 8888
  
  
_**#How to run different attack scenarios?**_
  
  
**_#How to use IDS?_**
