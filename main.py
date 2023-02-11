from prob_calculator import Hat, experiment


hat = Hat (negro = 6, rojo = 4, verde = 3)
prob = experiment(hat=hat, wait_balls={"rojo":2,"verde":1}, num_balls_drawn=5, num_experiments=994)
print(prob)