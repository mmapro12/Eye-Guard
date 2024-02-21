import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

cam_num = 1
quit_button = "q"

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
detector = FaceMeshDetector(maxFaces=1)

if not cap.isOpened(): quit(f"Camera `{cam_num}` can't open!")


while True:
    success, frame = cap.read()
    if not success: quit(f"Camera not useable!")

    # Finding faces
    frame, faces = detector.findFaceMesh(frame, draw=False)

    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]

        cv2.line(frame, pointLeft, pointRight, (0, 255, 0), 2)
        cv2.circle(frame, pointLeft, 5, (255, 0, 0), cv2.FILLED)
        cv2.circle(frame, pointRight, 5, (255, 0, 0), cv2.FILLED)
        

    cv2.imshow("Eye Guard", frame)
    if cv2.waitKey(1) == ord(quit_button):
        break


cv2.release()
cv2.destroyAllWindows()
