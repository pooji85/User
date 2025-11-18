# Use official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy all backend code
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir Flask flask-cors

# Create uploads folder inside container
RUN mkdir -p uploads

# Expose Flask port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
