"""
Use RealSense camera to create a video stream and depth colormap.

Objects in the depth colormap that are bluer in color are closer, and those
objects farther away will be shifted toward the red color spectrum. This app
requires a Intel RealSense camera to be connected on usb 3.0 port to work.
"""
import time
import sys
import numpy as np
import edgeiq
from edgeiq import realsense


def main():
    """Run RealSense Camera."""
    serial_numbers = []
    text = "RealSense Camera"

    serial_numbers = edgeiq.realsense.enumerate_realsense_cameras()
    if not serial_numbers:
        sys.exit("Program Ending No RealSense Camera Found")

    try:
        with edgeiq.realsense.RealSense(serial_numbers[0]) as video_stream, \
                edgeiq.Streamer() as streamer:
            print("starting RealSense camera")
            # let camera warm up
            time.sleep(2.0)

            # loop over to get frames
            while True:
                # Get color and depth images
                rs_frame = video_stream.read()

                combined = np.vstack((rs_frame.image,
                                      rs_frame.render_depth_image()))

                streamer.send_data(combined, text)

                if streamer.check_exit():
                    break

    finally:
        print("Closing RealSense Camera")
        video_stream.stop()
        streamer.close()
        print("Program Ending")


if __name__ == "__main__":
    main()
