
"""
Object Detection using Intel RealSense Cameara.

Use object detection to detect objects and the RealSense camera to get
the distances in meters to those objects in realtime. The types
of objects detected can be changed by selecting different models.  This app
requires a Intel RealSense camera to be connected on usb 3.0 port to work.

To change the computer vision model, the engine and accelerator,
and add additional dependencies read this guide:
https://alwaysai.co/docs/application_development/configuration_and_packaging.html
"""

import edgeiq
import time


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
        with edgeiq.RealSense() as video_stream, \
                edgeiq.Streamer() as streamer:

            print("starting RealSense camera")
            time.sleep(2.0)

            # loop detection
            while True:
                rs_frame = video_stream.read()
                results = obj_detect.detect_objects(rs_frame.image,
                                                    confidence_level=.6)
                frame = edgeiq.markup_image(rs_frame.image,
                                            results.predictions,
                                            colors=obj_detect.colors)

                # Generate text to display on streamer
                text = ["Model: {}".format(obj_detect.model_id)]
                text.append(
                        "Inference time: {:1.3f} s".format(results.duration))
                text.append("Objects:")

                for i, prediction in enumerate(results.predictions):
                    text.append("{}: {:2.1f}% Distance = {:2.2f}m".format(
                        prediction.label, prediction.confidence * 100,
                        rs_frame.compute_object_distance(
                            prediction.box)))

                streamer.send_data(frame, text)

                if streamer.check_exit():
                    break

    finally:
        print("Program Ending")


if __name__ == "__main__":
    main()
