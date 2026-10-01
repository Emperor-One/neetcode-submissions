class Solution:
    # The delimiter is used for separating "control" part
    # of the encoded string from the "data" part
    DELIMITER = ':'
    def encode(self, strs: List[str]) -> str:
        output = []
        for string in strs:
            output.append(f"{len(string)}{self.DELIMITER}{string}")

        print("".join(output))
        return "".join(output)

    def decode(self, s: str) -> List[str]:
        output = []
        i = length = 0
        data_part = False
        len_array = []

        while i < len(s):
            # We are in a "control" part of the string
            if data_part == False and s[i] != self.DELIMITER:
                len_array.append(s[i])
            
            # We are on the border between "control" and "data"
            elif data_part == False and s[i] == self.DELIMITER:
                length = int("".join(len_array))
                if length == 0:
                    output.append("")
                else:
                    data_part = True

            # We are in a "data" part
            elif data_part == True:
                output.append(s[i:i+length])
                data_part = False
                len_array = []
                i += length
                continue
            
            i += 1
        
        print(output)
        return output

