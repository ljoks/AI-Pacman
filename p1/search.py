# Lawrence Oks
# CAP 5636 Boloni

# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    closedSet = set() #closed set where visited nodes go
    fringe = util.Stack() #storing current nodes on the fringe, using Stack because DFS fringe is LIFO
    
    #first node on the fringe is always the start state
    fringe.push( (problem.getStartState(), []) ) #item pushed to the stack (node, [path to node])
    
    #loop through stack, popping until we find a goal node, pushing otherwise
    while True:
        popped = fringe.pop() #pop top object from the fringe (containing (node, [path to node]))
        node, path = popped[0], popped[1] #assign current node and its path to local vars
        #if this node is the goal state, success! we have found the goal, DFS complete
        if problem.isGoalState(node): 
            break
        #else we will visit its successors
        else:
            if node not in closedSet: #nodes in the closed set do not get visited
                #visiting node
                closedSet.add(node) #add to closedSet so we do not visit it again
                #get each successor of current node and add it to the fringe
                for successor in problem.getSuccessors(node):
                    fringe.push( (successor[0], path + [successor[1]]) ) 

    #finally, return path when goal state is found
    return path

    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #code almost identical, except using a queue instead of a stack for BFS

    closedSet = set() #closed set where visited nodes go
    fringe = util.Queue() #storing current nodes on the fringe, using Queue because BFS fringe is FIFO
    #first node on the fringe is always the start state
    fringe.push( (problem.getStartState(), []) ) #item pushed to the queue (node, [path to node])
    
    #loop through stack, popping until we find a goal node, pushing otherwise
    while True:
        popped = fringe.pop() #pop top object from the fringe (containing (node, [path to node]))
        node, path = popped[0], popped[1] #assign current node and its path to local vars
        #if this node is the goal state, success! we have found the goal, DFS complete
        if problem.isGoalState(node): 
            break
        #else we will visit its successors
        else:
            if node not in closedSet: #nodes in the closed set do not get visited
                #visiting node
                closedSet.add(node) #add to closedSet so we do not visit it again
                #get each successor of current node and add it to the fringe
                for successor in problem.getSuccessors(node):
                    fringe.push( (successor[0], path + [successor[1]]) ) 

    #finally, return path when goal state is found
    return path

    
    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #another similar code structure, but this search will use a priority queue for the fringe
    #additionally we will add a cost to each node by changing the item structure to 
    #     ( node, [path to node], cost up to this node )

    closedSet = set() #closed set where visited nodes go
    fringe = util.PriorityQueue() #storing current nodes on the fringe, using Queue because BFS fringe is FIFO
    #first node on the fringe is always the start state
    fringe.push( (problem.getStartState(), [], 0), 0) #item pushed to the queue (node, [path to node], cost), cost
    
    #loop through stack, popping until we find a goal node, pushing otherwise
    while True:
        popped = fringe.pop() #pop top object from the fringe (containing (node, [path to node]))
        node, path, cost = popped[0], popped[1], popped[2] #assign current node and its path AND its cost to local vars
        #if this node is the goal state, success! we have found the goal, DFS complete
        if problem.isGoalState(node): 
            break
        #else we will visit its successors
        else:
            if node not in closedSet: #nodes in the closed set do not get visited
                #visiting node
                closedSet.add(node) #add to closedSet so we do not visit it again
                #get each successor of current node and add it to the fringe
                for successor in problem.getSuccessors(node):
                    #before pushing to fringe we must now add a backwards cumulitive cost to the node before pushing
                    backCost = cost + successor[2] #adding cost of this successor to cumulative cost up to this point
                    fringe.push( (successor[0], path + [successor[1]], backCost), backCost ) 

    #finally, return path when goal state is found
    return path


    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # A* search should look like uniform cost except when we will decide priority in the queue by
    # the backwards cumulitive cost + the heuristic of the node
    
    closedSet = set() #closed set where visited nodes go
    fringe = util.PriorityQueue() #storing current nodes on the fringe, using Queue because BFS fringe is FIFO
    #first node on the fringe is always the start state
    fringe.push( (problem.getStartState(), [], 0), heuristic(problem.getStartState(), problem)) #item pushed to the queue (node, [path to node], cost), cost + heuristic
    
    #loop through stack, popping until we find a goal node, pushing otherwise
    while True:
        popped = fringe.pop() #pop top object from the fringe (containing (node, [path to node]))
        node, path, cost = popped[0], popped[1], popped[2] #assign current node and its path AND its cost to local vars
        #if this node is the goal state, success! we have found the goal, DFS complete
        if problem.isGoalState(node): 
            break
        #else we will visit its successors
        else:
            if node not in closedSet: #nodes in the closed set do not get visited
                #visiting node
                closedSet.add(node) #add to closedSet so we do not visit it again
                #get each successor of current node and add it to the fringe
                for successor in problem.getSuccessors(node):
                    #before pushing to fringe we must now add a backwards cumulitive cost to the node before pushing
                    backCost = cost + successor[2] #adding cost of this successor to cumulative cost up to this point
                    fringe.push( (successor[0], path + [successor[1]], backCost), backCost + heuristic(successor[0], problem) ) 

    #finally, return path when goal state is found
    return path



    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
