"""Test cases for the logger module."""

import os
import shutil
from unittest import TestCase
from unittest.mock import MagicMock
from glampy.logger import Logger


class TestLogger(TestCase):
    """Tests the Logger class."""

    def test___init__(self):
        """Tests the __init__ method of the Logger class."""
        logfile = "some_file_to_test"
        logger = Logger(log_name="test", log_file=logfile)
        self.assertEqual(len(logger.logger.handlers), 2, "blub")
        logger.logger.handlers[1].close()
        os.remove(logfile)

        logfile_1 = "logs/some_file_to_test"
        logger_1 = Logger(log_name="test", log_file=logfile_1)
        self.assertTrue(os.path.exists(logfile_1))
        logger_1.logger.handlers[1].close()
        shutil.rmtree("logs")

    def test_debug(self):
        """Tests the debug method of the Logger class."""
        logger = Logger(log_name="test")
        logger.logger.debug = MagicMock()
        logger.debug("test")

        assert logger.logger.debug.called

    def test_info(self):
        """Tests the info method of the Logger class."""
        logger = Logger(log_name="test")
        logger.logger.info = MagicMock()
        logger.info("test")

        assert logger.logger.info.called

    def test_warning(self):
        """Tests the warning method of the Logger class."""
        logger = Logger(log_name="test")
        logger.logger.warning = MagicMock()
        logger.warning("test")

        assert logger.logger.warning.called

    def test_error(self):
        """Tests the error method of the Logger class."""
        logger = Logger(log_name="test")
        logger.logger.error = MagicMock()
        logger.error("test")

        assert logger.logger.error.called
