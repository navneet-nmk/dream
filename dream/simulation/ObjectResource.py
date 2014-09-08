# ===========================================================================
# Copyright 2013 University of Limerick
#
# This file is part of DREAM.
#
# DREAM is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DREAM is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with DREAM.  If not, see <http://www.gnu.org/licenses/>.
# ===========================================================================
'''
Created on 18 Aug 2013

@author: George
'''
'''
Class that acts as an abstract. It should have no instances. All the Resources should inherit from it
'''
# from SimPy.Simulation import Resource
import simpy
from ManPyObject import ManPyObject

# ===========================================================================
#                    the resource that repairs the machines
# ===========================================================================
class ObjectResource(ManPyObject):
    
    def __init__(self,id='',name='',**kw):
        ManPyObject.__init__(self,id,name)
        self.initialized = False
        # list that holds the objectInterruptions that have this element as victim
        self.objectInterruptions=[]        
        # alias used for printing the trace
        self.alias=None
        # list with the coreObjects IDs that the resource services
        self.coreObjectIds=[]
        from Globals import G
        G.ObjectResourceList.append(self) 
        
    def initialize(self):
        from Globals import G
        self.env=G.env
        self.totalWorkingTime=0         #holds the total working time
        self.totalWaitingTime=0         #holds the total waiting time
        self.timeLastOperationStarted=0    #holds the time that the last repair was started        
        self.Res=simpy.Resource(self.env, capacity=self.capacity)
        # variable that checks whether the resource is already initialized
        self.initialized = True
        # list with the coreObjects IDs that the resource services
        self.coreObjectIds=[]
        # list with the coreObjects that the resource services
        self.coreObjects=[]
    
    # =======================================================================
    #                    checks if the worker is available
    # =======================================================================       
    def checkIfResourceIsAvailable(self,callerObject=None): 
        return len(self.Res.users)<self.capacity   
    
       
    # =======================================================================
    #                           returns the resource
    # =======================================================================
    def getResource(self):
        return self.Res
    
    # =======================================================================
    #               returns the active queue of the resource
    # =======================================================================
    def getResourceQueue(self):
        return self.Res.users
    
    # =======================================================================
    # check if the resource is already initialized
    # =======================================================================
    def isInitialized(self):
        return self.initialized
    
    #===========================================================================
    # print the route (the different stations the resource was occupied by)
    #===========================================================================
    def printRoute(self):
        pass
