def asdad(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return ''.join([str(alphabet.find(ind) + 1) for ind in text.lower() if ind in alphabet])
asdad('The sunset sets at twelve o clock.')