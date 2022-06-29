#Objective 3: Challenge
#Word extractor challenge
#program that outputs the sentence: Quick brown fox jumps over the lazy dog. The user can then pick to remove a word
Sentence = ["quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
print(Sentence)
RemoveNumber = int(input("Pick the number of the word you'd like to remove(remember it counts from 0)"))
Sentence[RemoveNumber] = ""
print(Sentence)
                   
