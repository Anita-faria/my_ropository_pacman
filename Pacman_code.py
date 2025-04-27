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



def breadthFirstSearch(problem):
    from util import Queue

    currState = problem.getStartState()
    if problem.isGoalState(currState):
        return []
    
    frontier = Queue()
    frontier.push((currState, []))  # Push the start state and an empty path
    explored = set()  # Set to keep track of explored states

    while not frontier.isEmpty():
        currState, currPath = frontier.pop()  # Pop the state and path from the queue

        if problem.isGoalState(currState):
            return currPath  # Return the path if the goal state is reached

        explored.add(currState)  # Mark the current state as explored

        for successor, action, stepCost in problem.getSuccessors(currState):
            if successor not in explored and not any(successor == f[0] for f in frontier.list):
                # Push the successor state and the updated path to the frontier
                frontier.push((successor, currPath + [action]))

    return []  # Return an empty list if no solution is found

def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    from util import Stack


    frontier = Stack()
    frontier.push((problem.getStartState(), []))
    explored = set()


    while not frontier.isEmpty():
        state, path = frontier.pop()


        if problem.isGoalState(state):
            return path


        if state not in explored:
            explored.add(state)
            for successor, action, cost in problem.getSuccessors(state):
                if successor not in explored:
                    frontier.push((successor, path + [action]))


    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    from util import PriorityQueue


    frontier = PriorityQueue()
    frontier.push((problem.getStartState(), []), 0)
    explored = set()


    while not frontier.isEmpty():
        state, path = frontier.pop()


        if problem.isGoalState(state):
            return path


        if state not in explored:
            explored.add(state)
            for successor, action, cost in problem.getSuccessors(state):
                if successor not in explored:
                    newPath = path + [action]
                    newCost = problem.getCostOfActions(newPath)
                    frontier.push((successor, newPath), newCost)


    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    from util import PriorityQueue


    frontier = PriorityQueue()
    startState = problem.getStartState()
    frontier.push((startState, []), heuristic(startState, problem))
    explored = set()


    while not frontier.isEmpty():
        state, path = frontier.pop()


        if problem.isGoalState(state):
            return path


        if state not in explored:
            explored.add(state)
            for successor, action, cost in problem.getSuccessors(state):
                if successor not in explored:
                    newPath = path + [action]
                    newCost = problem.getCostOfActions(newPath) + heuristic(successor, problem)
                    frontier.push((successor, newPath), newCost)


    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
