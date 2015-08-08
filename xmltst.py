
from xml.dom import minidom

doc = minidom.Document()
doc.appendChild(doc.createComment("This is a simple xml document."))
booklist = doc.createElement("booklist")
doc.appendChild(booklist)

def addBook(newbook):
    book = doc.createElement("book")
    book.setAttribute("id", newbook['id'])

    title = doc.createElement("title");
    title.appendChild(doc.createTextNode(newbook['title']))
    book.appendChild(title)

    author = doc.createElement("author")
    name = doc.createElement("name")
    firstname = doc.createElement("firstname")
    firstname.appendChild(doc.createTextNode(newbook['firstname']))
    lastname = doc.createElement("lastname")
    lastname.appendChild(doc.createTextNode(newbook['lastname']))
    name.appendChild(firstname)
    name.appendChild(lastname)
    author.appendChild(name)
    book.appendChild(author)

    pubdate = doc.createElement('pubdate')
    pubdate.appendChild(doc.createTextNode(newbook['pubdate']))
    book.appendChild(pubdate)

    booklist.appendChild(book)

addBook({"id":"1001", "title":"An apple", "firstname":"lin", "lastname":"yong", "pubdate":"20150805"});

f = file("book.xml", "w")
doc.writexml(f)
f.close()
