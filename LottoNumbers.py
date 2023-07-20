class LottoNumbers:
    def __init__(self, numbers, powerBall):
        self.numbers = numbers
        self.numbers.sort()
        
        self.powerBall = powerBall

    def ShowNumbers(self):
        print(f"This tickets numbers are {','.join(map(str, self.numbers))} with a powerball of {self.powerBall}.")
        
    def Match(self, winningNumbers):
        powerBall = winningNumbers.powerBall == self.powerBall
        powerBallString = "no"
        matchCount = 0

        for num in winningNumbers.numbers:
            matchCount += self.numbers.count(num)

        if (powerBall):
            powerBallString = "a"

        self.matchCount = matchCount
        self.hasPowerBall = powerBall
            
        print(f"The ticket {','.join(map(str, self.numbers))} with power ball {self.powerBall} has {matchCount} matches with {powerBallString} powerball.")

lottoNumbers = [
    LottoNumbers([3,16,19,28,55],16),
    LottoNumbers([35,45,48,59,64],13),
    LottoNumbers([5,18,31,38,53],12),
    LottoNumbers([2,19,20,45,49],26),
    LottoNumbers([8,23,30,55,59],20),
    LottoNumbers([4,17,21,62,64],21),
    LottoNumbers([29,33,35,38,66],2),
    LottoNumbers([2,12,14,63,67],4),
    LottoNumbers([24,45,46,62,64],6),
    LottoNumbers([27,37,39,47,52],2),
    LottoNumbers([15,53,54,59,64],13),
    LottoNumbers([1,5,18,42,56],6),
    LottoNumbers([3,8,23,42,64],2),
    LottoNumbers([11,13,23,41,65],7),
    LottoNumbers([20,25,41,48,65],5),
    LottoNumbers([27,35,46,61,66],3),
    LottoNumbers([5,26,32,43,62],11),
    LottoNumbers([6,17,22,31,37],7),
    LottoNumbers([9,15,24,35,67],25),
    LottoNumbers([25,33,40,43,54],26)
    ]

# Winning numbers from PowerBall 07/19/2023
winningNumbers = LottoNumbers([7,13,10,24,11],24)

for index,tickets in enumerate(lottoNumbers):
    tickets.Match(winningNumbers)
