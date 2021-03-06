import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        print("Escape hit, closing...")
        break

    elif k%256 == 32:
        img = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img, frame)
        print("{} written!".format(img))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()

from PIL import Image
import pytesseract

#img = input("Enter the name of the image with the respective extension : ")
im = Image.open(img)
l = input("In which language your text is: ")
if(l=='hindi'):
    short = "hin"
elif(l=='bengali'):
    short = "ben"
elif(l=='english'):
    short = 'eng'
elif(l=='spanish'):
    short = "spa"
elif(l=='chinese'):
    short = "chi_sim"
elif(l=='russian'):
    short = "rus"
elif(l=='japanese'):
    short = "jpn"
elif(l=='italian'):
    short = "ita"
elif(l=='korean'):
    short = "kor"
elif(l=='kannada'):
    short = "kan"
elif(l=='german'):
    short = "deu"
elif(l=='african'):
    short = "afr"
elif(l=='arabic'):
    short = "ara"
elif(l=='bulgarian'):
    short = "bul"
elif(l=='dutch'):
    short = "nld"
elif(l=='french'):
    short = "fra"
elif(l=='indonesia'):
    short = "ind"
elif(l=='urdu'):
    short = "urd"
elif(l=='turkish'):
    short = "tur"
elif(l=='tamil'):
    short = "tam"
elif(l=='swedish'):
    short = "swe"
elif(l=='romanian'):
    short = "ron"
elif(l=='serbian'):
    short = "srp"
elif(l=='portuguese'):
    short = "por"
elif(l=='persian'):
    short = "fas"
elif(l=='latin'):
    short = "lat"
elif(l=='irish'):
    short = "gle"
elif(l=='latvian'):
    short = "lav"
elif(l=='polish'):
    short = "pol"
else:
    print("You have entered wrong choice.")


text = pytesseract.image_to_string(im, lang = short)
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
y = TextBlob(text)
a = input("In which language you want the output: ")
if(a=='hindi'):
    m = "hi"
    out = y.translate(to = 'hi')
elif(a=='bengali'):
    m = "bn"
    out = y.translate(to='bn')
elif(a=='english'):
    m = 'en'
    out = y.translate(to='en')
elif(a=='spanish'):
    m = "es"
    out = y.translate(to='es')
elif(a=='chinese'):
    m = "zh-CN"
    out = y.translate(to='zh-CN')
elif(a=='russian'):
    m = "ru"
    out = y.translate(to='ru')
elif(a=='japanese'):
    m = "ja"
    out = y.translate(to='ja')
elif(a=='italian'):
    m = "it"
    out = y.translate(to='it')
elif(a=='korean'):
    m = "ko"
    out = y.translate(to='ko')
elif(a=='kannada'):
    m = "kn"
    out = y.translate(to='kn')
elif(a=='german'):
    m = "de"
    out = y.translate(to='de')
elif(a=='african'):
    m = "af"
    out = y.translate(to='af')
elif(a=='arabic'):
    m = "ar"
    out = y.translate(to='ar')
elif(a=='bulgarian'):
    m = "bg"
    out = y.translate(to='bg')
elif(a=='dutch'):
    m = "nl"
    out = y.translate(to='nl')
elif(a=='french'):
    m = "fr"
    out = y.translate(to='fr')
elif(a=='indonesia'):
    m = "id"
    out = y.translate(to='id')
elif(a=='urdu'):
    m = "ur"
    out = y.translate(to='ur')
elif(a=='turkish'):
    m = "tr"
    out = y.translate(to='tr')
elif(a=='tamil'):
    m = "ta"
    out = y.translate(to='ta')
elif(a=='swedish'):
    m = "sv"
    out = y.translate(to='sv')
elif(a=='romanian'):
    m = "ro"
    out = y.translate(to='ro')
elif(a=='serbian'):
    m = "sr"
    out = y.translate(to='sr')
elif(a=='portuguese'):
    m = "pt"
    out = y.translate(to='pt')
elif(a=='persian'):
    m = "fa"
    out = y.translate(to='fa')
elif(a=='latin'):
    m = "la"
    out = y.translate(to='la')
elif(a=='latvian'):
    m = "lv"
    out = y.translate(to='lv')
elif(a=='polish'):
    m = "pl"
    out = y.translate(to='pl')
else:
    out = "You have entered wrong choice."

from gtts import gTTS

speech = gTTS(str(out), m)
speech.save("hello.mp3")

from playsound import playsound

playsound("hello.mp3")
