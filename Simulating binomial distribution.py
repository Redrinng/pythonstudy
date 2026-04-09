# Simulating binomial distribution


# To use the random.binomial() method, we have to tell it how many trials we want to simulate (n) 
# and the probability of ‘success’ in a single trial (p), 
# and how many experiments to run.

# In the example below, there was 1 flip per trial (n), 
# the probability (p) of getting ‘success’ was .5 (the coin is fair), 
# and we conducted the experiment 2,000 times (size).

import numpy

print(numpy.random.binomial(n = 1, p = 0.5, size=2000))

# The output from our simulation is a list of 0’s and 1’s. This is the number of successes in each experiment. 
# In this case, since we are simulating a single trial, 1 would mean the outcome of the trial 
# was a success and 0 would mean the outcome was a failure.

# If we wanted to do 10 flips per experiment, the result would be a list of 
# numbers from 0 to 10 representing the number of successes in each experiment.

print(numpy.random.binomial(n=10, p=0.5, size=2000))

