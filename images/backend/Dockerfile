# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the backend code
COPY . .

# Collect static files (for Django)
RUN python manage.py collectstatic --noinput

# Expose port (e.g., 8000 for Django)
EXPOSE 8000

# Run the application with manage.py runserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]