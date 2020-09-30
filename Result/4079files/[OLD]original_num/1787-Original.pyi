# (generated with --quick)

from typing import Any
import unittest.case

BPEmb: Any
unittest: module

class BPEmbTest(unittest.case.TestCase):
    def test_emb_dim_100(self) -> None: ...
    def test_emb_dim_25(self) -> None: ...
    def test_emb_dim_50(self) -> None: ...
    def test_emb_model_download(self) -> None: ...
    def test_emb_vs_1000(self) -> None: ...
    def test_emb_vs_10000(self) -> None: ...
    def test_emb_vs_5000(self) -> None: ...
    def test_encode_decode_many_roundtrip(self) -> None: ...
    def test_encode_decode_roundtrip(self) -> None: ...
    def test_encode_ids_decode_ids_many_roundtrip(self) -> None: ...
    def test_encode_ids_decode_ids_roundtrip(self) -> None: ...
    def test_gensim_import(self) -> None: ...
    def test_pad_index(self) -> None: ...
    def test_pad_lookup(self) -> None: ...
    def test_pickle(self) -> None: ...
    def test_pickle_custom_cache_dir(self) -> None: ...
    def test_pickle_custom_no_cache(self) -> None: ...
    def test_sentencepiece_import(self) -> None: ...
