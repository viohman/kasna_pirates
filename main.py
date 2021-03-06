
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
# from flask import Response
# import time
""" Tested and failed
1. sending streaming responses with multiple "T" to try hitting more then once per round
2. lagging opponents with barrage of fake requests

Tested and Worked
1. creating multiple clones based on prefixed url and different revisions

"""

""" TO DO
1. force the bots to let IceKing win
2. try reinforced learning based on Q-table:
https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0
https://gym.openai.com/envs/FrozenLake-v0/
"""

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'L', 'R']

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)

    content = request.get_json()
    me = content["_links"]["self"]["href"]

    # arena_dims = content["arena"]["dims"]
    arena_state = content["arena"]["state"]
    my_location = [arena_state[me]["x"], arena_state[me]["y"]]
    my_dir = arena_state[me]["direction"]


    arena_state.pop(me)


    # def generate():
    #     for x in range(0, 2):
    #         time.sleep(2)
    #         yield 'T'

    for pirate in arena_state:
        # if "cloudbowl-samples-python-gpcpn53b3a-uc.a.run.app" in pirate:
        #     continue
        if arena_state[pirate]['x'] == my_location[0] and arena_state[pirate]['y'] < my_location[1] and my_dir == "N":
            if 0 < abs(my_location[1] - arena_state[pirate]['y']) <= 3:
                # def generate():
                #     for x in range(0, 3):
                #         yield 'T'
                # return Response(generate()) 
                if "cloudbowl-samples-python-gpcpn53b3a-uc.a.run.app" in pirate and me != "https://cloudbowl-samples-python-gpcpn53b3a-uc.a.run.app":
                    return "R"  
                return "T" 
            else:
                return "F" 

        if arena_state[pirate]['x'] == my_location[0] and arena_state[pirate]['y'] > my_location[1] and my_dir == "S":
            if 0 < abs(my_location[1] - arena_state[pirate]['y']) <= 3:
                # def generate():
                #     for x in range(0, 3):
                #         yield 'T'
                # return Response(generate())  
                if "cloudbowl-samples-python-gpcpn53b3a-uc.a.run.app" in pirate and me != "https://cloudbowl-samples-python-gpcpn53b3a-uc.a.run.app":
                    return "L"
                return "T"
            else:
                return "F" 
        if arena_state[pirate]['y'] == my_location[1] and arena_state[pirate]['x'] < my_location[0] and my_dir == "W":
            if 0 < abs(my_location[0] - arena_state[pirate]['x']) <= 3:
                # return Response(generate()) 
                if "cloudbowl-samples-python-gpcpn53b3a-uc.a.run.app" in pirate and me != "https://cloudbowl-samples-python-gpcpn53b3a-uc.a.run.app":
                    return "R"
                return "T"
            else:
                return "F" 
        if arena_state[pirate]['y'] == my_location[1] and arena_state[pirate]['x'] > my_location[0] and my_dir == "E":
            if 0 < abs(my_location[0] - arena_state[pirate]['x']) <= 3:
                # return Response(generate())
                if "cloudbowl-samples-python-gpcpn53b3a-uc.a.run.app" in pirate and me != "https://cloudbowl-samples-python-gpcpn53b3a-uc.a.run.app":
                    return "L" 
                return "T"
            else:
                return "F" 

        
    return moves[random.randrange(len(moves))]



if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  