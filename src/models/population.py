class Population:
    def __init__(self, initial_size, growth_rate):
        self.size = initial_size
        self.growth_rate = growth_rate

    def simulate(self, time_steps):
        """Simulates population growth over specified time steps.
        
        Args:
            time_steps (int): Number of time steps to simulate
            
        Returns:
            list: Population sizes at each time step
        """
        population_over_time = [self.size]
        
        for _ in range(time_steps):
            new_size = self.size * (1 + self.growth_rate)
            self.size = new_size
            population_over_time.append(new_size)
            
        return population_over_time