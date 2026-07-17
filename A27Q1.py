'''
class : BookStore

class veriable : NoOfBooks = 0

two instance veriable : Name (Book Name) , Author (Book Autho)

constructor veriable : __init__ accept Name and Author and initializase instance veriables

Inside constructor increment the class varible NoOfBooks by 1 whenever a new object is created

implement an instance method :
Dispaly() <Book Name> by <Author> No of Books : <NoOfBooks>
'''

class BookStore:

    NoOfBooks = 0
    

    def __init__(self,Name, Author):

        BookStore.NoOfBooks +=1

        self.Name = Name

        self.Author = Author

        
    
    def Display(self):

        print(f"{self.Name} by {self.Author} No of Books: {BookStore.NoOfBooks}")

obj1 = BookStore("Linux System Programming", "Robert Love")
obj1.Display()

obj2 = BookStore("C Programming","Dennis Ritchie")
obj2.Display()

