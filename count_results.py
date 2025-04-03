import re

def count_word_patterns(file_path):
    single_word_pattern = re.compile(r"\(\w+\)")
    vs_word_pattern = re.compile(r"\(\w+ vs \w+\)")
    
    single_word_count = 0
    vs_word_count = 0
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if vs_word_pattern.search(line):
                vs_word_count += 1
            elif single_word_pattern.search(line):
                single_word_count += 1
    
    return vs_word_count, single_word_count

# Use the uploaded file path
test_file_path = 'test_results.txt'
vs_word_count, single_word_count = count_word_patterns(test_file_path)

print(f"Lines with (WORD vs WORD): {vs_word_count}")
print(f"Lines with (WORD): {single_word_count}")
