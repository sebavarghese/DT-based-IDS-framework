# MasterThesis
DigitalTwin-SIEM-integration is cloned from  https://github.com/FrauThes/DigitalTwin-SIEM-integration and made changes for the project. and made changes for the project.

#Standalone working digital twin as a docker container (Digital twin simulation from https://github.com/FrauThes/DigitalTwin-SIEM-integration ) ------> 'siem' folder

1) Build docker image: docker build .
2) To run the built image : sudo docker run -it --rm --privileged -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix <imagename>

#To run the whole framework in docker, follow the steps below>
1) sudo xhost +si:localuser:root  
  //Comments: add root user to the local access control list of xhost on "Docker host", not inside container.
2) From deployments/docker, run the init script using 'sudo sh init.sh'. Give an IP on which elastic search needs to be deployed.
3) Once the project is ready, access kibana and ids in browser.
  Kibana port 5601 , ids (url comes on console) port 8888
  
  
#How to run different attack scenarios?
  
  
#How to use IDS?
