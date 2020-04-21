"""
dit is een opdracht van winc om python te leren
"""

#kosten van het fruit
apple = 3.55
pear = 4.3
kiwi = 12.155

print("fruit added:", apple + pear + kiwi)

fruitAdd = apple + pear + kiwi

fruitAverage = round(fruitAdd/3, 2)

print("fruit avegage:", fruitAverage)

#het aantal fruit
aantalApple = 2
aantalPear = 3
aantalKiwi = 2

fruitTotal = apple*aantalApple + pear*aantalPear + kiwi*aantalKiwi

print("fruit total:", fruitTotal)

kortingPercentage = 50

korting = fruitTotal*(kortingPercentage/100)

print("total met korting", round(korting, 2)) #totaal met korting berekend