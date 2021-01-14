fruit_ranking = [1, 2, 3]
fruit_name = ['Mango', 'Pineapple', 'Watermelon']
fruit_rank_dict = {}

for i in range(len(fruit_ranking)):
    fruit_rank_dict[fruit_ranking[i]] = fruit_name[i]

print(fruit_rank_dict)

#using dictionary comprehension
fruit_ranking = [1, 2, 3]
fruit = ['Mango', 'Pineapple', 'Watermelon']
fruit_ranking_dict = { fruit_ranking[i] : fruit[i] for i in range(len(fruit_ranking)) }
print(fruit_ranking_dict)
