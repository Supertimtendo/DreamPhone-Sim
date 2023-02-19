class guys:
    name: str
    phoneNo: str
    hangout: str
    clothing: str
    recreation: str
    boy_names = ['dave', 'george', 'dale', 'alan', 'james', 'phil', 'bruce', 'tyler', 'jamal', 'gary', 'dan', 'spencer',
                 'mark', 'jason', 'steve',
                 'john', 'paul', 'tony', 'wayne', 'mike', 'scott', 'bob', 'carlos', 'matt']
    locations = ['crosstown_mall', 'snack_shop', 'reel_movies', 'woodland_park', 'high_tide_beach', 'jims_gym']

    recreations = ['baseball', 'skateboarding', 'volleyball', 'surfing', 'basketball',
                   'tennis', 'ice_cream', 'cookies', 'hot_dogs', 'pizza', 'candy', 'popcorn', 'hat', 'tie',
                   'blue_jeans', 'jacket', 'glasses', 'anything_yellow']

    boy_nums = ['5551111', '5551233', '5554566', '5557899', '5552588', '5553333', '5553699', '5551477', '5559877',
                '5553211', '5557777', '5556544', '5558522', '5557411', '5559999',
                '5559633', '5555515', '5552442', '5553535', '5552226', '5555599', '5554884', '5556668', '5557557']
    def __init__(self, name, phoneNo, hangout, clothing, recreation):
        self.name = name
        self.phoneNo = phoneNo
        self.hangout = hangout
        self.clothing = clothing
        self.recreation = recreation

    def createGuys(self, names, nums, locs, rec) -> list:
        y=0
        guyslist = []
        if len(names)==len(nums):
            for x in names:
                if x%4:
                    y+=1
                guyslist[x] = guys(self, names[x], nums[x],locs[y],)
        pass

# reworking the game logic to work with objects -
# define guys as a class, populate boys as objects with all the appropriate attributes. for the clue reveal system
# we need to initialize the game with an RNG of each boy what clue they are going to reveal about the chosen boy,
# all clues will be negative deductions except for the few that are positive, which results in the "haha i'm not telling"
# reveal (when the clue is a positive trait, i.e. they "ARE" at the mall, the game will turn this into a non-reveal).
