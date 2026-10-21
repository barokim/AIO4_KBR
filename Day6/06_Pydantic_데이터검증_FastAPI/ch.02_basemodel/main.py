import day6_2

member = day6_2.Student(name='홍길동',age=20,interests=['AI'],nickname=None,student_id='23')
if member.age > 19:
    print('성인입니다')

print('main.py',__name__)