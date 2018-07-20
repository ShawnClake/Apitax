# Use Ubuntu 18.04
FROM tiangolo/uwsgi-nginx-flask:python3.6

# Update repo listings
RUN apt-get update

# Install system level things
RUN apt-get -y install git pandoc

# Install NodeJS and NPM
RUN cd /tmp && curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get -y install nodejs npm
RUN apt-get -y install build-essential

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
# This essentially bakes your project which uses Apitax into the image
# This folder should contain ['requirements.txt', 'Dockerfile', 'App/']
ADD . /app

# Get pip setup
RUN pip install wheel setuptools

# Install Apitax
RUN pip install apitax

# Install any needed packages specified in requirements.txt
RUN cd /app && pip install . ; exit 0

# Navigate to the web directory and install npm packages and build using webpack
RUN cd /usr/local/lib/python3.6/site-packages/apitax/ah/api/dashboard && npm install && npm run build

# Return to the working directory
WORKDIR /app

# Make port 80 available to the world outside this container
EXPOSE 80
EXPOSE 443

