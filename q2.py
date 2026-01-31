def string_info(words):
    result = {}
    for word in words:
        length = len(word)
        parity = "even" if length % 2 == 0 else "odd"
        result[word] = {
             "length": length,
             "parity": parity
        }
     return result
print(string_info(["data", "science"]))
