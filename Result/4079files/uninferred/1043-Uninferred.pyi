from absl.testing import absltest

class AeadKeyTemplatesTest(absltest.TestCase):
    def test_aes128_eax(self) -> None: ...
    def test_aes256_eax(self) -> None: ...
    def test_create_aes_eax_key_template(self) -> None: ...
    def test_aes128_gcm(self) -> None: ...
    def test_aes256_gcm(self) -> None: ...
    def test_create_aes_gcm_key_template(self) -> None: ...
    def test_aes256_ctr_hmac_sha256(self) -> None: ...
    def test_aes128_ctr_hmac_sha256(self) -> None: ...
    def test_create_aes_ctr_hmac_aead_key_template(self) -> None: ...
    def test_xchacha20_poly1305(self) -> None: ...
