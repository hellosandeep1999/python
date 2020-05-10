"""
Code Challenge
  Filename:
      bibliog.py

    0. Create a Book class which stores the follwing information about the book
       authorlast, authorfirst, title, place, publisher and year
       Also create a instance method write_bib_entry which 
       returns a formatted bibliographic reference for the book
       
    1. Create a two instances of Book in the name of beauty and pynut
        The Evidential Power of Beauty
        Python in a Nutshell
        
    2. How would you print out the author attribute of the pynut instance
    
    3. If you type print beauty.write_bib_entry() at the interpreter, what will happen?
    
    4. How would you change the publication year for the beauty book to"2010"?
    
    5. Create another instance of the Book class as makeup, book of your choice
       Execute the write_bib_entry method for that
       
    6. Add a method make_authoryear to the class definition that will create
       an attribute authoryear and will set that attribute to a string that
       has the last name of the author and then the year in parenthesis.
       The method should not have a return statement.
       
    7. Create an Article class that manages information about articles. 
       It will be very similar to the class definition for Book, except publisher
       and place information will be unneeded and article title, volume number,
       and pages will be needed. Make sure this class also has the methods
       write_bib_entry and make_authoryear 
    
"""
#0. Create a Book class which stores the follwing information about the book
#       authorlast, authorfirst, title, place, publisher and year
#       Also create a instance method write_bib_entry which 
#       returns a formatted bibliographic reference for the book

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

beauty=Book('Christie','Agatha','And Then There Were None','England','	Collins Crime Club','1939')

pynut=Book('de Saint-Exupéry','Antoine','The Little Prince','France','Éditions Gallimard','1943')



# 2.How would you print out the author attribute of the pynut instance

print(pynut.write_bib_entry())

# 3.If you type print beauty.write_bib_entry() at the interpreter, what will happen?

print(beauty.write_bib_entry())

# 4.How would you change the publication year for the beauty book to"2010"?

beauty.year="2010"
print(beauty.write_bib_entry()) 

# 5.Create another instance of the Book class as makeup, book of your choice
#   Execute the write_bib_entry method for that

make_up = Book("Larsson" , "Stieg", "The Girl with the Dragon Tattoo", "Sweden","Norstedts förlag", "2005")
print(make_up.write_bib_entry())


#    6. Add a method make_authoryear to the class definition that will create
#       an attribute authoryear and will set that attribute to a string that
#       has the last name of the author and then the year in parenthesis.
#       The method should not have a return statement.


beauty.make_authoryear()
print(beauty.authoryear)


#    7. Create an Article class that manages information about articles. 
#       It will be very similar to the class definition for Book, except publisher
#       and place information will be unneeded and article title, volume number,
#       and pages will be needed. Make sure this class also has the methods
#       write_bib_entry and make_authoryear 


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
