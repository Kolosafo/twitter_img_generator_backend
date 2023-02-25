from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFile
import urllib.request
ImageFile.LOAD_TRUNCATED_IMAGES = True


# INCOMING USER IMAGE SHOULD BE 400X400


image_path = "media/images/"
font_path = "media/better_together.ttf"
font = ImageFont.truetype(font_path, 70)

gold_ring = Image.open((image_path + "gold_ring.png"))
gold_ring_no_bg = Image.open((image_path + "gold_ring_no_bg.png"))
watermark = Image.open((image_path + "watermark_1.png"))
watermark2 = Image.open((image_path + "watermark_2.png"))
test_profile_pic = Image.open((image_path + "test_pic.png"))

resize_pp = test_profile_pic.resize((410, 410))
last_overlay = Image.open((image_path + "last_overlay.png"))


profile_pic_size = Image.new("RGB", (400, 400))
original = Image.new("RGB", (400, 400))

draw = ImageDraw.Draw(profile_pic_size)
draw.ellipse((0, 0, 400, 400), fill='blue', outline='blue')

add_watermark = watermark.resize((400, 400))


def apc_design(img: str = None, postDesign: bool = None):
    apc_animated = Image.open((image_path + "Logos/apc_logo.png"))
    unopen_img = "img"
    try:
        if img:
            urllib.request.urlretrieve(img, unopen_img)
            profile_pic = Image.open(unopen_img)
        else:
            profile_pic = resize_pp
    except Exception as E:
        print("OMO NA ME", E)

    _profile_pic = profile_pic.resize((400, 400))
    resize_logo = apc_animated.resize((100, 100))
    if not postDesign:
        profile_pic_size.paste(_profile_pic, (0, 0))
        profile_pic_size.paste(gold_ring, (0, 0), gold_ring)
        profile_pic_size.paste(resize_logo, (220, 281), resize_logo)
        profile_pic_size.paste(last_overlay, (0, 0), last_overlay)
        original.paste(profile_pic_size, (0, 0))
        profile_pic_size.paste(add_watermark, (0, 0), add_watermark)
        watermarked = profile_pic_size
        return watermarked, original

    elif postDesign:
        profile_pic_size.paste(_profile_pic, (0, 0))
        profile_pic_size.paste(gold_ring_no_bg, (0, 0), gold_ring_no_bg)
        profile_pic_size.paste(resize_logo, (220, 281), resize_logo)
        profile_pic_size.paste(add_watermark, (0, 0), add_watermark)

        return profile_pic_size


def pdp_design(img: str = None, postDesign: bool = None):
    pdp_animated = Image.open((image_path + "Logos/pdp_logo.png"))
    unopen_img = "img"
    try:
        if img:
            urllib.request.urlretrieve(img, unopen_img)
            profile_pic = Image.open(unopen_img)
        else:
            profile_pic = resize_pp

        _profile_pic = profile_pic.resize((400, 400))
        resize_logo = pdp_animated.resize((100, 100))

        if not postDesign:
            profile_pic_size.paste(_profile_pic, (0, 0))
            profile_pic_size.paste(gold_ring, (0, 0), gold_ring)
            profile_pic_size.paste(resize_logo, (220, 281), resize_logo)
            profile_pic_size.paste(last_overlay, (0, 0), last_overlay)
            original.paste(profile_pic_size, (0, 0))
            profile_pic_size.paste(add_watermark, (0, 0), add_watermark)
            watermarked = profile_pic_size
            return watermarked, original

        elif postDesign:
            print("OMO E DEY HERE OOO")
            profile_pic_size.paste(_profile_pic, (0, 0))
            profile_pic_size.paste(gold_ring_no_bg, (0, 0), gold_ring_no_bg)
            profile_pic_size.paste(resize_logo, (220, 281), resize_logo)
            profile_pic_size.paste(add_watermark, (0, 0), add_watermark)

            return profile_pic_size
    except Exception as E:
        print("PDP ERROR, NA ME", E)
        return profile_pic_size


def lp_design(img: str = None, postDesign: bool = None):
    lp_animated = Image.open((image_path + "Logos/lp-img.png"))
    unopen_img = "img"
    try:
        if img:
            urllib.request.urlretrieve(img, unopen_img)
            profile_pic = Image.open(unopen_img)
        else:
            profile_pic = resize_pp
    except Exception as E:
        print("Error EXceptiom", E)

    _profile_pic = profile_pic.resize((400, 400))
    resize_logo = lp_animated.resize((100, 100))

    if not postDesign:
        profile_pic_size.paste(_profile_pic, (0, 0))
        profile_pic_size.paste(gold_ring, (0, 0), gold_ring)
        profile_pic_size.paste(resize_logo, (220, 281), resize_logo)
        profile_pic_size.paste(last_overlay, (0, 0), last_overlay)
        original.paste(profile_pic_size, (0, 0))
        profile_pic_size.paste(add_watermark, (0, 0), add_watermark)
        watermarked = profile_pic_size
        return watermarked, original

    elif postDesign:
        profile_pic_size.paste(_profile_pic, (0, 0))
        profile_pic_size.paste(gold_ring_no_bg, (0, 0), gold_ring_no_bg)
        profile_pic_size.paste(resize_logo, (220, 281), resize_logo)

        profile_pic_size.paste(add_watermark, (0, 0), add_watermark)
        return profile_pic_size


def nnpp_design(img: str = None, postDesign: bool = None):
    nnpp_animated = Image.open((image_path + "Logos/nnpp_logo.png"))
    resize_logo = nnpp_animated.resize((100, 100))
    unopen_img = "img"
    if img:
        urllib.request.urlretrieve(img, unopen_img)
        profile_pic = Image.open(unopen_img)
    else:
        profile_pic = resize_pp

    _profile_pic = profile_pic.resize((400, 400))

    if not postDesign:
        profile_pic_size.paste(_profile_pic, (0, 0))
        profile_pic_size.paste(gold_ring, (0, 0), gold_ring)
        profile_pic_size.paste(resize_logo, (220, 281), resize_logo)
        profile_pic_size.paste(last_overlay, (0, 0), last_overlay)
        original.paste(profile_pic_size, (0, 0))
        profile_pic_size.paste(add_watermark, (0, 0), add_watermark)
        watermarked = profile_pic_size
        return watermarked, original

    elif postDesign:
        profile_pic_size.paste(_profile_pic, (0, 0))
        profile_pic_size.paste(gold_ring_no_bg, (0, 0), gold_ring_no_bg)
        profile_pic_size.paste(resize_logo, (220, 281), resize_logo)
        original.paste(profile_pic_size, (0, 0))
        profile_pic_size.paste(add_watermark, (0, 0), add_watermark)
        watermarked = profile_pic_size

        return watermarked, original


# TEXT LENGTH FORMATTER
# 21 WORDS = WIDTH: 580
# 11 WORDS =  WIDTH: 650
# SUBTRACT 6.4 FOR EVERY WORD THAT IS MORE THAN 11 CHARACTERS
banner_watermark = watermark2
banner_original = Image.new("RGB", (1500, 500))


def banner_design(name: str, party: str):
    if party == "LP":
        lp_banner = Image.open((image_path + "po_banner_design.png"))
        banner = lp_banner
        draw_layer = ImageDraw.Draw(banner)
    elif party == "PDP":
        pdp_banner = Image.open((image_path + "pdp_banner_design.png"))
        banner = pdp_banner
        draw_layer = ImageDraw.Draw(banner)
    elif party == "APC":
        apc_banner = Image.open((image_path + "apc_banner_design.png"))
        banner = apc_banner
        draw_layer = ImageDraw.Draw(banner)
    elif party == "NNPP":
        nnpp_banner = Image.open((image_path + "nnpp_banner_design.png"))
        banner = nnpp_banner
        draw_layer = ImageDraw.Draw(banner)
    # print(len("Yakubu Kolo"))
    if(len(name) > 11):
        newWidth = 650 - ((len(name) - 11) * 6.4)
        # print("new width", newWidth)
    elif len(name) < 11:
        newWidth = 650 + ((11 - len(name)) * 6.4)

    else:
        newWidth = 650
    try:
        draw_layer.text((newWidth, 250), name, "white", font=font)
    except Exception as E:
        print("BANNER ERROR, NA ME", E)
    banner_original.paste(banner, (0, 0))
    banner.paste(banner_watermark, (0, 0), banner_watermark)
    watermarked = banner
    return watermarked, banner_original


post_water = watermark
post_original = Image.new("RGB", (1080, 1080))


def post_design(party: str, name: str, img: str):

    if party == "LP":
        wm, _picture = lp_design(img)
        picture = _picture.resize((450, 450))
        lp_banner = Image.open((image_path + "lp_post_design.png"))
        lp_banner.paste(picture, (330, 220))
        banner = lp_banner
    elif party == "PDP":
        wm, _picture = pdp_design(img)
        picture = _picture.resize((450, 450))
        pdp_banner = Image.open((image_path + "pdp_post_design.png"))
        pdp_banner.paste(picture, (330, 220))
        banner = pdp_banner
    elif party == "APC":
        wm, _picture = apc_design(img)
        picture = _picture.resize((450, 450))
        apc_banner = Image.open((image_path + "apc_post_design.png"))
        apc_banner.paste(picture, (330, 220))
        banner = apc_banner
    elif party == "NNPP":
        wm, _picture = nnpp_design(img)
        picture = _picture.resize((450, 450))
        nnpp_banner = Image.open((image_path + "nnpp_post_design.png"))
        nnpp_banner.paste(picture, (330, 220))
        banner = nnpp_banner

    draw_layer = ImageDraw.Draw(banner)
    if(len(name) > 11):
        newWidth = 430 - ((len(name) - 11) * 6.4)
    elif len(name) < 11:
        newWidth = 430 + ((11 - len(name)) * 6.4)

    else:
        newWidth = 420
    draw_layer.text((newWidth, 704), name, "white", font=font)

    post_original.paste(banner, (0, 0))
    # post_original.show()
    banner.paste(post_water, (0, 0), post_water)
    watermarked = banner
    return watermarked, post_original


# name_card = Image.open((image_path + "name_card.png"))
# insp_card = Image.open((image_path + "insp_card.png"))
# card_2 = Image.open((image_path + "insp_card.png"))
# _font_path = "media/komikz.ttf"
# _font = ImageFont.truetype(_font_path, 130)


# def twenty_words_separator(text: str):

#     text_card_list = []

#     split_text = text.split()
#     middleIndex = int(len(split_text) / 2)
#     split_one = split_text[:middleIndex]
#     split_three = split_text[middleIndex:]

#     merged_split_one = " ".join(split_one)
#     merged_split_two = " ".join(split_three)

#     text_card_list.append(merged_split_one)
#     text_card_list.append(merged_split_two)

#     # print(text_card_list)

#     return merged_split_one, merged_split_two


# font_path_3 = "media/midspicy.ttf"
# font_3 = ImageFont.truetype(font_path_3, 120)

# apc_ballot = Image.open((image_path + "apc_ballot.png"))
# pdp_ballot = Image.open((image_path + "pdp_ballot.png"))
# nnpp_ballot = Image.open((image_path + "nnpp_ballot.png"))
# lp_ballot = Image.open((image_path + "lp_ballot_og.png"))


# lp_post_3_base = Image.open((image_path + "post_design_3_2.png"))
# apc_post_3_base = Image.open((image_path + "apc_post_design_3.png"))
# pdp_post_3_base = Image.open((image_path + "pdp_post_design_3.png"))
# nnpp_post_3_base = Image.open((image_path + "nnpp_post_design_3.png"))


# def post_3_design(img: str, name: str, inspirational_qoute: str, party: str):
#     watermark3 = Image.open((image_path + "watermark3.png"))
#     post_3_original = Image.new("RGB", (4000, 4000))
#     unopen_img = "img"
#     try:
#         if img:
#             urllib.request.urlretrieve(img, unopen_img)
#             profile_pic = Image.open(unopen_img)
#         else:
#             profile_pic = resize_pp
#     except Exception as E:
#         print("OMO NA ME", E)
#     if party == "APC":
#         base = apc_post_3_base
#     if party == "PDP":
#         base = pdp_post_3_base
#     if party == "LP":
#         base = lp_post_3_base
#     if party == "NNPP":
#         base = nnpp_post_3_base


    
#     resize_user_pic = profile_pic.resize((2300, 2300))
#     _base = post_3_original
#     _base.paste(resize_user_pic, (-120, 600), resize_user_pic)
#     try:
#         _base.paste(base, (0, 0), base)
#     except:
#         pass
#     # base.paste(resize_user_pic, (-120, 600), resize_user_pic)
    

#     if(len(name) > 11):
#         newWidth = 430 - ((len(name) - 11) * 6.4)
#     elif len(name) < 11:
#         newWidth = 640 + ((11 - len(name)) * 6.4)

#     else:
#         newWidth = 420
#     # draw_layer.text((newWidth, 704), name, "white", font=font)
#     draw_layer = ImageDraw.Draw(name_card)
#     draw_layer.text((newWidth, 50), name, "white", font=_font)
#     _base.paste(name_card, (70, 2900), name_card)

#     # inspirational text adding
#     insp_text_one, insp_text_two = twenty_words_separator(inspirational_qoute)
#     draw_layer2 = ImageDraw.Draw(insp_card)
#     draw_layer2.text((50, 50), insp_text_one, "black", font=font_3)
#     _base.paste(insp_card, (260, 3100), insp_card)

#     draw_layer3 = ImageDraw.Draw(card_2)
#     draw_layer3.text((50, 50), insp_text_two, "black", font=font_3)
#     _base.paste(card_2, (280, 3255), card_2)
#     if party == "APC":
#         resize_ballot = apc_ballot.resize(
#             (apc_ballot.size[0]*4, apc_ballot.size[1]*4))
#     if party == "PDP":
#         resize_ballot = pdp_ballot.resize(
#             (pdp_ballot.size[0]*4, pdp_ballot.size[1]*4))
#     if party == "LP":
#         resize_ballot = lp_ballot.resize(
#             (lp_ballot.size[0]*4, lp_ballot.size[1]*4))
#     if party == "NNPP":
#         resize_ballot = nnpp_ballot.resize(
#             (nnpp_ballot.size[0]*4, nnpp_ballot.size[1]*4))
#     # print("RESIZE BALLOT", resize_ballot.size)
#     _base.paste(resize_ballot, (0, 2600), resize_ballot)
#     post_3_original.paste(_base, (0, 0))
#     # post_3_original.show()
#     _base.paste(watermark3, (0, 0), watermark3)
#     watermarked = _base

#     return watermarked, post_3_original

#     # base.show()


