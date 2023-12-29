#!/usr/bin/env python3
#
# Populate SLI "python3_output" context from standard input
# -----------------------------------------------------------------------------
#


import argparse
import sys
from sli import contextManager

# Parse command line arguments
parser = argparse.ArgumentParser(description='Populate SLI "python3_output" context from standard input')
parser.add_argument('-cn', '--context-name', default='default', help='Use a context manager other than global', metavar='TEXT')
parser.add_argument('-cp', '--context-password', default='', help='Password for encrypted context', metavar='TEXT')
args = parser.parse_args()

if sys.stdin.isatty():
    parser.print_help()
    sys.exit(1)
else:
    stdin = ''
    for line in sys.stdin:
        stdin += line

sli_context = contextManager.ContextManager({ 'context_name': args.context_name, 'context_password': args.context_password, 'use_context': True })
current_context = sli_context.load_context()
current_context['python3_output'] = stdin
sli_context.save_context(current_context)
