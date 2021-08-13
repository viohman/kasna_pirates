
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import logging
import random
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'L', 'R']

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    logger.info("Test test test")

    content = request.get_json()
    me = content["_links"]["self"]["href"]

    arena_dims = content["arena"]["dims"]
    arena_state = content["arena"]["state"]
    my_location = [arena_state[me]["x"], arena_state[me]["y"]]
    my_dir = arena_state[me]["direction"]


    arena_state.pop(me)

    for pirate in arena_state:
        if arena_state[pirate]['x'] == my_location[0] and arena_state[pirate]['y'] < my_location[1] and my_dir == "N":
            if 0 < abs(my_location[1] - arena_state[pirate]['y']) <= 3:
                return "T"
            else:
                return "F"    
        if arena_state[pirate]['x'] == my_location[0] and arena_state[pirate]['y'] > my_location[1] and my_dir == "S":
            if 0 < abs(my_location[1] - arena_state[pirate]['y']) <= 3:
                return "T"
            else:
                return "F" 
        if arena_state[pirate]['y'] == my_location[1] and arena_state[pirate]['x'] < my_location[0] and my_dir == "W":
            if 0 < abs(my_location[0] - arena_state[pirate]['x']) <= 3:
                return "T"
            else:
                return "F" 
        if arena_state[pirate]['y'] == my_location[1] and arena_state[pirate]['x'] > my_location[0] and my_dir == "E":
            if 0 < abs(my_location[0] - arena_state[pirate]['x']) <= 3:
                return "T"
            else:
                return "F" 

        
    return moves[random.randrange(len(moves))]




if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  