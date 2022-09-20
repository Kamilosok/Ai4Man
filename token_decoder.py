import hashlib

#Made it in a class just because
class Tokener:

    @staticmethod
    def decrypt(pk, ciphertext):
        #Decrypt the token and hand it over to the bot
        key, n = pk
        plain = [chr((char ** key) % n) for char in ciphertext]
        decToken = str()
        for ch in plain:
            decToken += ch

        return decToken

    @staticmethod
    def accessFile(self):

        #Open the file and extract the private key, turn it into a tuple, then make the coded token operable
        file = open('TokenButHashedAlsoPrivateKey.txt', 'r')
        private = []
        tempInt= file.readline()
        private += [int(tempInt)]
        tempInt = file.readline()
        private += [int(tempInt)]

        codedToken = []
        for inter in file:
            codedToken.append(int(inter))

        return self.decrypt(private, codedToken)



def main():
    tok = Tokener()
    tok.accessFile()

if __name__ == "__main__":
    main()