import re


def mask_bad_words(chat_message: str, bad_words: list[str]) -> str:
    """메시지에서 금지어가 발견된 모든 구간을 글자 수만큼 마스킹합니다."""
    # 문자열을 글자 목록으로 바꾸면 필요한 위치만 '*'로 바꿀 수 있습니다.
    masked_characters = list(chat_message)

    for word in bad_words:
        # 빈 문자열은 금지어로 처리하지 않습니다.
        if not word:
            continue

        # escape는 '.', '+' 같은 특수문자도 문자 그대로 찾게 합니다.
        # IGNORECASE는 영어 대소문자를 구분하지 않게 합니다.
        pattern = re.compile(re.escape(word), re.IGNORECASE)
        search_start = 0

        while True:
            # 항상 원본에서 검색해야 앞서 마스킹한 부분과 겹친 금지어도 찾습니다.
            match = pattern.search(chat_message, search_start)
            if match is None:
                break

            # 발견된 구간의 각 글자를 별표 하나로 바꿉니다.
            for index in range(match.start(), match.end()):
                masked_characters[index] = '*'

            # 한 글자 뒤부터 다시 검색하면 서로 겹친 금지어도 찾을 수 있습니다.
            search_start = match.start() + 1

    # 수정한 글자 목록을 다시 하나의 문자열로 합칩니다.
    return ''.join(masked_characters)


if __name__ == '__main__':
    # (메시지, 금지어 목록, 예상 결과) 순서로 테스트를 정의합니다.
    test_cases = [
        ('너는 바보야', ['바보'], '너는 **야'),
        ('BAD, Bad, bad!', ['bad'], '***, ***, ***!'),
        ('bad BAD', ['BaD'], '*** ***'),
        ('안녕하세요!', ['바보'], '안녕하세요!'),
        ('', ['바보'], ''),
        ('안녕하세요', [], '안녕하세요'),
        ('그대로 유지', [''], '그대로 유지'),
        ('바보!', ['', '바보'], '**!'),
        ('바보바보', ['바보'], '****'),
        ('바보 멍청이', ['바보', '멍청이'], '** ***'),
        ('바보!', ['바보', '바보'], '**!'),
        ('a.b aXb', ['a.b'], '*** aXb'),
        ('C++ [bad] $', ['c++', '[bad]', '$'], '*** ***** *'),
        ('abcde', ['abc', 'cde'], '*****'),
        ('abcde', ['cde', 'abc'], '*****'),
        ('ababa', ['aba'], '*****'),
        ('BADminton', ['bad'], '***minton'),
        ('  바보,\nBAD!\t끝  ', ['바보', 'bad'], '  **,\n***!\t끝  '),
        ('🙂바보🙂', ['바보'], '🙂**🙂'),
        ('hello world', ['hello world'], '***********'),
        ('짧음', ['아주긴금지어'], '짧음'),
        ('*** bad', ['bad'], '*** ***'),
    ]

    for message, words, expected in test_cases:
        actual = mask_bad_words(message, words)
        assert actual == expected, (message, words, expected, actual)
        # 마스킹하더라도 전체 글자 수는 원본과 같아야 합니다.
        assert len(actual) == len(message)

    print(f'{len(test_cases)}개 테스트 통과')
