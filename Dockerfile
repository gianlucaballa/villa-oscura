# Use an official Python runtime as the base image.
FROM python:3.12-alpine

# Set the working directory in the container.
WORKDIR /app

# Copy the current directory contents into the container at /app.
COPY . .

# Run the game when the container starts.
CMD ["python", "villa_oscura.py"]