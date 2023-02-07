import googlemaps
gmaps = googlemaps.Client(key='AIzaSyB5lmWIJS5mYWqzlbTZs1UVeh4zsRjLf-M')

print("vi tri :")
source = input()
print("vi tri nha hang:")
dest = input()
my_dist = gmaps.distance_matrix(source,dest)['rows'][0]['elements'][0]
distance = my_dist['distance']['text']
time  = my_dist['duration']['text']
print("khoang cach la : "+ distance)
print("thoi gian : "+ time)


# import googlemaps
# gmaps = googlemaps.Client(key='AIzaSyB5lmWIJS5mYWqzlbTZs1UVeh4zsRjLf-M')

# def calDist(data):
#     dis_matrix = []
#     time_matrix = []
#     userloc = input()
#     for i in range(data.shape[0]):
#     # for i in range(n):
#         # data = pd.read_csv('data/dss_data_test.csv')
#         my_dist = gmaps.distance_matrix(userloc,data['location'].iloc[i])['rows'][0]['elements'][0]
#         distance = my_dist['distance']['text']
#         time = my_dist['duration']['text']
#         dis_matrix.append(distance)
#         time_matrix.append(time)
        
#     return dis_matrix, time_matrix    