from shapes.hexagon import hexagon
from shapes.pentagon import pentagon
from shapes.triangle import triangle
from shapes.circle import circle
from shapes.square import square
from shapes.eptagon import eptagon

from shape_iterator import ShapeSortIterator

if __name__ == "__main__":
    shapes_list = [cls(7) for cls in [hexagon, pentagon, circle, triangle, eptagon, square]]
    print(*shapes_list, sep='\n')
    print("### sorted by area")
    sorter = ShapeSortIterator(shapes_list, lambda s, o: s.calculate_area() < o.calculate_area())
    print(*sorter, sep='\n')
    print("### sorted by area (descending)")
    sorter.set_compare(lambda s,o: s.calculate_area() > o.calculate_area())
    print(*sorter, sep='\n')
    print("### sorted by perimeter")
    sorter.set_compare(lambda s,o: s.calculate_perimeter() < o.calculate_perimeter())
    print(*sorter, sep='\n')
