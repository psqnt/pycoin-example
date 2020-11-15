# Example HD Wallet Generation in Python
This python script shows a how to generate a private key for a BIP39 compliant
wallet using BIP32 mnemonic words

Many more functions and utilties would need to be added to this to have a fully functioning wallet,
but this is the key generation aspect. These can be imported into electrum and used.

Also can use this to verify wallet creation and derived addresses:
https://iancoleman.io/bip39/

## Dependencies
Both open source projects, commands below or use requirements.txt
```
pip install mnemonic
pip install pycoin
```

## Usage
```
mkdir pycoin-example (or git clone this)
python3 -m venv venv
. venv/bin/activate
python hd_wallet.py
```

## Example Output
```
HD Wallet Info
--------------
Seed Words: science wall execute wheel zero captain evoke used appear orange impose oyster
 Root xprv: tprv8ZgxMBicQKsPdHq347pUqd2rz79EwMWXN2rEkKELB9dDosWnNdraR4d3w5rLse5GURteNmfUgywveBWmB5cYdi4DLdTwR1mMY9csc2yJzKe
 Root xpub: tpubD6NzVbkrYhZ4WkrpwmV5F2gyZ8fB6ghRwLT22qGdbRRceMmZ12gAbZEv7DNBhhP9KpAcpaGt6hbDwtePzsiUSQvv76KxbogYWAotsAW1Dsi
  Root WIF: cPfRHz9enKLxULYFq4E6uc7k1eL3Amtk3aNsWe85PbTvzx7oU7AZ
   Address: mmnmTMzjC8pD7gge1koi8impmtXEYHo5x3
--------------
```


