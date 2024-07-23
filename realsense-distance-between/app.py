"""
Get distances between detected objects using Intel RealSense Cameara.

Use object detection to detect objects and the RealSense camera to get
the distances in meters to those objects in realtime. The types
of objects detected can be changed by selecting different models.  This app
requires a Intel RealSense camera to be connected on usb 3.0 port to work.
The RealSenseFrame.compute_distance_between_objects Get distance in meters
between two detected objects in 3D space.

To change the computer vision model, the engine and accelerator,
and add additional dependencies read this guide:
https://docs.alwaysai.co/application_development/application_configuration.html
"""
import time
import cv2
import edgeiq
from edgeiq import realsense


def midpoint(pointA, pointB):
    """Get midpoint between two objects."""
    return((pointA[0] + pointB[0]) * 0.5, (pointA[1] + pointB[1]) * 0.6)


def main():
    """Run Object Detector."""
    obj_detect = edgeiq.ObjectDetection(
            "alwaysai/ssd_mobilenet_v2_coco_2018_03_29")
    obj_detect.load(engine=edgeiq.Engine.DNN)

    print("Loaded model:\n{}\n".format(obj_detect.model_id))
    print("Engine: {}".format(obj_detect.engine))
    print("Accelerator: {}\n".format(obj_detect.accelerator))
    print("Labels:\n{}\n".format(obj_detect.labels))

    try:
        with edgeiq.realsense.RealSense() as video_stream, \
                edgeiq.Streamer() as streamer:
            print("Starting RealSense camera")
            time.sleep(2.0)

            # loop detection
            while True:
                rs_frame = video_stream.read()
                segments = []
                mid_point = []
                center_object_one = []
                center_object_two = []

                results = obj_detect.detect_objects(rs_frame.image,
                                                    confidence_level=.6)

                if len(results.predictions) > 1:
                    for i in range(len(results.predictions)):
                        for j in range((i+1), len(results.predictions)):
                            segments.append(rs_frame.compute_distance_between_objects(
                                results.predictions[i].box, results.predictions[j].box))
                            center_object_one.append(results.predictions[i].box.center)
                            center_object_two.append(results.predictions[j].box.center)
                            mid_point.append(midpoint(results.predictions[i].box.center,
                                             results.predictions[j].box.center))

                # Generate text to display on streamer
                text = ["Model: {}".format(obj_detect.model_id)]
                text.append(
                        "Inference time: {:1.3f} s".format(results.duration))
                text.append("Segment Distnces in Meters:")

                for i, segment in enumerate(segments, 0):
                    text.append("Segment {}: = {:1.2} Meters".format(i,
                                                                     segment))
                    cv2.putText(rs_frame.image,
                                '{:1.2} Meters'.format(segment),
                                (int(mid_point[i][0]),
                                 int(mid_point[i][1]-50)),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                    cv2.arrowedLine(rs_frame.image,
                                    (int(center_object_one[i][0]),
                                     int(center_object_one[i][1])),
                                    (int(center_object_two[i][0]),
                                     int(center_object_two[i][1])),
                                    color=(0, 0, 255), thickness=3)

                streamer.send_data(rs_frame.image, text)

                if streamer.check_exit():
                    break

    finally:
        video_stream.stop()
        print("Program Ending")


if __name__ == "__main__":
    main()
