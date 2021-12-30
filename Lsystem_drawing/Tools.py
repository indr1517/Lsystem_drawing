from PIL import Image, ImageDraw

def connect(ims):
    dst = Image.new("RGB",(sum([im.width for im in ims]),ims[0].height))
    dst.paste(ims[0],(0,0))
    for i,im in enumerate(ims[1:]):
        dst.paste(im,(sum([im2.width for im2 in ims[:i+1]]),0))

    return dst


def connect_vert(ims):
    dst = Image.new("RGB", (ims[0].width,sum([im.height for im in ims])))
    dst.paste(ims[0], (0, 0))
    for i, im in enumerate(ims[1:]):
        dst.paste(im, (0, sum([im2.height for im2 in ims[:i + 1]])))

    return dst


def connect_mat(ims):
    return connect_vert([connect(ims_line) for ims_line in ims])

def save_img_list(ims,filename,mode="v"):
    """未デバッグ"""
    if mode=="v":
        width = ims[0].width
        height = sum([im.height for im in ims])
    elif mode=="h":
        width = sum([im.width for im in ims])
        height = ims[0].height
    elif mode=="m":
        width = max([sum([im.width for im in line]) for line in ims])
        height = sum([line[0].height for line in ims])
    else:
        raise ModeError("無効なmode:"+mode)

    dst = Image.new("RGB", (width,height))
    if mode in {"h","v"}:
        for i,im in enumerate(ims):
            x = 0 if mode == "v" else sum([im2.width for im2 in ims[:i-1]])
            y = 0 if mode == "h" else sum([im2.height for im2 in ims[:i-1]])
            dst.paste(im,(x,y))
    else:
        for y,line in enumerate(ims):
            for x,im in enumerate(line):
                px = sum([im2.width for im2 in line[:x]])
                py = sum([line[0].height for line in ims[:y]])
                dst.paste(im, (px, py))
    dst.save(filename)

class ModeError(Exception):
    pass