# Source : https://leetcode.com/problems/robot-room-cleaner/description/

# Algo/DS : Graph, DFS

# Complexity : O(n*n)


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot(object):
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution(object):
    def go_up(self, robot):
        return robot.move()
    
    def go_down(self, robot):
        robot.turnLeft()
        robot.turnLeft()
        ok = robot.move()
        robot.turnLeft()
        robot.turnLeft()
        return ok
   
    def go_left(self, robot):
        robot.turnLeft()
        ok = robot.move()
        robot.turnRight()
        return ok
        
        
    def go_right(self, robot):
        robot.turnRight()
        ok = robot.move()
        robot.turnLeft()  
        return ok
   
    
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()
        self.clean(robot,0,0, visited)
        
    def clean(self, robot, i,j, visited)
        if (i,j)  in visited : return
        visited.add((i,j))
        robot.clean()
              
        # up
        if self.go_up(robot) :
            self.clean(robot,i-1,j,visited)
            self.go_down(robot)
            
        # down
        if self.go_down(robot) :
            self.clean(robot,i+1, j,visited)
            self.go_up(robot)
            
        # left
        if self.go_left(robot):
            self.clean(robot,i, j-1,visited)
            self.go_right(robot)
            
        # right
        if self.go_right(robot) :
            self.clean(robot,i,j+1,visited)
            self.go_left(robot)
        
    
        
        
        
        
        
        
        