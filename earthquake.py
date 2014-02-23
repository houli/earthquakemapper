import time

class Earthquake(object):


    def __init__(self, identifier, magnitude, place, longitude, latitude, time, depth):
        self.identifier = identifier
        self.magnitude = magnitude
        self.place = place
        self.longitude = longitude
        self.latitude = latitude
        self.time = time
        self.depth = depth

    def get_magnitude(self):
        return self.magnitude

    def get_place(self):
        return self.place

    def get_longitude(self):
        return self.longitude

    def get_latitude(self):
        return self.latitude

    def get_time(self):
        return time.strftime("%D %H:%M", time.localtime(int(self.time / 1000)))

    def get_depth(self):
        return self.depth

    def get_id(self):
        return self.identifier