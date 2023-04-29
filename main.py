import cv2

image = cv2.imread('imeg.jpeg')
q = cv2.imread('1.jpg')

print(image)
print(q)

casc = cv2.CascadeClassifier('haarcascade_eye.xml')

eyes = casc.detectMultiScale(image)

print(eyes)

for (x, y, w, h) in eyes:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 3)
cv2.imshow('imeg', image)
eyes = casc.detectMultiScale(q)
for (x, y, w, h) in eyes:
    cv2.rectangle(q, (x, y), (x+w, y+h), (0, 0, 255), 3)

cv2.imshow('1', q)

cv2.waitKey()

