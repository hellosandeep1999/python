"""
Code Challenge
   Name:
       Bibliography Case Study 
   Filename:
       bibliography.py

Since we programmed Book and Article with write bib entry methods, let’s take advantage of that. 
Write a method write_bibliog_alpha for the Bibliography class we just created that actually writes out a bibliography
(as a string) with blank lines between the entries, with the entries sorted alphabetically by author name. 
The bibliography should be returned using a return statement in the method. 

Some hints:
    Elements of a list do not have to all have the same type.
    
    for loops do not only loop through lists of numbers but through any iterable. 
    
    This includes lists of any sort, including lists of objects 
    (such as Book and Article instances.
    
    Strings are immutable, so you cannot append to an existing string. Instead, do a reassignment combined with concatenation (i.e., a=a+b).

    To initialize a string, in order to grow it in concatenation steps such
    as in a for loop, start by setting the string variable to an empty string
    (which is just ’’).

"""  

import operator

class Book:
    def __init__(self, authorlast, authorfirst, title, place, publisher, year):
        self.authorlast = authorlast
        self.authorfirst = authorfirst
        self.title = title
        self.place = place
        self.publisher = publisher
        self.year = year
    
    def write_bib_entry(self):
        return self.authorlast \
               + ', ' + self.authorfirst \
               + ', ' + self.title + ', ' + self.place \
               + ':  ' + self.publisher + ', ' \
               + self.year + '.'
    
    def make_authoryear(self):
        self.authoryear=self.authorlast+'('+str(self.year)+')'


class Article(object):
    def __init__(self, authorlast, authorfirst, title, volume, pages, year):
        self.authorlast = authorlast
        self.authorfirst = authorfirst
        self.title = title
        self.volume = volume
        self.pages = pages
        self.year = year
    
    def make_authoyear(self):
        self.authoyear= self.authorlast + '('+ self.year +' )'
    
    def write_bib_entry(self):
        return self.authorlast + ', ' + self.authorfirst \
                               + ', ' + self.title + ', ' + self.volume \
                               + ':  ' + self.pages + ', ' \
                               + self.year + '.'        

     
class Bibliography():
    def __init__(self,entrieslist):
        self.entrieslist = entrieslist
        
    def sort_entries_alpha(self):
        tmp = sorted(self.entrieslist , key = operator.attrgetter('authorlast','authorfirst'))
        self.entrieslist= tmp
        del tmp
    def write_bibliog_alpha(self):
        self.sort_entries_alpha()
        output = ''
        for each in self.entrieslist:
            output = output + each.write_bib_entry() +'\n'
        return output[0:]
    
            
beauty=Book('Christie','Agatha','And Then There Were None','England','	Collins Crime Club','1939')

pynut=Book('de Saint-Exupéry','Antoine','The Little Prince','France','Éditions Gallimard','1943')

nature = Book( "Smith", "Jane", "My Nobel prize-winning paper","481", "234-236", "2012" )

science = Article( "Doe", "Samuel", "My almost Nobel prize-winning paper","500", "36-38", "2011" )

noname = Article( "Doe", "John", "My no-one-has-heard-of paper","49", "34-36", "2005" )            

mybib = Bibliography([beauty, pynut,nature,science,noname])

if __name__ == '__main__':
    print ("Entries list Befor sorting : \n",[i.authorlast for i in mybib.entrieslist])
    mybib.sort_entries_alpha()
    print("Entries list after sorting : \n",[i.authorlast for i in mybib.entrieslist])
    print("Writting Bibliography: \n\n",mybib.write_bibliog_alpha())