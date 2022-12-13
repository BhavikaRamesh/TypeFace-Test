Before searching for all the phonetic combinations of a given word, I would like to encode the word based on an algorithm called Soundex algorithm.

Soundex algorithm:
Step 1: Keep the first letter in its position and remove all occurrences of the alphabets a, e, i, o, u, y, h, w.
Step 2: Replace all consonants after the first letter with it's mapped digits.
        b, f, p, v → 1
        c, g, j, k, q, s, x, z → 2
        d, t → 3
        l → 4
        m, n → 5
        r → 6
Step 3: If two or more letters with the same number are adjacent in the original name, only retain the first letter.
Step 4: Two letters with the same number separated by 'h', 'w' or 'y' are coded as a single number. Letters separated by a vowel are coded twice. This rule also applies to the first letter.
Step 5: Append 3 zeros if result contains less than 3 digits. Remove all except first letter and 3 digits after it.

For example, if the given word is "Murthy", the encoded string will be "M630". Since the phonetic combinations of the given word will all have the same encoded string, to get the combinations, the encoded string must be decoded in the reverse order of the algorithm.
This algorithm is also called as Reverse Soundex. By performing reverse soundex, many words will be generated which might not sound like the given word. To select the word which sound like the given word, Levenshtein distance can be used where the two parameters will be original string and each word from the combination. If the distance between the words is same, that word can be appeded to the list of the phonetic combinations of the given word.