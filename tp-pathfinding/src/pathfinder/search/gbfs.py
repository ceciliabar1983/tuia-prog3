from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node
        
        frontier = PriorityQueueFrontier()
        root.estimated_distance = grid.h(root)
        frontier.add(root, root.estimated_distance)

        while True:
            if frontier.is_empty():
                return NoSolution(reached)
            nodo = frontier.pop()
            if grid.objective_test(nodo.state):
                return Solution(nodo,reached)

            for action in grid.actions(nodo.state):
                succesor = grid.result(nodo.state, action)
                succesor_cost = nodo.cost + grid.individual_cost(nodo.state, action)
                if succesor not in reached or succesor_cost < reached[succesor]:
                    son= Node( "", state=succesor,cost=succesor_cost,parent=nodo,action=action  )

                    reached[succesor] = succesor_cost
                    son.estimated_distance = grid.h(son)
                    frontier.add(son, son.estimated_distance)


        return NoSolution(reached)
