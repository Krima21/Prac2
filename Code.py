k = int(input())
room_number_list = list(map(int, input().split()))
room=set(room_number_list)
for i in room:
     if room_number_list.count(i)==1:
         print(i)
