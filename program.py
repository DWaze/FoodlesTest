from collections import Counter


def termFrequency(sentence: str, amount: int) -> list:
    result = Counter(sentence.split()).most_common(n=amount)
    result.sort(key=lambda x: x[0])
    result.sort(key=lambda x: x[1], reverse=True)
    return result
