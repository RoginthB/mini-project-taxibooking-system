class Taxi:
    @staticmethod
    def taxi(id):
        taxi_id = id
        curend_point = 'A'
        free_time = 6
        earnings = 0
        details = [taxi_id, curend_point, free_time, earnings]
        return details


class BookingTaxi(Taxi):
    def __init__(self, pickup_point, drop_point, pickup_time, points):
        self.pickup_point = pickup_point
        self.drop_point = drop_point
        self.pickup_time = pickup_time
        self.n = 4
        self.lst = points
        self.taxis = self.create_a_taxi()
        self.distance_of_point = self.distance_of_point()

    def create_a_taxi(self):
        taxis = []
        for i in range(1, self.n + 1):
            taxis.append(BookingTaxi.taxi(i))
        return taxis

    def key_value1(self):
        return (self.lst[1]),

    def key_value2(self):
        return (self.lst[2]),

    def key_value3(self):
        return (self.lst[3]),

    def earning_based_sort(self):
        sort_of_earning_taxi = self.taxis
        a=sort_of_earning_taxi.sort(key=self.key_value3)
        return a

    def near_location_sort(self):
        sort_of_near_point = self.taxis
        a=sort_of_near_point.sort(key=self.key_value1)
        return a

    def free_time(self):
        sort_of_free_time = self.taxis
        a=sort_of_free_time.sort(key=self.key_value2)
        return a

    def distance_of_point(self):
        lst = self.lst
        a = lst.index(self.pickup_point)
        b = lst.index(self.drop_point)
        if a < b:
            return b - a
        else:
            return a - b

    def booking(self):
        for i in range(self.n):
            x = self.taxis[i]
            if (x[2] <= self.pickup_time) and (x[2] <= self.pickup_time + self.distance_of_point):
                x[1] = self.drop_point
                x[2] = self.pickup_point + self.distance_of_point
                x[3] = (self.distance_of_point - 5) * 10 + 100
                result = x
                self.taxis.insert(i, result)
                break
        return self.taxis
