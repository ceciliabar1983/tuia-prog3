from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize expanded with the empty dictionary
        expanded = dict()

        if grid.objective_test(root.state):
            return Solution(root, expanded)
        
        

        # Initialize frontier with the root node
        
        frontier = StackFrontier()
        frontier.add(root)

        while True:
            if frontier.is_empty():
                return NoSolution(expanded)
            nodo = frontier.remove()
            if nodo.state in expanded:
                continue
            expanded[nodo.state] = True

            for action in grid.actions(nodo.state):
                succesor = grid.result(nodo.state, action)
                if succesor not in expanded:
                    son = Node( "", state=succesor, cost=nodo.cost + grid.individual_cost(nodo.state, action), parent=nodo, action=action)
                    if grid.objective_test(succesor):
                        return Solution(son,expanded)
                    frontier.add(son)

        return NoSolution(expanded)
