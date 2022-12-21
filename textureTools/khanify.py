from PIL import Image
import time
path = "/Users/admin/Documents/3DKhan/RealisticTest/testRoom/TestRoomLightmap-denoised2.png"
output_path = "/Users/admin/Documents/3DKhan/RealisticTest/testRoom/lightmapParts"
output_name = None
file_limit = 20 #MB
flip_x = False
flip_y = False
rotate = False

if (output_path[-1] != "/"):
    output_path+="/"
if (output_name is None):
    output_name = path.split("/")[-1].split(".")[0]



def save_file(filename, text):
    print("Writing file: "+filename)
    with open(filename, 'w') as f:
        f.write(text)

def create_var(name, append):
    out = "window."+name.replace("-", "_")
    if append:
        out += "+="
    else:
        out += "="
    out +="\""
    return (out, len(out))

def create_header(name, img):
    out = "window."+name.replace("-", "_")+"_data=["
    out+=str(img.width)+","
    out+=str(img.height)+","
    out+=str( len( img.getpixel((0,0)) ) )
    out += "];"
    return out

def get_hex(value):
    hex_value = hex(val).split('x')[-1]
    if len(hex_value) < 2:
        hex_value = "0"+hex_value
    return hex_value

output_str, bytes_used = create_var(output_name, False)

file_index = 0
startTime = time.time()
with Image.open(path) as im:
    header = create_header(output_name, im)
    output_str = header + output_str
    bytes_used += len(header)

    xrange = []
    if(flip_x): xrange = range(im.width-1, -1, -1)
    else: xrange = range(im.width)

    yrange = []
    if(flip_y): yrange = range(im.height-1, -1, -1)
    else: yrange = range(im.height)

    for y in yrange:
        for x in xrange:
            position = (x, y)
            if rotate: position = (y, x)
            for val in im.getpixel(position):
                output_str += get_hex(val)
                bytes_used+=2
                if(bytes_used >= file_limit*1000000-2):
                    output_str+="\";"
                    save_file(output_path+output_name+str(file_index)+".js", output_str)
                    output_str, bytes_used = create_var(output_name, True)
                    file_index+=1
    
    output_str+="\";"
    save_file(output_path+output_name+str(file_index)+".js", output_str)
    
    print("Completed in: "+str(time.time()-startTime)+" seconds.")

