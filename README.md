# Product App with Microservices and Docker
This project is a simple product app that showcases my extensive knowledge of microservices and Docker. The app allows an admin to add, view and manage products, and also includes a like feature for each product. The admin interface was built using Django, while the like functionality was built with Flask. The two microservices, admin (Django) and main (Flask), communicate with each other through RabbitMQ using the Pika library. The front-end was built using React and TypeScript.

## Features
Simple product management system with admin interface
Like feature for each product using Flask microservice
Communication between Django and Flask microservices through RabbitMQ and Pika
Modern and responsive React front-end

## Technologies
Python
Django
Flask
RabbitMQ
Pika
React
TypeScript
Docker

## Getting Started
To get started with the project, you'll need Docker installed on your local machine. Follow these steps to set up and run the app:

1. Clone the repository and navigate to the root directory.
```bash
  git clone https://github.com/yusufom/micro.git
  cd micro
```

2. Build the Docker images for the admin, main and frontend services.
```bash
  docker-compose build
```
3. Start the Docker containers.
```bash
  docker-compose up
```
4. Open your web browser and go to http://localhost:3000 to view the app.




