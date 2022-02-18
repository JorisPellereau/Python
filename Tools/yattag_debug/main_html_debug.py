from yattag import Doc
from yattag import indent
from html_blocs_class import *

# Init Class

html_blocs = html_blocs_class()
#print(dir(html_blocs))
doc  = html_blocs.doc
tag  = html_blocs.tag
text = html_blocs.text

button_name = ["TOTO", "TITI", "TATA"]
div_content = ["Hello coco", "Hola", "TOTO"]

doc.asis('<!DOCTYPE html>')
with tag('html'):
    with tag('head'):
        with tag('style'):
            text('body {font-family: Arial;}')
            text(html_blocs.tab_style())
            text(html_blocs.tab_button_style())
            text(html_blocs.tab_button_hover())
            text(html_blocs.tab_button_active())
            text(html_blocs.tab_content())
            
    with tag('body'):
        with tag('h2'):
            text('BODY')

        html_blocs.multiple_align_button(len(button_name), button_name)
        html_blocs.multiple_div_tab(len(button_name), button_name, div_content)


        html_blocs.tab_script()
   
print(indent(doc.getvalue()))


f = open("index.html", "w")
f.write(indent(doc.getvalue()))
f.close()
