# Use a lightweight Python image as the base python version 3.11.3
FROM python:slim

# Set the working directory inside the container
WORKDIR /app

#Setting Label

LABEL MAINTAINER="githubofkrishnadhas <krishnadhasnk1997@gmail.com>"

#Copy the Pipfile and Pipfile.lock to the working directory
COPY Pipfile Pipfile.lock ./

# Install Pipenv and the project dependencies
RUN pip install pipenv && pipenv install --ignore-pipfile

# Copy the application files to the working directory
COPY app.py ./ 

# Set the default command to run the script with pipenv

CMD ["pipenv", "run", "python", "app.py"]


