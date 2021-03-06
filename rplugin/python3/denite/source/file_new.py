# FILE: file_new.py
# AUTHOR: momotaro <momotaro.n@gmail.com>
# License: MIT license

from .base import Base
import os

class Source(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'file_new'
        self.kind = 'file'
        self.matchers = ['filter_file_new']

    def on_init(self, context):
        directory = context['args'][0] if len(
            context['args']) > 0 else context['path']
        if os.path.isdir(directory):
            context['__dir'] = os.path.relpath(
                    self.vim.call('expand', directory), context['path'])
            context['__files'] = [os.path.basename(path)
                                  for path in os.listdir(context['__dir'])]
        context['__prompt'] = "[new file]"

    def gather_candidates(self, context):
        return [{ 'word': '___dummy___'}] if '__dir' in context else []
