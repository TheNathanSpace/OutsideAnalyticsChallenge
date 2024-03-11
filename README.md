# Outside Analytics Coding Challenge

My solution to the Outside Analytics Spring 2024 coding challenge.

## Execution

The program is all contained in `elevator.py` and just depends on the Python stdlib.
It was written for Python 3.10.4 but should work for any modern Python version.

Some simple test cases are contained in `test_elevator.py`.

```shell
# Run on single input
python elevator.py [starting floor] [floors to visit]

# Run test cases
python test_elevator.py
```

Output is in the format

```
[total travel time] [floors visited in order]
```

## Details

Based on the given problem description, the `starting floor` and `floors to visit` inputs provide the floors to visit in
the order to be visited; that is, they should not be reordered for more efficiency. So, the problem is simply to, given
its path, calculate its travel time.

The list of `floors to visit` is treated like a queue, traveling to the floor at the front of the queue. We simply
iterate over the queue, adding the cost of moving from the current floor to the next floor until all floors have been
visited.