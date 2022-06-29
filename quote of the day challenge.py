#Objective 10: Challenges
#Quote of the day challenges
quote = open("quote.txt","r")
end = False
quotebank = []
line = quote.readline()
while line != "":
    quotebank.append(line)
    line = quote.readline()
import random
dayquote = random.choice(quotebank)
print(dayquote)
quote.close()
