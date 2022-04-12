# 1. Copy()
Bikes={'Bike_1':'CT100','Bike_2':'HeroHonda','Bike_3':'Yamaha'}
Two_wheelers = Bikes.copy()
print("All two wheelers in the market: ", Two_wheelers)


# 2. Get()
print('The second bike:', Bikes.get('Bike_2'))


# 3. Update()
Bikes.update({'Bike_4': 'TVS'})
print("List of bikes in the market after update 1:", Bikes)



# 4. Items()
print('All bikes:', Bikes.items())


# 5. keyes()
print('All bikes:', Bikes.keys())


# 6. sort()
print('All bikes:',sorted(Bikes.items()))


# 7. values()
print('The second bike:',Bikes.values())



# 8. len()
print('Overall number of bikes:',len(Bikes))

# 9. str()
Bikes_str = str(Bikes)
print('Format of Bikes datatype:',type(Bikes_str))