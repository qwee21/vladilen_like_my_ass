import math

class Point3D:
    def __init__(self, x=3, y=3, z=4):
        self.x = x
        self.y = y
        self.z = z

    def distance_to_point(self, other_point):
        dx = self.x - other_point[0]
        dy = self.y - other_point[1]
        dz = self.z - other_point[2]
        distance = math.sqrt(dx**2 + dy**2 + dz**2)
        return distance

    def distance_to_origin(self):
        origin = [0, 0, 0]
        return self.distance_to_point(origin)

    def find_closest_point(self, points):
        return min(points, key=lambda point: self.distance_to_point(point))

    def to_spherical_coordinates(self):
        radius = self.distance_to_origin()
        theta = math.atan2(self.y, self.x)
        if radius != 0:
            phi = math.acos(self.z / radius)
        else:
            phi = 0
        return radius, math.degrees(theta), math.degrees(phi)

    def to_cylindrical_coordinates(self):
        radius = math.sqrt(self.x**2 + self.y**2)
        theta = math.atan2(self.y, self.x)
        z = self.z

        return radius, math.degrees(theta), z


