# Pull Python image 
FROM python:3

# Set working directory to 'container' folder
WORKDIR /container

# Move the requirements file into the container
COPY requirements.txt ./

# install all requirements
RUN pip3 install -r requirements.txt

# moves all files into the container
COPY . .


EXPOSE 5001

# sets up python entrypoint
ENTRYPOINT [ "python3" ] 

# runs app.py to launch the flask server in production
CMD [ "app.py" ]