**MasterThesis**
This is the code repository for my master thesis project titled 'Digital Twin based Intrusion Detection for Industrial Control Systems'. The main contribution of this work is a security framework for ICS that uses a digital twin of an ICS for security monitoring and has an ML-based IDS for intrusion detection. The digital twin solution used in this work is the framework proposed in 'https://dl.acm.org/doi/10.1145/3407023.3407039' and cloned from the authors' github repo: https://github.com/FrauThes/DigitalTwin-SIEM-integration. 

DigitalTwin-SIEM-integration folder is cloned from  and made changes for the project. Description of changes made is described in a later section on this page. Furthermoreand changes made in  this project are to model different attack scenarios inside digital twin docker container, and detect anomalies using machine learning based IDS running as another container.

**_#Standalone working digital twin as a docker container (Digital twin simulation from https://github.com/FrauThes/DigitalTwin-SIEM-integration ) ------> 'siem' folder_**

1) Build docker image: docker build .
2) To run the built image : sudo docker run -it --rm --privileged -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix <imagename>

**_#To run the whole framework in docker, follow the steps below:_**
1) sudo xhost +si:localuser:root  
  //Comments: add root user to the local access control list of xhost on "Docker host", not inside container.
2) From 'DigitalTwin-SIEM-integration/deployments/docker', run the init script using 'sudo sh init.sh'. Give an IP on which elastic search needs to be deployed.
3) Once the project is ready, access kibana and ids in browser.
  Kibana port 5601 , ids (url comes on console) port 8888
  
  
_**#How to run different attack scenarios?**_
  
  
**_#How to use IDS?_**
