# Source: http://www.codewars.com/kata/5389864ec72ce03383000484/train/python

# Downside to refactored method is that it calculates al of the possibilities before returning
def refactored_autocomplete(input, dictionary):
    input = filter(lambda i: i.isalpha(), input.lower())
    return [w for w in dictionary if w.lower().startswith(input)][:5]



def original_autocomplete(input, dictionary):
    input = ''.join(c for c in input if c.isalpha()).upper()
    result = []
    input_len = len(input)
    for word in dictionary:
        if(len(result) >= 5): break
        cleaned_word = ''.join(c for c in word if c.isalpha()).upper()
        print (input[0:input_len], cleaned_word[0:input_len])
        if(input[0:input_len].upper() == cleaned_word[0:input_len]):
            result.append(word)
    return result

