# (generated with --quick)

import __future__
from typing import Any

Column: Any
INTEGER: Any
REAL: Any
TEXT: Any
declarative_base: Any
division: __future__._Feature
print_function: __future__._Feature

class Tables(object):
    def get_phrase_table(self, tablename = ...) -> type: ...
    def get_sentence_table(self, tablename = ...) -> type: ...
    def get_transphraseprob_table(self, tablename = ...) -> type: ...
    def get_trigram_table(self, tablename) -> type: ...
    def get_trigramprob_table(self, tablename) -> type: ...
    def get_trigramprobwithoutlast_table(self, tablename) -> type: ...
    def get_unigram_table(self, tablename) -> type: ...
    def get_unigramprob_table(self, tablename) -> type: ...
    def get_wordalignment_table(self, tablename) -> type: ...
    def get_wordprobability_table(self, tablename) -> type: ...