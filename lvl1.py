#Word Replacement Game
sentence = input("\nEnter a sentence of choice: ")
print(f"Interesting, {sentence}")

word1= input(f"Enter a word you would remove in the sentence '{sentence}': ")
word2 = input(f"Enter the new word you want to replace with '{word1}' : ")
print(sentence.replace(word1,word2))
