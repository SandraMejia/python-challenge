# PyParagraph

# Sandra Mejia Avendaño

# ------------------------------------------------------------------------------------

import re

wordLengthList = []
sentenceLengthList = []

file = "raw_data/paragraph_2.txt"

with open(file, 'r') as text:
    
    lines = text.read()
    print("\n")
    print("Paragraph to Analyze\n---------------------")
    print(lines)
    print("\n")

    words = re.split("[ -]", lines)
    sentences = re.split("(?<=[.!?]) +", lines)

for word in words:
    wordLengthList.append(len(word))
wordlength = round((sum(wordLengthList)/len(wordLengthList)), 2)

for sentence in sentences:
    wordsInSentence = re.split("[ -]", sentence)
    sentenceLengthList.append(len(wordsInSentence))
sentencelength = round((sum(sentenceLengthList)/len(sentenceLengthList)) , 2)

print("---------------------\nParagraph Analysis\n---------------------")
print(f"Approximate Word Count: {len(words)}")
print(f"Approximate Sentence Count: {len(sentences)}")
print(f"Average Letter Count: {wordlength}")
print(f"Average Sentence Length: {sentencelength}\n")