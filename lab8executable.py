"""
Author: Corey Keller
Creation: 3/28/2024
File Name: lab8executable.py
Purpose: Use the class files to showcase function.
"""
from lab8addressClass import Address
from lab8emergencyContactClass import EmergencyContact
from lab8studentClass import Student

#create objects
student1Address=Address("1234", "Main Street","Indianapolis", "IN", "46207", True)
student1EmergencyContact=EmergencyContact("Joe", "Smith", "Cell", "123-456-7890", "thisisanemail@yahoo.com", "Father", student1Address)
student1=Student("John", "Smith", "123456789", "Full Time", student1Address, 3.9, student1EmergencyContact)

#print objects
print(student1Address)
print(student1EmergencyContact)
print(student1)

#show setter, getter, and additional actions
student1.setGPA(3.5)
print(student1.getGPA())
print(student1.address.inStateorOut())