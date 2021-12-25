import main


def test_simple_text():
    message = "hello world!"
    expected_output = 12
    output = main.message_size(message)
    assert output == expected_output


def test_empty_text():
    message = ""
    expected_output = 0
    output = main.message_size(message)
    assert output == expected_output


def test_oneletter_text():
    message = "A"
    expected_output = 1
    output = main.message_size(message)
    assert output == expected_output
