class Course:
  def __init__(self,code,title,capacity=30):
    self.code= code
    self.title= title
    self.capacity= capacity
    self.students= []

  def add_student(self,student):
    if len(self.students) >= self.capacity:
      print(f"{self.code} is full.")
      return False
    if student not in self.students:
      self.students.append(student)
      return True 
    return False

  def remove_student(self,student):
    if student in self.students:
      self.students.remove(student)
      return True
    return False

class Student:
  def __init__(self,name,student_id,major):
    self.name=name
    self.student_id= student_id
    self.major= major
    self.courses= []
    

  def enroll(self,course):
     if course.add_student(self):
      self.courses.append(course)
      print(f"{self.name} enrolled {course.code}.")

  def drop(self,course):
     if course.remove_student(self):
      self.courses.remove(course)
      print(f"{self.name} dropped {course.code}.")

  def get_courses(self):
    return [f"{c.code} - {c.title}" for c in self.courses]
