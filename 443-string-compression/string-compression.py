class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i=0
        write =0
        while i <len(chars):
            current=chars[i]
           
            count=0
            while i<len(chars) and chars[i]==current:
                
                
                
                i+=1
                count+=1
            chars[write]=current
            write+=1
            if count>1:
                for ch in str(count):
                    chars[write]=ch
                    write+=1
        return write 