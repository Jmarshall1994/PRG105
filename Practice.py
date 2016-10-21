

class Course(object):
    """
    This is a docstring.
    """


logic = Course()

logic.department = "PRG"
logic.number = "105"
logic.section = "001"
logic.title = "Programming Logic"

print logic


print logic.department
print "\n\n"


def create_course():
    c = Course()
    c.department = raw_input("Please enter department code")
    c.number = raw_input("Please enter course number")
    c.section = raw_input("Please enter section number")
    c.title = raw_input("Please enter course title")
    return c
course1 = create_course()
print("\n" + course1.department + "_" + course1.number + "_" + course1.section + " " +course1.title)