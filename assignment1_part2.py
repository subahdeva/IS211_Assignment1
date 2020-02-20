#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Book(object):
    """ Book class"""
    def __init__(self, bauthor, btitle):
        self.author = bauthor.strip().title()
        self.title = btitle.strip().title()

    def display(self):
        return '{}, written by {}'.format(self.title, self.author)


if __name__ == '__main__':
    MYBOOK = Book('John Steinbeck', 'Of Mice and Men')
    print MYBOOK.display()


# In[ ]:




