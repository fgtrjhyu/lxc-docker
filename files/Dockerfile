FROM ubuntu
RUN apt-get update
RUN apt-get install -y openjdk-6-jre-headless
RUN mkdir -p /var/java
ADD winstone-1.0.5-boot.jar /var/java/
ADD servlet-api.jar /var/java/
ADD helloworld.war /var/java/
ADD run /var/java/
RUN chmod 777 /var/java/run
EXPOSE 8080
