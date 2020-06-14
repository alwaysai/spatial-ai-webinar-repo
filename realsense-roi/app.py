import time
import edgeiq
import numpy as np
"""
Using the RealSense camera to do object detection and find the distances from the camera
to the detected objects
"""


def main():
    obj_detect = edgeiq.ObjectDetection(
            "alwaysai/ssd_mobilenet_v2_coco_2018_03_29")
    obj_detect.load(engine=edgeiq.Engine.DNN)

    print("Loaded model:\n{}\n".format(obj_detect.model_id))
    print("Engine: {}".format(obj_detect.engine))
    print("Accelerator: {}\n".format(obj_detect.accelerator))
    print("Labels:\n{}\n".format(obj_detect.labels))


    try:
        with edgeiq.RealSense() as video_stream, \
                edgeiq.Streamer() as streamer:

            print("starting RealSense camera")
            time.sleep(2.0)

            # loop detection
            while True:
                distances = []
                depth_image, color_image = video_stream.read()

                roi = video_stream.roi(depth_image, color_image, min=None, max=0.9)

                # frame = edgeiq.resize(color_image, width=416)
                results = obj_detect.detect_objects(roi, confidence_level=.6)
                roi = edgeiq.markup_image(
                        roi, results.predictions, colors=obj_detect.colors)
                for prediction in results.predictions:
                    distances.append(video_stream.compute_object_distance(prediction.box,depth_image))


                # Generate text to display on streamer
                text = ["Model: {}".format(obj_detect.model_id)]
                text.append(
                        "Inference time: {:1.3f} s".format(results.duration))
                text.append("Objects:")

                for i, prediction in enumerate(results.predictions):
                    text.append("{}: {:2.1f}% Distance = {:2.2f}m".format(
                        prediction.label, prediction.confidence * 100, distances[i]))

                streamer.send_data(roi, text)


                if streamer.check_exit():
                    break

    finally:
        print("Program Ending")


if __name__ == "__main__":
    main()
