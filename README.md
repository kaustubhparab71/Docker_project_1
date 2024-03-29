<br clear="both">

<h2 align="left">Dockerized Python Flask Application</h2>

Welcome to the Dockerized Python Flask Application repository!
This repository contains a simple Flask application that runs inside a Docker container.
It also includes instructions on how to set up the application on a cloud VM with Docker, Git, and a Linux OS.

###
<h2 align="left">Prerequisites</h2>

Before you begin, ensure that you have the following installed on your cloud VM:

Docker
Git
Linux OS

<h2 align="left">Getting Started</h2>
1 - check versions or your required applications & start cloning your repository on your VM.


<div align="center">
  <img  src="https://github.com/kaustubhparab71/kaustubhparab71/assets/33633535/78c1ba8b-459a-43b3-a51b-74f99cc2d0f7" />
  </div>


  
2 -  Edit your docker file according to your requirement & using that file create docker image file with below command.

        docker build -t kp07pythonapp . 


        
  <div align="center">
  <img  src="https://github.com/kaustubhparab71/kaustubhparab71/assets/33633535/385bfcc9-4b04-4077-b066-27c4e468388d" />
</div>



3 -  after you able to see that image in all docker images by cammand , after that by using that image you can run your dockerize python program on specified port.

<div align="center">
  <img  src="https://github.com/kaustubhparab71/kaustubhparab71/assets/33633535/d3f8541a-3ecc-482d-94aa-04e2333b0a70" />
</div>


        docker images
        docker run -it -p 5000:5000 kp07pythonapp



        <div align="center">
  <img  src="https://github.com/kaustubhparab71/kaustubhparab71/assets/33633535/28d414a9-b50c-41af-b414-869d0e739d26" />
</div>


4 -  After open that link on port 5000 you able to see your python program running on browser.

<div align="center">
  <img  src="https://github.com/kaustubhparab71/kaustubhparab71/assets/33633535/1d4f3edb-0440-4491-ae15-7d1bb3804c68" />
</div>



**Additional Documentation**

      
  Project Structure
  
docker_kp.py : Main Flask application file.

requirement.txt/ : all required modules & dependancy.

Dockerfile/ : Docker file in which we add all docker insruction to bo done by docker image.


<h3 Recorded Video Link    < /h3>

[![Watch the video](https://github.com/kaustubhparab71/kaustubhparab71/assets/33633535/2c880ea9-e63f-47af-8cc0-ec3dba7376a9
)


        

