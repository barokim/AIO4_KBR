# 포함관계(in, not in) => in 포함 not int은 불포함
# if role == 'admin' or role == 'manager' or role == 'staffe'


allowed_roles = ['admin', 'manager', 'staffe']
role = 'admin'
if role in allowed_roles:
    print('접근허용')
else:
    print('접근불가')
