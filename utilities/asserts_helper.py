def assert_element_exist(response):
    assert response, "search failed, one or more elements were not found on the page"


def assert_words_in_result(response, word: str):
    assert response, f"at least one result does not contains the word {word}"


def assert_title_word(response, word: str):
    assert response, f"title does not contains the word {word}"


def assert_login(response):
    assert response, "user cannot be logged"


def assert_message(response, msg):
    assert response, f"{msg} message is not the expected"


def assert_attach_file(response):
    assert response, "the input field or the file were not found"


def assert_uploaded_file(response):
    assert response, "file cannot be uploaded"