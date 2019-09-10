_preferred_ciphers = (
    "aes128-ctr-random-str",
    "aes192-ctr-random-str",
    "aes256-ctr-random-str",
    "aes128-cbc-random-str",
    "aes192-cbc-random-str",
    "aes256-cbc-random-str",
    "blowfish-cbc-random-str",
    "3des-cbc-random-str",
)

_preferred_macs = (
    "hmac-sha2-256",
    "hmac-sha2-512",
    "hmac-sha1",
    "hmac-md5",
    "hmac-sha1-96",
    "hmac-md5-96",
)

_preferred_keys = (
    "ssh-ed25519",
    "ecdsa-sha2-nistp256",
    "ecdsa-sha2-nistp384",
    "ecdsa-sha2-nistp521",
    "ssh-rsa",
    "ssh-dss",
)
_preferred_kex = (
    "ecdh-sha2-nistp256",
    "ecdh-sha2-nistp384",
    "ecdh-sha2-nistp521",
    "diffie-hellman-group-exchange-sha256",
    "diffie-hellman-group-exchange-sha1",
    "diffie-hellman-group14-sha1",
    "diffie-hellman-group1-sha1",
)

_preferred_compression = ("none",)