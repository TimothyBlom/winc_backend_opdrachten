#opdracht 1

hans = "Hans van Breukelen"
print(hans)
berry = "Berry van Aerle"
print(berry)
frank = "Frank Rijkaard"
print(frank)
ronald = "Ronald Koeman"
print(ronald)
adri = "Adri van Tiggelen"
print(adri)
gerald = "Gerald Vanenburg"
print(gerald)
arnold = "Arnold Mühren"
print(arnold)
jan = "Jan Wouters"
print(jan)
erwin = "Erwin Koeman"
print(erwin)
marco = "Marco van Basten"
print(marco)
ruud = "Ruud Gullit"
print(ruud)
joop = "Joop Hiele"
print(joop)
wilbent = "Wilbert Suvrijn"
print(wilbent)
johnS = "John van t Schip"
print(johnS)
johnB = "John Bosman"
print(johnB)
wim = "Wim Kieft"
print(wim)

firstScoreTime = 35
secondScoreTime = 54

firstGoal = "the first goal is scored by", hans, "in the", firstScoreTime, "th minute"
secondGoal = "the second goal is scored by", ronald, "in the", secondScoreTime, "th minute"

print(firstGoal)
print(secondGoal)

#opdracht 2

hans_lastname_first = hans[hans.find(' ')+1:] + ', ' + hans[0:hans.find(' ')]

print(hans_lastname_first)

firstName = hans[0:hans.find(' ')]
print(firstName)

lastName = hans[hans.find(' ')+1:]
print(lastName)

lenghtLastName = len(lastName[hans.find("")+1:])
print("lenght last name:", lenghtLastName)

firstLetter = hans[0: 1] + ". " + lastName
print(firstLetter)

firstNameTimesLenght = (len(firstName) * (firstName + "! ")).strip(" ")
                        
print(firstNameTimesLenght)

print(firstNameTimesLenght[-1] == " ")