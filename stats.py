def get_word_count(text):
    print(f'Found {len(text.split())} total words')

def get_char_count(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def char_sort(char_counts):
    sorted_chars = []
    
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_chars.append({"char": char, "num": count})
    
    # Sort descending by 'num'
    sorted_chars.sort(key=lambda x: x["num"], reverse=True)
    
    return sorted_chars