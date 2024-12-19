from io import StringIO

class StringBuilder:
    string=None

    def __init__(self):
        self.string=StringIO()

    def Append(self,str):
        self.string.write(str)

    def __str__(self):
        return self.string.getvalue()

s=StringBuilder()
s.Append("Hi ")
s.Append("This is ")
s.Append("Python Lecture")
print(s)
# s="this is the string"
# s=list(s)
# print(''.join(s),s)
