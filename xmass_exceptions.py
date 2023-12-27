class TooSmallTreeException(Exception):
    def __init__(self, num_of_lines):
        self.message = f"The tree is too small! Try value at least equal to 2. Current value: {num_of_lines}"
        super().__init__(self.message)


class TooSmallIntervalException(Exception):
    def __init__(self, interval):
        self.message = f"The Interval must be one or higher! Current value: {interval}"
        super().__init__(self.message)
