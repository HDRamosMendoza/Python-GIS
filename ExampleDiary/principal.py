#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Contact(object):
	def __init__(self, **kwargs):
		self.name = kwargs.get('name', None)
		self.phone = kwargs.get('phone', None)
		self.email = kwargs.get('email', None)

class ContactBook(Contact):
	def __init__(self, name, phone, email):
		super(ContactBook, self).__init__(name=name, phone=phone, email=email);
		self._contacts = []

	def add(self, param_name, param_phone, param_email):
		contact = ContactBook(param_name, param_phone, param_email)
		self._contacts.append(contact)

	def search(self, param_name):
		for item in self._contacts:
			if item.name.lower() == param_name.lower():
				self._print_contact(item)
				break
		else:
			self.notFound()

	def update(self, param_name):
		for i, item in enumerate(self._contacts):
			if item.name.lower() == param_name.lower():
				item.name = str(raw_input(''' Insert new Name: '''))
				item.phone = str(raw_input(''' Insert new Phone: '''))
				item.email = str(raw_input(''' Insert new Email: '''))
				self._contacts[i] = item
				break
		else:
			self.notFound()

	def delete(self, param_name):
		for i, item in enumerate(self._contacts):
			if item.name == param_name:
				del self._contacts[i]
				print("Delete contact")
				break
		else:
			print("Does not exist")
				#del my_list[1] # Removes index 1 from the list
				#my_list.remove(4) # Removes the integer 4 from the list, not the index 4
				#my_list.pop(2) # Removes index 2 from the list

	def listContact(self):
		contactItem = self._contacts
		if contactItem.__len__() == 0:
			self.notFound()
		else:
			print(" --------------------------- ") 
			for item in contactItem:
				print(" Contact: ")
				self._print_contact(item)

	def _print_contact(self, item):
		print("     Name: {0}".format(item.name))
		print("     Phone: {0}".format(item.phone))
		print("     Email: {0}".format(item.email))
		print(" --------------------------- ")  

	@staticmethod
	def notFound():
		print("Not found")

def run():
	contact_book = ContactBook('Daniel','999130638','sdsd')

	while True:
		command = str(raw_input('''
			¿ Main ?
			----------------------
			*> [a]dd contact
			*> [u]pdate contact
			*> [s]earch contact
			*> [d]elete contact
			*> [l]ist contact
			*> [e]xit

			> Select Item :
			'''))

		if command.strip() == 'a':
			print '*> Add contact'
			in_name = str(raw_input('   Insert name: '))
			in_phone = str(raw_input('   Insert phone: '))
			in_email = str(raw_input('   Insert email: '))
			contact_book.add(in_name.strip(), in_phone.strip(), in_email.strip())

		elif command.strip() == 'u':
			print '*> Update contact'
			in_name = str(raw_input('''Name: '''))
			contact_book.update(in_name.strip())

		elif command.strip() == 's':
			print '*> Search contact'
			in_name = str(raw_input('''Name: '''))
			print(" --------------------------- ")
			print(" 	Result ")
			print(" --------------------------- ")
			contact_book.search(in_name.strip())

		elif command.strip() == 'd':
			print '*> Delete contact'
			in_name = str(raw_input('''Name :'''))
			print(" --------------------------- ")
			print(" 	Result ")
			print(" --------------------------- ")
			contact_book.delete(in_name.strip())

		elif command.strip() == 'l':
			print '*> List contact'
			contact_book.listContact()

		elif command.strip() == 'e':
			print '>>>>> Exit'
			break

		else:
			print('comando no encontrado')

if __name__ == '__main__':
	run()