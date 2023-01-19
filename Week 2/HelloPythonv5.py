from HelloModule import CourseOrientation

print("Information for Mobile Computing Course Orientation")
#create an object
# mobileOrientation = HelloModule.CourseOrientation()
mobileOrientation = CourseOrientation()
mobileOrientation.displayCourseInfo()


print("The name of module ", __name__)