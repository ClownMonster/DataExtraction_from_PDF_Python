import PyPDF2 as pdf 


'''
 opening the file with read binary mode
 if u wish to write then use wb (write binay)  mode

'''
try:
    file = open('./sample.pdf',"rb")
except FileNotFoundError as e:
    print(e)

''' 
 There are three methods to pdf 
1.pdf.PdfFileReader(file)
2.pdf.PdfFileMerger
3.pdf.PdfFileWriter

'''
pages = pdf.PdfFileReader(file) # reading the pdf file into pages


# prints the information of the passed document
def get_DocumetInfo():
    global pages
    x = pages.getDocumentInfo()
    print(x) 
    return


# prints the number of pages in the document
def get_NumberOfPages():
    global pages
    n = pages.getNumPages()
    print('Number of pages in the document :',n)
    return
    

def get_pageMode():
    global pages
    m = pages.getPageMode()
    print(m)
    

# print the encryption status of the pages
def check_encryption():
    global pages
    print(pages.isEncrypted)
    

# if page encripted decription can be done with password field
def make_decryption():
    global pages
    password = '' # add password here
    status = pages.decrypt(password)
    print(status) # prints the decription status



# prints the data in a required page 
def get_page_data(pageNo):
    global pages
    page1 = pages.getPage(pageNo) # get the each page
    print(page1.extractText())
    return

