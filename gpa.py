class GPA(object):
	def __init__(self,history,math,science,english,other):
		self.dictGPA = { 	
							"english": english,
							"math": math,
							"science": science,
							"history": history,
							"other": other
						}
		self.h_ap_letterGrade_to_GPA_dict = {
											"a+": 5.0,
											"a": 5.0,
											"a-": 4.7,
											"b+": 4.3,
											"b": 4.0,
											"b-": 3.7,
											"c+": 3.3,
											"c": 3.0,
											"c-": 2.7,
											"d+": 2.3,
											"d": 2.0,
											"d-": 1.7,
											"f": 0.0

										}
		self.acp_letterGrade_to_GPA_dict = {
											"a+": 4.5,
											"a": 4.5,
											"a-": 4.2,
											"b+": 3.8,
											"b": 3.5,
											"b-": 3.2,
											"c+": 2.8,
											"c": 2.5,
											"c-": 2.2,
											"d+": 1.8,
											"d": 1.5,
											"d-": 1.2,
											"f": 0.0

										}
		self.cp_letterGrade_to_GPA_dict = {
											"a+": 4.0,
											"a": 4.0,
											"a-": 3.7,
											"b+": 3.3,
											"b": 3.0,
											"b-": 2.7,
											"c+": 2.3,
											"c": 2.0,
											"c-": 1.7,
											"d+": 1.3,
											"d": 1.0,
											"d-": 0.7,
											"f": 0.0

										}
	def courseGPA(self,grade,level):
		if level == "h" or level == "ap":
			return self.h_ap_letterGrade_to_GPA_dict[grade]
		if level == "acp":
			return self.acp_letterGrade_to_GPA_dict[grade]
		if level == "cp":
			return self.cp_letterGrade_to_GPA_dict[grade]
	def finalGPA(self,englishGPA,mathGPA,scienceGPA,historyGPA,otherGPA):
		return (englishGPA+mathGPA+scienceGPA+historyGPA+otherGPA)/4

		

level_history = input("What level history do you take? (h,acp,cp)>> ")
history = input("What grade did you get in history? (ie. a,a-)>> ")
level_math = input("What level math do you take? (h,acp,cp)>> ")
math = input("What grade did you get in math? (ie. a,a-)>> ")
level_science = input("What level science do you take? (h,acp,cp)>> ")
science = input("What grade did you get in science? (ie. a,a-)>> ")
level_english = input("What level english do you take? (h,acp,cp)>> ")
english = input("What grade did you get in english? (ie. a,a-)>> ")
level_other = input("What level other class (ie. ap or language) class do you take? (h,acp,cp)>> ")
other = input("What grade did you get in your other class? (ie. a,a-)>> ")

gpa = GPA(history,math,science,english,other)

#history
historyGPA = gpa.courseGPA(history,level_history)

#math
mathGPA = gpa.courseGPA(math,level_math)

#science
scienceGPA = gpa.courseGPA(science,level_science)

#english
englishGPA = gpa.courseGPA(english,level_english)

#other
otherGPA = gpa.courseGPA(other,level_other)

print("-"*10)
print("Your Final GPA is ",gpa.finalGPA(englishGPA,mathGPA,scienceGPA,historyGPA,otherGPA))
print("-"*10)

print("Your GPA for history is ", gpa.courseGPA(history,level_history))
print("Your GPA for math is ", gpa.courseGPA(math,level_math))
print("Your GPA for science is ", gpa.courseGPA(science,level_science))
print("Your GPA for english is ", gpa.courseGPA(english,level_english))
print("Your GPA for your other class is ", gpa.courseGPA(english,level_english))
