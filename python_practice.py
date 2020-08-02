#counties = ["Arapahoe", "Denver", "Jefferson"]
#double equals sign '==' is a comparison operator or Boolean operator which means 'equal to'
#if counties[1] == 'Denver':
#    print(counties[1])

#If else statement practice
#temperature = int(input("What is the temperature outside?"))
#if temperature >80:
#    print("Turn on AC")
#else:
#    print("Open the windows")

# #what is the score
# score = int(input("What is your test score?"))

#Determine Grade
#if score >= 90:
#    print('your grade is an A')
#else:
#    if score >= 80:
    #     print('your grade is a B')
    # else:
    #     if score >= 70:
    #         print('your grade is a C')
    #     # else:
    #         if score >= 60:
    #             print('your grade is a D')
    #         else:
    #             print('your grade is an F')

# #if-elif-else practice

# #what is the score
# score = int(input("what is your test score?"))

# #determine grade
# if score >= 90:
#     print("your grade is an A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# for k, v in [(90, 'A'), (80, 'B'), (70, 'c')]:
#     if score >= k:
#         print(f"your grade is trash ({v})")
#         break

# #Membership operators practice
# counties = ['Arapahoe', 'Denver', 'Jefferson']
# if 'El Paso' in counties:
#     print('El Paso is in the list of counties')
# else:
#     print('El Paso is not in the list of counties')
    
# #use and operator
# if 'Arapahoe' in counties and 'El Paso' in counties:
#     print('Arapahoe and El Paso are in the list of counties')
# else:
#     print('Arapahoe or El Paso is not in the list of counties')

# #use or operator
# if 'Arapahoe' in counties or 'El Paso' in counties:
#     print('Arapahoe or El Paso is in the list of counties')
# else:
#     print('Neither Arapahoe nor El Paso are in the list of counties')

# #not operator
# if 'Arapahoe' in counties and 'El Paso' not in counties:
#     print ('Only Arapahoe is in the list of counties')
# else:
#     print('Arapahoe is in the list of counties and El Paso is not in the list of counties')

# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1

# counties = ["Arapahoe", "Denver", "Jefferson"]
# for county in counties:
#     print(county)

# #variable i is used to indicate the index, or the values 0, 1, and 2 is the length of the counties list
# #inside the range() function, we get the length of the list of counties
# #when we iterate through the list where variable i is equal to 0, the 0 is passed into the print(counties[i]) statement, where i = 0, and Arapahoe is printed
# for i in range(len(counties)):
#     print(counties[i])

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(county)

# #when using the Keys() method, it doesn't matter what variable name we use in the for loop. The keys() method will print each key in order.
# for county in counties_dict.keys():
#     print(county)

# #using the values method
# for voters in counties_dict.values():
#     print(voters)

# #using dictionary_name[key] to get value for the key
# for county in counties_dict:
#     print(counties_dict[county])

# #another method we can use to get the values of a key is to use the get() method on the dictionary in the for loop
# for county in counties_dict:
#     print(counties_dict.get(county))

# #if we want to print the key-value pair of the dictionary, we use the items() method in the for loop
# for county, voters in counties_dict.items():
#     print(county, 'county has', voters, 'registered voters.')
#     print(f"{county} county has {voters} registered voters.")

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
# for county_dict in voting_data:
#     print(county_dict)

# for i in range(len(voting_data)):
#     print(voting_data[i])

# #get the values from a list of dictionaries
# #first, use for loop to retrieve each dictionary
# for county_dict in voting_data:
#     #second for loop, use the values() method on the variable county_dict to reference the data in the second for loop in order to get each value
#     for value in county_dict.values():
#         print(value)

# #to retrieve the number of registered voters from each dictionary
# for county_dict in voting_data:
#     print(county_dict['registered voters'])

# #if we only want to print the county name from each dictionary, we can use:
# for county_dict in voting_data:
#     print:(county_dict['county'])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county, voters in counties_dict.items():
    print(f'{county} county has {voters} registered voters.')

voting_data = [
    {
        "county": "Arapahoe",
        "registered_voters": 422829,
    }, 
    {"county":"Denver", "registered_voters": 463353}, 
    {"county":"Jefferson", "registered_voters": 432438}
]

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']} registered voters.")