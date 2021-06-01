from caesar_cipher import __version__
from caesar_cipher.caesar_cipher import *


def test_version():
    assert __version__ == '0.1.0'

# encrypt a string with a given shift
# encryption should handle upper and lower case letters
# encryption should allow non-alpha characters but ignore them, including white space

def test_encrypt_with_a_given_shift():
    expected ='N bfsy yt xfd xtrjymnsl'
    actual= encrypt('I want to say something',5)
    assert actual==expected

#decrypt a previously encrypted string with the same shift
def test_decrypt():
    expected='I want to say something'
    actual = decrypt('N bfsy yt xfd xtrjymnsl',5)
    assert actual == expected 

#decrypt encrypted version of It was the best of times, it was the worst of times. WITHOUT knowing the shift used.
def test_crack():
    assert crack('H vzms sn rzx rnldsghmf')=='I want to say something'
    assert crack('N bfsy yt xfd xtrjymnsl')=='I want to say something'