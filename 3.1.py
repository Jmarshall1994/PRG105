x=input("What is the day of the week you need?");
List_days={'0':'MONDAY',   '1':'TUESDAY',   '3':'WEDNESDAY',   '4':'THURSDAY', '5':'FRIDAY',   '6':'SATURDAY',  '7':'SUNDAY'};
try:
    print(List_days[x]);
except KeyError:
    print('invalid input');
