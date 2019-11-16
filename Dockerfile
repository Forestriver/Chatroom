# Python runtime as a parent image
FROM python:3.7

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install gevent

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Define environment variable
ENV FLASK_APP="chat.py"

# Run app.py when the container launches
CMD ["flask", "run", "--host", "0.0.0.0"]
