import unittest
from src.models.population import Population

class TestPopulation(unittest.TestCase):

    def setUp(self):
        self.population = Population(initial_size=100, growth_rate=0.1)

    def test_growth_rate(self):
        self.assertEqual(self.population.growth_rate, 0.1)

    def test_population_growth(self):
        self.population.update_population(time=1)
        self.assertGreater(self.population.current_size, 100)

    def test_population_density(self):
        self.population.update_population(time=1)
        self.assertEqual(self.population.current_density, self.population.current_size / self.population.area)

if __name__ == '__main__':
    unittest.main()