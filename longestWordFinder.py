def longest_word(words):
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

# Testing
print(longest_word(["apple", "banana", "cherry", "date"]))  # Output: banana
print(longest_word(["dog", "cat", "elephant", "bat"]))      # Output: elephant
