def count_vegetables(string):
    count_dictionary = {}
    allowed_words = ["cabbage", "carrot", "celery", "cucumber", "mushroom", "onion", "pepper", "potato", "tofu", "turnip"]

    for word in string.split(' '):
        word = word.strip()
        if len(word) <= 0 or word not in allowed_words:
            pass
        elif word in count_dictionary:
            count_dictionary[word] += 1
        else:
            count_dictionary[word] = 1

    return sorted(zip(count_dictionary.values(),count_dictionary.keys()), key=lambda x: (x[0], x[1]), reverse=True)

print count_vegetables('potato tofu cucumber cabbage turnip pepper onion carrot celery mushroom potato tofu cucumber cabbage')
s2 = '''mushroom chopsticks chopsticks turnip mushroom carrot mushroom cabbage mushroom carrot tofu pepper cabbage potato cucumber
 mushroom mushroom mushroom potato turnip chopsticks cabbage celery celery turnip pepper chopsticks potato potato onion cabbage cucumber
 onion pepper onion cabbage potato tofu carrot cabbage cabbage turnip mushroom cabbage cabbage cucumber cabbage chopsticks turnip pepper
 onion pepper onion mushroom turnip carrot carrot tofu onion tofu chopsticks chopsticks chopsticks mushroom cucumber chopsticks carrot
 potato cabbage cabbage carrot mushroom chopsticks mushroom celery turnip onion carrot turnip cucumber carrot potato mushroom turnip
 mushroom cabbage tofu turnip turnip turnip mushroom tofu potato pepper turnip potato turnip celery carrot turnip'''
print count_vegetables(s2)