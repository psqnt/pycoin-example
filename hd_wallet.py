from mnemonic import Mnemonic
from pycoin.symbols.btc import network
from pycoin.symbols.xtn import network as testnetwork

# Parameters
language = 'english'
length = 24 # Can also be 24
passphrase = "" # Can leave blank
mainnet = True

# Script
mnemo = Mnemonic(language)
if length == 12:
    words = mnemo.generate(strength=128)
else:
    words = mnemo.generate(strength=256)

seed = mnemo.to_seed(words, passphrase=passphrase)

if mainnet == True:
    key = network.keys.bip32_seed(seed)
else:
    key = testnetwork.keys.bip32_seed(seed)

root_xprv = key.hwif(as_private=True)
root_xpub = key.hwif()
root_wif = key.wif()
root_address = key.address()

print("HD Wallet Info")
print("--------------")
print(f"Seed Words: {words}")
print(f" Root xprv: {root_xprv}")
print(f" Root xpub: {root_xpub}")
print(f"  Root WIF: {root_wif}")
print(f"   Address: {root_address}")
print("--------------")
