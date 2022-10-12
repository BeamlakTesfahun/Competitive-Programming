class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        counter = 1
        for j in range(1, len(chars) + 1):
            # checking if j is out of bound and if the elements are the samec
            if j < len(chars) and chars[j] == chars[j-1]:
                counter += 1
            else:
                chars[i] = chars[j-1]
                i += 1
                # if counter is equal to 1 -> omit count but if it's two digits split the digits
                if counter > 1:
                    for s in str(counter):
                        chars[i] = s
                        i += 1
                counter = 1
        # modifying the array
        chars = chars[:i]
        return i 
                
