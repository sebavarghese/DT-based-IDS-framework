Follow the below steps to run the standalone docker container:

1) Build docker image 
command: **docker build .**
2) Run the built image
command: **sudo docker run -it --rm --privileged -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix**
