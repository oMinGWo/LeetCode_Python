class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """

        map = {}
        for d in deck:
            if d in map:
                map[d] += 1
            else:
                map[d] = 1

        m = 0
        for key in map.keys():
            if map[key] == 1:
                return False
            if map[key] != m:
                m = map[key]
