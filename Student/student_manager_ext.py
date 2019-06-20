class Student:
    """ A simple GPA calculator
    """

    # a map linking letter grads to GPA points
    POINTS = {'A+':4.3, 'A0':4.0,'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D0':1.0}

    #constructor
    def __init__(self, student_name, student_id):
        """ create a new instance of the GPA calculator"""
        # a map of course names to letter grades for a student, e.g., self_grades["ADSA"]="A0"
        self._grades = {}
        self._student_name = student_name
        self._student_id = student_id
        # complete with initialisation of self._student_name and self._student_id


    def get_student_name(self):
        """ Return the name of the student """
        return self._student_name

    def get_student_id(self):
        """ Return the name of the student """
        return self._student_id


    def get_gpa(self):
        """ returns the GPA of the student """
        # this function should caluclate the GPA and print it.
        # HINT: for each course in self._grades, you need to retrieve the corresponding points from Student.POINTS (and then calculate the GPA)
        sum  = 0
        for x in self._grades:
          sum += self.POINTS[self._grades[x]]
        return sum / len(self._grades)

    def add_grade(self, course_name, letter):
        """ Add a new grade """
        # You should improve this function by checking that the letter grade entered is correct.
        # Notice that, for instance, 'Good', 'AB', 'AB+' or 'D-' are not allowed as letter grades (only letter grades in POINTS are allowed)
        if letter in self.POINTS:
            self._grades[course_name] = letter

    def print_grades(self):
        #This function should print the list of courses with the respective letter grades achieved by a student
        for x in self._grades:
            print(x, self._grades[x])


# New methods to implement
    def update_grade(self, course_name, letter):

        self._grades[course_name] = letter

    def get_strange_gpa(self):

        l = self._grades
        print(l)
        if len(l) == 1:
            return l[0]
        else:
            print("calling...")
            print(l[1:])
            return l[0] * strange_gpa(l[1:])
        print(l)



    def get_count_of_above_bplus(self):
        """
        This function should return the number of courses passed by a student with a grade equal to or greater than B+
        """
        for x in self._grades:
            if self.POINTS[self._grades[x]] >= 3.3:
                print(x, self._grades[x])


if __name__ == '__main__':
    # Run this test to check the correctness of your implementation

    def strange_gpa(l):
        if len(l) == 1:
            return l[0]
        else:
            print("calling...")
            print(l[1:])
            return l[0] * strange_gpa(l[1:])

    l = [3, 8, 9, 2]
    print(strange_gpa(l))


