#!/usr/bin/env python
# coding: utf-8

# In[1]:


def listdivide(numbers, divide=2):
    items = [x for x in numbers if x % divide == 0]
    return len(items)


class ListDivideException(Exception):
    pass


def testlistdivide():
    tests = [([1, 2, 3, 4, 5], 2, 2),
             ([2, 4, 6, 8, 10], 2, 5),
             ([30, 54, 63, 98, 100], 10, 2),
             ([], 2, 0),
             ([1, 2, 3, 4, 5], 1, 5)]

    for items, div, res in tests:
        comp = listdivide(items, div)
        if comp != res:
            raise ListDivideException()


if __name__ == '__main__':
    print testlistdivide()


# In[ ]:




