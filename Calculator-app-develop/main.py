import sys 
from UI_standard_calculator import *
from operation_logic import Operation as Ops






class MainApp(UiMainWindow, QMainWindow) 
    """
    Main application
    """ 
    current_operation = None
    is_div_by_zero = False
    is_invalid_input = False
    is_percent_btn_clicked = False


    def __init__(self):
        super(MainApp, self).__init__()
        self.calc_screen.setText('0')
        self.widgets()


    def widgets(self):
        for count, x in enumerate(self.all_btns):
            x.clicked.connect(lambda checked, index=count, btn=x: self.on_num_btn_click(btn, index)) # 'checked' is the default parameter that passes the clicked signal



    def on_num_btn_click(self, btn, index):
        """
        Method to handle all button clicks.
        
        :param btn: Button which ahs been clicked.
        :param index: Index of button in the button list.
        """
        if btn.text() in ['0','1','2','3','4','5','6','7','8','9']:
            if self.calc_screen.text() == '0':
                self.calc_screen.setText('')
            self.calc_screen.setText(self.calc_screen.text() + btn.text())

        if index == 0: # Percentage button clicked
            self.is_percent_btn_ckicked = True
            if len(self.calc_screen.text()) == 0 and self.calc_screen.text() == '0':
                return # do nothing


            if '=' in self.small_calc_screen.text():
                self.calc_screen.setText(str(Ops.percentage_raw(self.calc_screenText()))) 
                self.small_calc_screen.setText(self.calc_screen.text())
                return



            # Just clicked percentage, without extra value, so use the first value in "memory":
            elif ('+' in self.small_calc_screen.text() and self.calc_screen.text() == '0') or\
                 ('-' in self.small_calc_screen.text() and self.calc_screen.text() == '0') or\
                 ('x' in self.small_calc_screen.text() and self.calc_screen.text() == '0') or\
                 ('/' in self.small_calc_screen.text() and self.calc_screen.text() == '0') or:
                 self.small_calc_screen.setText(self.small_calc_screen.text() + ' ' + str(Ops.percentage_raw(self.small_calc_screen.text().split()[0])))
                 self.on_num_btn_click(btn=self.all_btns[-1], index=23)
                 self.is_percentage_btn_clicked = False
                 return

            if index == 1: # 'CE' (Clear Entry) button clicked
                self.calc_screen.setText('0')

            if  index ==2: # 'C'(Clear) button clicked
                 if (self.is_div_by_zero or self.is_invalid_input) is True:
                     self.all_btns[2]._animation2.setLoopCount(0)
                     self.all_btns[2]._animation2.setDuration(500)
                     self.all_btns[2]._animation2.stop()
                     self.calc_screen.setMaxLength(13) # todo: make global variable or Class attribute
                     self.calc_screen.setStyleSheet('font-size: 30pt, padding: 5x 0px;')
                     self.is_div_by_zero = False
                     self.is_invalid_input = False
                     for b in self.all_btns:
                         b.selfEnabled(True)
                 self.small_calc_screen.setText('')
                 self.calc_screen.setText('0')


            if index == 3: # backspace button clicked
                if self.calc_screen.text() == '0':
                    return

                if self.small.calc_screen.setText() != '':
                    self.small.calc_screen.setText('')
                    return
                elif len(self.calc_screen.text()) == 1 and self.calc_screen.text() !='0':
                    self.calc_screen.text('0')
                elif len(self.calc_screen.text()) !='':
                    self.calc_screen.text(self.calc_screen.text()[0:-1])

            if index == 4: # inverse button clicked
                if len(self.calc_screen.text()) == 1 and self.calc_screen.text() == '0':
                    self.small_calc_screen.setText('1/( ' + self.calc_screen.text() + ')')
                    self.handle_math_errors(error_msg='Cannot divide by zero!')
                    self.is_div_by_zero = True

                else:
                  self.small_calc_screen.setText('1/('+self.calc_screen.text()+')')
                  self.calc_screen.setText('0')


                  # For user convinience
                  self.small_calc_screen.setText(self.small_calc_screen.text() + '=')
                  self.calc_screen.setText(str(Ops.inverse(self.small_calc_screen.text().split()[1])))

                self.current_operation = 'inv'

            if index == 5: # squared button clicked
                if len(self.calc_screen.text()) == 1 and self.calc_screen.text() == '0':
                    self.small_calc_screen.setText('sqr( 0 ) ')

                else:
                    self.small_calc_screen.setText(' + self.calc_screen.Text() + ') 
                    self.calc_screen.setText('0')

                   # For user convenience:
                self.small_calc_screen.setText(self.small_calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.squared(self.small_calc_screen.text().split()[1])))

            self.current_operation = 'sqr'

        if index == 6:  # square root button clicked
            if '-' in self.calc_screen.text():
                self.small_calc_screen.setText('sqrt( ' + self.calc_screen.text() + ' ) =')
                self.handle_math_errors(error_msg='Invalid Input!')
                self.is_invalid_input = True

            else:
                self.small_calc_screen.setText('sqrt( ' + self.calc_screen.text() + ' )')

                # For user convenience
                self.small_calc_screen.setText(self.small_calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.squareroot(self.small_calc_screen.text().split()[1])))

            self.current_operation = 'sqrt'

        if index == 7:  # division button clicked
            if '/' in self.small_calc_screen.text():
                if self.calc_screen.text() == '0':
                    self.small_calc_screen.setText(self.small_calc_screen.text() + '0')
                    self.handle_math_errors(error_msg='Cannot divide by zero!')
                    self.is_div_by_zero = True
                    return
                self.small_calc_screen.setText(str(Ops.division(self.small_calc_screen.text().split()[0],
                                                                self.calc_screen.text())))
            else:
                self.small_calc_screen.setText(self.calc_screen.text() + ' / ')  # can't use division symbol

            self.calc_screen.setText('0')
            self.current_operation = 'div'

        if index == 8:  # multiplication button clicked
            if 'x' in self.small_calc_screen.text():
                self.small_calc_screen.setText(str(Ops.multiply(self.small_calc_screen.text().split()[0],
                                                                self.calc_screen.text())) + ' x ')
            else:
                self.small_calc_screen.setText(self.calc_screen.text() + ' x ')

            self.calc_screen.setText('0')
            self.current_operation = 'mul'

        if index == 9:  # subtraction button clicked
            if '-' in self.small_calc_screen.text():
                self.small_calc_screen.setText(str(Ops.subtract(self.small_calc_screen.text().split()[0],
                                                                self.calc_screen.text())) + ' - ')
            else:
                self.small_calc_screen.setText(self.calc_screen.text() + ' - ')

            self.calc_screen.setText('0')
            self.current_operation = 'sub'

        if index == 10:  # addition button clicked
            if '+' in self.small_calc_screen.text():
                self.small_calc_screen.setText(str(Ops.add(self.small_calc_screen.text().split()[0],
                                                           self.calc_screen.text())) + ' + ')
            else:
                self.small_calc_screen.setText(self.calc_screen.text() + ' + ')

            self.calc_screen.setText('0')
            self.current_operation = 'add'

        if index == 11:  # plus-minus button clicked
            if len(self.calc_screen.text()) == 1 and self.calc_screen.text() == '0':
                return  # do nothing

            else:
                self.small_calc_screen.setText('negate( ' + self.calc_screen.text() + ' )')
                self.calc_screen.setText('0')

                # For User convenience:
                self.small_calc_screen.setText(self.small_calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.negate(self.small_calc_screen.text().split()[1])))

            self.current_operation = 'neg'

        if index == 12:  # point button clicked
            if '.' in self.calc_screen.text():
                return  # don't allow multiple points
            else:
                self.calc_screen.setText(self.calc_screen.text() + '.')

        if index == 13:  # equal to button clicked
            if '=' in self.small_calc_screen.text():
                return  # do nothing if an answer has already been gotten

            if self.current_operation == 'add':
                if self.is_percent_btn_clicked is True:
                    self.small_calc_screen.setText(self.small_calc_screen.text() + ' =')
                else:
                    self.small_calc_screen.setText(self.small_calc_screen.text() + self.calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.add(self.small_calc_screen.text().split()[0],
                                                     self.small_calc_screen.text().split()[2])))
            elif self.current_operation == 'sub':
                if self.is_percent_btn_clicked is True:
                    self.small_calc_screen.setText(self.small_calc_screen.text() + ' =')
                else:
                    self.small_calc_screen.setText(self.small_calc_screen.text() + self.calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.subtract(self.small_calc_screen.text().split()[0],
                                                          self.small_calc_screen.text().split()[2])))

            elif self.current_operation == 'mul':
                if self.is_percent_btn_clicked is True:
                    self.small_calc_screen.setText(self.small_calc_screen.text() + ' =')
                else:
                    self.small_calc_screen.setText(self.small_calc_screen.text() + self.calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.multiply(self.small_calc_screen.text().split()[0],
                                                          self.small_calc_screen.text().split()[2])))

            elif self.current_operation == 'div':
                if self.is_percent_btn_clicked is True:
                    self.small_calc_screen.setText(self.small_calc_screen.text() + ' =')
                else:
                    self.small_calc_screen.setText(self.small_calc_screen.text() + self.calc_screen.text() + ' =')

                # Check for dividing by zero error:
                if self.small_calc_screen.text().split()[2] == '0':
                    self.handle_math_errors(error_msg='Cannot divide by zero!')
                    self.is_div_by_zero = True
                    return

                self.calc_screen.setText(str(Ops.division(self.small_calc_screen.text().split()[0],
                                                          self.small_calc_screen.text().split()[2])))

            elif self.current_operation == 'sqr':
                self.small_calc_screen.setText(self.small_calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.squared(self.small_calc_screen.text().split()[1])))

            elif self.current_operation == 'neg':
                self.small_calc_screen.setText(self.small_calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.negate(self.small_calc_screen.text().split()[1])))

            elif self.current_operation == 'inv':
                self.small_calc_screen.setText(self.small_calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.inverse(self.small_calc_screen.text().split()[1])))

            elif self.current_operation == 'sqrt':
                self.small_calc_screen.setText(self.small_calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.squareroot(self.small_calc_screen.text().split()[1])))


    def handle_math_errors(self, error_msg):
        """
        Method to handle errors during calculations like: "DividingByZero" and "InvalidInput".

        :param error_msg: Message to indicate calculation error
        """
        self.calc_screen.setStyleSheet('font-size: 18pt; padding: 18px 0px;')
        self.calc_screen.setMaxLength(23)
        self.calc_screen.setText(error_msg)
        for count, b in enumerate(self.all_btns):
            if count == 2:
                continue
            b.setEnabled(False)
        self.all_btns[2]._animation2.setDuration(900)
        self.all_btns[2]._animation2.setLoopCount(-1)
        self.all_btns[2]._animation2.start()







if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
    
