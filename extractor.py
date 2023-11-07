file = open("C:\\Users\\ntaru\\OneDrive\\Desktop\\python doi extractor\\bib.txt",encoding='utf8')

#gets the bib file and gives me all the doi links
lines = file.readlines()

for line in lines:
    if('doi' in line):
        print(line)


#LOAD LINKS AND USING PYTHON WEB MANIPULATION LOAD WEB PAGES FOR ALL OF THEM AND THEN DOWNLOAD ACCORDINGLY 


# take the doi's and then run it through chatgpt for chronological ordering and out of date filtering
#load the doi's in the other python file, place path and then get the pdf's
