# Disclaimer:
# this code was made to work with specific files in mind
# HTML files based on "color_scheme_template.html" 
# you can find this template in https://github.com/fm3chanic/color_schemes
# the target file is "konsole_theme_template.colorscheme"
# you can find this template in https://github.com/fm3chanic/kde_konsole_themes

import pandas as pd
import sys

def create_rgb(input):
    input = input.lstrip('#')
    input = input.strip()
    return tuple(int(input[i:i+2], 16) for i in (0, 2, 4))

#define required lists
tab1_values = []
tab2_values = []

#define valuse for replacement
tab1_replace = ['BackGround1','BackGround2','BackGround3','ForeGround1','ForeGround2','ForeGround3','HighLight1','HighLight2','HighLight3']
tab2_replace = ['Syn1','Syn2','Syn3','Syn4','Syn5','Syn6','Syn7']

input_file = f'{sys.argv[1]}.html'
output_file = f'{sys.argv[1]}.colorscheme'

#output of read_html() is a list with two data frames
df = pd.read_html(input_file, header=0)

#copying data frames to create dedicated lists
tab1 = df[0]
tab1_values = tab1.iloc[0:9,1].tolist()

tab2 = df[1]
tab2_values = tab2.iloc[0:7,1].tolist()

# reading the template
f = open('konsole_theme_template.colorscheme', 'r', encoding='utf-8')
content = f.read()
f.close()

#iterating through lists
#mapped expression will be replaced with color codes accordingly
for i in range(9):
    content = content.replace(tab1_replace[i], str(create_rgb(tab1_values[i])).strip(')').strip('('))

for i in range(7):
    content = content.replace(tab2_replace[i], str(create_rgb(tab2_values[i])).strip(')').strip('('))    

content = content.replace("ThemeName", sys.argv[1])

# creating the completed output file
f = open(output_file, 'w', newline='\n', encoding='utf-8')
f.write(content)
f.close()