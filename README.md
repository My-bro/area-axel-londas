# Area

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [License](#license)

## Description

ActionREAction is an automation platform inspired by services like IFTTT and Zapier. It allows users to create automated workflows by connecting various services through actions and reactions. The platform comprises an application server, a web client, and a mobile client, all orchestrated using Docker Compose for seamless deployment and scalability.


### Demo

<video width="100%" controls>
  <source src="asset/Make_Applet.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

## Usage

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/julesreyn/area.git
cd area
```

> **Note:** To run and compile the project, you need to have Docker and Docker Compose installed on your machine.

To run the project, execute the following command:

```bash
docker-compose up -d
```

To stop the project, execute the following command:

```bash
docker-compose down
```

To build only a specific service, execute the following command:

```bash
# service-name available options: frontend, backend, database

docker-compose build <service-name>

```

## Project Structure

The project is divided into three main components:

- **Backend:** The application server is a fastapi application that serves as the core of the platform. It is responsible for handling user authentication, managing services, and orchestrating workflows.

- **Frontend:** The web client is a React application that provides users with a graphical interface to create and manage workflows. It communicates with the backend through a RESTful API.

- **Mobile:** The mobile client is a Flutter application that allows users to receive notifications and manage workflows on the go. It communicates with the backend through a RESTful API.

## Documentation

The project documentation is available in the `docs` directory. It includes all the necessary information to understand, run, and contribute to the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
