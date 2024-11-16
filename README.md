# Setup

You can encrypt your password and auto-save it in ```credentials.json``` using ```encrypt.py``` and then entering your password.

You should have a ```credentials.json``` file with the following content:

```
{
  "username": {your username},
  "password": {your encrypted password}
}
```

# Run

To run the script, execute the following command:

```
python book.py -k {your decryption key}
```
