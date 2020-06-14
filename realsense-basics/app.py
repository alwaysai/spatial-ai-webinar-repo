import time
import edgeiq
import sys
import numpy as np
"""
Use this app with the RealSense camera to create a video stream
and depth_colormap were objects that are blue are closer,
and those farther away will be shifted toward the red color
spectrum
"""


def main():
    serial_numbers = []
    text = "RealSense Camera"

    serial_numbers = edgeiq.enumerate_realsense_cameras()
    if not serial_numbers:
        sys.exit("Program Ending No RealSense Camera Found")


    try:
        with edgeiq.RealSense(serial_numbers[0]) as video_stream, \
                edgeiq.Streamer() as streamer:
                print("starting RealSense camera")
                # let camera warm up
                time.sleep(2.0)

                # loop over to get frames
                while True:
                    # Get color and depth images
                    depth_image, color_image = video_stream.read()

                    depth_colormap = video_stream.render_depth_image(depth_image)

                    combined = np.vstack((color_image, depth_colormap))

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
