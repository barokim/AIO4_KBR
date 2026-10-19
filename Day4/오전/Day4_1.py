'''
충돌사항이 발생했을때
'''

import random
numbers = [random.randint(1,100) for i in range(10)]
numbers[0] =numbers[-1]
