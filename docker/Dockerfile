# Use Ubuntu 18.04
FROM ubuntu:18.04

# Install NodeJS and NPM
RUN apt-get update
RUN apt-get -y install nodejs
RUN apt-get -y install npm

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
# This essentially bakes your project which uses Apitax into the image
# This folder should contain ['requirements.txt', 'Dockerfile', 'App/']
ADD . /app

# Install Python 3 and PIP
RUN apt-get -y install python3 python3-pip

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Navigate to the web directory and install npm packages and build using webpack
RUN cd /usr/local/lib/python3.6/dist-packages/apitax/ah/web/node/node && npm install && npm run build

# Return to the working directory
WORKDIR /app

### ADD ANY ADDITIONAL BUILD STEPS FOR YOUR APPLICATION HERE ### 


### END ADDITIONAL BUILD STEPS ###

# Make port 5080 available to the world outside this container
EXPOSE 5080

# Run the main.py file found in your project application
CMD ["python3", "App/main.py", "--web", "--debug", "--no-build"]


