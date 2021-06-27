# Monty hall problem

This code runs an experimental verification of the [Monty Hall brain teaser](https://en.wikipedia.org/wiki/Monty_Hall_problem), which is rephrased below:

*Suppose you're on a game show, and you're given the choice of three  doors: Behind one door is a car; behind the others, goats. You pick a  door, say No. 1, and the host, who knows what's behind the doors, opens  another door, say No. 3, which has a goat. He then says to you, "Do you  want to pick door No. 2?" Is it to your advantage to switch your choice?*

The intuitive (but incorrect) answer is that it makes no difference whether you switch or not: the odds of getting a car are 50/50.

The actual answer is that you should always switch; when you switch, you have a 2/3 chance of getting the car, and when you don't you have a 1/3 chance of getting the car.

![](Result.png)



## But why!!?

Remember the host is not choosing their door randomly; they know more about the situation then the contestant, and **always** choose a door with a goat, and **never** choose the door that the contestant chose. This means the door they didn't change is more likely than not to have a car.

Consider the three initial guesses below. If you DID choose a car, then by switching your guess you will always lose. If you didn't choose a car, by switching your guess you will always win. The key thing to note is that you are twice as likely to have initially chosen a goat as a car; therefore it is always in your interests to switch.

| Initial guess | Odds of getting car if you switch | Odds of getting car if you don't switch |
| ------------- | --------------------------------- | --------------------------------------- |
| Car           | 0                                 | 1                                       |
| Goat          | 1                                 | 0                                       |
| Goat          | 1                                 | 0                                       |

## how to use:

Basically just press run MontyHall.py to reproduce the figure above. The only non standard library is matplotlib for plotting. 





