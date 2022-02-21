from pyzotero import zotero
import os.path

zot = zotero.Zotero(xxxxxx, 'user', 'xxxxx')#identification avec le compte Zotero
items = zot.items(limit=1000)#on réupère les 1000 premiers (suffisant j'espère) de la librairie 
path=os.path.dirname('C:\\Users\\guill\\Desktop\\biblio\\')
type_list=['journalArticle','report','webpage','presentation']
for item in items:
    if item['data']['itemType'] in  type_list:
        short_date = item['meta']['parsedDate']
        short_date = short_date[:4]
        name = "("+item['meta']['creatorSummary']+","+short_date+")"+".md"
        path_test = os.path.join(path, name)
        if os.path.exists(path_test) == False:
            file = open(path_test, "x",encoding='utf-8')
            h1 = "# "+ item['data']['title']
            file_id= item['data']['key']
            file.write(file_id+"\n")
            file.write(h1)
            file.close()
        else:
            ofile = open(path_test,'r')
            firstline = ofile.readline().rstrip()
            file_id= item['data']['key']
            if firstline != file_id:
                name = "("+item['meta']['creatorSummary']+","+short_date+"b"+")"+".md"
                path_test = os.path.join(path, name)
                file = open(path_test, "x",encoding='utf-8')
                h1 = "# "+ item['data']['title']
                file.write(file_id+"\n")
                file.write(h1)
                file.close()
            else:
                print(file_id, "is already in the repertory")
print("___fin___")
            
        
        
        
