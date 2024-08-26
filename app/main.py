from __future__ import annotations
from math import acos, degrees, radians, cos, sin, ceil


class Vector:
    def __init__(self, x_coord: int | float, y_coord: int | float) -> None:
        self.x_coord = round(x_coord, 2)
        self.y_coord = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(
            self.x_coord + other.x_coord,
            self.y_coord + other.y_coord
        )

    def __sub__(self, other: Vector) -> Vector:
        return Vector(
            self.x_coord - other.x_coord,
            self.y_coord - other.y_coord
        )

    def __mul__(self, other: int | float | Vector) -> Vector | int | float:
        if type(other) in (int, float):
            return Vector(self.x_coord * other, self.y_coord * other)
        return (self.x_coord * other.x_coord) + (self.y_coord * other.y_coord)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return cls(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return (self.x_coord ** 2 + self.y_coord ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        vector_length = self.get_length()
        return Vector(
            self.x_coord / vector_length,
            self.y_coord / vector_length
        )

    def angle_between(self, other_vector: Vector) -> int:
        return ceil(
            degrees(
                acos(
                    (self * other_vector)
                    / (self.get_length() * other_vector.get_length())
                )
            )
        )

    def get_angle(self) -> int:
        positive_y = Vector(0, 1)
        cos_theta = self * positive_y / self.get_length()
        angle = int(degrees(acos(cos_theta)))

        return angle

    def rotate(self, degrees_: int) -> Vector:
        radian = radians(degrees_)
        cos_theta = cos(radian)
        sin_theta = sin(radian)

        new_x = self.x_coord * cos_theta - self.y_coord * sin_theta
        new_y = self.x_coord * sin_theta + self.y_coord * cos_theta

        return Vector(new_x, new_y)
