# Source : https://leetcode.com/problems/judge-route-circle/description/
# Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means #it moves back to the original place.

# Algo/DS : String

# Complexity : O(n)


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
                
        return True if moves.count('L') == moves.count('R') and moves.count('D') == moves.count('U') else False
        