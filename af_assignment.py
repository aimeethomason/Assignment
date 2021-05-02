# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 11:17:21 2021

@author: Aimee Thomason
"""
# Import relevant packages from the python library.
# Import random provides access to random functions.

import random
import requests
import bs4


# Using an __init__ method, define an agent class using x and y variables.This 
# code will have a parameter label called self to assign the object. Anything defined
# to this class, belongs only to this class. The x and y variables will implement a property
# attribute to protect the variables.
# The move method defined within the agent class, allows the new self._x and 
# self._y co-ordinates to move randomly.
# If and else command statements are used to control and condition the agent 
# co-ordinates. The random.randit function will assign random floating values 
# between 0 and 100 to the co-ordinates. This is used to determine if the agent 
# coordinates should increase or decrease by one based on the random number used and
# whether this is greater or less than the value of 0.5.  
# The torus approach is also used to solve boundary problems by using the modulus operator
# and plotting the remainder of the division.
# Link the agents to the enviornment to allow for interaction.Here, all agents are 
# linked to the same environment object. This means that as one agents changes
# the environment data, the environment changes for all agents.
# Create a link to get the list of agents into each agent.

class Agent():
    def __init__(self,environment,agents, y, x):
        self.environment = environment
        self.agents = agents
        self.store = 0
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)

        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
            
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y
        
    def move(self):
        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
    
        if random.random() < 0.5:
            self._y = (self._y + 1) % 100
        else:
            self._y = (self._y - 1) % 100
            
# The following code will use an eat method within the agent class. This allows 
# for the environment data to be altered. If self._x and self._y are greater than
# 10, the environment will minus 10 and add it to the store.
       
    def eat(self): 
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10

# The following code will make a sharing neighbour method within the agent class.
# This will allow the agent to search for close neighbours and share resources with
# them. This method will calculate the distance to each of the other agents, and if
# they fall within neighbourhood distance, it should set it, and its neighbours'
# stores equal to the average of their two stores.
          
    def share_with_neighbours(self, neighbourhood):
        for agent in self.agents:
            dist = self.distance_between(agent)
        if dist <= neighbourhood:
            sum = self.store + agent.store
            average = sum /2
            self.store = average
            agent.store = average
        
      
      # print("sharing " + str(dist) + " " + str(average))
            
# The following code will create a function which returns the Euclidian distance between
# each of the agents using Pythagoras' theorem.

    def distance_between(self,agent):
        return (((self._x -agent._x)**2) + ((self._y - agent._y)**2))**0.5
                  
# Set the property x and y.
            
    #def x(self):
        #return self._x
        
    #def y(self):
        #return self._y
        
# Use the get function to obtain the atrribute value for the x and y co-ordinates.
      
    def getx(self):
        return self._x
    
    def gety(self):
        return self._y
    
# Use the self function to set the attribute value for the x and y co-ordinates.

    def setx(self, value):
        self._x = value
        
    def sety(self, value):
        self._y= value
