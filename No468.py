class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """

        if '.' in IP:
            ss = IP.split('.')
            if len(ss) != 4:
                return 'Neither'
            for s in ss:
                if s.startswith('0') and len(s) != 1:
                    return 'Neither'
                if not s.isdigit() or int(s) < 0 or int(s) > 255:
                    return 'Neither'
            return 'IPv4'
        elif ':' in IP:
            ss = IP.split(":")
            if len(ss) != 8:
                return 'Neither'
            for s in ss:
                if len(s) > 4 or len(s) == 0:
                    return 'Neither'
                for c in s:
                    if not c.isdigit() and c not in ['A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f']:
                        return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'
