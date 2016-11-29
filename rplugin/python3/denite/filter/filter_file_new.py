# FILE: filter_file_new.py
# AUTHOR: momotaro <momotaro.n@gmail.com>
# License: MIT license

from .base import Base

class Filter(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'filter_file_new'
        self.description = 'filter for file_new source'

    def filter(self, context):
        if context['input'] == '':
            return []

        for candidate in context['candidates']:
            if candidate['word'] == context['input']:
                return []

        return [{
                'word': '[new file] ' + context['input'],
                'action__path': context['input'] }]
