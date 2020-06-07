def find_max_prefix(dictionary, word):
    _max = 0
    for prefix, count in dictionary.items():
        if len(prefix) < len(word) and word.startswith(prefix):
            _max = max(_max, count)
    return _max


def solution(n, words):
    words = sorted(words)
    chains = dict()
    for word in words:
        existing_chain_length = find_max_prefix(chains, word)
        if word in chains:
            chains[word] = max(existing_chain_length + 1, chains[word])
        else:
            chains[word] = existing_chain_length + 1
    return max(chains.values())


n = int(input())
words = []
for i in range(n):
    words.append(input())

print(solution(n, words))

assert solution(5, ['a', 'ab', 'd', 'dc', 'abc']) == 3
assert solution(5, ['a', 'a', 'a', 'a', 'a']) == 1
assert solution(5, ['a', 'a', 'a', 'aa', 'a']) == 2
assert solution(5, ['a', 'aaa', 'a', 'aa', 'a']) == 3
assert solution(5, ['xzz', 'xz', 'x', 'abc', 'abd']) == 3
