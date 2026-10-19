import random
ages = random.sample(range(15,100), 10)
results = []
for i in ages:
    if i >= 20:
        results.append('성인')
    else:
        results.append('미성년자')

print(results)