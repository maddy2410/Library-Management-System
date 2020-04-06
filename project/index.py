from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import mysql.connector
import datetime
from PyQt5.uic import loadUiType

ui , _= loadUiType('layout.ui')
login , _= loadUiType('login.ui')
signup , _= loadUiType('signup.ui')

class Login(QWidget , login):


	def __init__(self):
		QWidget.__init__(self)
		self.setupUi(self)
		self.handle_buttons()
		self.label_3.setVisible(False)
		self.label_4.setVisible(False)
		style=open(r'themes/darkgray.css','r')
		style=style.read()
		self.setStyleSheet(style)


	def handle_buttons(self):
		self.pushButton.clicked.connect(self.Handle_login)
		self.pushButton_2.clicked.connect(self.handle_signup)

	def Handle_login(self):
		username=self.lineEdit.text()
		password=self.lineEdit_2.text()

		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		

		m='''select count(*) from users where user_name = %s'''
		self.cur.execute(m,(username,))
		k=self.cur.fetchone()
		if k[0]!=0:
			a="""select * from users where user_name = %s"""
			self.cur.execute(a,(username,))
			d=self.cur.fetchone()
			if password==d[3]:
				self.label_3.setVisible(False)
				self.window1=MainApp()
				self.close()
				self.window1.show()
				
			else:
				self.label_3.setVisible(True)
				self.lineEdit.setText('')
				self.lineEdit_2.setText('')
		else:
			self.label_3.setVisible(True)
			self.lineEdit.setText('')
			self.lineEdit_2.setText('')
		
			
	def handle_signup(self):
		self.window2=SignUP()
		self.close()
		self.window2.show()
		
		
		
class SignUP(QWidget , signup):


	def __init__(self):
		QWidget.__init__(self)
		self.setupUi(self)
		self.handle_buttons()
		self.label_5.setVisible(False)
		style=open(r'themes/darkgray.css','r')
		style=style.read()
		self.setStyleSheet(style)

	def handle_buttons(self):
		self.pushButton.clicked.connect(self.sign_in)
		
	def sign_in(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		username=self.lineEdit.text()
		email=self.lineEdit_2.text()
		password=self.lineEdit_3.text()
		re_entered = self.lineEdit_4.text()
		
		b="""select count(*) from users where user_name=%s"""
		self.cur.execute(b,(username,))
		d=self.cur.fetchone()
		if d[0]==0:
			if password==re_entered:
				self.cur.execute('''
				insert into users(user_name,user_email,user_password) values(%s,%s,%s)''',(username,email,password))
				self.db.commit()
				self.lineEdit.setText('')
				self.lineEdit_2.setText('')
				self.lineEdit_3.setText('')
				self.lineEdit_4.setText('')
				
				self.back_to_login()
				
			else:
				self.label_5.setText("Please Add A Valid Password Twice")
				self.lineEdit_3.setText('')
				self.lineEdit_4.setText('')
		else:
			self.label_5.setText("Username Already Taken :(")
			self.lineEdit.setText('')
			self.lineEdit_2.setText('')
			self.lineEdit_3.setText('')
			self.lineEdit_4.setText('')
		
		
	def back_to_login(self):
		self.window3=Login()
		self.close()
		self.window3.show()
		


class MainApp(QMainWindow , ui):


	def __init__(self):
		QMainWindow.__init__(self)
		self.setupUi(self)
		self.open_day_to_day_tab()
		self.handle_ui_changes()
		self.handle_buttons()
		self.show_authors()
		self.show_categories()
		self.show_publishers()
		self.author_combo()
		self.category_combo()
		self.publisher_combo()
		self.show_all_clients()
		self.show_all_books()
		self.show_day_ops()
		self.dark_gray_theme()
	
	def handle_ui_changes(self):
		self.hiding_themes()
		self.tabWidget.tabBar().setVisible(False)


	def handle_buttons(self):
		self.pushButton_5.clicked.connect(self.show_themes)
		self.pushButton_22.clicked.connect(self.hiding_themes)
		
		self.pushButton.clicked.connect(self.open_day_to_day_tab)
		self.pushButton_3.clicked.connect(self.open_book_collection_tab)
		self.pushButton_2.clicked.connect(self.open_user_info_tab)
		self.pushButton_4.clicked.connect(self.open_edit_info_tab)
		self.pushButton_27.clicked.connect(self.open_client_tab)
		
		self.pushButton_8.clicked.connect(self.add_new_books)
		
		
		self.pushButton_15.clicked.connect(self.add_category)
		self.pushButton_16.clicked.connect(self.add_author)
		self.pushButton_17.clicked.connect(self.add_publisher)
		
		self.pushButton_7.clicked.connect(self.add_new_books)
		
		self.pushButton_9.clicked.connect(self.search_books)
		self.pushButton_8.clicked.connect(self.edit_books)
		
		self.pushButton_10.clicked.connect(self.delete_books)
		
		self.pushButton_12.clicked.connect(self.login)
		
		self.pushButton_11.clicked.connect(self.add_new_user)
		
		self.pushButton_14.clicked.connect(self.edit_user_data)
		
		
		self.pushButton_18.clicked.connect(self.dark_orange_theme)
		self.pushButton_19.clicked.connect(self.dark_gray_theme)
		self.pushButton_24.clicked.connect(self.classic_theme)
#		self.pushButton_23.clicked.connect(self.dark_orange1_theme)
#		self.pushButton_20.clicked.connect(self.dark_orange_theme)
		self.pushButton_21.clicked.connect(self.qdarkstyle_theme)
		
		
		self.pushButton_20.clicked.connect(self.add_new_client)
		self.pushButton_25.clicked.connect(self.search_client)
		self.pushButton_23.clicked.connect(self.edit_client)
		self.pushButton_26.clicked.connect(self.delete_client)
		
		self.pushButton_6.clicked.connect(self.handle_day_to_day)

	
	def show_themes(self):
		self.groupBox_3.show()
		
		
	def hiding_themes(self):
		self.groupBox_3.hide()
							##OPENING TABS##	
		
	def open_day_to_day_tab(self):
		self.tabWidget.setCurrentIndex(0)
		
	def open_book_collection_tab(self):
		self.tabWidget.setCurrentIndex(1)
		
	def open_user_info_tab(self):
		self.tabWidget.setCurrentIndex(3)
		
	def open_edit_info_tab(self):
		self.tabWidget.setCurrentIndex(4)
	
	def open_client_tab(self):
		self.tabWidget.setCurrentIndex(2)
	
	##handling books##
	
	def show_all_books(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		a='''select book_code,book_name,book_category,book_author,book_publisher,book_price,book_description from book'''
		self.cur.execute(a)
		data=self.cur.fetchall()
		
		self.tableWidget_5.setRowCount(0)
		self.tableWidget_5.insertRow(0)
		
		for row,form in enumerate(data):
			for column , item in enumerate(form):
				self.tableWidget_5.setItem(row,column,QTableWidgetItem(str(item)))
				column+=1
			rowposition=self.tableWidget_5.rowCount()
			self.tableWidget_5.insertRow(rowposition)
	
	def add_new_books(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		book_title=self.lineEdit_2.text()
		book_code=self.lineEdit_3.text()
		book_category = self.comboBox_4.currentText()
		book_publisher = self.comboBox_5.currentText()
		book_author = self.comboBox_3.currentText()
		book_price = self.lineEdit_4.text()
		book_description=self.textEdit_75.toPlainText()
		a=(book_title,book_description,book_code,book_category,book_author,book_publisher,book_price)
		
		self.cur.execute('''insert into book(book_name,book_description,book_code,book_category,book_author,book_publisher,book_price) values(%s,%s,%s,%s,%s,%s,%s) ''',a)
		self.db.commit()
		self.statusBar().showMessage("New Book Added ^-^")
		self.lineEdit_3.setText("")
		self.lineEdit_2.setText('')
		self.lineEdit_4.setText('')
		self.textEdit_75.setPlainText('')
		self.comboBox_3.setCurrentIndex(0)
		self.comboBox_5.setCurrentIndex(0)
		self.comboBox_4.setCurrentIndex(0)

		self.show_all_books()
		
		
	def search_books(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		book_title=self.lineEdit_6.text()
		a="""select * from book where book_name = %s"""
		self.cur.execute(a,(book_title,))
	
		d=self.cur.fetchone()
		self.lineEdit_5.setText(d[3])
		self.comboBox_6.setCurrentText(d[5])
		self.comboBox_7.setCurrentText(d[4])
		self.comboBox_8.setCurrentText(d[6])
		self.lineEdit_71.setText(str(d[7]))
		self.textEdit_2.setPlainText(d[2])
		
	def edit_books(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()

		book_name=self.lineEdit_6.text()
		self.lineEdit_6.setEnabled(False)
		book_code=self.lineEdit_5.text()
		book_category=self.comboBox_7.currentText()
		book_publisher=self.comboBox_8.currentText()
		book_author=self.comboBox_6.currentText()
		book_description=self.textEdit_2.toPlainText()
		book_price=self.lineEdit_71.text()

		a='''update book set book_description=%s,book_code=%s,book_category=%s,book_author=%s,book_publisher=%s,book_price=%s where book_name=%s'''
		self.cur.execute(a,(book_description,book_code,book_category,book_author,book_publisher,book_price,book_name))
		
		self.db.commit()

		self.lineEdit_5.setText('')
		self.lineEdit_6.setText('')
		self.lineEdit_71.setText('')

		self.comboBox_7.setCurrentIndex(0)
		self.comboBox_6.setCurrentIndex(0)
		self.comboBox_8.setCurrentIndex(0)
		
		self.lineEdit_6.setEnabled(True)
		self.statusBar().showMessage("The book Info has Been UPDATED ;)")
		self.tableWidget_5.setRowCount(0)
		self.cur.execute('''delete from book where book_name=%s''',('',))
		self.db.commit()
		self.show_all_books()


		
	def delete_books(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		title=self.lineEdit_6.text()
		warning = QMessageBox.warning(self,"Delete the book's data","are you sure you want to delete this book's data",QMessageBox.Yes | QMessageBox.No)
		if warning==QMessageBox.Yes:
			a="""delete from book where book_name = %s"""
			self.cur.execute(a,(title,))
			self.db.commit()
			self.lineEdit_5.setText('')
			self.lineEdit_6.setText('')
			
			self.comboBox_8.setCurrentIndex(0)
			self.comboBox_8.setCurrentIndex(0)
			
			self.textEdit_2.setPlainText('')
			self.statusBar().showMessage("Book is Deleted :(")
			
		self.show_all_books()
		
	## CLIENT ##
	def add_new_client(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		
		client_name=self.lineEdit_7.text()
		client_email=self.lineEdit_21.text()
		client_id=self.lineEdit_22.text()
		b='''select count(*) from clients where client_adhaar=%s'''
		self.cur.execute(b,(client_id,))
		d=self.cur.fetchone()
		if d[0]==0:
			a='''insert into clients(client_name,client_email,client_adhaar) values(%s,%s,%s)'''
			
			self.cur.execute(a,(client_name,client_email,client_id))
			self.db.commit()
			self.statusBar().showMessage('New Client Added !!')
			self.lineEdit_7.setText('')
			self.lineEdit_21.setText('')
			self.lineEdit_22.setText('')
			
		else:
			self.label_38.setText('Adhaar Number Already Registered')
			self.lineEdit_22.setText('')
			
		self.show_all_clients()
		
		
		
	def show_all_clients(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		a='''select client_name,client_email from clients'''
		self.cur.execute(a)
		data=self.cur.fetchall()
		self.tableWidget_4.setRowCount(0)
		self.tableWidget_4.insertRow(0)
		
		
		for row,form in enumerate(data):
			for column , item in enumerate(form):
				self.tableWidget_4.setItem(row,column,QTableWidgetItem(str(item)))
				column+=1
			rowposition=self.tableWidget_4.rowCount()
			self.tableWidget_4.insertRow(rowposition)
				
		
		
	def search_client(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		client_adhaar=self.lineEdit_24.text()
		
		a='''select * from clients where client_adhaar=%s'''
		self.cur.execute(a,(client_adhaar,))
		d= self.cur.fetchone()
		
		
		self.lineEdit_26.setText(d[1])
		self.lineEdit_25.setText(d[2])
		self.lineEdit_23.setText(d[3])
		self.lineEdit_23.setEnabled(False)
			
		
		
	def edit_client(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		
		
		client_adhaar=self.lineEdit_24.text()
		client_name=self.lineEdit_26.text()
		client_email=self.lineEdit_25.text()
		
		a='''update clients set client_name=%s,client_email=%s where client_adhaar=%s'''
		self.cur.execute(a,(client_name,client_email,client_adhaar))
		self.db.commit()
		self.statusBar().showMessage('YAY !! Your Data Has Been Updated..')
		
		self.show_all_clients()
		
		
	def delete_client(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		
		client_adhaar=self.lineEdit_24.text()
		
		a='''delete from clients where client_adhaar=%s'''
		warning=QMessageBox.warning(self,"Delete the CLIENT data","are you sure you want to delete this CLIENT's data",QMessageBox.Yes | QMessageBox.No)
		if warning==QMessageBox.Yes:
			self.cur.execute(a,(client_adhaar,))
			self.db.commit()
			self.statusBar().showMessage(":( WE'LL MISS YOU BUDDY ...")
			self.lineEdit_25.setText('')
			self.lineEdit_24.setText('')
			self.lineEdit_26.setText('')
		self.show_all_clients()		
	
	
	## USER INFO ##
	def add_new_user(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		username=self.lineEdit_8.text()
		email=self.lineEdit_9.text()
		password=self.lineEdit_10.text()
		re_entered = self.lineEdit_11.text()
		
		b="""select count(*) from users where user_name=%s"""
		self.cur.execute(b,(username,))
		d=self.cur.fetchone()
		if d[0]==0:
			if password==re_entered:
				self.cur.execute('''
				insert into users(user_name,user_email,user_password) values(%s,%s,%s)''',(username,email,password))
				self.statusBar().showMessage("YAY!! Welcome to The Family BRUH..")
				self.db.commit()
				self.lineEdit_10.setText('')
				self.lineEdit_11.setText('')
				self.lineEdit_8.setText('')
				self.lineEdit_9.setText('')
			else:
				self.label_29.setText("Please Add A Valid Password Twice")
				self.lineEdit_10.setText('')
				self.lineEdit_11.setText('')
		else:
			self.label_29.setText("Username Already Taken :(")
			self.lineEdit_10.setText('')
			self.lineEdit_11.setText('')
			self.lineEdit_8.setText('')
			self.lineEdit_9.setText('')

			
	def login(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		username=self.lineEdit_12.text()
		password=self.lineEdit_13.text()
		
		a="""select * from users where user_name = %s"""
		self.cur.execute(a,(username,))
		d=self.cur.fetchone()
		if password==d[3]:
			self.groupBox_4.setEnabled(True)
			self.pushButton_14.setEnabled(True)
			self.lineEdit_14.setText(d[1])
			self.lineEdit_15.setText(d[2])
		
	def edit_user_data(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		u1=self.lineEdit_12.text()
		username=self.lineEdit_14.text()
		email=self.lineEdit_15.text()
		password=self.lineEdit_17.text()
		password2=self.lineEdit_16.text()
		
		b="""select count(*) from users where user_name=%s"""
		self.cur.execute(b,(username,))
		d=self.cur.fetchone()
		
		if d[0]==0:
			if password==password2:
				self.cur.execute('''update users set user_name = %s,user_email=%s,user_password=%s where user_name=%s''',(username,email,password,u1))
				self.db.commit()
				self.statusBar().showMessage("Your Data Has Been Successfully Updated :)")
				self.lineEdit_17.setText('')
				self.lineEdit_16.setText('')				
				self.lineEdit_14.setText('')				
				self.lineEdit_15.setText('')
				self.lineEdit_13.setText('')
				self.lineEdit_12.setText('')
			else:
				self.label_30.setText('Please Add A Valid Password Twice')
				self.lineEdit_17.setText('')
				self.lineEdit_16.setText('')
		else:
			if u1==username:
				if password==password2:
					self.cur.execute('''update users set user_name = %s,user_email=%s,user_password=%s where user_name=%s''',(username,email,password,u1))
					self.db.commit()
					self.statusBar().showMessage("Your Data Has Been Successfully Updated :)")
					self.lineEdit_17.setText('')
					self.lineEdit_16.setText('')				
					self.lineEdit_14.setText('')				
					self.lineEdit_15.setText('')
					self.lineEdit_13.setText('')
					self.lineEdit_12.setText('')
					self.groupBox_4.setEnabled(False)	
				else:
					self.label_30.setText('Please Add A Valid Password Twice')
					self.lineEdit_17.setText('')
					self.lineEdit_16.setText('')
					
			
			else:
				self.label_30.setText("OOPS This Username Is Already Taken!!")
				self.lineEdit_14.setText('')
			
				self.groupBox_4.setEnabled(False)	
		
		
	
	
	## THEMES ##
	
	def dark_blue_theme(self):
		style=open(r'themes/darkblue.css','r')
		style=style.read()
		self.setStyleSheet(style)
		
	def dark_orange_theme(self):
		style=open(r'themes/darkorange.css','r')
		style=style.read()
		self.setStyleSheet(style)
		
	def dark_gray_theme(self):
		style=open(r'themes/darkgray.css','r')
		style=style.read()
		self.setStyleSheet(style)
		
	def classic_theme(self):
		style=open(r'themes/classic.css','r')
		style=style.read()
		self.setStyleSheet(style)
		
	def dark_orange1_theme(self):
		style=open(r'themes/darkorange1.css','r')
		style=style.read()
		self.setStyleSheet(style)
		
	def qdarkstyle_theme(self):
		style=open(r'themes/qdark.css','r')
		style=style.read()
		self.setStyleSheet(style)
		
	## DAY TO DAY OPERATIONS ##
		
	def handle_day_to_day(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		book_title=self.lineEdit.text()
		client_name=self.lineEdit_27.text()
		types=self.comboBox.currentText()
		number_of_days=self.comboBox_2.currentIndex()+1
		todays_date=datetime.date.today()
		to_date=todays_date+datetime.timedelta(days=int(number_of_days))

		a='''insert into dayoperations(book_name,client,type,days,date,to_date)
		 values(%s,%s,%s,%s,%s,%s);'''
		
		self.cur.execute(a,(book_title,client_name,types,number_of_days,todays_date,to_date))
		self.db.commit()
		self.show_day_ops()
		self.lineEdit.setText('')
		self.lineEdit_27.setText('')
		self.comboBox.setCurrentIndex(0)
		self.comboBox_2.setCurrentIndex(0)
		self.statusBar().showMessage('New Operation Added!!')
		
		
	def show_day_ops(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		book_title=self.lineEdit.text()
		a='''select book_name,client,type,date,to_date from dayoperations where book_name=%s'''
		self.cur.execute(a,(book_title,))
		self.tableWidget.setRowCount(0)
		self.tableWidget.insertRow(0)
		d= self.cur.fetchall()

		for row,form in enumerate(d):
			for column,item in enumerate(form):
				
				self.tableWidget.setItem(row,column,QTableWidgetItem(str(item)))
				column+=1

			rowposition=self.tableWidget.rowCount()
			self.tableWidget.insertRow(rowposition)


		
	## EDIT INFO ##
	
	def add_category(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		category_name=self.lineEdit_18.text()
		self.cur.execute('''
		insert into category (category_name) values(%s)
		''',(category_name,))
		self.db.commit()
		self.statusBar().showMessage("New Category Successfully Added")
		self.lineEdit_18.setText('')
		
		self.show_categories()
		self.category_combo()
		
		
		
	def show_categories(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		self.cur.execute("""select category_name from category""")
		self.d=self.cur.fetchall()
		self.db.commit()
		if self.d:
			self.tableWidget_985.setRowCount(0)
			self.tableWidget_985.insertRow(0)
			for row, form in enumerate(self.d):
				for column,item in enumerate(form):
					self.tableWidget_985.setItem(row,column,QTableWidgetItem(str(item)))
					column+=1
				
				row_position=self.tableWidget_985.rowCount()
				self.tableWidget_985.insertRow(row_position)
			
				
		
	def add_author(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		author_name=self.lineEdit_19.text()
		self.cur.execute('''
		insert into authors (author_name) values(%s)
		''',(author_name,))
		self.db.commit()
		self.lineEdit_19.setText("")
		self.statusBar().showMessage("New Author Successfully Added")
		self.show_authors()
		self.author_combo()
		
		
		
	def show_authors(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		self.cur.execute("""select author_name from authors""")
		self.d=self.cur.fetchall()
		self.db.commit()
		if self.d:
			self.tableWidget_2.setRowCount(0)
			self.tableWidget_2.insertRow(0)
			for row, form in enumerate(self.d):
				for column,item in enumerate(form):
					self.tableWidget_2.setItem(row,column,QTableWidgetItem(str(item)))
					column+=1
				
				row_position=self.tableWidget_2.rowCount()
				self.tableWidget_2.insertRow(row_position)
		
		
		
		
		
		
		
	def add_publisher(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		
		publisher_name=self.lineEdit_20.text()
		self.cur.execute('''
		insert into publisher (publisher_name) values(%s)
		''',(publisher_name,))
		self.db.commit()
		self.statusBar().showMessage("New Publisher Successfully Added")
		self.lineEdit_20.setText("")
		self.show_publishers()
		self.publisher_combo()
	
	def show_publishers(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		self.cur.execute("""select publisher_name from publisher""")
		self.d=self.cur.fetchall()
		self.db.commit()
		if self.d:
			self.tableWidget_3.setRowCount(0)
			self.tableWidget_3.insertRow(0)
			for row, form in enumerate(self.d):
				for column,item in enumerate(form):
					self.tableWidget_3.setItem(row,column,QTableWidgetItem(str(item)))
					column+=1
				
				row_position=self.tableWidget_3.rowCount()
				self.tableWidget_3.insertRow(row_position)
				
	
	
	## COMBO BOXES :DISPLAYING DATA  ##
	
	def author_combo(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		a="""select author_name from authors"""
		self.cur.execute(a)
		d=self.cur.fetchall()
		self.comboBox_6.clear()
		for it in d:
			self.comboBox_6.addItem(it[0])
			self.comboBox_3.addItem(it[0])
		
		self.db.commit()
		
	def category_combo(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		a="""select category_name from category"""
		self.cur.execute(a)
		d=self.cur.fetchall()
		self.comboBox_7.clear()
		for it in d:
			self.comboBox_7.addItem(it[0])
			self.comboBox_4.addItem(it[0])
		self.db.commit()
				
		
		
	def publisher_combo(self):
		self.db = mysql.connector.connect(host='localhost',user='root',password='123456',db='library')
		self.cur = self.db.cursor()
		a="""select publisher_name from publisher"""
		self.cur.execute(a)
		d=self.cur.fetchall()
		self.comboBox_8.clear()
		for it in d:
			self.comboBox_8.addItem(it[0])
			self.comboBox_5.addItem(it[0])		
		self.db.commit()
		
		
	
def main():
    app=QApplication(sys.argv)
    window=Login()

    window.show()
    app.exec_()




if __name__=="__main__":
    main()