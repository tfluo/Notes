```python
PASSWORD = 'xxxxxxx'
SERVER = 'xxxxx'
MAILBOX = 'xxxxxx\\xxxxxx'
PRINCIPAL = 'Name for pricipal'
FONT_SIZE = 11
SELF_IP = '1.1.1.1'

BODY_VALUES = ['Line1', 'Line2', 'Line3']

from win32com.client import Dispatch
ss = Dispatch('Lotus.Notessession')  ## NOTE: should not be 'Lotus.NotesSession'
ss.Initialize(PASSWORD)
db = ss.GetDatabase(SERVER, MAILBOX)

doc = db.CreateDocument()
doc.ReplaceItemValue('Form', 'Memo')
doc.ReplaceItemValue('Principal', PRINCIPAL)
doc.ReplaceItemValue('Sendto', 'user1/ou/ou/o')
doc.ReplaceItemValue('Copyto', 'user2/ou/ou/o')

style = ss.CreateRichTextStyle
style.FontSize = FONT_SIZE

body = doc.CreateRichTextItem('Body')
body.AppendStyle(style)

for i, LineText in enumerate(BODY_VALUES):
    if i: body.AddNewLine(1)
    body.AppendText(LineText)
body.AddNewLine(2)
body.AppendText('mail from %s' % SELF_IP)
doc.Send(False)
doc.Save(True, False)
```

```python
#https://win32com.goermezer.de/category/lotus-notes
from win32com.client import Dispatch
session = Dispatch('Lotus.NotesSession')

def iterateDocuments(view):
   """ wrapper for iterating documents from a view, fe:
       for doc in iterateDocuments(inbox): print doc.GetItemValue('Subject') """
   doc = view.GetFirstDocument()
   while doc:
      yield doc
      doc = view.GetNextDocument(doc)

def iterateDatabases(server, filetype=1247):
   """ wrapper for iterating databases from a server, fe:
       for db in iterateDatabases('server'): print db.Title """
   db = server.GetFirstDatabase(filetype)
   while db:
      yield db
      db = server.GetNextDatabase()

def iterateEntries(ACL):
   """ wrapper for iterating ACL entries for a database, fe:
   for entry in iterateEntries(db.ACL):
         if entry.IsPerson: print entry.Name"""
   entry = ACL.GetFirstEntry()
   while entry:
      yield entry
      entry = ACL.GetNextEntry(entry)
```
