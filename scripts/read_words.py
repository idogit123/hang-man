def get_words_from_file(file_path: str) -> list[str]:
    with open(file_path, 'r') as file:
        words = file.read().split('\n')
        return words
    
def get_word_from_file(file_path: str, word_index: int) -> str:
    return get_words_from_file(file_path)[word_index]