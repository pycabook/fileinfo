from unittest.mock import patch

from fileinfo.logger import Logger


@patch('datetime.datetime.now')
def test_log(mock_now):
    test_now = 123
    test_message = "A test message"
    mock_now.return_value = test_now

    test_logger = Logger()
    test_logger.log(test_message)
    assert test_logger.messages == [(test_now, test_message)]
