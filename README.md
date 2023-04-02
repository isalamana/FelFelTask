# FelFelTask

New approach for the fleet monitoring system in FELFEL.

## Table of Contents

- [Usage](#usage)
- [Content](#content)

## Usage

To run the system follow the folling steps:
  - Download files from this directory.
  - Open a terminal in the directory of the downloaded folder. 
  - Build the docker compose.
   ```
  docker-compose build
  ```
  - Up the docker compose.
  ```
  docker-compose up
  ```
  - The system will start running
  
  ## Content
  
  ### Server - Application A 
  
  A self-contained fleet management system, accessible through a set of well-defined RESTful endpoints.
  It fulfills the following requirements:
  
    - ability to add a new device to the fleet
    - ability to delete a device from the fleet
    - ability to retrieve information about a device in a fleet
    - ability to change the properties of a device in the fleet.
    
  ### Testing - Application B
  
  A testing client for the management system.
  
  It is designed as a State Machine that tests the REST endpoints in the following manner:
  
    - retrieves a Device Id randomly from this list: [112, 358, 132, 134]
    - checks if it the device is already present in the database, using the REST API.
    - if the device is present, deletes it
    - if the device is not present, inserts it, and in a different step it modifies the properties of that device.
