from random import choice


class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.values = {'x_values': [0], 'y_values': [0]}

        # Direction options
        self.direction = [1, -1]
        # Distance options
        self.distance = [0, 1, 2, 3, 4]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.values['x_values']) < self.num_points:

            # Decide which direction to go and how far to go in that direction.
            x_step = self._get_step()
            y_step = self._get_step()

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the new position.
            x = self.values['x_values'][-1] + x_step
            y = self.values['y_values'][-1] + y_step

            self.values['x_values'].append(x)
            self.values['y_values'].append(y)

    def _get_step(self):
        dir = choice(self.direction)
        dis = choice(self.distance)
        return (dir * dis)
