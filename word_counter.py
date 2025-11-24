sentence = input("Type your sentence")
def count_words(sentence):
    words=sentence.split()
    word_count={}
    for word in words:
        word_count[word]=word_count.get(word,0)+1
    return word_count

#call function and print result
result = count_words(sentence)
print(result)
    #for word, count in word_count.items():
        #print(f"{word}: {count}")
