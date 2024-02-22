import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector


def main():
    if cv2.VideoCapture(1, cv2.CAP_DSHOW):
        cam_num = 1
    else:
        cam_num = 0
    quit_button = "q"

    cap = cv2.VideoCapture(cam_num, cv2.CAP_DSHOW)
    detector = FaceMeshDetector(maxFaces=1)

    if not cap.isOpened():
        quit(f"Camera `{cam_num}` can't open!")

    while True:
        success, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))
        if not success:
            quit(f"Camera not usable!")

        # Finding faces
        frame, faces = detector.findFaceMesh(frame, draw=False)

        if faces:
            face = faces[0]
            pointLeft = face[145]
            pointRight = face[374]

            # Drawing on the eyes
            # cv2.line(frame, pointLeft, pointRight, (0, 255, 0), 2)
            # cv2.circle(frame, pointLeft, 5, (255, 0, 0), cv2.FILLED)
            # cv2.circle(frame, pointRight, 5, (255, 0, 0), cv2.FILLED)

            w, _ = detector.findDistance(pointLeft, pointRight)
            W = 6.3
            # print(w)

            # Finding Focal Length
            # d = 62
            # f = (w * d) / W

            # IMPORTANT: F (Finding Distance)
            f = 600
            d = W * f / w
            print(d)

            # Notification System

            # Depth is close
            if d <= 35:
                cvzone.putTextRect(frame, "Be careful", (20, 70), 5, 3, (0, 0, 255))
            else:
                cvzone.putTextRect(frame, "Good", (20, 70), 5, 3, (0, 255, 0))

            # Adding text in the video
            cvzone.putTextRect(frame,
                               f"Depth: {int(d)} cm",
                               (face[10][0] - 100, face[10][1] - 50),
                               scale=2
                               )

        cv2.imshow("Eye Guard", frame)
        if cv2.waitKey(1) == ord(quit_button):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

# TODO: Resolution problem
