# Use Ubuntu 18.04
FROM ubuntu:18.04

# Update repo listings
RUN apt-get update

# Install system level things
RUN apt-get -y install git pandoc

# Install build tools
RUN apt-get -y install build-essential python-dev

# Install Python 3 and PIP
RUN apt-get -y install python3 python3-pip

# Install NodeJS and NPM
RUN apt-get -y install nodejs
RUN apt-get -y install npm

# Install NGINX
RUN apt-get -y install nginx

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
# This essentially bakes your project which uses Apitax into the image
# This folder should contain ['requirements.txt', 'Dockerfile', 'App/']
ADD . /app

# Install uwsgi
RUN pip3 install uwsgi




# Install any needed packages specified in requirements.txt
RUN pip3 install .

## Start setting up the WSGI





# Navigate to the web directory and install npm packages and build using webpack
RUN cd /app/apitax/ah/api/dashboard && npm install && npm run build

# Return to the working directory
WORKDIR /app

# Make port 80 available to the world outside this container
EXPOSE 80
EXPOSE 443
EXPOSE 5080

# Run the main.py file found in your project application
#CMD ["python3", "app/main.py", "--web", "--debug", "--no-build"]

#CMD uwsgi --socket 127.0.0.1:3031 --wsgi-file /app/apitax/ah/api/Server.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191
CMD uwsgi --http :5080 --wsgi-file /app/main.py --callable app --processes 4 --threads 2


