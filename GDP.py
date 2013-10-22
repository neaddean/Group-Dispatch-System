defaultPeopleArray = []  ## [time][floor][dest][freq]

class GDP():
    def __init__(self, 
                 floorNum = 9,
                 ##primary floor?
                 elevatorNum = 2,
                 dTime = .11, 
                 peopleFreqArray = defaultPeopleArray, 
                 filename = 'default',
                 doorDelay = 5,
                 floorDelay = 2):
################# Assign Default Parameters #####################
        self.floorNum = floorNum
        self.elevatorNum = elevatorNum
        self.dTime = dTime
        self.peopleFreqArray = peopleFreqArray
        if (filename == default):
            self.filename = "GDP_result_" + str(floorNum) + "_" + str(elevatorNum)
        else:
            self.filename = filename
        self.doorDelay = doorDelay
        self.floorDelay = floorDelay

        self.timePassed = 0
