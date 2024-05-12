## Customapp2

# Prerequisites

This document provides instructions for downloading Docker and installing Frappe.

## Docker

Download Docker Desktop from the official website:

[Download Docker](https://www.docker.com/products/docker-desktop)

## Frappe

Follow the guide provided at the link below to install Frappe v15:

[Install Frappe v15](<link_to_frappe_installation_guide>)

## ERPNext

Complete Frappe ERPNext setup

# Installation

To install this feature, follow these steps:

1. If you don't have Docker, first download Docker. [Download Docker](https://www.docker.com/products/docker-desktop/)

2. Pull and run Ubuntu image in Docker:

    ```bash
    docker pull ubuntu:22.04
    docker run -dt --name bench -p 8000:8000 ubuntu:22.04 /bin/bash
    ```

3. Switch user:

    ```bash
    su - erp_user
    ```

4. Start MariaDB:

    ```bash
    sudo service mariadb start
    ```

5. Start Redis:

    ```bash
    sudo service redis-server start
    ```

6. Change directory to frappe-bench:

    ```bash
    cd frappe-bench
    ```

7. Start Bench:

    ```bash
    bench start
    ```

8. Install custom app:

    Clone repository to apps folder in frappe bench directory:

    ```bash
    git clone https://github.com/abhi-146/server-side-project/
    bench --site [sitename] install-app [appname]
    ```



#### License

mit
