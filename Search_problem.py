# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 20:58:45 2023

@author: youse
"""

import random
import time

from tkinter import *

root = Tk()

my_canvas = Canvas(root, width = 575, height = 575, highlightthickness=0)

my_canvas.configure(bg='white')

my_canvas.pack()




class Node:
    
    def __init__ (self,num, x, y):
        self.x = x
        self.y = y
        self.num = num
        self.character = ""
        self.letter = None
        self.arrows = self.checkP()
        self.color = "green"
        self.Circle = None
        self.minC = None
        self.path = []
        
    
    def checkP(self):
        arrows = []
        if self.y != 75 : 
            arrows.append(arrow(self.x+30, self.y, self.x+30, self.y-75, self.num, self.num-4))
        if self.x != 450: 
            arrows.append(arrow(self.x+50, self.y+20, self.x+125, self.y+20, self.num, self.num+1))
        if self.y != 450 : 
            arrows.append(arrow(self.x+20, self.y+50, self.x+20, self.y+125, self.num, self.num+4))
        if self.x != 75: 
            arrows.append(arrow(self.x, self.y+30, self.x-75, self.y+30, self.num, self.num-1))
        if self.x != 75 and self.y != 75: 
            arrows.append(arrow(self.x, self.y-7, self.x-75, self.y-82, self.num, self.num-5))
        if self.y != 75 and self.x != 450: 
            arrows.append(arrow(self.x+50, self.y-7, self.x+125, self.y-82, self.num, self.num-3))
        if self.x != 450 and self.y != 450: 
            arrows.append(arrow(self.x+50, self.y+57, self.x+125, self.y+132, self.num, self.num+5))
        if self.y != 450 and self.x != 75: 
            arrows.append(arrow(self.x, self.y+57, self.x-75, self.y+132, self.num, self.num+3))
        return arrows
    
    def getArrows(self):
         return self.arrows
     
    def getStringPath(self):
        path = []
        for i in self.path:
            path.append(str(i.nf)+" --> "+str(i.nl))
        return path
     
    def getPlacedArrows(self):
        List = []
        for i in self.arrows:
            if i.color == "black":
                List.append(i)
        return List
     
        
    def getStringPlacedArrows(self):
        List = []
        for i in self.getPlacedArrows():
            List.append(str(i.nf)+" --> "+str(i.nl))
        return List
    
    def getStringPlacedArrowsCost(self):
        List = []
        for i in self.getPlacedArrows():
            List.append(str(i.nf)+" -("+str(i.costValue)+")-> "+str(i.nl))
        return List
    
    def drawCircles(self):
        self.Circle = my_canvas.create_oval(self.x, self.y, self.x+50, self.y+50, fill= self.color)
        self.minC = my_canvas.create_oval(self.x+12.5, self.y+12.5, self.x+37.5, self.y+37.5, fill="White")
        
    def drawLetter(self, letter):
        self.character = letter
        if letter == "C":
            self.letter = my_canvas.create_text(self.x+24.5, self.y+25.5, text=self.character, font= "Calibri 16 bold")
        else:
            self.letter = my_canvas.create_text(self.x+25.5, self.y+25.5, text=self.character, font= "Calibri 16 bold")
        
    def clearLetter(self):
        self.character = ""
        self.letter = None
       
      
class arrow:
    
    def __init__(self, x1, y1, x2, y2, nf, nl):
        self.color = "white"
        self.cost = "white"
        self.Arrow = None
        self.cost = None
        self.randomIntegers = [1,2,3,7,8,9]
        self.costValue = self.randomIntegers[random.randint(0,5)]
        self.nf = nf
        self.nl = nl
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.setXY()
        
    def setXY(self):
        if self.x1 == self.x2:
            if self.y1 - self.y2 > 0:
                self.x3 = self.x1+10
                self.y3 = self.y2+37.5
            elif self.y1 - self.y2 < 0:
                self.x3 = self.x1-10
                self.y3 = self.y1+37.5
        elif self.y1 == self.y2:
            if self.x1 - self.x2 > 0:
                self.x3 = self.x2+37.5
                self.y3 = self.y1+10
            elif self.x1 - self.x2 < 0:
                self.x3 = self.x1+37.5
                self.y3 = self.y1-10
        else:
            if self.y1 - self.y2 > 0 and self.x1 - self.x2 > 0:
                self.x3 = self.x1-2
                self.y3 = self.y1-17
            elif self.y1 - self.y2 > 0 and self.x1 - self.x2 < 0:
                self.x3 = self.x1+2
                self.y3 = self.y1-17
            elif self.y1 - self.y2 < 0 and self.x1 - self.x2 > 0:
                self.x3 = self.x1-2
                self.y3 = self.y1+17
            elif self.y1 - self.y2 < 0 and self.x1 - self.x2 < 0:
                self.x3 = self.x1+2
                self.y3 = self.y1+17
                
    def checkV(self,x1,y1,x2,y2):
        if (x1 % 25) != 0:
            if (x1+5 % 25) == 0:
                x1 += 5
                x2 +=5
            elif (x1-5 % 25) == 0:
                x1-=5
                x2-=5
                
        if (y1 % 25) != 0:
            if (y1+5 % 25) == 0:
                y1 += 5
                y2 +=5
            elif (y1-5 % 25) == 0:
                y1-=5
                y2-=5 
        return([x1,y1,x2,y2])
    
    
    def drawArrow(self):
        self.Arrow = my_canvas.create_line(self.x1,self.y1,self.x2,self.y2,fill=self.color,arrow="last", width=5)
        
    def deleteArrow(self):
        my_canvas.delete(self.Arrow)
        self.Arrow = None
        self.color = "white"
        
        
    def generateCost(self):
        self.costValue = self.randomIntegers[random.randint(0,5)]
            
    def disableCost(self):
        my_canvas.delete(self.cost)
        self.cost = None

                
    def enableCost(self):
            if  button3.cget("text") == "Remove Cost":
               self.cost =  my_canvas.create_text(self.x3,self.y3, text=str(self.costValue), font="Calibri 12 bold")
class Map:
    
    def __init__(self, List_N):
        self.List_N = List_N
        self.List_A = self.fetchArrows()
        self.letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
        self.Placed_Arrows = []
        self.costs = None
        self.start_index = 0
        self.goal_index = 0
        self.check = True
    
    def fetchArrows(self):
        List_A = []
        for i in self.List_N:
            for e in i.getArrows():
                List_A.append(e)
        return List_A
    
    def updatePlacedArrows(self):
        List = []
        for index in range(len(self.List_A)):
            if self.List_A[index].color != "white":
                List.append(index)
        self.Placed_Arrows = List
    
    def createPaths(self):
        random_index = []
        for i in range(random.randint(8,80)):
            index = random.randint(0, 83)
            if index not in random_index:
                random_index.append(index)
                self.List_A[index].color = "black"
        self.Placed_Arrows = random_index
        
    def clearPaths(self):
        for i in self.Placed_Arrows:
            self.List_A[i].color = "white"
            my_canvas.delete(self.List_A[i].Arrow)
            my_canvas.delete(self.List_A[i].cost)
            
            
            
    def clearNodes(self):
        for i in self.List_N:
            my_canvas.delete(i.Circle)
            my_canvas.delete(i.minC)
            
        for i in self.List_A:
            i.generateCost()
        self.costs = self.getCosts()
            
            
    def drawArrows(self):
        check =  button3.cget("text") == "Remove Cost"
        for i in self.Placed_Arrows:
            self.List_A[i].drawArrow()
            if check:
                self.List_A[i].enableCost()
            else:
                self.List_A[i].disableCost()
    
    def createMission(self):
        self.clearMission()
        while True :
            start_index = random.randint(0,15)
            goal_index = random.randint(0,15)
            if start_index != goal_index:
                self.start_index = start_index
                self.goal_index = goal_index
                self.shuffle()
                break
      
    def shuffle(self):
        self.check = False
        self.clearNodes()
        while True:
            print("Start Again")
            self.clearPaths()
            self.createPaths()
            check = self.checkForPath(self.start_index, self.goal_index, [])
            if check:
                self.drawArrows()
                self.List_N[self.start_index].color = "red"
                self.List_N[self.goal_index].color = "gold"
                randomLetters = []
                for i in self.List_N:
                    i.drawCircles()
                    while True:
                        letter = self.letters[random.randint(0, 15)]
                        if letter not in randomLetters:
                            randomLetters.append(letter)
                            i.drawLetter(letter)
                            break
                break
    
    def clearMission(self):
        self.List_N[self.start_index].color = "green"
        self.List_N[self.goal_index].color = "green"
    
        
    def Cost(self):
        if button3.cget("text") == "Apply Cost":
            button3.__setitem__("text", "Remove Cost")
            for arrow in range(len(m.List_A)):
                m.List_A[arrow].costValue = m.costs[arrow]
                
            for i in self.Placed_Arrows:
                self.List_A[i].enableCost()
            
        else:
            button3.__setitem__("text", "Apply Cost")
            for i in self.Placed_Arrows:
                self.List_A[i].disableCost()
            
            
    def getCosts(self):
        Costs = []
        for i in self.List_A:
            Costs.append(i.costValue)
        return Costs
        
            
    def checkForPath(self, x, y, Visited_Nodes):
        check = False
        print(str(x)+"   goal = "+str(y))
        Visited_Nodes.append(self.List_N[x])
        for i in self.List_N[x].getPlacedArrows():
            current_Node = self.List_N[i.nl-1]
            if current_Node not in Visited_Nodes:
                if i.nl-1 == y:
                    print(str(i.nl-1)+"   goal = "+str(y))
                    check = True
                    break
                else:
                    check = self.checkForPath(i.nl-1, y, Visited_Nodes)
                    if check:
                        break
        return check 
    
    
    def checkForLengthedPath(self, x, y, Visited_Nodes, length, count):
        print(str(x)+"   goal = "+str(y) +" Visited Nodes = "+str(len(Visited_Nodes)))
        Visited_Nodes.append(self.List_N[x])
        count += 1
        check = [False, count]
        if len(self.Placed_Arrows) < length:
            return [False, count]
        for i in self.List_N[x].getPlacedArrows():
            current_Node = self.List_N[i.nl-1]
            if current_Node not in Visited_Nodes:
                if i.nl-1 == y:
                    print(str(i.nl-1)+"   goal = "+str(y) +"  length = "+str(count) + " check = "+str(count < length))
                    return  [True, count]
                else:
                    c = self.checkForLengthedPath(i.nl-1, y, Visited_Nodes.copy(), length, count)
                    if c[0] and c[1] >= length:
                        check = c
                        continue
                    elif c[0] and c[1] < length:
                        return c
        return check
    
    def checkClick(self, event):
        x = event.x
        y = event.y
        index = 0
        for arrow in self.List_A:
            if arrow.x1 == arrow.x2:
                if x >= arrow.x1-17.5 and x <= arrow.x1+17.5:
                    self.checkUpDown(arrow, x, y, index)
            elif arrow.y1 == arrow.y2:
                if y >= arrow.y1-17.5 and y <= arrow.y1+17.5:
                    self.checkRightLeft(arrow, x, y, index)
            elif abs(arrow.x1 - arrow.x2) == abs(arrow.y1 - arrow.y2):
                if arrow.y1 >= y and arrow.y2 <= y:
                    self.checkUpDiagonal(arrow, x, y, index)
                elif arrow.y1 <= y and arrow.y2 >= y:
                    self.checkDownDiagonal(arrow, x, y, index)   
            index += 1
                
    def checkUpDown(self, arrow, x , y, index):
        if x >= arrow.x1-2.5 and x <= arrow.x1+2.5 and arrow.y1 - arrow.y2 > 0 and y >= arrow.y2 and y <= arrow.y1:
            self.arrowClick(arrow, index)
        elif abs(x-arrow.x3) <= 3.5 and abs(y-arrow.y3) <= 4 and arrow.Arrow != None:
            self.costClick(arrow, index)
        elif x >= arrow.x1-2.5 and x <= arrow.x1+2.5 and arrow.y1 - arrow.y2 < 0 and y >= arrow.y1 and y <= arrow.y2:
            self.arrowClick(arrow, index)
        elif abs(x-arrow.x3) <= 3.5 and abs(y-arrow.y3) <= 4 and arrow.Arrow != None:
           self.costClick(arrow, index)
           
    def checkRightLeft(self, arrow, x, y, index):
        if y >= arrow.y1-2.5 and y <= arrow.y1+2.5 and arrow.x1 - arrow.x2 > 0 and x >= arrow.x2 and x <= arrow.x1:
            self.arrowClick(arrow, index)
        elif abs(x-arrow.x3) <= 4 and abs(y-arrow.y3) <= 3.5 and arrow.Arrow != None:
            self.costClick(arrow, index)
        elif y >= arrow.y1-2.5 and y <= arrow.y1+2.5 and arrow.x1 - arrow.x2 < 0 and x >= arrow.x1 and x <= arrow.x2:
            self.arrowClick(arrow, index)
        elif abs(x-arrow.x3) <= 4 and abs(y-arrow.y3) <= 3.5 and arrow.Arrow != None:
            self.costClick(arrow, index)
            
    def checkUpDiagonal(self, arrow, x, y, index):
        if arrow.x1 <= x and arrow.x2 >= x and abs(y-arrow.y1)-(x-arrow.x1) >= -2.5 and  abs(y-arrow.y1)-(x-arrow.x1) <= 2.5:
            self.arrowClick(arrow, index)
        elif abs(x-arrow.x3) <= 4 and abs(y-arrow.y3) <= 4 and arrow.Arrow != None:
            self.costClick(arrow, index)
        elif arrow.x1 >= x and arrow.x2 <= x and abs(y-arrow.y1)+(x-arrow.x1) >= -2.5 and  abs(y-arrow.y1)+(x-arrow.x1) <= 2.5:
            self.arrowClick(arrow, index)
        elif abs(x-arrow.x3) <= 4 and abs(y-arrow.y3) <= 4 and arrow.Arrow != None:
            self.costClick(arrow, index)
    
    def checkDownDiagonal(self, arrow, x, y, index):
        if arrow.x1 <= x and arrow.x2 >= x and abs(y-arrow.y1)-(x-arrow.x1) >= -2.5 and  abs(y-arrow.y1)-(x-arrow.x1) <= 2.5:
            self.arrowClick(arrow, index)
        elif abs(x-arrow.x3) <= 4 and abs(y-arrow.y3) <= 4 and arrow.Arrow != None:
            self.costClick(arrow, index)
        elif arrow.x1 >= x and arrow.x2 <= x and abs(y-arrow.y1)+(x-arrow.x1) >= -2.5 and  abs(y-arrow.y1)+(x-arrow.x1) <= 2.5:
            self.arrowClick(arrow, index)
        elif abs(x-arrow.x3) <= 4 and abs(y-arrow.y3) <= 4 and arrow.Arrow != None:
            self.costClick(arrow, index)
            
            
    def arrowClick(self, arrow, index):
        if arrow.color != "white":
            arrow.color == "white"
            arrow.deleteArrow()
            arrow.disableCost()
            m.updatePlacedArrows()
        else:
            arrow.color = "black"
            arrow.drawArrow()
            arrow.costValue = m.costs[index]
            arrow.enableCost()
            m.updatePlacedArrows()
            
            
    def costClick(self, arrow, index):
        arrow.disableCost()
        value = arrow.costValue
        while arrow.costValue == value:
            arrow.generateCost()
        m.costs[index] = arrow.costValue
        arrow.enableCost()

class AI:

    def __init__(self, Node):
        self.Node = Node
        self.frontier = []
        self.Visited_Nodes = []
        self.Reached_Nodes = []
        
        
    def UpdateBreadth(self):
        for arrow in m.List_A:
            if arrow.color == "red":
               arrow.deleteArrow()
               arrow.color = "black"
               arrow.drawArrow()
        for node in self.Reached_Nodes:
            node.path = []
            
        m.costs = m.getCosts()    
        self.Node = m.List_N[m.start_index]
        self.frontier = []
        self.Visited_Nodes = []
        self.Reached_Nodes = []
        self.expandBreadth()
    
    def UpdateDepth(self):
        for arrow in m.List_A:
            if arrow.color == "red":
               arrow.deleteArrow()
               arrow.color = "black"
               arrow.drawArrow()
        for node in self.Reached_Nodes:
            node.path = []
            
        m.costs = m.getCosts()
        self.Node = m.List_N[m.start_index]
        self.frontier = []
        self.Visited_Nodes = []
        self.Reached_Nodes = []
        self.expandDepth() 
        
        
    def UpdateUniformCost(self):
        for arrow in m.List_A:
            if arrow.color == "red":
               arrow.deleteArrow()
               arrow.color = "black"
               arrow.drawArrow()
        for node in self.Reached_Nodes:
            node.path = []
          
        m.costs = m.getCosts()    
        self.Node = m.List_N[m.start_index]
        self.frontier = []
        self.Visited_Nodes = []
        self.Reached_Nodes = []
        self.expandUniformCost()
    
    def expandBreadth(self):
        print("Curren Node = "+str(self.Node.num)+" frontier = "+str(self.getStringFrontier()))
        if len(self.frontier) == 0 and (len(self.Node.getPlacedArrows()) == 0 or self.Node in self.Visited_Nodes):
            print("Goal cannot be reached *X*")
            return False
        elif self.Node in self.Visited_Nodes:
            self.Node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return self.expandBreadth()
        elif self.Node.color == "gold": # reached goal node
            return self.declareGoal()
        else:
            Next_Nodes = []
            print(self.Node.getStringPlacedArrows())
            for arrow in self.Node.getPlacedArrows():
                nextNode = m.List_N[arrow.nl-1]
                if nextNode not in self.Reached_Nodes:
                    for road in self.Node.path:   
                        nextNode.path.append(road) # add all parent roades to path
                    nextNode.path.append(arrow) # add the current road to path
                Next_Nodes.append(nextNode) # add all next nodes
                if nextNode not in self.Reached_Nodes:
                    self.Reached_Nodes.append(nextNode)
            self.Visited_Nodes.append(self.Node)
            
            Next_Nodes = self.getSortedNodes(Next_Nodes)
            
            List = []
            for i in Next_Nodes:
                List.append(i.num)
            print(List)
            
            for i in Next_Nodes:
                self.frontier.append(i)  # add all next nodes to the frontier
                
            
            
            self.Node = self.frontier[0]   # Update Next Node from the frontier
            self.frontier = self.frontier[1:]
            
        return self.expandBreadth()
            
            
    
    
    def expandDepth(self):
        print("Curren Node = "+str(self.Node.num)+" frontier = "+str(self.getStringFrontier()))
        if len(self.frontier) == 0 and (len(self.Node.getPlacedArrows()) == 0 or self.Node in self.Visited_Nodes):
            print("Goal cannot be reached *X*")
            return False
        elif self.Node in self.Visited_Nodes:
            self.Node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return self.expandDepth()
        elif self.Node.color == "gold": # reached goal node
            return self.declareGoal()
        else:
            Next_Nodes = []
            print(self.Node.getStringPlacedArrows())
            for arrow in self.Node.getPlacedArrows():
                nextNode = m.List_N[arrow.nl-1]
                nextNode.path = []
                for road in self.Node.path:   
                    nextNode.path.append(road) # add all parent roades to path
                nextNode.path.append(arrow) # add the current road to path
                Next_Nodes.append(nextNode) # add all next nodes
                if nextNode not in self.Reached_Nodes:
                    self.Reached_Nodes.append(nextNode)
            self.Visited_Nodes.append(self.Node)
            
            Next_Nodes = self.getSortedNodes(Next_Nodes)
            
            List = []
            for i in Next_Nodes:
                List.append(i.num)
            print(List)
        
            
            for i in Next_Nodes[::-1]:
                self.frontier = [i]+self.frontier # add all next nodes to the frontier
                
            self.Node = self.frontier[0]   # Update Next Node from the frontier
            self.frontier = self.frontier[1:]
            
        return self.expandDepth()
    
    def expandUniformCost(self):
        print("Curren Node = "+str(self.Node.num)+" frontier = "+str(self.getStringFrontier()))
        if len(self.frontier) == 0 and (len(self.Node.getPlacedArrows()) == 0 or self.Node in self.Visited_Nodes):
            print("Goal cannot be reached *X*")
            return False
        elif self.Node in self.Visited_Nodes:
            self.Node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return self.expandUniformCost()
        elif self.Node.color == "gold": # reached goal node
            return self.declareGoal()
        else:
            Next_Nodes = []
            print(self.Node.getStringPlacedArrowsCost())
            for arrow in self.Node.getPlacedArrows():
                nextNode = m.List_N[arrow.nl-1]
                if nextNode not in self.Reached_Nodes or (len(nextNode.path) != 0 and arrow.costValue+self.getNodeCostValue(self.Node) <= nextNode.path[-1].costValue):
                    nextNode.path = []
                    for road in self.Node.path:   
                        nextNode.path.append(road) # add all parent roades to path
                    if len(nextNode.path) != 0:
                        arrow.costValue += nextNode.path[-1].costValue
                    nextNode.path.append(arrow) # add the current road to path
                if len(nextNode.path) != 0:
                    Next_Nodes.append(nextNode) # add all next nodes
                if nextNode not in self.Reached_Nodes:
                    self.Reached_Nodes.append(nextNode)
            self.Visited_Nodes.append(self.Node)
            
            
            List = []
            for i in Next_Nodes:
                List.append(i.num)
            print(List)
            
            
            for i in Next_Nodes:
                self.frontier.append(i)  # add all next nodes to the frontier
            
            self.frontier = self.getSortedNodes(self.frontier)
            self.frontier = self.getSortedCostFrontier()
            
            List = []
            for i in self.frontier:
                List.append(i.num)
            print(List)
            
            self.Node = self.frontier[0]   # Update Next Node from the frontier
            self.frontier = self.frontier[1:]
            
        return self.expandUniformCost()
    
    def declareGoal(self):
        print("Reached Goal ^^")
        m.check = True
        index = 0
        check = True
        while check:
            arrow = self.Node.path[index]
            my_canvas.delete(arrow.Arrow)
            arrow.color = "red"
            arrow.Arrow = my_canvas.create_line(arrow.x1,arrow.y1,arrow.x2,arrow.y2,fill=arrow.color,arrow="last", width=5)
            root.update()
            time.sleep(0.7)
            index += 1
            check = len(self.Node.path) != index and m.check
           
        for arrow in range(len(m.List_A)):
            m.List_A[arrow].costValue = m.costs[arrow]
            
        path = []
        for i in self.Node.path:
            path.append(i.nf)
        path.append(self.Node.num)
        return path
        
    def getNodeCostValue(self, Node):
        if len(Node.path) != 0:
            return Node.path[-1].costValue
        else :
            return 0
    
    def getSortedNodes(self, Nodes):
        List = []
        for letter in m.letters:
            for node in Nodes:
                if letter == node.character:
                    List.append(node)
        return List
        
    def getSortedCostFrontier(self):
        costs = []
        newFrontier = []
        for node in self.frontier:
            costs.append(node.path[-1].costValue)
            
            
        costs.sort()
        print("List of costs = "+str(costs))
        
        for cost in costs:
            for node in self.frontier:
                if cost == node.path[-1].costValue and node not in newFrontier:
                    newFrontier.append(node)
                    
        return newFrontier
    
    def getStringFrontier(self):
        List = []
        for i in self.frontier:
            List.append(i.num)
        return List
    
List_N = []

List_N.append(Node(1, 75, 75))

List_N.append(Node(2, 200, 75))

List_N.append(Node(3, 325, 75))

List_N.append(Node(4, 450, 75))

List_N.append(Node(5, 75, 200))

List_N.append(Node(6, 200, 200))

List_N.append(Node(7, 325, 200))

List_N.append(Node(8, 450, 200))

List_N.append(Node(9, 75, 325))

List_N.append(Node(10, 200, 325))

List_N.append(Node(11, 325, 325))

List_N.append(Node(12, 450, 325))

List_N.append(Node(13, 75, 450))

List_N.append(Node(14, 200, 450))

List_N.append(Node(15, 325, 450))

List_N.append(Node(16, 450, 450))


m = Map(List_N)

frame = Frame(root, bg = "white")
button1 = Button(frame, padx=40, pady=10, text="Shuffle", bg="white", command=m.shuffle, width = 1)
button2 = Button(frame, padx=40, pady=10, text="New Mission", bg="white", command=m.createMission, width = 1)
button3 = Button(frame, padx=40, pady=10, text="Apply Cost", bg="white", command=m.Cost, width = 1)

m.createMission()

Ai = AI(m.List_N[m.start_index])

button4 = Button(frame, padx=40, pady=10, text="Breadth Search", bg="white", command=Ai.UpdateBreadth, width = 1)
button5 = Button(frame, padx=40, pady=10, text="Depth Search", bg="white", command=Ai.UpdateDepth, width = 1)
button6 = Button(frame, padx=40, pady=10, text="Cost Search", bg="white", command=Ai.UpdateUniformCost, width = 1)

    
    
my_canvas.bind('<Button 1>', m.checkClick)

frame.pack()
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=LEFT)
button5.pack(side=LEFT)
button6.pack(side=LEFT)


root.mainloop()