def detect_anagrams(word, candidates):
    anagrams = []
    for candidate in candidates:
        if word.lower() != candidate.lower() and sorted(word.lower()) == sorted(candidate.lower()):
            anagrams.append(candidate)
    return anagrams
