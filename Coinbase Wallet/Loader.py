
import picamera
import qrtools
from qrtools import QR
import os
from PIL import Image
import sys, re
import warnings
warnings.filterwarnings("ignore")
warnings.filterwarnings(action= 'ignore')

oledWidth   =  48
oledHeight  =  48
threshold   =  100
myFileName  = ""

def convert(pixels) :

    data = [[0 for x in range(oledHeight/8)] for x in range(oledWidth)]

    for i in range(oledWidth):
        for j in range(oledHeight/8):
            for bit in range(8):
                data[i][j] |= (pixels[i][j*8 + bit] << bit)
    return data



def toBinary(im):
    # Convert image to monochrome if necessary
    if (im.mode != "1"):
        im.convert("1")

    binary = [[0 for x in range(oledHeight)] for x in range(oledWidth)]

    for j in range(oledHeight):
        for i in range(oledWidth):
            value = im.getpixel((i, j))[0]
            binary[i][j] = int(value < threshold)

    return binary



def output(data):

    if sys.argv[1]=="private":
        myFileName="privatekey.h"
        myFirstLine="const unsigned char privkey [288] = { \n"
    else:
        myFileName="publickey.h"
        myFirstLine="const unsigned char pubkey [288] = { \n"

    with open(myFileName, 'w') as myFile:

        myFile.write(myFirstLine)

        for j in range(oledHeight/8):
            for i in range(oledWidth):
                if (j==5 and i==47):
                    myFile.write(format(data[i][j], '#04x'))
                else:
                    myFile.write(format(data[i][j], '#04x') + ", ")
                if (i%16 == 15):
                    myFile.write("\n")



        myFile.write("\n};")



qr = qrtools.QR()

print "Alt Loader for Alt Wallet"
print "Roni Bandini, Buenos Aires, Argentina, May 2022"
print ""

print ">> Reading Cam"

camera=picamera.PiCamera()
camera.resolution = (800, 600)
camera.brightness = 50
camera.color_effects = (128,128)
camera.capture('cam.jpg')
camera.close()


print ">> Extracting info"
qr.data="NULL"
qr.decode('cam.jpg')
print qr.data

if qr.data=="NULL":
    print "No QR found"
    quit()

myCode = QR(data=qr.data, pixel_size=3, margin_size=0)
myCode.encode()
print ">> Moving image"
os.system("sudo mv " + myCode.filename + " /home/pi/btc/myQR.png")

print ">> Resizing"
img = Image.open(r"/home/pi/btc/myQR.png")
newsize = (48, 48)
img = img.resize(newsize)
img.save("myQR48.png")

print ">> Converting to JPG"
im = Image.open("myQR48.png")
rgb_im = im.convert('RGB')
rgb_im.save('myQR48.jpg')


print ">> Converting to Bytearray"
binary = toBinary(rgb_im)
data = convert(binary)
output(data)

if sys.argv[1]=="private":
    print ">> File exported as privatekey.h Place into Arduino project folder"
else:
    print ">> File exported as publickey.h Place into Arduino project folder"

print ">> Removing img files"
os.remove("cam.jpg")
os.remove("myQR.png")
os.remove("myQR48.jpg")
os.remove("myQR48.png")
