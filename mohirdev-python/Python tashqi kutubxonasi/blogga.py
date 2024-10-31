# --------------------------- Amazing topic for my blog  --------------------------- #

# import googletrans

# url = f"https://api.adviceslip.com/advice"
# r = requests.get(url)
# advice = r.json()['slip']['advice']
# print(advice)

# translator = googletrans.Translator()
# tarjima = translator.translate(advice, dest='uz')
# print(tarjima.text)

# --------------------------- Amazing topic for my blog  --------------------------- #

# import requests
# from bs4 import BeautifulSoup


# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)
# # pprint(r.text)

# soup = BeautifulSoup(r.text, "html.parser")
# # print(soup.prettify())
# news = soup.find_all(class_="small-cards__default-text")

# for i in range(len(news)):
#     print(news[i].text)
# # print(len(news))

# --------------------------- Amazing topic for my blog --------------------------- #

# import requests

# from bs4 import BeautifulSoup
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt


# sahifa = "https://kun.uz/news/main"
# r = requests.get(sahifa)
# # pprint(r.text)

# soup = BeautifulSoup(r.text, "html.parser")
# # print(soup.prettify())
# news = soup.find_all(class_="small-cards__default-text")
# matn = ""
# for n in news:
#     matn += n.text

# stopwords = ["учун", "бўйича", "лекин", "билан", "ва", "бор", "ҳам", "хил", "йил"]
# wordcloud = WordCloud(
#     width=1000,
#     height=1000,
#     background_color="white",
#     stopwords=stopwords,
#     min_font_size=20,
# ).generate(matn)

# # plot the WordCloud image
# plt.figure(figsize=(8, 8), facecolor=None)
# plt.imshow(wordcloud)
# plt.axis("off")
# plt.tight_layout(pad=0)
# plt.show()

# --------------------------- Amazing topic for my blog --------------------------- #

# import cv2

# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# )
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# while True:
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
#         roi_gray = gray[y : y + w, x : x + w]
#         roi_color = frame[y : y + h, x : x + w]
#         eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
#         for (ex, ey, ew, eh) in eyes:
#             cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

#     cv2.imshow("frame", frame)

#     if cv2.waitKey(1) == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()

# --------------------------- Amazing topic for my blog --------------------------- #

# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process
# from uzwords import words

# # ikki so'z 'ortasida o'xshashlik foizini topish
# print(fuzz.ratio("salom",'assalom'))
# print(fuzz.ratio("salom","salim"))

# # Matnlar orasidan 3 ta eng o'xshashlarini ajratib olish
# text = "салом"
# matches = process.extract(text, words, limit=3)
# print(matches)

# # Matnlar orasidan eng o'xshashini topish
# text = "талба"
# match = process.extractOne(text, words)
# print(match)

# --------------------------- Amazing topic for my blog --------------------------- #

# # wxPython
# import wx
# from googletrans import Translator

# tarjimon = Translator()


# class MyFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(parent=None, title="Oʻzbek-Ingliz Lugʻat")
#         panel = wx.Panel(self)
#         my_sizer = wx.BoxSizer(wx.VERTICAL)
#         self.text_ctrl = wx.TextCtrl(panel)
#         my_sizer.Add(self.text_ctrl, 0, wx.ALL | wx.EXPAND, 5)

#         my_btn = wx.Button(panel, label="TARJIMA")
#         my_btn.Bind(wx.EVT_BUTTON, self.on_press)
#         my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)

#         self.text_out = wx.TextCtrl(panel, style=wx.TE_READONLY)
#         my_sizer.Add(self.text_out, 0, wx.ALL | wx.EXPAND, 5)
#         panel.SetSizer(my_sizer)
#         self.Show()

#     def on_press(self, event):
#         value = self.text_ctrl.GetValue()
#         if not value:
#             self.text_out.SetValue("Soʻz kiritmadingiz")
#         else:
#             tarjima = tarjimon.translate(value, src="uz", dest="en")
#             self.text_out.SetValue(tarjima.text.capitalize())


# if __name__ == "__main__":
#     app = wx.App()
#     frame = MyFrame()
#     app.MainLoop()