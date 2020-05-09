import asyncio
import unittest
from unittest import mock
from asyncechoclient import EchoClient

class EchoClientTests(unittest.TestCase):
    def test_init(self):
        message = "test"
        loop = asyncio.get_event_loop()
        result = EchoClient(message, loop)

        self.assertEqual(result.message, message)
        self.assertEqual(result.loop, loop)

    def test_connection_made(self):
        mock_transport = mock.Mock()
        message = "test"
        loop = asyncio.get_event_loop()
        target = EchoClient(message, loop)
        target.connection_made(mock_transport)
        self.assertEqual(target.transport, mock_transport)
        mock_transport.write.assert_called_with(b"test")

    def test_data_received(self):
        mock_transport = mock.Mock()
        message = "test"
        data = b"test-data"
        loop = asyncio.get_event_loop()
        target = EchoClient(message, loop)
        target.transport = mock_transport
        target.data_received(data)
        mock_transport.close.assert_called_with()

    def test_connection_lost(self):
        mock_transport = mock.Mock()
        message = "test"
        data = "test-data"
        mock_loop = mock.Mock()
        target = EchoClient(message, mock_loop)
        target.connection_lost(None)
        mock_loop.stop.assert_called_with()