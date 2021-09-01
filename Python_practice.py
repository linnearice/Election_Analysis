voting_data=[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
print(voting_data)

voting_data.insert(2,[{'county': "El Paso", 'registered_voters':461149}])
#voting_data.insert(2,[{'county': "Denver", 'registered_voters':463353}])

#voting_data.pop(0)

#voting_data.remove([{'county': "El Paso", 'registered_voters':461149}])
print(voting_data)