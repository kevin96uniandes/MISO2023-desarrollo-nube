# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the rest of the application code into the container
COPY . .

# Copy the requirements file into the container
COPY app.py .  

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port on which your Flask app will run
EXPOSE 5000

# Define the command to start your Flask app
CMD ["flask", "run", "-h", "0.0.0.0"]
