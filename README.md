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
