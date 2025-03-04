import cv2 as cv
import numpy as np
import os
import pyautogui
import random
from time import time, sleep
from windowcapture import WindowCapture

# تغيير دليل العمل إلى مكان وجود السكربت
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# مسار مجلد الصور
arrow_dir = r"D:\asda story\Newfolder\newarrows\arrows"

# تحميل صور الأسهم وتحويلها إلى حواف
arrows = {}
for direction in ["up", "left", "down", "right"]:
    image = cv.imread(os.path.join(arrow_dir, f"{direction}.png"), 0)
    if image is not None:
        arrows[direction] = cv.Canny(image, 50, 150)  # تطبيق Canny Edge Detection
    else:
        arrows[direction] = None
        print(f"⚠️ لم يتم تحميل الصورة: {direction}")

# إنشاء كائن WindowCapture
wincap = WindowCapture("AsdaStory (ME)")

loop_time = time()
while True:
    start_time = time()  # لحساب الزمن الإجمالي

    # التقاط صورة من اللعبة
    screenshot = wincap.get_screenshot()

    # تحويل للصورة الرمادية
    gray_screenshot = cv.cvtColor(screenshot, cv.COLOR_BGR2GRAY)

    # تطبيق Canny Edge Detection على صورة اللعبة
    edge_screenshot = cv.Canny(gray_screenshot, 50, 150)

    # البحث عن الأسهم والضغط عليها
    keys_pressed = 0
    for direction, template in arrows.items():
        if template is None:
            continue

        result = cv.matchTemplate(edge_screenshot, template, cv.TM_CCOEFF_NORMED)
        threshold = 0.8  # تعديل الحساسية حسب الحاجة
        locations = np.where(result >= threshold)

        # إذا تم العثور على السهم، اضغط على الزر المناسب
        for loc in zip(*locations[::-1]):  # تحويل إحداثيات المطابقة
            print(f"✅ تم العثور على {direction}، يتم الضغط عليه الآن")
            pyautogui.press(direction)  # الضغط على الزر
            keys_pressed += 1

            # إضافة تأخير عشوائي بين 200-500 مللي ثانية
            delay = random.uniform(0.2, 0.5)
            sleep(delay)

            # إذا تجاوز الوقت الإجمالي 3 ثوانٍ، توقف
            if time() - start_time > 3:
                print("⏳ تجاوز الزمن 3 ثوانٍ، التوقف عن الضغط!")
                break

    # عرض النافذة بعد تطبيق Edge Detection
    cv.imshow("Edge Detection", edge_screenshot)

    # طباعة معدل الإطارات
    print("FPS {}".format(1 / (time() - loop_time)))
    loop_time = time()

    # الخروج عند الضغط على 'q'
    if cv.waitKey(1) == ord("q"):
        cv.destroyAllWindows()
        break

print("✅ تم الانتهاء.")
