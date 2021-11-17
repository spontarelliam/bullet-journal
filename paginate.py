from PIL import Image, ImageDraw, ImageFont
import time 
# create Image object with the input image
#
special_pages = ['',
                 'Index',
                 'Index',
                 # 'Shopping List',
                 # 'Shopping List',
                 'Future Log',
                 'Future Log',
                 'Good Ideas',
                 'Good Ideas',
                 'Members',
                 'Members',
                 'Partners',
                 'Partners'
                 ]



def add_special_page(title, pg):
    fnt = ImageFont.truetype('/usr/share/fonts/TTF/DejaVuSans.ttf', 70)
    if pg % 2 == 0:
        xpos = 800
    else:
        xpos = 2400

    d.text((xpos, 6), str(title), font=fnt, fill=(0,0,0,255))


 
image = Image.open('dotgrid.png').convert('RGBA')
 
# image = image.rotate(90)
image = image.transpose(Image.ROTATE_90) 

# get a font
fnt = ImageFont.truetype('/usr/share/fonts/TTF/DejaVuSans.ttf', 40)
# get a drawing context

total_pages = 200
sheets_per_signet = 10
pages_per_signet = sheets_per_signet * 4
total_signets = int(total_pages / pages_per_signet)


# for page in range(1, int(total_pages/2), 2):
for signet in range(total_signets):
    last_lpage = (1 + signet) * pages_per_signet + 1 # initialize
    last_rpage = (signet + 0) * pages_per_signet # initialize
    print("\n Signet = ", str(signet+1))
    for sheet in range(sheets_per_signet):
        for i in range(2):
            if i == 0: # front sheet
                lpage = last_lpage - 1
                rpage = last_rpage + 1
                last_rpage = rpage
                last_lpage = lpage
            if i == 1: # back sheet
                lpage = last_rpage + 1
                rpage = last_lpage - 1
                last_rpage = lpage
                last_lpage = rpage

            print(lpage, rpage)

            txt = Image.new('RGBA', image.size, (255,255,255,0))    
            d = ImageDraw.Draw(txt)
            d.text((50,2440), str(lpage), font=fnt, fill=(0,0,0,255))
            d.text((3170,2440), str(rpage), font=fnt, fill=(0,0,0,255))

            for idx, special_page in enumerate(special_pages):
                title = special_page
                pg = idx + 1
                if pg == lpage or pg == rpage:
                    add_special_page(title, pg)

            out = Image.alpha_composite(image, txt)

            out.save("pages/dotgrid_paginated-"+str(signet+1)+","+str(sheet+1).zfill(3)+","+str(i)+".png", "PNG")
