#리스트에서 불량을 모두 지우고 정상만 남게
items = ['정상','불량','불량','정상']
# for item in items[:]:  #[:] 슬라이싱: 리스트를 복사 처음부터 끝까지라는 의미
#     if item == '불량':
#         items.remove('불량')  # if문이 한번에 한번만 지우게 되어있으므로 1번더 쓴다
#     # if item == '불량':
#     #         items.remove('불량')
# result = [item for item in items if item != '불량']
result = []
for item in items:
    if item != '불량':
        result.append(item)

print(f'검수결과 : {result}')