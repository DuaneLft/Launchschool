# Which of the following values can't be used as a key in a dict object and why?

'cat'                           
(3, 1, 4, 1, 5, 9, 2)           
['a', 'b']                      # This list can not be used as a key because it is mutable
{'a': 1, 'b': 2}                # This dictionary can not be used as a key because it's mutable
range(5)
{1, 4, 9, 16, 25}               # This set can not be used as a key since it's not a frozenset and therefore mutable
3
0.0
frozenset({1, 4, 9, 16, 25})