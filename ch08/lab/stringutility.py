class StringUtility:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return self.string

    def vowels(self):
        count = 0
        for i in self.string:
            if i in "aeiouAEIOU":
                count += 1
        if count == 0:
            return "0"
        elif count < 5:
            return str(count)
        else:
            return "many"

    def bothEnds(self):
        if len(self.string) < 2:
            return ""
        return self.string[0:2] + self.string[len(self.string) - 2:len(self.string)]

    def fixStart(self):
        if self.string == "":
            return ""
        return self.string[0] + self.string[1:].replace(self.string[0], "*")

    def asciiSum(self):
        sum = 0
        for i in self.string:
            sum += ord(i)
        return sum

    def cipher(self):
        result = ""
        for i in self.string:
            if i == "z":
                result += "a"
            if i == "Z":
                result += "A"
            result += chr(ord(i) + len(self.string))
        return result
