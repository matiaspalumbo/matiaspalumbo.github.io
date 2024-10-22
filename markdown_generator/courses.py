import pandas as pd
import os


talks = pd.read_csv("courses.csv", sep=";", header=0)


html_escape_table = {
    "&": "&amp;",
    '"': "&quot;",
    "'": "&apos;"
    }

def html_escape(text):
    if type(text) is str:
        return "".join(html_escape_table.get(c,c) for c in text)
    else:
        return "False"

loc_dict = {}

for row, item in talks.iterrows():

    url_slug = item.title.lower().replace(' ', '-')
    
    md_filename = str(item.date) + "-" + url_slug + ".md"
    html_filename = str(item.date) + "-" + url_slug 
    year = item.date[:4]
    
    md = "---\ntitle: \""   + item.title + '"\n'
    md += "collection: courses" + "\n"
    
    if len(str(item.type)) > 3:
        md += 'type: "' + item.type + '"\n'
    else:
        md += 'type: "Course"\n'
    
    md += "permalink: /courses/" + html_filename + "\n"
        
    if len(str(item.date)) > 3:
        md += "date: " + str(item.date) + "\n"
    
    if len(str(item.location)) > 3:
        md += 'location: "' + str(item.location) + '"\n'
           
    md += "---\n"
        
    
    if len(str(item.description)) > 3:
        md += "\n"

        if item.hours > 0:
            md +=  f"*({int(item.hours)}-hour course)* "

        md += html_escape(item.description) + "\n"

        if len(str(item.bibliography)) > 3:
            md += "\n**Bibliography**: " + html_escape(item.bibliography) + "\n"


        
    md_filename = os.path.basename(md_filename)
    
    with open("../_courses/" + md_filename, 'w') as f:
        f.write(md)
