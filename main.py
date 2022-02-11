#
# The are 6 points(A,B,C,D,E,F) 15 KM apart 60 min travel between each, n taxis all taxis at A starting
# 100 rs for first 5 KM and then 10 for each of the further KMs, rate from pickup to drop only
# pickup time example : 9 hrs, 15 hrs
# When a customer books a Taxi, a free taxi at that point is allocated
# -If no free taxi is available at that point, a free taxi at the nearest point is allocated.
# -If two taxi’s are free at the same point, one with lower earning is allocated
# -If no taxi is free at that time, booking is rejected
# Input 1:
# Customer ID: 1
# Pickup Point: A
# Drop Point: B
# Pickup Time: 9
# Output 1:
# Taxi can be allotted.
# Taxi-1 is allotted

# # import Taxi_details
import Taxi_booking

print("--------- Choose you operation ----------")
print(" 1 - Booking a Taxi  ")
print(" 0 - Show a details of Taxi ")
a = int(input("enter you task No. : "))
point = ['A', 'B', 'C', 'D', 'E', 'F']
if a == 1:
    x = True
    while x:
        pickup_point = input("enter the pickup point: ")
        drop_point = input("enter the drop point : ")
        pickup_time = input("enter the pickup time : ")
        if (pickup_point in point) and (drop_point in point):
            t = Taxi_booking.BookingTaxi(pickup_point, drop_point, pickup_time,point)
            taxis = t.create_a_taxi()
            print(taxis)
            print(" distances point :")
            t.distance_of_point()
            print(" free time : ")
            t.free_time()
            print(" near location sort : ")
            t.near_location_sort()
            print("earning sort : ")
            t.earning_based_sort()





            print("--------- Choose you operation ----------")
            print(" 1 - continue booking  ")
            print(" 0 - stop booking ")
            y = int(input("enter you task No. : "))
            if y == 1:
                x = True
            else:
                x = False
elif a == 0:
    print("wating for you resalut")
else:
    print("you input is not valid")
