#Dictionaries - mutable SYNTAX: {'myVar': 'Hello'}
# .update({'a':'d'}) overrides old value

#print(dictionary.items()) prints all items


#lists SYNTAX ['here','is','a','list']

myDictionary = {
    'a': '65',
    'b': '98'
}

myList = ['this', 'is', 'my', 'list']

print(myList[1:3])              #[1,2)
print(myList[0:4:2])            # [0,4) skip every other

#list.append('element')

#list.extend(['multiple','items'])

#TUPLES

#basically a list that you cannot change

#in general, tuple for heterogenous data, good for function returns

myTuple = ('hello', 'this', 2)

print(myTuple)


#functionssssss

def squares_until(upper_limit):

    squares = []

    for n in range(upper_limit/2):
        n_squared = n**2

        if n_squared < upper_limit:
            squares.append(n_squared)
        else:
            break

    return squares


print(squares_until(50))


#EXCEPTIONS

try:
    {}['a key that is not in the dictionary']
except KeyError:
    print('Caught a KeyError!')


#CLASSES

class Adventurer(object):
    def __init__(self, name, health, experience, level, adventurer_type):
        self.name = name
        self.health = health
        self.experience = experience
        self.level = level
        self.adventurer_type = adventurer_type

    def format(self):
        format_str = ('Our adventurer\'s name is {0}')
        return format_str.format(self.name)

myAdventurer = Adventurer('Brian', 100, 'none', 100,'Rogue')
print(myAdventurer.format())
