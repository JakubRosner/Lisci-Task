# Base image
FROM python:3.11

RUN pip install --upgrade pip

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt update

# Create directory for the application code
RUN mkdir /app

# Set working directory
WORKDIR /app

# Set environment variables
ENV DJANGO_ENV=docker
ENV DJANGO_SETTINGS_MODULE=lisci.settings

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY ./LisciTask .

# Create super user
CMD echo "from django.contrib.auth import get_user_model; \
    User = get_user_model(); \
    User.objects.create_superuser('admin', 'admin@lisci.com', 'admin')" | python manage.py shell

# Collect static files
CMD python manage.py collectstatic --no-input

# Run the application
EXPOSE 8000
CMD python manage.py makemigrations \
 && python manage.py migrate \
 && python manage.py runserver 0.0.0.0:8000