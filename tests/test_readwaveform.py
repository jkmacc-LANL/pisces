import tempfile
import numpy as np
from numpy.testing import assert_array_equal

import pisces.io.readwaveform as rwf


def test_read_s3():
    # 100 big-endian 3-byte samples from an s3 file
    BYTS = (b'\x00\x01\x02\x00\x00\xc4\x00\x00}\x00\x00P\xff\xff\x08\xff\xfe\xfd\x00\x00\xa3\x00'
            b'\x00\xa6\xff\xfe\xca\x00\x00\xca\x00\x01\x9d\xff\xff\x10\xff\xff5\xff\xffT\xff\xffV'
            b'\xff\xff\xce\x00\x00J\x00\x00\xf4\x00\x01g\x00\x01\x7f\x00\x00\x01\xff\xff!\x00\x00='
            b'\x00\x00\xb3\x00\x00,\x00\x00c\x00\x00\xb6\x00\x00z\xff\xff\x98\xff\xff.\x00\x00@\x00'
            b'\x01\x1f\x00\x00\xc0\x00\x00\x11\x00\x01\x18\x00\x01b\xff\xff\xc9\x00\x00\x14\x00'
            b'\x01A\x00\x01q\x00\x00u\xff\xff\xa8\x00\x00\x8a\xff\xff\xe2\xff\xff\x11\x00\x01\r'
            b'\x00\x00\x86\xff\xfe\xf3\x00\x00\xd9\x00\x00I\xff\xff1\x00\x01\xdd\x00\x01s\x00\x00Q'
            b'\x00\x01\xab\x00\x00\xb0\x00\x00\x1b\x00\x00\xb0\xff\xff\x07\xff\xff\xd8\x00\x01\x8c'
            b'\xff\xffh\xff\xffo\x00\x00#\xff\xff\xae\xff\xff\xc5\xff\xff`\x00\x00.\x00\x01\x13'
            b'\x00\x00\xb9\xff\xff\xf9\x00\x00(\xff\xff\xc2\xff\xfe\xe9\xff\xff\xca\x00\x01%\x00'
            b'\x00\xe3\xff\xffO\xff\xfe\x82\x00\x00\x00\x00\x01\x17\xff\xff\xab\x00\x00A\x00\x00e'
            b'\xff\xff\xb4\x00\x00,\x00\x00Q\x00\x01\x80\xff\xfe\xfd\xff\xfd\xb0\xff\xff\xad\x00'
            b'\x00\x10\x00\x01\xe8\x00\x01\x15\xff\xff\xcf\x00\x00\xde\x00\x00\x9f\xff\xff\x85\xff'
            b'\xff5\x00\x01\x8f')

    # 100 corresponding values from the s3 file
    data = np.array([258, 196, 125, 80, -248, -259, 163, 166, -310, 202, 413, -240, -203, -172,
                     -170, -50, 74, 244, 359, 383, 1, -223, 61, 179, 44, 99, 182, 122, -104, -210,
                     64, 287, 192, 17, 280, 354, -55, 20, 321, 369, 117, -88, 138, -30, -239, 269,
                     134, -269, 217, 73, -207, 477, 371, 81, 427, 176, 27, 176, -249, -40, 396,
                     -152, -145, 35, -82, -59, -160, 46, 275, 185, -7, 40, -62, -279, -54, 293,
                     227, -177, -382, 0, 279, -85, 65, 101, -76, 44, 81, 384, -259, -592, -83, 16,
                     488, 277, -49, 222, 159, -123, -203, 399], dtype=np.int32)

    with tempfile.SpooledTemporaryFile() as f:
        f.write(BYTS)
        f.seek(0)
        s3 = rwf.read_s3(f, 0, 100)

    assert_array_equal(s3, data)
