def detect_anagrams(word, candidates):
    anagrams = []
    for candidate in candidates:
        match = 0
        if len(word) == len(candidate) and word.lower() != candidate.lower():
            for char in word:
                if word.lower().count(char) == candidate.lower().count(char):
                    match += 1
            if match == len(word):
                anagrams.append(candidate)
    return anagrams
