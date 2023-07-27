# Routing and Planning Application Readme
This repository contains the code for a routing and planning application that enables users to navigate across a network of superchargers or gas stations. The application implements a dynamic vehicle digital twin for accurate route and energy consumption calculations. It optimizes the path searching algorithm for low latency route calculation by introducing just-in-time compilation capability and utilizing Google APIs for path graphs, along with the A* algorithm for finding the shortest path.

## Features
Routing: The application allows users to input their starting location and destination, and it calculates the optimal route considering factors like energy consumption, distance, and charging/gas station availability.
Energy Consumption: The dynamic vehicle digital twin accurately estimates the energy consumption of the vehicle based on its make and model, along with real-time factors like weather, road conditions, and vehicle load.
Latency Optimization: The path searching algorithm is optimized for low latency calculations, ensuring quick responses to user queries.
Graph Visualization: The application provides an option to visualize the path graphs generated using Google APIs, allowing users to understand the route better.
Superchargers/Gas Stations Network: The application's network of superchargers or gas stations is kept up-to-date with the latest data to ensure reliable route planning.
Project Structure
helper: This directory contains the constants.py file, which stores various constants used throughout the application. These constants might include charging rates, vehicle specifications, or API keys.
maps: The map_generator.py file in this directory is responsible for fetching and generating path graphs from Google APIs based on user input.
mst: The kruskals.py file in this directory implements Kruskal's algorithm for generating the minimum spanning tree of the graph.
path: The optimum_path.py file in this directory calculates the optimum path using the A* algorithm, considering energy consumption and other relevant factors.
graph.py: This file contains the implementation of the graph data structure used for the application's operations.
main.py: The main entry point of the application, where users can interact with the routing and planning functionalities.

## How to Use
Clone the repository to your local machine.
Ensure you have all the required dependencies installed. You can find the necessary dependencies in the requirements.txt file.
Make sure to update the constants.py file in the helper directory with appropriate values for your specific application. This may include API keys, vehicle specifications, or any other relevant constants.
Run the main.py file to launch the application.
Input your starting location and destination to find the optimal route. The application will provide information on the best path, including charging/gas station stops if applicable, estimated energy consumption, and other relevant details.
Contributing
Contributions to this project are welcome. If you have any ideas, bug fixes, or improvements, please feel free to create a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
We would like to acknowledge the following libraries and APIs that have been instrumental in the development of this application:

Google Maps API: For providing path graphs and map data.
A* Algorithm: For the efficient calculation of the shortest path.
Kruskal's Algorithm: For generating the minimum spanning tree.
