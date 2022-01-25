FROM jenkins/jenkins:2.319.2-jdk11
USER root
RUN apt-get update && apt-get install -y lsb-release
RUN curl -fsSLo /usr/share/keyrings/docker-archive-keyring.asc \
  https://download.docker.com/linux/debian/gpg
RUN echo "deb [arch=$(dpkg --print-architecture) \
  signed-by=/usr/share/keyrings/docker-archive-keyring.asc] \
  https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" > /etc/apt/sources.list.d/docker.list
RUN apt-get update && apt-get install -y docker-ce-cli
RUN apt-get install wget build-essential python3-pip nodejs npm screen -y
RUN pip3 install websocket-client requests
RUN npm i -g concurrently -y
ADD ./bot /bot
RUN chmod 777 /bot/*
USER jenkins
RUN mkdir /var/jenkins_home/jobs
ADD ./jobs /var/jenkins_home/jobs/
RUN mkdir /var/jenkins_home/users
ADD ./users /var/jenkins_home/users/
USER root
RUN chmod 777 /var/jenkins_home/users/*
ENTRYPOINT concurrently --kill-others "/bin/bash /bot/startup.sh" "/bin/bash /usr/local/bin/jenkins.sh"