def main():
    # Import necessary modules
    from models.population import Population
    import json

    # Load parameters from JSON file
    with open('data/parameters.json') as f:
        parameters = json.load(f)

    # Initialize the population model
    initial_population = parameters['initial_population']
    growth_rate = parameters['growth_rate']
    time_steps = parameters['time_steps']

    population_model = Population(initial_population, growth_rate)

    # Run the simulation
    population_over_time = population_model.simulate(time_steps)

    # Output the results
    for time, population in enumerate(population_over_time):
        print(f"Time: {time}, Population: {population}")

if __name__ == "__main__":
    main()