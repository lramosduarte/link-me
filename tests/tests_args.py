from unittest import TestCase

from linkme.args import InitiatorArgs


class InitiatorArgsTestCase(TestCase):

    def test_make_instance_class_with_success(self):
        initiator = InitiatorArgs()
        self.assertIsInstance(initiator, InitiatorArgs)

    def test_init_args_with_success(self):
        initiator = InitiatorArgs()
        initiator.start([])

    def test_init_args_call_unread_command_success(self):
        initiator = InitiatorArgs()
        args = initiator.start(['unread'])
        self.assertEqual('unread', args.commands)

    def test_init_args_with_no_valid_command(self):
        initiator = InitiatorArgs()
        with self.assertRaises(SystemExit) as ex:
            initiator.start(['no_valid_command'])

    def test_init_args_with_positional_arg_uploader_with_success(self):
        initiator = InitiatorArgs()
        args = initiator.start(['--uploader', 'script2.py'])
        self.assertIsNotNone(args.uploader)

    def test_init_args_call_upload_command_success(self):
        initiator = InitiatorArgs()
        args = initiator.start(['upload'])
        self.assertEqual('upload', args.commands)
