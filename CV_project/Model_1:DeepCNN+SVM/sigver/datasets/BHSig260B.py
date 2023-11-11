import os
from sigver.datasets.base import IterableDataset
from skimage.io import imread
from skimage import img_as_ubyte


class BHSig260BengaliDataset(IterableDataset):
    """ Helper class to load the BHSig260-Bengali dataset
    """
    def __init__(self, path):
        self.path = path
        self.users = list(range(1, 100+1))

    @property
    def genuine_per_user(self):
        return 24

    @property
    def skilled_per_user(self):
        return 30

    @property
    def simple_per_user(self):
        return 0

    @property
    def maxsize(self):
        return 435, 1329

    def get_user_list(self):
        return self.users

    def iter_genuine(self, user):
        """ Iterate over genuine signatures for the given user"""
        files = []
        for i in range(1, 24 + 1):
            if i < 10:
                i = "0" + str(i)
                
            files.append('B-S-{}-{}-{}.tif'.format(user, 'G', i))
        for f in files:
            full_path = os.path.join(self.path, 'Genuine', f)
            img = imread(full_path, as_gray=True)
            yield img_as_ubyte(img), f

    def iter_forgery(self, user):
        """ Iterate over skilled forgeries for the given user"""
        files = []
        for i in range(1, 30 + 1):
            if i < 10:
                i = "0" + str(i)
            files.append('B-S-{}-{}-{}.tif'.format(user, 'F', i))
        for f in files:
            full_path = os.path.join(self.path, 'Forgery', f)
            img = imread(full_path, as_gray=True)
            yield img_as_ubyte(img), f
        
    def iter_simple_forgery(self, user):
        yield from ()  # No simple forgeries
