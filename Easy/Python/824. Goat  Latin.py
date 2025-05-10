def toGoatLatin(sentence):
    sentence = sentence.split()
    output = ""
    for i in range(len(sentence)):
        if sentence[i][0] == 'a' or sentence[i][0] == 'e' or sentence[i][0] == 'i' or sentence[i][0] == 'o' or sentence[i][0] == 'u':
            sentence[i]+="ma"
        else:
            sentence[i] +=  sentence[i][0]
            sentence[i]+="ma"
            sentence[i]=sentence[i].replace(sentence[i][0],'',1)
            
        sentence[i] += "a"*(i+1)
        if i != len(sentence)-1:
            sentence[i]+=" "
        output+=sentence[i]

    return output

#Example 1 
print(toGoatLatin("I speak Goat Latin") )