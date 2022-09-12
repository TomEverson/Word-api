class word:
    def load_words(check):
        with open('word.txt') as word_file:
            valid_words = set(word_file.read().split())
        output = []
        for word in valid_words:
            if word.startswith(check):
                output.append(word)

        return output


print(word.load_words("apple"))

