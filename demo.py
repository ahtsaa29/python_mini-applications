import PySimpleGUI as pg
import cv2

cam = cv2.VideoCapture(0)

layout = [[pg.Text(text="Demo Software")]]

another_layout =[[pg.Button("Button 1"),pg.Button("Button 2")]]

button1_layout = [[pg.Text("Name"),pg.Input(key="name")],[pg.Button("Capture"),pg.Button("bye")]]

window = pg.Window("Demo", another_layout ,size=(300,300))


while True:
    event, values = window.read()
    print(event, values)
    # if event in (None, 'Exit'):
    #     break
    if event == pg.WIN_CLOSED or event == 'Exit':
      window.close()

    if event == "Button 2":
        print(" i am 2")

    if event == "Button 1":
        print(" i am 1")
        window = pg.Window("Button 1", button1_layout ,size=(300,300))

    if event == "Capture":
        name = values['name']
        print(name)
        check, frame = cam.read()
        cv2.imshow(name, frame)
        key = cv2.waitKey(1)
        if key == 27:
            break

    