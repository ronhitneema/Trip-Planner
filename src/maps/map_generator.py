import os
import uuid

import sys
sys.path.append('../')

from helper import constants

class MapGenerator:
    def __init__(self, locations, shortest_path):
        self.locations = locations
        self.shortest_path = [x for x, y in shortest_path]

    def generate_map(self):
        """
        Generates map for the given map locations with the shortest path
        """
        origin = self.locations[self.shortest_path[0]]
        destination = self.locations[self.shortest_path[-1]]
        waypoints = []
        for index in range(1, len(self.locations)-1):
            waypoints.append(self.locations[self.shortest_path[index]])

        # Build the URL for the map
        url = f'https://www.google.com/maps/embed/v1/directions?key={constants.Constants.GOOGLEAPIKEY.value}&origin={origin}&destination={destination}&waypoints={"|".join(waypoints)}'

        # Define the contents of the HTML file
        html_content = f'''<!DOCTYPE html>
        <html>
        <head>
        	<title>Google Maps Embed API Example</title>
        	<style>
        		#map {{
        			height: 600px;
        			width: 100%;
        		}}
        	</style>
        </head>
        <body>
        	<h1>Directions from {origin} --to-- {destination}</h1>
        	<iframe id="map" src="{url}"></iframe>
        </body>
        </html>
        '''
        new_uuid = uuid.uuid4()

        # Write the HTML file to disk
        with open(f'map-{str(new_uuid)}.html', 'w') as f:
            f.write(html_content)

        os.system(f'open map-{str(new_uuid)}.html')


