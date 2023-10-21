# Data-WareHouse-DimensionalModelling-for-Airbnb-App-Using-Postgresql-Docker


This project aims to demonstrate how to perform dimensional modeling for a data warehouse using PostgreSQL and Docker. The project focuses on modeling data from an Airbnb-like application.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

In the context of data warehousing, dimensional modeling is a technique used to design the data structure for analytical reporting. This project provides an example implementation of dimensional modeling for an Airbnb-like app. It shows how to model various entities like users, properties, bookings, reviews, etc., and how to create a star schema using the PostgreSQL database.

## Prerequisites

Before getting started, make sure you have the following installed on your system:

- Docker: [https://www.docker.com/](https://www.docker.com/)
- PostgreSQL: [https://www.postgresql.org/](https://www.postgresql.org/)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/your-repo.git
```
2. Navigate to the project directory
```
cd your-repo
```
3. Build the Docker image
```
docker-compose build
```

4. Start the Docker containner
```
docker-compose up -d
```

This will start the PostgreSQL database container and create the necessary tables for the dimensional model.

## Usage
To use the dimensional model, you can connect to the PostgreSQL database using your preferred database client and execute queries against the created tables. The dimensional model provides a structure that enables efficient reporting and analysis of the Airbnb-like app data.

The project also includes sample queries that demonstrate how to retrieve insights from the dimensional model. You can find these queries in the queries directory.
