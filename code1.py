import itertools
def anagram(word):
 tmp=[''.join(i) for i in itertools.permutations(word)]
 return list(set(tmp))
