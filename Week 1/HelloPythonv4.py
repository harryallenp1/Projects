#Object Oriented Programming Paradigm
class CourseOrientation:
    def displayCourseInfo(self):
        courseTitle = "Programming Principles"
        courseCode = 10004

        print(courseCode, courseTitle)

print("Trying to create class object")

print("Information for Mobile Computing Course Orientation")
#create an object
mobileOrientation = CourseOrientation()
mobileOrientation.displayCourseInfo()

print("Information for Data Analytics Course Orientation")
#create an object
analyticsOrientation = CourseOrientation()
analyticsOrientation.displayCourseInfo()
