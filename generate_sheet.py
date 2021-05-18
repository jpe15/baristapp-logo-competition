import glob, os, shutil
from string import Template
#%%
original_image_folder = os.path.expanduser('~/Box/BaristApp Logo Comp/')
#%%
cell_template = \
    """
<td>
                <img class="large" src="$imgfile" />
                <img class="normal" src="$imgfile" />
                <img class="small" src="$imgfile" />
                <img class="smaller" src="$imgfile" />
</td>"""
row_template = Template("<tr>\n" + "<td>$num</td>" + 2*cell_template + "\n</tr>\n")
#%%
anonymized_keys = ''
table_contents = ''
for ii, fname in enumerate( 
    glob.glob(os.path.join(original_image_folder,'*.png'))):
    # Anonymize the file, store its old name, and copy anonymous version here
    anonymized_keys+=f'{ii+1} : {os.path.split(fname)[-1]}\n'
    anon_imgfile = f'{ii+1}.png'
    shutil.copy(fname,
        os.path.join('.',anon_imgfile)
    )
    table_contents += row_template.substitute({'num':ii+1, 'imgfile': anon_imgfile})
#%%
with open('sheet_TEMPLATE.html','r') as f:
    F = f.readlines()
insert_index = F.index('<!-- CONTENTS HERE -->\n')
F[insert_index] = table_contents
with open('index.html','w') as f:
    f.writelines(F)
with open('anon_vs_original.log','w') as f:
    f.writelines(anonymized_keys)
