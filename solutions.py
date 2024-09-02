#filter for those under 10000 income
lowIncome = [
  person for person in data if person['Income'] <= 10000
]
#filter for those with over 4 children
greaterThan4Children = [
  person for person in data if person['numberOfChildren'] > 4
]
#filter for those who are disabled or of veteran status
disabledOrVeteran = [
  person for person in data if person['disabledStatus'] != "None" or person['veteranStatus'] == "Yes"
]

print("Dataset size:" + {len(data)})
print("Low income:" + len(lowIncome)})
print("More than 4 children:" + len(greaterThan4Children))
print("Disabled or veteran status:" + {len(disabledOrVeteran)})

#Filter for just unemployed people in dataset
unemployed_filter = [person for person in data if person['employmentStatus'] == 'Unemployed']

housing_alloc = []
#Append up to 10 unemployed people to our housing allocation
for person in unemployed_filter:
    if len(housing_alloc) < 10:
        housing_alloc.append(person)

total_count = 0
#add total count of children
for person in housing_alloc:
    total_count += person['numberOfChildren]
    total_count += 1

print(total_count)




