FROM ubuntu
RUN mkdir -p /var/java
RUN apt-get update
RUN apt-get install -y openjdk-6-jdk libservlet2.5-java
ADD https://winstone.googlecode.com/files/winstone-1.0.5-boot.jar /var/java/winstone-1.0.5-boot.jar
ADD https://dl.dropboxusercontent.com/u/50900611/docker/helloworld.war /var/java/helloworld.war
ADD https://dl.dropboxusercontent.com/u/50900611/docker/run /var/java/run
RUN chmod 777 /var/java/run
EXPOSE 8080
