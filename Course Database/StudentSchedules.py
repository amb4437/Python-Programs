class ClassTime:

    def __init__(self, days, hour):
       """ Days should be a string such as: WMF or TT.
        Hour is a non-negative integer in 0...23.  That is,
        all classes start on the hour."""
       self._days = days
       # Check that the hour supplied is legal
       if hour in range(24):
           self._hour = hour
       else:
           print ("Hour supplied not legal.  Must be integer ", end="")
           print ("between 0 and 23.")
           
    def __str__(self):
        return self._days + " " + self.hourToString()

    def getDays(self):
        return self._days

    def getHour(self):
        return self._hour

    def hourToString(self):
        """Turn the stored value (0..23) into a
        more congenial printable string"""
        h = self._hour
        if h == 0:
            return "12am"
        elif h < 12:
            return str(h) + "am"
        else:
            return str(h - 12) + "pm"

#----------------------------------------------------------------------

class Course:
    """Define a Course object containing:
    - an integer unique number
    - a string course dept (e.g., "CS")
    - a string course number (e.g., "313E")
    - s string course longname (e.g., "Elements of Software Design")
    - a string location (e.g., "RLM 5.104")
    - a string instructor name (e.g., "Young, W.")
    - a ClassTime object indicating days and time the course meets
    """

    def __init__(self, uniqueNumber, courseDept, courseNumber, courseLongName, 
                 location, instructor, classTime):
        self._uniqueNumber = uniqueNumber
        self._courseDept = courseDept
        self._courseNumber = courseNumber
        self._courseLongName = courseLongName
        self._location = location
        self._instructor = instructor.strip()
        self._classTime = classTime

    def splitDeptAndNum(deptNum):
        # Note that this is a class method rather than an
        # instance method. 
        index = 0
        while not deptNum[index].isdigit():
            index += 1
        dept = deptNum[:index]
        Num = deptNum[index:]
        return (dept, Num)

    def courseName (self):
        return self._courseDept + self._courseNumber

    def __str__(self):
        return "   " + ("%05d" % self._uniqueNumber) + ": " + self.courseName() + " (" + self._courseLongName + \
               ") " + str(self._classTime) + " in " + self._location + \
               " taught by " + self._instructor

    def getUniqueNumber(self):
        return self._uniqueNumber

    def getCourseDept(self):
        return self._courseDept

    def getCourseNumber(self):
        return self._courseNumber

    def getCourseLongName(self):
        return self._courseLongName

    def getInstructor(self):
        return self._instructor
    
    def getClassTime(self):
        return self._classTime

    def getClassDays(self):
        # This is used to extract the days
        # component from the classTime object
        classTime = self.getClassTime()
        return classTime.getDays()
    
    def getClassHour(self):
        # This is used to extract the hour
        # component from the classTime object
        classTime = self.getClassTime()
        return classTime.getHour()
    
    def getLocation(self):
        return self._location

#----------------------------------------------------------------------

class CourseList:
    """A CourseList is a mapping from courseNames (e.g., CS3132E) to
    Course objects containing all of the course information.  This
    uses a dictionary to represent the mapping."""

    def __init__(self):
        self._courses = {}

    def __str__(self):
        if len(self._courses) > 0:
        
            output = ""
            for c in self._courses.values():
                output += str(c) + "\n"
            return output
        else:
            return "Student is not registered for any courses"

    def isEmpty(self):
        return self._courses == {}

    def courseListed(self, courseName):
        return courseName in self._courses

    def getCourse(self, courseName):
        if courseName in self._courses:
            return self._courses[courseName]
        else:
            print ("Course " + courseName + " not in catalog")

    def addCourse(self, courseName, courseObject):
        """Add a course (by courseName) to this CourseList"""
        self._courses[courseName] = courseObject

    def searchByUniqueNumber(self, uniqueNumber):
        # Return the course with a given unique number
        for course in self._courses.values():  # This is the keys, not the values
            if course.getUniqueNumber() == uniqueNumber:
                return course
        # print("No course with that uniqueNumber in database")
        return None

    # But the courseName is the key, so wouldn't it be more efficient to just look
    # for the key and return the associated course. 

    def searchByCourseName(self, courseName):
        # recall that the courseName is used as the key, so just
        # check whether the key is defined and then access the 
        # associated Course
        if courseName in self._courses:
            return self._courses[courseName]
        else:
            return None

    def searchByDept(self, deptID):
        # Return all courses from that department.
        coursesFound = []
        for course in self._courses.values():
            if course.getCourseDept() == deptID:
                coursesFound.append( course )
        return coursesFound

    def searchByDays(self, days):
        # Return all courses on those days
        coursesFound = []
        for course in self._courses.values():
            if course.getClassDays() == days:
                coursesFound.append( course )
        return coursesFound

    def searchByTime(self, time):
        # Return all courses on those days
        coursesFound = []
        for course in self._courses.values():
            # The class hour is stored as an integer.
            if str(course.getClassHour()) == time:
                coursesFound.append( course )
        return coursesFound

#----------------------------------------------------------------------

# THE TOP LEVEL

def printHelp ():
    print("""
     help
        see a useful list of available commands

     catalog
        see list of available courses

     info COURSENAME
        give all information about the course
  
     info UNIQUENUMBER
        give all information about the course 

     courses department DEPTID
        list all courses for a given department

     courses days DAYS
        list all courses on given days (e.g., TT, MWF)

     courses time TIME 
        list all courses that begin at a specific time 
        (use integer between 0 and 23 to designate hour)
        
     enroll name
       add a student to the Students Database with empty schedule
       
     add name courseName
        assuming the student exists in the database, add the course to that
        student's schedule
        
     schedule students-name
        print information on the student named

     stop or quit or exit
        exit the system""")

def createCoursesDatabase():
    """Read successive lines from file classlist and create
    corresponding Course objects.  A sample line is:
    
    54640:CS313E:Elements of Software Design:MWF:9:WAG 201:Young, W

    """

    courseDatabase = CourseList()
    roster = StudentList()
    
    courseFile = open("classlist", 'r')
    for line in courseFile:
        # split the line into fields
        fields = line.split(":")
        # get the unique number
        uniqueNumber = int(fields[0])
        # the next field contains both the courseDept and the courseNumber,
        # put them in uppercase just to be consistent
        courseDept, courseNumber = Course.splitDeptAndNum(fields[1])
        courseDept = courseDept.upper()
        courseNumber = courseNumber.upper()
        # get the course long name
        courseLongName   = fields[2]
        # the classTime comes in the next two fields
        classTime    = ClassTime(fields[3], int(fields[4]))
        location     = fields[5]
        instructor   = fields[6]
        course = Course(uniqueNumber, courseDept, courseNumber, courseLongName,
                        location, instructor, classTime)

        # Recall that the courseName (e.g., CS313E) is actually stored in two 
        # fields, Dept and Number
        courseName = course.courseName()

        print ("   Adding course " + courseName)
        print (course)
        courseDatabase.addCourse(courseName, course)
    return courseDatabase

def coursesInterface(courses):
    
    roster= StudentList()
    while True:
        command = input("\nQuery the database: ")
        commandFields = command.split()
        if not commandFields:
            continue
        op = commandFields[0]
        if op == "stop" or op == "quit" or op == "exit":
            break
        elif op == "help":
            printHelp()
        elif op == "catalog":
            print( courses )
        elif op == "info":
            arg = commandFields[1]
            if arg.isdigit():
                # Asking for uniqueNumber
                # Unique numbers in the database are stored as ints
                arg = int(arg)
                course = courses.searchByUniqueNumber( arg )
            else:
                # Assume arg is a courseName
                course = courses.searchByCourseName( arg )
            if course:
                print( course )
        elif op == "courses":
            # In this case there should be two arguments
            arg1 = commandFields[1]
            arg2 = commandFields[2]
            if arg1 == "department" or arg1 == "dept":
                coursesFound = courses.searchByDept( arg2 )
            elif arg1 == "days":
                coursesFound = courses.searchByDays( arg2 )
            else:
                # Assumes arg1 is "time"
                coursesFound = courses.searchByTime( arg2 )
            for course in coursesFound:
                print (course)
                
        elif op == "enroll":
          arg1 = commandFields[1]
          roster.addStudent(arg1)
          
        elif op == "add":
          arg1 = commandFields[1]
          arg2 = commandFields[2]
          if roster.isEnrolled(arg1):
            student = roster.getStudent(arg1)
            student.addClass(arg2, courses)
            
        elif op == "schedule":
          arg1 = commandFields[1]
          if roster.isEnrolled(arg1):
            print(roster.getStudent(arg1))
          else:
            print ("Student is not enrolled")
 
        
        else:
            print("Unrecognized command: " + command)
            
            
#----------------------------------------------------------------------            

class Schedule(CourseList):
    """A schedule is just a CourseList, but the actual
    courses that the student is taking."""

    def __init__(self, studentName):
      CourseList.__init__(self)
      self._studentName = studentName      

    def addClass(self, courseName, coursesDatabase):
      """This links a new course into the student's schedule
      But doesn't recreate the course.  It is linked from the
      master list of classes."""
      course = coursesDatabase.getCourse(courseName)
      self.addCourse(courseName, course)

#----------------------------------------------------------------------

class Student:
    """A student has a name and an associated schedule."""

    def __init__(self, name):
      self._schedule = Schedule(name)
      self._name= name

    def getName(self):
      return self._name

    def getSchedule(self):
      return self._schedule

    def hasClass(self, classNumber):
      return self._schedule.courseListed(self, classNumber)         

    def addClass(self, classNumber, catalog):
      self._schedule.addClass(classNumber, catalog)
            
    #def getClass(self, classNumber):
    #  return self._schedule
      
      
    def __str__(self):
      newstr = "student" + str(self._name) + "\n" + "Printing schedule" + str(self._name) + "\n" + str(self._schedule)
      return newstr
      
      


#----------------------------------------------------------------------

class StudentList:
    """A roster of the students currently enrolled.  Maps a
    student's name to a Student object. """

    def __init__(self):
      roster = {}
      self.roster = roster
    
    def isEnrolled(self, studentName):
      return studentName in self.roster

    def getStudent(self, studentName):
      return self.roster[studentName]

    def addStudent(self, studentName):
      """Create a new Student record for this student and add
      to the student roster. """
      self.roster[studentName] = Student(studentName)

    def __str__(self):
      """Create a list of students (string)."""
      newstr = ''
      for key in self.roster:
        newstr += key
      return newstr


#----------------------------------------------------------------------
                
def main():
    courses = createCoursesDatabase()
    coursesInterface( courses )

main()

