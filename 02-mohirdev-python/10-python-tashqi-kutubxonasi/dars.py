from googletrans import Translator

tarjimon = Translator() # Translator - maxsus class. tarjimon - obyekt

# matn_uz = "Python - dunyodagi eng mashhur dasturlash tili"
# matn_ru = "Python — самый популярный язык программирования в мире"

# # tarjima = tarjimon.translate(matn_uz)

# # tarjima_ru = tarjimon.translate(matn_uz, dest='ru')

# tarjima_uz = tarjimon.translate(matn_ru, dest='uz')

# # print(tarjima.origin)
# # print(tarjima.text)
# print(tarjima_uz.text)
# # print(tarjima_ru.text)
# # print(tarjima.src)


# msg = "Tarjima uchun so'z kiriting (c - dasturni tugatish): "
# while True:
#     somsa = input(msg)
#     if somsa == "c":
#         break
#     try:
#         tarjima_uz = tarjimon.translate(somsa, src='uz', dest='en')
#     except Exception as e:
#         print('Qaytadan urinib ko\'ring! Iltimos')
#     print(tarjima_uz.text)
# print('dastur tugadi')


# --------------------------- Translator | up --------------------------- #



# import requests
# from pprint import pprint

# sahifa = 'https://kun.uz/news/main'

# r = requests.get(sahifa)
# pprint(r.text)


# --------------------------- Link ishlamadi --------------------------- #

# country = "Uzbekistan"
# url = f"https://restcountries.eu/rest/v2/name/{country}"
# r = requests.get(url)
# r_json = r.json()[0]
# print(r_json['capital'])

# --------------------------- Link ishlamadi --------------------------- #



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

# import cv2
# import numpy as np

# # Load the hat image (assuming it might not have an alpha channel)
# hat_img = cv2.imread('hat.png')

# cap = cv2.VideoCapture(0)
# face_cascade = cv2.CascadeClassifier(
#     cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# )

# while True:
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.3, 5)
#     for (x, y, w, h) in faces:
#         # Resize the hat image to fit the face width
#         hat_resized = cv2.resize(hat_img, (w, int(w * hat_img.shape[0] / hat_img.shape[1])))

#         # Calculate the position of the hat
#         hat_x1 = x
#         hat_x2 = x + w
#         hat_y1 = y - hat_resized.shape[0]
#         hat_y2 = y

#         if hat_y1 < 0:  # If the hat goes out of the frame, adjust its position
#             hat_y1 = 0
#             hat_y2 = hat_resized.shape[0]

#         # Get the region of interest (ROI) on which to place the hat
#         roi = frame[hat_y1:hat_y2, hat_x1:hat_x2]

#         # If the hat image does not have an alpha channel, create a mask
#         if hat_resized.shape[2] == 3:
#             hat_gray = cv2.cvtColor(hat_resized, cv2.COLOR_BGR2GRAY)
#             _, mask = cv2.threshold(hat_gray, 1, 255, cv2.THRESH_BINARY)
#             mask_inv = cv2.bitwise_not(mask)
#             hat = hat_resized
#         else:
#             # Extract the mask and inverse mask from the hat image with alpha channel
#             mask = hat_resized[:, :, 3]
#             mask_inv = cv2.bitwise_not(mask)
#             hat = hat_resized[:, :, 0:3]

#         # Black-out the area of the hat in ROI
#         img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

#         # Take only the hat region from the hat image
#         hat_fg = cv2.bitwise_and(hat, hat, mask=mask)

#         # Add the hat to the ROI and place it back in the image
#         dst = cv2.add(img_bg, hat_fg)
#         frame[hat_y1:hat_y2, hat_x1:hat_x2] = dst

#     cv2.imshow("frame", frame)

#     if cv2.waitKey(1) == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()


# --------------------------- Amazing topic for my blog --------------------------- #

# import cv2
# import numpy as np

# # Load the hijab image
# hijab_img = cv2.imread('hijab.png', -1)

# # Load the pre-trained face detector and gender classification model
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# gender_net = cv2.dnn.readNetFromCaffe(
#     'deploy_gender.prototxt',
#     'gender_net.caffemodel'
# )

# # List of gender labels
# gender_list = ['Male', 'Female']

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#     for (x, y, w, h) in faces:
#         face = frame[y:y + h, x:x + w]
#         blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)
        
#         # Predict gender
#         gender_net.setInput(blob)
#         gender_preds = gender_net.forward()
#         gender = gender_list[gender_preds[0].argmax()]
        
#         if gender == 'Female':
#             # Resize the hijab image to fit the face width
#             hijab_resized = cv2.resize(hijab_img, (w, int(w * hijab_img.shape[0] / hijab_img.shape[1])))

#             # Calculate the position of the hijab
#             hijab_x1 = x
#             hijab_x2 = x + w
#             hijab_y1 = y - hijab_resized.shape[0]
#             hijab_y2 = y

#             if hijab_y1 < 0:  # If the hijab goes out of the frame, adjust its position
#                 hijab_y1 = 0
#                 hijab_y2 = hijab_resized.shape[0]

#             # Get the region of interest (ROI) on which to place the hijab
#             roi = frame[hijab_y1:hijab_y2, hijab_x1:hijab_x2]

#             # Handle cases where the hijab image might not have an alpha channel
#             if hijab_resized.shape[2] == 3:
#                 hijab_gray = cv2.cvtColor(hijab_resized, cv2.COLOR_BGR2GRAY)
#                 _, mask = cv2.threshold(hijab_gray, 1, 255, cv2.THRESH_BINARY)
#                 mask_inv = cv2.bitwise_not(mask)
#                 hijab = hijab_resized
#             else:
#                 # Extract the mask and inverse mask from the hijab image with alpha channel
#                 mask = hijab_resized[:, :, 3]
#                 mask_inv = cv2.bitwise_not(mask)
#                 hijab = hijab_resized[:, :, 0:3]

#             # Black-out the area of the hijab in ROI
#             img_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

#             # Take only the hijab region from the hijab image
#             hijab_fg = cv2.bitwise_and(hijab, hijab, mask=mask)

#             # Add the hijab to the ROI and place it back in the image
#             dst = cv2.add(img_bg, hijab_fg)
#             frame[hijab_y1:hijab_y2, hijab_x1:hijab_x2] = dst

#     cv2.imshow("frame", frame)

#     if cv2.waitKey(1) == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()




# import cv2
# import numpy as np

# # Load the eyeglasses image
# glasses_img = cv2.imread('glasses.png', -1)

# # Load the pre-trained face and eye detectors
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

# cap = cv2.VideoCapture(0)

# while True:
#     ret, frame = cap.read()

#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)

#     for (x, y, w, h) in faces:
#         # Detect eyes within the face region to place the eyeglasses
#         roi_gray = gray[y:y+h, x:x+w]
#         roi_color = frame[y:y+h, x:x+w]
#         eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 4)

#         if len(eyes) >= 2:
#             # Assume the first two detected eyes are the actual eyes (to avoid false positives)
#             eye_1 = eyes[0]
#             eye_2 = eyes[1]

#             # Calculate the distance and angle between the eyes
#             if eye_1[0] > eye_2[0]:
#                 eye_1, eye_2 = eye_2, eye_1

#             eye_center_x = (eye_1[0] + eye_2[0] + eye_2[2]) // 2
#             eye_center_y = (eye_1[1] + eye_2[1] + eye_2[3]) // 2

#             glasses_width = int(1.5 * (eye_2[0] + eye_2[2] - eye_1[0]))
#             glasses_height = int(glasses_width * glasses_img.shape[0] / glasses_img.shape[1])
#             glasses_resized = cv2.resize(glasses_img, (glasses_width, glasses_height))

#             glasses_x1 = eye_center_x - glasses_width // 2
#             glasses_x2 = glasses_x1 + glasses_width
#             glasses_y1 = eye_center_y - glasses_height // 2
#             glasses_y2 = glasses_y1 + glasses_height

#             if glasses_x1 < 0:
#                 glasses_x1 = 0
#             if glasses_x2 > frame.shape[1]:
#                 glasses_x2 = frame.shape[1]
#             if glasses_y1 < 0:
#                 glasses_y1 = 0
#             if glasses_y2 > frame.shape[0]:
#                 glasses_y2 = frame.shape[0]

#             roi_glasses = frame[glasses_y1:glasses_y2, glasses_x1:glasses_x2]

#             # Ensure the ROI and the mask are the same size
#             glasses_resized = cv2.resize(glasses_resized, (roi_glasses.shape[1], roi_glasses.shape[0]))

#             if glasses_resized.shape[2] == 3:
#                 glasses_gray = cv2.cvtColor(glasses_resized, cv2.COLOR_BGR2GRAY)
#                 _, mask_glasses = cv2.threshold(glasses_gray, 1, 255, cv2.THRESH_BINARY)
#                 mask_glasses_inv = cv2.bitwise_not(mask_glasses)
#                 glasses = glasses_resized
#             else:
#                 mask_glasses = glasses_resized[:, :, 3]
#                 mask_glasses_inv = cv2.bitwise_not(mask_glasses)
#                 glasses = glasses_resized[:, :, 0:3]

#             mask_glasses = cv2.cvtColor(mask_glasses, cv2.COLOR_GRAY2BGR)
#             mask_glasses_inv = cv2.cvtColor(mask_glasses_inv, cv2.COLOR_GRAY2BGR)

#             img_bg_glasses = cv2.bitwise_and(roi_glasses, mask_glasses_inv)
#             glasses_fg = cv2.bitwise_and(glasses, mask_glasses)
#             dst_glasses = cv2.add(img_bg_glasses, glasses_fg)
#             frame[glasses_y1:glasses_y2, glasses_x1:glasses_x2] = dst_glasses

#     cv2.imshow("frame", frame)

#     if cv2.waitKey(1) == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()



import cv2
import numpy as np
from keras.models import load_model

# Load the pre-trained models
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
gender_model = load_model('path_to_gender_model.h5')  # Load your gender detection model
hijab_img = cv2.imread('hijab.png', -1)  # Load the hijab image with transparency

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        # Get the face region
        face = frame[y:y+h, x:x+w]
        
        # Preprocess face for gender model
        face_resized = cv2.resize(face, (96, 96))  # Resize to model input size
        face_resized = face_resized.astype('float32') / 255
        face_resized = np.expand_dims(face_resized, axis=0)
        
        # Predict gender
        gender_prediction = gender_model.predict(face_resized)
        gender = 'Female' if gender_prediction[0][0] > 0.5 else 'Male'

        if gender == 'Female':
            # Resize hijab image to fit on the face
            hijab_resized = cv2.resize(hijab_img, (w, h))
            
            # Extract the alpha mask of the overlay image
            alpha_mask = hijab_resized[:, :, 3] / 255.0
            alpha_inverse = 1.0 - alpha_mask

            for c in range(0, 3):
                frame[y:y+h, x:x+w, c] = (alpha_mask * hijab_resized[:, :, c] +
                                          alpha_inverse * frame[y:y+h, x:x+w, c])

    cv2.imshow('Hijab Overlay', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
