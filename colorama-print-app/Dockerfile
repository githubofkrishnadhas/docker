# Use a lightweight Python image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

#Setting Label

LABEL MAINTAINER="githubofkrishnadhas <krishnadhasnk1997@gmail.com>"



#Copy the Pipfile and Pipfile.lock to the working directory
COPY Pipfile Pipfile.lock ./

# Install Pipenv and the project dependencies
RUN pip install pipenv && pipenv install --system --deploy

# Copy the application files to the working directory
COPY app.py ./ 

# Set the default command to run the script with pipenv

CMD ["pipenv", "run", "python", "app.py"]


