from absl.testing import absltest

def setUpModule() -> None: ...
def _hybrid_decrypt_key_manager(): ...
def _hybrid_encrypt_key_manager(): ...

class HybridKeyManagerTest(absltest.TestCase):
    def test_hybrid_decrypt_primitive_class(self) -> None: ...
    def test_hybrid_encrypt_primitive_class(self) -> None: ...
    def test_hybrid_decrypt_key_type(self) -> None: ...
    def test_hybrid_encrypt_key_type(self) -> None: ...
    def test_new_key_data(self) -> None: ...
    def test_new_key_data_invalid_params_throw_exception(self) -> None: ...
    def test_new_key_data_on_public_key_manager_fails(self) -> None: ...
    def test_encrypt_decrypt(self) -> None: ...
    def test_decrypt_fails(self) -> None: ...