from random import randint
from matplotlib import pyplot as plt

class MontyHall:

    def __init__(self):
        # this method is executed every time an instance of this class is created (see the if __name__ == '__main__' block
        # at the bottom of this code

        self.Nexperiments = 1000  # how many times to repeat experiment

        # initialise variables to keep track of what happens
        self.GotCar = 0
        self.GotCamel = 0

        # set up some axes for plotting on later
        fig, (self.axs1, self.axs2) = plt.subplots(ncols=2, nrows=1, figsize=(10, 5))

        # run experiments with and without switching guess and plot the results:
        self.SwitchGuess = True
        self.RunExperiment()
        self.PlotResults()
        self.SwitchGuess = False
        self.RunExperiment()
        self.PlotResults()
        plt.show()

    def SetUpDoors(self):
        """
        Set up three doors, one of which randomly has a car behind it and the other two have camels
        :return:
        """
        # start by putting a camel behind every door:
        self.Doors = ['camel', 'camel', 'camel']
        # now randomy overwrite one of these
        door_ind = randint(0, 2)  # random number between 0 and 2
        self.Doors[door_ind] = 'car'

    def RunExperiment(self):
        """
        Run through the problem self.Nexperiments times, keeping track of whether the contestant got a car or a
        camel each time. The parameter to switch guesses (or not) is set in the __init__ function.
        :return:
        """

        for i in range(self.Nexperiments):
            self.SetUpDoors()  # each time set the doors up differently
            random_guess_ind = randint(0, 2)

            # now we need to generate the ind for the door the host will open.
            # which must 1) not be the same as random_guess_ind, and 2) not have a house behind it
            # Im just going to brute force this by making guesses until I get a valid one:
            while True:
                host_opens_door_ind = randint(0, 2)
                if (not host_opens_door_ind == random_guess_ind) and self.Doors[host_opens_door_ind] == 'camel':
                    # then we have found a valid door to open, and we can quit this loop
                    break

            # now the player is presented with a choice: would they like to switch their guess or not?
            if self.SwitchGuess:
                # we will switch our guess to the remaining door.
                # generate the last indice (the one no one has picked yet)
                switched_guess_ind = [a for a in [0,1,2] if not a in [random_guess_ind,host_opens_door_ind]]
                switched_guess_ind = switched_guess_ind[0]
                Result = self.Doors[switched_guess_ind]
            else:
                Result = self.Doors[random_guess_ind]

            # keep track of the results for later analysis
            if Result == 'camel':
                self.GotCamel += 1
            else:  # they got a car
                self.GotCar += 1

        # convert number of times they got something percentages:
        self.GotCar = self.GotCar * 100 / self.Nexperiments
        self.GotCamel = self.GotCamel * 100 / self.Nexperiments

    def PlotResults(self):
        """
        Create a simple bar plot of the results
        :return:
        """

        if self.SwitchGuess == True:
            self.axs1.bar(['Got car', 'got camel'],[self.GotCar,self.GotCamel])
            self.axs1.set_ylabel("%")
            self.axs1.set_title('Always switch guess')
        else:
            self.axs2.bar([0, 1], [self.GotCar, self.GotCamel])
            self.axs2.bar(['Got car', 'got camel'],[self.GotCar,self.GotCamel])
            self.axs2.set_ylabel("%")
            self.axs2.set_title('Never switch guess')

if __name__ == '__main__':
    MontyHall()







