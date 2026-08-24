# Dockerized Web Application Deployment

A containerized Flask web application integrated with MongoDB using Docker and Docker Compose. This project demonstrates practical Docker concepts including multi-stage image building, multi-container application deployment, custom networking, and persistent database storage using Docker volumes.

## Project Overview

This project implements a Python Flask web application connected to a MongoDB database. The Flask application and MongoDB database run in separate Docker containers and are managed together using Docker Compose.

A custom Docker network is used for communication between the containers, while a Docker volume is configured to persist MongoDB data even when the MongoDB container is recreated.

## Technologies Used

- Python
- Flask
- MongoDB
- HTML
- CSS
- Docker
- Docker Compose

Docker Concepts Demonstrated

- Dockerfile and Docker image creation
- Multi-stage Docker build
- Docker containerization
- Docker Compose
- Multi-container application setup
- Custom Docker bridge network
- Container-to-container communication
- Docker volumes
- MongoDB persistent data storage
- Container lifecycle management

## Project Architecture

                    User
                      |
                      v
              Flask Application
                 Container
                      |
                Docker Network
                      |
                      v
               MongoDB Container
                      |
                      v
                Docker Volume
              Persistent Storage

The Flask application runs in one container, while MongoDB runs in a separate container. Both containers communicate through a custom Docker network.

MongoDB uses a Docker volume so that database data can persist independently of the MongoDB container.

### Important Files

- "app.py" – Flask application source code.
- "index.html" – HTML template for the web interface.
- "style.css" – CSS styling for the application.
- "requirements.txt" – Python dependencies required by the Flask application.
- "dockerfile" – Instructions for building the Flask application Docker image.
- "docker-compose.yml" – Configuration for running Flask and MongoDB containers together.
- ".dockerignore" – Specifies files and directories that should not be included in the Docker build context.

## Flask Application

The application is developed using Python Flask and provides the web interface for the project.

The Flask application communicates with MongoDB to perform database-related operations. The application is containerized using Docker so that it can run in an isolated environment with its required dependencies.

### Dockerfile

The project uses a Dockerfile to create a Docker image for the Flask application.

A multi-stage Docker build is used to separate the build-related environment from the final application environment. This helps create a cleaner application image by copying only the required application files and dependencies into the final stage.

### Docker Compose

Docker Compose is used to manage the Flask application and MongoDB as multiple services.

The Compose configuration handles:

- Flask application container
- MongoDB container
- Container networking
- MongoDB persistent volume
- Port configuration
- Service management

The application can be started using a single Docker Compose command instead of manually creating each container.

### Docker Network

A custom Docker bridge network is used for communication between the Flask and MongoDB containers.

The Flask application can communicate with MongoDB through the Docker network using the MongoDB service name.

This allows the containers to communicate with each other without requiring MongoDB to be exposed as a separate host service.

Docker Volume and Data Persistence

Docker volumes are used to provide persistent storage for MongoDB.

Normally, data stored inside a container's writable layer can be lost when the container is removed. By using a Docker volume, MongoDB data is stored separately from the container.

Therefore:

- MongoDB data is stored in a Docker volume.
- Removing and recreating the MongoDB container does not remove the volume automatically.
- The existing database data can be reused by the newly created MongoDB container.
- The volume provides persistence for database data.

### Useful commands for checking Docker volumes:

docker volume ls

To inspect a volume:

docker volume inspect <volume-name>

«Note: "docker compose down -v" removes the associated volumes, so it should be used carefully when persistent database data needs to be retained.»

Running the Project

Clone the repository:

git clone <repository-url>

Move into the project directory:

cd dockerized-webapp

Build the Docker image and start the containers:

docker compose up --build

After the containers start successfully, access the Flask application through the configured application port in a web browser.

Docker Compose Commands

Check the running containers:

docker compose ps

View container logs:

docker compose logs

Stop and remove the containers:

docker compose down

Stop and remove containers along with their associated volumes:

docker compose down -v

Difference Between "down" and "down -v"

"docker compose down" removes the containers and related Compose resources but keeps the named volumes.

"docker compose down -v" also removes the associated volumes. If MongoDB data is stored in that volume, removing the volume can result in loss of the persisted database data.

## Practical Workflow

The project was implemented through the following steps:

1. Created the Flask web application.
2. Added the required Python dependencies.
3. Created the Dockerfile for the Flask application.
4. Implemented a multi-stage Docker build.
5. Configured MongoDB as a separate container.
6. Created the Docker Compose configuration.
7. Configured a custom Docker network for container communication.
8. Configured a Docker volume for MongoDB persistent storage.
9. Built the Docker image.
10. Started the Flask and MongoDB containers using Docker Compose.
11. Checked Docker images and container status.
12. Tested communication between Flask and MongoDB.
13. Verified the application output.
14. Tested database persistence using the Docker volume.

## Verification

The project was verified by checking:

- Flask container status.
- MongoDB container status.
- Docker image creation.
- Container logs.
- Communication between Flask and MongoDB.
- Flask application output.
- MongoDB data persistence using the Docker volume.

### Key Learning Outcomes

Through this practical, I gained hands-on experience with:

- Containerizing a Flask web application.
- Creating and building Docker images.
- Using a multi-stage Dockerfile.
- Managing multiple containers using Docker Compose.
- Creating and using Docker networks.
- Establishing communication between application and database containers.
- Using Docker volumes for persistent database storage.
- Managing Docker container lifecycle.
- Monitoring container and image status using Docker commands.
- Integrating a Flask application with MongoDB.

Conclusion

This project provided hands-on experience in Docker-based application deployment using a Flask web application and MongoDB. It demonstrated multi-container application architecture, Docker networking, Docker Compose, container lifecycle management, and persistent database storage using Docker volumes.
