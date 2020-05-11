"""
Code Challenge 2
  Filename:
      bibliog.py
    
    0. Create a Book class which stores the following information about the book
       authorlast, authorfirst, title, place, publisher and year
       Also create a instance method write_bib_entry which 
       returns a formatted bibliographic reference for the book
       
    1. Create a two instances of Book in the name of beauty and pynut
        The Evidential Power of Beauty
        Python in a Nutshell
        
    2. How would you print out the author attribute of the pynut instance
    
    3. If you type print beauty.write_bib_entry() at the interpreter, 
       what will happen?
    
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

# This class provides a template for holding and manipulating information about a book. 
# returns a formatted bibliographic reference for the book.

class Book(object):
    
    # authorlast, authorfirst, title, place, publisher and year
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
  
                                                          
# Create a few instances of Book classes:
beauty = Book( "Dubay", "Thomas", "The Evidential Power of Beauty", "San Francisco", "Ignatius Press", "1999", )
pynut  = Book( "Martelli", "Alex", "Python in a Nutshell", "Sebastopol, CA", "O'Reilly Media, Inc.", "2003" )


#How would you print out the author attribute of the pynut instance
print(Book.write_bib_entry(pynut))

                            
#If you type print beauty.write_bib_entry() at the interpreter, what will happen?
print(beauty.write_bib_entry())


#How would you change the publication year for the beauty book to"2010"?
beauty.year="2010"
print(beauty.write_bib_entry())


#Create another instance of the Book class as makeup, book of your choice
# Execute the write_bib_entry method for that
makeup = Book("Doe" , "John", "Good Book", "Chicago","Me Press", "2012")
print(makeup.write_bib_entry())



#Add a method make_authoryear to the class definition that will create an attribute authoryear 
#and will set that attribute to a string that has the last name of the author and then the year
#in parenthesis. The method should not have a return statement.

class Book(object):
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
        self.authoryear = self.authorlast + '('+ self.year +' )'

makeup = Book("Doe" , "John", "Good Book", "Chicago","Me Press", "2012")

print(makeup.make_authoryear()) 
# It will return None becuase make_authoyear has not return attributes
print(makeup.authoryear)


#Create an Article class that manages information about articles. 
#It will be very similar to the class definition for Book, except publisher
#and place information will be unneeded and article title, volume number,
#and pages will be needed. Make sure this class also has the methods
#write_bib_entry and make_authoryear.
       

class Article(object):
    def __init__(self, authorlast, authorfirst, title, volume, pages, year):
        self.authorlast = authorlast
        self.authorfirst = authorfirst
        self.title = title
        self.volume = volume
        self.pages = pages
        self.year = year
        
    def make_authoryear(self):
        self.authoyear= self.authorlast + '('+ self.year +' )'
        
    def write_bib_entry(self):
        return self.authorlast + ', ' + self.authorfirst \
                               + ', ' + self.title + ', ' + self.volume \
                               + ':  ' + self.pages + ', ' \
                               + self.year + '.'
