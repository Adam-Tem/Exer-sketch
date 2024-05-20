import numpy as np
class CoordPoint:

    def __init__(self, coord, is_left, is_bottom):

        self.x = coord[0]
        self.y = coord[1]
        self.is_left = is_left
        self.is_bottom = is_bottom

    def set_coord(self, new_coord):
        self.x = new_coord[0]
        self.y = new_coord[1]
    
    def get_coord(self):
        return np.array([self.x, self.y])
    
    def set_x(self, new_x):
        self.x  = new_x
    
    def get_x(self):
        return self.x
    
    def set_y(self, new_y):
        self.y = new_y

    def get_y(self):
        return self.y
    
    def get_is_left(self):
        return self.is_left
    
    def get_is_bottom(self):
        return self.is_bottom
    
    def compare_point(self, other):
        """
        A function to evaluate how to adjust points after a move has been made.
        Select the most appropriate point given the two points in question.
        Args: self, other: [coord, is_left, is_bottom]
        """
        if self.get_is_left() == other.get_is_left():

            if self.get_is_left() == True:
                max_x = max(self.get_x(), other.get_x())           
                self.set_x(max_x)
                other.set_x(max_x)
            
            else:
                min_x = min(self.get_x(), other.get_x())           
                self.set_x(min_x)
                other.set_x(min_x)
        
        elif self.get_is_bottom() == other.get_is_bottom():
                
                if self.get_is_bottom() == True:
                    max_y = max(self.get_y(), other.get_y())           
                    self.set_y(max_y)
                    other.set_y(max_y)
                else:
                    min_y = min(self.get_y(), other.get_y())           
                    self.set_y(min_y)
                    other.set_y(min_y)