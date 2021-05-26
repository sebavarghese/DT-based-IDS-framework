**# MasterThesis**
DigitalTwin-SIEM-integration is cloned from  https://github.com/FrauThes/DigitalTwin-SIEM-integration and made changes for the project. and changes made in  this project are to model different attack scenarios inside digital twin docker container, and detect anomalies using machine learning based IDS running as another container.

**_#Standalone working digital twin as a docker container (Digital twin simulation from https://github.com/FrauThes/DigitalTwin-SIEM-integration ) ------> 'siem' folder_**

1) Build docker image: docker build .
2) To run the built image : sudo docker run -it --rm --privileged -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix <imagename>

**_#To run the whole framework in docker, follow the steps below>_**
1) sudo xhost +si:localuser:root  
  //Comments: add root user to the local access control list of xhost on "Docker host", not inside container.
2) From 'DigitalTwin-SIEM-integration/deployments/docker', run the init script using 'sudo sh init.sh'. Give an IP on which elastic search needs to be deployed.
3) Once the project is ready, access kibana and ids in browser.
  Kibana port 5601 , ids (url comes on console) port 8888
  
  
_**#How to run different attack scenarios?**_
  
  
**_#How to use IDS?_**
