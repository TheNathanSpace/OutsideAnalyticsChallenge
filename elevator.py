import sys


class Elevator:
    # Constant given in problem description
    FLOOR_TRAVEL_TIME = 10

    def __init__(self, starting_floor: str, to_visit: str):
        """
        Parse command line inputs
        :param starting_floor: The floor to start at (as a string)
        :param to_visit: The list of floors to visit (as a string)
        """
        self.starting_floor: int = int(starting_floor)
        self.current_floor: int = self.starting_floor

        """
        Handle case where an empty list of floors
        to visit is given.
        """
        if to_visit:
            self.to_visit: list[int] = [int(e) for e in to_visit.split(",")]
        else:
            self.to_visit = []

        # We start by visiting the starting floor.
        self.visited: list[int] = [self.current_floor]

        self.cost = 0

    def next_floor(self):
        """
        Pop the next floor, add the cost it takes to travel to it,
        set it as the new current floor, and add it to the list of
        floors visited.
        """
        next_floor = self.to_visit.pop(0)
        self.cost += abs(self.current_floor - next_floor) * self.FLOOR_TRAVEL_TIME
        self.current_floor = next_floor
        self.visited.append(self.current_floor)

    def run(self):
        """
        Continuously go to the next floors. When finished,
        return the cost and list of floors visited.
        """
        while len(self.to_visit) > 0:
            self.next_floor()

        # Must convert floors visited from ints to strings to be able to join
        return f"{self.cost} {','.join([str(e) for e in self.visited])}"


if __name__ == '__main__':
    print(Elevator(sys.argv[1], sys.argv[2]).run())
