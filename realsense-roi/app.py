"""
Region of interest Object Detection using Intel RealSense Cameara.

Use object detection to detect objects and the RealSense camera to get
the distances in meters to those objects in realtime. The types
of objects detected can be changed by selecting different models.  This app
requires a Intel RealSense camera to be connected on usb 3.0 port to work.
The RealSenseFrame.roi method captures a region of interest (ROI) within
frame or image and detects objects and their distances from cameara witin
that region.

        This function supports different behavior based on the inputs:
        * When only min is set pixels closer than min are removed.
        * When only max is set pixels further than max are removed.
        * When both min and max are set pixels closer than min and
        further than max are removed.

        The removed pixels are replaced by values of the `shade` parameter
        in grayscale.

To change the computer vision model, the engine and accelerator,
and add additional dependencies read this guide:
https://alwaysai.co/docs/application_development/configuration_and_packaging.html
"""
import time
import edgeiq
from edgeiq import realsense


def main():
    """Run ROI Object Detector."""
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

            print("starting RealSense camera")
            time.sleep(2.0)

            # loop detection
            while True:
                rs_frame = video_stream.read()
                roi = rs_frame.roi(min=None, max=0.9)

                # frame = edgeiq.resize(color_image, width=416)
                results = obj_detect.detect_objects(roi, confidence_level=.6)
                frame = edgeiq.markup_image(
                        roi, results.predictions, colors=obj_detect.colors)

                # Generate text to display on streamer
                text = ["Model: {}".format(obj_detect.model_id)]
                text.append(
                        "Inference time: {:1.3f} s".format(results.duration))
                text.append("Objects:")

                for prediction in results.predictions:
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
