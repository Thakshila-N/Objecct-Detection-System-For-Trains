import cv2
import winsound

from gui_buttons import Buttons



# Initialize Button
button = Buttons()
button.add_button("elephant", 20, 20)
button.add_button("person", 20, 100)

colors = button.colors

# Opencv DNN
net = cv2.dnn.readNet("dnn_model/yolov4-tiny.weights", "dnn_model/yolov4-tiny.cfg")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(320, 320), scale=1/255)

# Load class lists
classes = []
with open("dnn_model/classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)

print("objects list")
print(classes)

# Initialize camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


def click_button(event, x, y, flags, params):
    global button_elephant
    if event == cv2.EVENT_LBUTTONDOWN:
        button.button_click(x, y)



# Create window
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", click_button)


while True:
    # Get frames
    ret, frame = cap.read()

    # Get active button list
    active_buttons = button.active_buttons_list()
    print("Active buttons", active_buttons)



    # Object Detection
    (class_ids, scores, bboxes) = model.detect(frame)
    for class_id, score, bbox in zip(class_ids, scores, bboxes):
        (x, y, w, h) = bbox
        class_name = classes[class_id]

        if class_name in active_buttons:
            cv2.putText(frame, class_name, (x, y - 10), cv2.FONT_HERSHEY_PLAIN, 2, (200, 8, 50), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (200, 8, 50), 3)
            winsound.Beep(500, 200) # beep sound


# Display Button
    button.display_buttons(frame)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()