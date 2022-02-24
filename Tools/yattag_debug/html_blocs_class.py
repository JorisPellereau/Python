from yattag import Doc
from yattag import indent

import numpy as np

class html_blocs_class:


    def __init__(self):
        self.doc, self.tag, self.text = Doc().tagtext()
        background_color = "#f1f1f1"
        

    # == STYLE CONFIGURATION ==

    # Tab Style
    def tab_style(self, overflow = "hidden", border = "1px solid #ccc", background_color = "#f1f1f1"):
        tab_style_str = ".tab" + "{" + "overflow: {0};border: {1};background-color: {2};".format(overflow, border, background_color) + "}"

        return tab_style_str
        

    # Tab Button Style
    def tab_button_style(self,
                         background_color = "inherit",
                         float_tab        = "left",
                         border           = "none",
                         outline          = "none",
                         cursor           = "pointer",
                         padding          = "14px 16px",
                         transition       = "0.3s"):
        tab_button_style_str = ".tab button" + "{" + "background-color: {0}; float: {1}; border: {2}; outline: {3}; cursor: {4};padding: {5};transition: {6};".format(background_color, float_tab, border, outline, cursor, padding, transition) + "}"
        
        return tab_button_style_str

    def tab_button_hover(self, background_color = "#ddd"):
        str = ".tab button:hover" + "{" + "background-color: {0};".format(background_color) + "}"

        return str


    def tab_button_active(self, background_color = "#ccc"):
    #/* Create an active/current tablink class */
        str = ".tab button.active" + "{" + "background-color: {0};".format(background_color) + "}"
        return str

    def tab_content(self,
                    display    = "none",
                    padding    = "6px 12px",
                    border     = "1px solid #ccc",
                    border_top = "none"):

        #/* Style the tab content */
        str = ".tabcontent" + "{" +"display: {0}; padding: {1}; border: {2}; border-top: {3};".format(display, padding, border, border_top) + "}"

        return str

    

    def multiple_align_button(self,
                              button_nb        = 1,
                              button_name_list = ['Button_{0}'.format(i) for i in range(1)]):
        with self.tag('div', klass = 'tab'):
            for i in range(0, button_nb):
                with self.tag('button', klass='tablinks', onclick='openButton(event, \'{0}\')'.format(button_name_list[i])):
                    self.text(button_name_list[i])
                   
                    


    def multiple_div_tab(self,
                         div_number  = 1,
                         div_name    = ["DIV_NAME_{0}".format(i) for i in range(1)],
                         div_content = ['TMP_{0}'.format(i) for i in range(1)]):

        for i in range(0, div_number):
            with self.tag('div', id=div_name[i], klass="tabcontent"):
                with self.tag("h3"):
                    self.text(div_name[i])

                with self.tag('p'):

                    # Print string
                    if(type(div_content[i]) == str):
                       self.doc.asis(div_content[i])
                    else:
                       div_content[i]


    def tab_script(self):
        with self.tag('script'):
            self.doc.asis("""
            function openButton(evt, buttonName) {
              var i, tabcontent, tablinks;
              tabcontent = document.getElementsByClassName("tabcontent");
              for (i = 0; i < tabcontent.length; i++) {
                tabcontent[i].style.display = "none";
              }
              tablinks = document.getElementsByClassName("tablinks");
              for (i = 0; i < tablinks.length; i++) {
                tablinks[i].className = tablinks[i].className.replace(" active", "");
              }
              document.getElementById(buttonName).style.display = "block";
              evt.currentTarget.className += " active";
            }
            """)
                


    def create_page_with_multiple_button(self, page_name   = "page_name",
                                         buttons_name_list = ["BUTTON_0", "BUTTON_1"],
                                         div_content_list  = ["CONTENT_BUTTON_0", "CONTENT_BUTTON_1"]):
        
        self.doc.asis('<!DOCTYPE html>')
        with self.tag('html'):
            with self.tag('head'):
                with self.tag('style'):
                    self.text('body {font-family: Arial;}')
                    self.text(self.tab_style())
                    self.text(self.tab_button_style())
                    self.text(self.tab_button_hover())
                    self.text(self.tab_button_active())
                    self.text(self.tab_content())
                    self.text(self.tab_config())
                    
            with self.tag('body'):
                with self.tag('h2'):
                    self.text(page_name)

                self.multiple_align_button(len(buttons_name_list), buttons_name_list)
                self.multiple_div_tab(len(buttons_name_list), buttons_name_list, div_content_list)


                self.tab_script()
        return indent(self.doc.getvalue())


    def tab_config(self):
        str = """table,
        td {
        border: 1px solid #333;
        }
        
        thead,
        tfoot {
        background-color: #333;
        color: #fff;
        }
        """

        return str

    def np_array_2_tab(self,
                       np_array     = np.zeros([10, 2], int),
                       table_name   = "TABLE_NAME",
                       collumn_name = ["COL_0", "COL_1"],
                       int_format   = "HEX",
                       digit_nb     = 8):

        row_nb     = np_array.shape[0]
        collumn_nb = np_array.shape[1] + 1 # Add Index
        
        doc, tag, text = Doc().tagtext()
        with tag('table'):
            with tag('thead'):
                with tag('tr'):
                    with tag('th', colspan=str(collumn_nb)):
                        doc.asis(table_name)
                        
            with tag('tbody'):
                for j in range(0, row_nb):

                    # Print Line
                    with tag('tr'):
                        for i in range(0, collumn_nb):

                            # # Print Collumn Name
                            # if(j == 0):
                            #     if(i == 0):
                            #         text('')
                            #     else:
                            #         text(collumn_name[i-1])
                            # else:
                            # Print Collumn
                            with tag('td'):
                                if(i == 0):
                                    text(str(j))
                                else:
                                    if(int_format == "HEX"):
                                        digit_format = "{0:0" + str(digit_nb) + "X" + "}"
                                        text(digit_format.format(np_array[j,i-1]))
                                    else:
                                        text(str(np_array[j,i-1]))
                                    
        return indent(doc.getvalue())
