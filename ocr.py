import cv2, pytesseract as pt, streamlit as st, math

def extract_int(input):
    try:
        return int(input)
    except:
        return None

window1 = st.image([])
window2 = st.image([])

image = cv2.imread("S/sample1.png")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# thresh = cv2.dilate(thresh, None, iterations=1)
thresh_eroded = cv2.erode(thresh, None, iterations=2)


# RETR_EXTERNAL
contours, hierarchy = cv2.findContours(thresh_eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cordinates = []
for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    if 45 < w < 60 and 45 < h < 60:
        cordinates.append((x, y, w, h))
        cv2.rectangle(rgb, (x, y), (x + w, y + h), (255, 0, 0), 1)

window1.image(rgb)
window2.image(thresh_eroded)

numbers = []
options = "--oem 3 --psm 6"
for coor in cordinates:
    x, y, w, h = coor
    new = pt.image_to_string(thresh[y:y + h, x:x + w], config=options)
    numbers.append(extract_int(new[0]))

FACTOR = int(math.sqrt(len(numbers)))

st.write(numbers)

cv2.destroyAllWindows()

