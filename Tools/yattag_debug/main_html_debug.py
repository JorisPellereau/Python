from yattag import Doc
from yattag import indent
from html_blocs_class import *

import numpy as np
# Init Class

html_blocs = html_blocs_class()

np_array = np.zeros([8, 64], int)
np_array[:,0] = 5555
np_array[:,1] = 888
#print(html_blocs.np_array_2_tab(np_array))
#print()

#div_content_list = [html_blocs.np_array_2_tab(np_array), "CONTENT_BUTTON_1"]


html_page_str = html_blocs.create_page_with_multiple_button(page_name         = "page_name",
                                                            buttons_name_list = ["BUTTON_0", "BUTTON_1"],
                                                            div_content_list  = [html_blocs.np_array_2_tab(np_array), "CONTENT_BUTTON_1"])

f = open("index.html", "w")
f.write(html_page_str)
f.close()

print(html_page_str)


print(dir(html_blocs.doc))



