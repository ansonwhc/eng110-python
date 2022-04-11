class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Location (latitude={self.latitude}, longitude={self.longitude}"

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"


if __name__ == "__main__":
    Bham_Academy = Location(52.488647, -1.887249)
    print(Bham_Academy.__str__())
    print(Bham_Academy.__repr__())
