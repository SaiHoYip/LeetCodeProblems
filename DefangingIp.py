class Solution(object):
    def defangIPaddr(self, address):
        newAddress = ''
        for i in range(len(address)):
            if address[i] == ".":
                newAddress += '[.]'
            else:
                newAddress += address[i]
        return newAddress

print(Solution.defangIPaddr('','1.2.3'))