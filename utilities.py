class PointTransformer():
    def __init__(self, min_corner, max_corner, shift, aspect, width, height):
        self._min_corner = min_corner  # this is tuple
        self._max_corner = max_corner  # this is tuple
        self._shift = shift  # and this tuple too
        self._aspect = aspect
        self._width = width
        self._height = height

        self._x_coeff = self._height * self._aspect if self._aspect <= self._width / self._height else self._width
        self._y_coeff = self._height if self._aspect <= self._width / self._height else self._width / self._aspect

    def transform(self, point):
        return ((point[0] - self._min_corner[0]) * self._x_coeff / (self._max_corner[0] - self._min_corner[0]) + self._shift[0],
                (point[1] - self._min_corner[1]) * self._y_coeff / (self._max_corner[1] - self._min_corner[1]) + self._shift[1])

    def transform_inverse(self, point):
        return ((point[0] - self._shift[0]) * (self._max_corner[0] - self._min_corner[0]) / self._x_coeff + self._min_corner[0],
                (point[1] - self._shift[1]) * (self._max_corner[1] - self._min_corner[1]) / self._y_coeff + self._min_corner[1])
