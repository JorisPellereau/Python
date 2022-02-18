from yattag import Doc

class html_blocs_class:


    def __init__(self):
        self.doc, self.tag, self.text = Doc().tagtext()
        background_color = "#f1f1f1"
        


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
                with self.tag('button', klass='tablinks', onclick='openCity(event, \'{0}\')'.format(button_name_list[i])):
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
                    self.text(div_content[i])


    def tab_script(self):
        with self.tag('script'):
            self.doc.asis("""
            function openCity(evt, cityName) {
              var i, tabcontent, tablinks;
              tabcontent = document.getElementsByClassName("tabcontent");
              for (i = 0; i < tabcontent.length; i++) {
                tabcontent[i].style.display = "none";
              }
              tablinks = document.getElementsByClassName("tablinks");
              for (i = 0; i < tablinks.length; i++) {
                tablinks[i].className = tablinks[i].className.replace(" active", "");
              }
              document.getElementById(cityName).style.display = "block";
              evt.currentTarget.className += " active";
            }
            """)
                
