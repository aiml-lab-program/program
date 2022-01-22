#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 12:59:24 2021

@author: dse
"""

class Graph:
    def __init__(self,graph,heuristicNodeList,startNode):
        self.graph  = graph
        self.H = heuristicNodeList
        self.start = startNode
        self.parent = {}
        self.status = {}
        self.solutionGraph = {}
       
    def applyAOStar(self):
        self.aoStar(self.start,False)
       
    def getNeighbour(self,v):
        return self.graph.get(v,"")
   
    def getStatus(self,v):
        return self.status.get(v,0)
   
    def setstatus(self,v,val):
        self.status[v] = val
       
    def getHeuristicNodeValue(self,n):
        return self.H.get(n,0)
   
    def setHeuristicNodeValue(self,n,value):
        self.H[n] = value
       
    def printSolution(self):
        print("For graph solution , traverse the graph from the start node :",self.start)
        print("-------------------------------------------------")
        print(self.solutionGraph)
        print("-------------------------------------------------")
       
    def computeMinimumCostCHildNode(self,v):
        minimumcost = 0
        costToChildNodeListDict = {}
        costToChildNodeListDict[minimumcost] = []
        flag = True
       
        for nodeInfoTupleList in self.getNeighbour(v):
            cost = 0
            nodeList = []
           
            for c,weight in nodeInfoTupleList:
                cost = cost + self.getHeuristicNodeValue(c) + weight
                nodeList.append(c)
               
            if flag == True:
                minimumcost = cost
                costToChildNodeListDict[minimumcost]  = nodeList
                flag = False
               
            else :
                if minimumcost > cost :
                    minimumcost = cost
                    costToChildNodeListDict[minimumcost] = nodeList
                   
        return minimumcost,costToChildNodeListDict[minimumcost]
   
   
    def aoStar(self,v,backTracking):
        print("Heuristic values : ",self.H)
        print("Solution Graph : ",self.solutionGraph)
        print("Processing Node : ",v)
        print("-------------------------------")
       
        if self.getStatus(v) >= 0:
            minimumcost , childNodeList = self.computeMinimumCostCHildNode(v)
            print(minimumcost,childNodeList)
            self.setHeuristicNodeValue(v, minimumcost)
            self.setstatus(v, len(childNodeList))
           
            solved = True
           
            for childnode in childNodeList:
                self.parent[childnode] = v
                if self.getStatus(childnode) != -1:
                    solved = solved & False
                   
            if solved == True:
                self.setstatus(v, -1)
                self.solutionGraph[v] = childNodeList
               
            if v!= self.start:
                self.aoStar(self.parent[v], True)
               
            if backTracking == False:
                for childnode in childNodeList:
                    self.setstatus(childnode, 0)
                    self.aoStar(childnode, False)
                   


h1 = {'A':1,'B':6,'C':2,'D':12,'E':2,'F':1,'G':5,'H':7,'I':7,'J':1}

graph = {'A' : [[('B',1),('C',1)],[('D',1)]],
         'B' : [[('G',1)],[('H',1)]],
         'C' : [[('J',1)]],
         'D' : [[('E',1),('F',1)]],
         'G' : [[('I',1)]]
    }

G1 = Graph(graph, h1, 'A')
G1.applyAOStar()
G1.printSolution()




h2 = {'A':1,'B':6,'C':12,'D':10,'E':4,'F':4,'G':5,'H':7}

graph2 = {'A' : [[('B',1),('C',1)],[('D',1)]],
          'B' : [[('G',1)],[('H',1)]],
          'D' : [[('E',1),('F',1)]]
    }

#G2 = Graph(graph2, h2, 'A')
#G2.applyAOStar()
#G2.printSolution()

