# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 11:17:21 2021

@author: Aimee Thomason
"""
# Import relevant packages from the python library.
# Import random provides access to random functions.
# Import requests provides access to HTTP library, enabling HTTP requests in Python, 
# reducing complexities behind the interface.
# Import bs4 is a python library for pulling data out of HTML and XML files. This 
# provides idiomatic ways of navigating, searching, and modifying the parse tree, 
# saving the programmer time.

import random
import requests
import bs4

# The following code will create a new class called agent. Within this class, an 
# __init__ method is used to pass self, environment, agents and both the y and x 
# coordinates into the agents constructor.
class Agent():
    def __init__(self,environment,agents, y, x):
        # The parameter label called self is used to assign the object. Thereby, anything 
        # defined to this class belongs only to this class.
        self.environment = environment
        self.agents = agents
        self.store = 0
        # The random.randit function is used to assign random floating values between 0 
        # and 300 to the self._x and self._y coordinates, matching the extent of the
        # environment.
        self._x = random.randint(0,300)
        self._y = random.randint(0,300)
        
# Here, if and else command statements are used to control and condition the agent
# coordinates. These again, use random.randit to assign random floating values to
# the same extent as the environment.

        if (x == None):
            self._x = random.randint(0,300)
        else:
            self._x = x
            
        if (y == None):
            self._y = random.randint(0,300)
        else:
            self._y = y
                        
# The following code will use a move function defined by self within the agent class.
# This will allow the new self._x and self._y coordinates to move randomly. The value of
# the self._x and self._y coordinates should increase or decrease by one based on the random
# number generated and whether this is greater or less than the value of 0.5. A torus approach
# is also used to solve boundary problems by using the modulus operator and plotting the 
# remainder of the division.
        
    def move(self):
        if random.random() < 0.5:
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300
    
        if random.random() < 0.5:
            self._y = (self._y + 1) % 300
        else:
            self._y = (self._y - 1) % 300
            
# The following code defines an eat function within the agent class, associated with self.
# This links all agents to the same environment object. Thereby, as one agent changes the
# environment data, the environment changes for all agents. For instance, If self._x and 
# self._y are greater than 10, the environment will minus 10 and add it to the store.

    def eat(self): 
         if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10

# The code below defines a share_with_neighbours function within the agent class, associated 
# with self and neighbourhood. This will allow the agents to search for close neighbours and 
# share resources with them. Here, the distance to each of the other agents will be calculated,
# and if they fall within neighbourhood distance, it should set it and its neighbours' stores
# equal to the average of their two stores.
        
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
        if dist <= neighbourhood:
            sum = self.store + agent.store
            average = sum /2
            self.store = average
            agent.store = average
            
# The following code will define a function within the agent class, which returns the 
# Euclidian distance between each of the agents using Pythagoras' theorem.

    def distance_between(self,agent):
        return (((self._x -agent._x)**2) + ((self._y - agent._y)**2))**0.5
        
# Using a get function defined by self within the agent class allows for the attribute
# values for the self._x and self._y coordinates to be obtained.
      
    def getx(self):
        return self._x
    
    def gety(self):
        return self._y
    
# Here, a set function is defined within the agent class, associated with self. This
# will set the attribute values for the self._x and self._y coordinates.

    def setx(self, value):
        self._x = value
        
    def sety(self, value):
        self._y= value
