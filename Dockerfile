FROM python:3.10-slim

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

#copy files to code 
COPY . /code

#Give permissions to the code folder
RUN chmod +x /code/src

# Set the working directory to /code
WORKDIR /code/src

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONPATH "${PYTHONPATH}:/code/src"

CMD pip install -e . 