from numpy import array, mean, binary_repr, zeros
from numpy.random import randint
from scipy.ndimage import zoom

from arpy.hamming import (encode, decode,
                          msg_size, data_size)

marker_size = msg_size + 2
max_id = 2 ** (msg_size * data_size)


class HammingMarker(object):
    def __init__(self, id, contours=None):
        if not 0 <= id < max_id:
            msg = 'Id must be {} <= id < {} (id={})'.format(0, max_id, id)
            raise ValueError(msg)

        self.id = id
        self.hamming_code = self._encode_id(self.id)
        self.contours = contours

    @property
    def center(self):
        if self.contours is None:
            return None

        return mean(self.contours, axis=0)

    def toimage(self, size=marker_size):
        img = zeros((marker_size, marker_size))
        img[1:-1, 1:-1] = self.hamming_code
        img = 1 - img

        scale = size / float(marker_size)
        return zoom(img, zoom=scale, order=0)

    @classmethod
    def generate(cls):
        return HammingMarker(id=randint(max_id))

    def _encode_id(self, id):
        s = binary_repr(id, width=msg_size * data_size)
        B = array(list(s), dtype=int).reshape(msg_size, data_size)
        return encode(B)
