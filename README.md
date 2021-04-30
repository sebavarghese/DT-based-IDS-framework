# MasterThesis

#Standalone working digital twin as a docker container (Digital twin simulation from https://github.com/FrauThes/DigitalTwin-SIEM-integration ) ------> 'siem' folder

1) Build docker image: docker build .
2) To run the built image : sudo docker run -it --rm --privileged -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix <imagename>
