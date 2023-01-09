import googlemaps
gmaps = googlemaps.Client(key='AIzaSyD6HqlWEEDsiS41-aoBRdZmUunsMYL-VkI')

print("vi tri :")
source = input()
print("vi tri nha hang:")
dest = input()
my_dist = gmaps.distance_matrix(source,dest)['rows'][0]['elements'][0]
distance = my_dist['distance']['text']
time  = my_dist['duration']['text']
print("khoang cach la : "+ distance)
print("thoi gian : "+ time)


