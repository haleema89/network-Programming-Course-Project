## Project Title
News Service System – Client/Server Project
## semester
first semester:2025-2026
## Group
- Course: ITNE352 – Network Programming
- Sec:2
- Group Name:GB3
- Student 1:Fatema Salem Rashed 202302468(serever side)
- Student 2: haleema khamis 202104099 (client side)
## Content of Table
| table: | 
|----------|
|Introduction|
| Decsciption of the project |
| Requitements|
|HOW TO|
|the Scripts|
|Additional concepts|
|Acknowledgments|
|conclusion|
|Reference|
## Introduction
This project is a Python-based client-server application that provides access to online news
The server communicates with NewsAPI and supports multiple client connections
Users can request and view news headlines and sources using various search options.
## Decsciption of the project
This initiative focuses on developing a complete client-server system for delivering news services. The server is structured to manage several client connections simultaneously through the use of socket programming methods. It retrieves current news information from NewsAPI, processes that data, and saves the resulting content in . JSON format, making it easy to access and manage. On the client end, users can engage with a user-friendly, menu-driven interface. This feature enables them to search for news articles and sources using different criteria, such as keywords, country, and category. The project demonstrates a practical application of fundamental principles including networking, API integration, file handling, and organized data exchange among distributed systems.
## Requitements
To set up and execute this project locally, you need to install the necessary dependencies using the built-in pip package manager. Ensure you have an active internet connection and a valid NewsAPI key, which can be obtained from newsapi.org.
Once the project files are downloaded or cloned, navigate to the project directory and use pip to install the required dependency (requests), keeping in mind that all other modules used are part of Python's standard library. For security purposes, the NewsAPI key can be configured either directly in the server code or via an environment variable.
The system operates on a client-server architecture. The server is initialized first (using python server.py), enabling it to handle multiple client connections concurrently through TCP. The client application (executed with python client.py) then connects to the server, allowing users to interact via a menu-driven interface.
The server manages incoming requests, communicates with the NewsAPI service to retrieve data, efficiently stores full JSON responses locally, and returns structured summaries and detailed results to the client in real-time, ensuring seamless coordination between the two components.
## HOW TO
To set up and run this project locally, ensure that Python 3.10 or higher is installed on your system along with the built-in pip package manager. The project requires an active internet connection and a valid NewsAPI key, which can be obtained by creating a free developer account at newsapi.org. After downloading or cloning the project files, navigate to the project directory using a terminal or command prompt. It is recommended to create and activate a virtual environment to isolate dependencies, then install the required external library using pip install requests, as the remaining modules (socket, threading, json, and os) are part of Python’s standard library. Next, configure the NewsAPI key either by directly assigning it to the API_KEY variable in the server script or by setting it as an environment variable and retrieving it within the code. Once the configuration is complete, start the server by running python server.py, which will listen for incoming client connections on the specified port. In a separate terminal window, run the client application using python client.py, enter a username when prompted, and interact with the system through the menu-based interface to request news headlines or sources. The server processes each request, retrieves data from NewsAPI, and stores the full JSON responses in the local data directory while returning summarized results and detailed information to the client in real time.
## the Scripts 
# server
The server script implements a multi-client TCP server that accepts concurrent client connections using threads. For each connected client, the server receives a username, then repeatedly accepts menu requests ( headlines by country/category/keywords or sources by country/category/language), calls the NewsAPI endpoint (top-headlines or sources), saves the full API response as a JSON file in the data/ directory, and returns a summarized list of up to 15 results and a full detailed record for a user-selected index. The server keeps running until the client sends a quit command.
# Standard library: socket, threading, json, os
# Third-party: requests (HTTP requests to NewsAPI)
