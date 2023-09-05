def count_occurrences(word, text):
    count = 0
    words = text.split()
    for w in words:
        if w.lower() == word.lower():
            count += 1
    return count

def replace_word(word, old_word, new_word):
    words = word.split()
    replaced_words = []
    count = 0
    for w in words:
        if w.lower() == old_word.lower():
            count += 1
            if count % 2 == 0:
                replaced_words.append(new_word)
            else:
                replaced_words.append(old_word)
        else:
            replaced_words.append(w)
    return ' '.join(replaced_words)

filename = "file_to_read.txt"
word_to_count = "terrible"
even_word = "pathetic"
odd_word = "marvellous"

# Read the file
with open(filename, 'r') as file:
    text = file.read()

# Calculate the count of "terrible"
count = count_occurrences(word_to_count, text)
print(f"The word '{word_to_count}' appears {count} time(s).")

# Replace the word
new_text = replace_word(text, word_to_count, even_word)

# Create a new file and write the modified text to it
result_filename = "result.txt"
with open(result_filename, 'w') as file:
    file.write(new_text)

print(f"The modified text has been written to '{result_filename}'.")
