import base64

Token = input("Enter your token: ")
Token = base64.b64decode(Token)
Token = Token.decode("utf-8")
print(Token)