# Write code to assign to the variable compri all the values of the key name in any of the sub-dictionaries in the
# dictionary tester. Do this using a list comprehension.
import json

tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
# print(json.dumps(tester, indent=2))
tester1 = tester['info']
# print(json.dumps(tester1, indent=2))

tester2 = [item['name'] for item in tester1]

print(tester2)
