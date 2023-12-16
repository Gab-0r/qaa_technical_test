def assert_element_exist(response):
    assert response, "search failed, one or more elements were not found on the page"


def assert_words_in_result(response, word: str):
    assert response, f"at least one result does not contains the word {word}"


def assert_title_word(response, word: str):
    assert response, f"title does not contains the word {word}"

