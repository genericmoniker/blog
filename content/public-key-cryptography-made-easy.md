Title: Public Key Cryptography Made Easy
Date: 2014-09-06 17:00
Author: Eric
Category: How It Works
Tags: Cryptography, Security
Slug: public-key-cryptography-made-easy
Status: published

Learning about cryptography can be discouraging. You get so bombarded by
"don't invent your own", "you're doing it wrong", and "even really smart
people screw this up" that you wonder why you even bother to try. For
me, the answer is because if you don't learn it, someone who knows even
less than you will end up implementing it (badly, [but with
confidence](http://www.brainyquote.com/quotes/quotes/b/bertrandru101364.html))
on your project. So despite being fraught with peril (because I am not
an Expert), I'll share a little about the concepts of public key
cryptography in a form that has been helpful to me.

"Traditional" or symmetric encryption works like this:

```python
# encrypt
ciphertext = encrypt(message, secret_key)

# decrypt
message = decrypt(ciphertext, secret_key)
```

Public key cryptography (asymmetric encryption) is so named because
there is an additional key beyond the one you keep secret in traditional
algorithms. You have a key generator that gives you both keys, like
this:

```python
public_key, private_key = keygen()
```

The private key needs to be kept secret, just like with symmetric
encryption. The public one can be shared with the world. Print it on a
T-shirt if you like. In fact, anyone that wants to send you an encrypted
message *needs* your public key. It looks like this:

```python
# encrypt
ciphertext = encrypt(message, public_key)

# decrypt
message = decrypt(ciphertext, private_key)
```

In practice, though, public key cryptography is prohibitively slow, so
you'll combine it with a faster symmetric algorithm, so that the process
looks like this:

```python
# encrypt
symmetric_key = random()
ciphertext = symmetric_encrypt(message, symmetric_key)
encrypted_symmetric_key = encrypt(symmetric_key, public_key)

# decrypt
decrypted_symmetric_key = decrypt(encrypted_symmetric_key, private_key)
message = symmetric_decrypt(ciphertext, decrypted_symmetric_key)
```

In this case, when sending the encrypted message, you'd include the
encrypted symmetric key along with it.

Aside from encrypting and decrypting messages, public key cryptography
can be used to digitally sign a message and verify the signature. The
signature for the message is created by encrypting a hash of the
message, but using the private key for the encryption instead of the
public key. Only the holder of the private key can sign, but anyone can
verify the signature with the public key. This looks like:

```python
# sign
signature = encrypt(hash(message), private_key)

# verify
is_valid = decrypt(signature, public_key) == hash(message)
```

**Update**: Speaking of being wrong, corrections made to the mixed
symmetric/asymmetric example on 24 Jan 2018.