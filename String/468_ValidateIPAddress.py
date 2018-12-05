# Source : https://leetcode.com/problems/validate-ip-address/description/

# Algo/DS : String, IP

# Complexity :

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        dot_count = IP.count(".")
        if  dot_count > 0: 
            return self.checkIP4(IP)
        else:
            return self.checkIP6(IP)
    '''
    check:
    - length after split should be 4
    - for individual item:
        - len(i) >= 1
        - if len(i)> 1 then no leading 0
        - no +, -
        - 0<i<255 : int(i) would be in try catch
    '''
    def checkIP4(self,IP):
        IP = IP.split(".")
        if len(IP) != 4 : return "Neither"
        for i in IP:
            if not i : return "Neither"
            if i[0] in ['0',"+", '-'] and len(i) > 1: return "Neither"
            try:
                if 0 > int(i) or int(i) > 255: return "Neither"
            except:
                return "Neither"        
        return "IPv4"

    '''
    check:
    - length after split should be 8
    - for individual item:
        - 1<= len(i) <=4
        - chars in i should be 0-9 / A-F/a-f
    '''
    
    def checkIP6(self,IP):
        IP = IP.split(":")
        if len(IP) != 8: return "Neither"
        for i in IP:
            if not i : return "Neither"
            if len(i) > 4 : return "Neither"
            for char in i:
                if char not in "0123456789abcdefABCDEF":return "Neither"
            #if i[0] == '0': return "Neither"
            
        
        return "IPv6"
            
        