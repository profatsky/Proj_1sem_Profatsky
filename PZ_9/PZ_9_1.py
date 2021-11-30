# На трех участках выращиваются следующие сельскохозяйственные культуры: картофель, лук, морковь, горох, капуста, редис.
# Определить, какие из этих культур имеются на каждом участке, имеются хотя бы на одном из участков и не имеются ни на
# одном участке.
vegetables = {'картофель', 'лук', 'морковь', 'горох', 'капуста', 'редис'}  # множество культур
# Участки
first_place = {'картофель', 'морковь', 'горох'}
second_place = {'картофель', 'лук', 'морковь', 'капуста'}
third_place = {'картофель', 'морковь', 'горох'}

# Находим те культуры, которые имеются на каждом участке
in_every = first_place.intersection(second_place, third_place)
print(f'Культуры {in_every} имеются на каждом участке')

# Находи те культуры, которые имеются хотя бы на одном из участков
in_one = vegetables.intersection(first_place.union(second_place, third_place))
in_one = in_one.difference(in_every)
print(f'Культуры {in_one} имеются хотя бы на одном из участков')

# Находим те культуры, которые не имеются ни на одном участке
vegetables_on_places = first_place.union(second_place, third_place)
in_any = vegetables.difference(vegetables_on_places)
print(f'Культуры {in_any} нет ни на одом участке')


