from data.Settings import Settings
from data.DefineAndFillModel import DefineAndFillModel as df
import os
from reportlab.pdfgen import canvas
from datetime import datetime


def model_menu(M: Settings, xml_directory, report_directory):
    
    n = 1  
    #------------------------------------MODEL TEST------------------------------------#
    while n:
        os.system('cls') 
        print('What model do you want to test?')
        print("(to go to the menu insert q)\n" )
        name_model = input()
        
        # back to menu
        if(name_model == 'q'):
            break
        
        # model doesn't exist
        elif(df.open_model_xml(M, name_model, xml_directory) is None):
            os.system('cls') 
            print(f"{name_model} DOESN'T EXIST\n")
            print("To go to the menu insert anything\n")
            c = input()
            break
        
        # set model ready to test
        else:
            M.reset_model_test()
            M.set_model_test(name_model)
            os.system('cls') 
            print(f"{name_model} IS READY TO TEST\n")
            print("To start the test insert anything\n")
            c = input()

            #------------------------------------TEST MENU------------------------------------#
            while True:
                os.system('cls') 
                print("-------------Test Menu-------------\n\n")
                print("1- Led test         2- Button test\n")
                print("3- LCD test         4- Generate report\n")
                print("            5- Menu")
                print("\n\n----------------------------------\n")
                c = input()
                
                # led test
                if (c== '1'):
                    n2 = 1

                # button test  
                elif (c== '2'):
                    n2 = 2

                # lcd test    
                elif (c== '3'):
                    n2 = 3

                # report
                elif(c== '4'):
                    n2 = 4
                
                # back to menu
                elif(c== '5'):
                    n = 0
                    break

                else:
                    continue

                led_test(M, n2)
                button_test(M, n2)
                display_test(M, n2)
                generate_report(n2, name_model, report_directory)


#------------------------------------LED TEST------------------------------------#
def led_test(M: Settings, n2):
    while(n2==1):
        os.system('cls')
        print("What led do you want to test?\n")
        print("(to go to the menu insert q)\n" )
        led_name = input()

                    # back to test menu
        if(led_name == 'q'):
            break

                    # test a specific led
        else:
            index_led = M.index_led(led_name)

                        # led doesn't exist
            if(index_led is None):
                print(f"{led_name} DOESN'T EXIST\n")
                print("To test another one or go to the test menu insert anything\n")
                c = input()
                continue
                        
                        # led exists
            else:
                result_test = 'FUNCAO'

                            # test sucess
                if(result_test == -1):
                    os.system('cls')
                    print(f"{led_name} TEST FAILED\n")
                    print("To test another one or go to the test menu insert anything\n")
                    c = input()
                    continue

                            # test failed
                else:
                    os.system('cls')
                    print(f"{led_name} IS TESTED\n")
                    print("To test another one or go to the test menu insert anything\n")
                    c = input()
                    continue

#------------------------------------BUTTON TEST------------------------------------#
def button_test(M:Settings, n2):
    while(n2==2):
        os.system('cls')
        print("What button do you want to test?\n")
        print("(to go to the test menu insert q)\n" )
        button_name = input()
                    
                    # back to test menu
        if(button_name == 'q'):
            break
                    
                    # test a specific button
        else:
            index_button = M.index_button(button_name)

                         # button doesn't exist
            if(index_button is None):
                os.system('cls')
                print(f"{button_name} DOESN'T EXIST\n")
                print("To test another one or go to the test menu insert anything\n")
                c = input()
                continue
                        
                        # button exists
            else:
                result_test = 'FUNCAO'
                            
                            # test sucess
                if(result_test == -1):
                    os.system('cls')
                    print(f"{button_name} TEST FAILED\n")
                    print("To test another one or go to the test menu insert anything\n")
                    c = input()
                    continue
                            
                            # test failed
                else:
                    os.system('cls')
                    print(f"{button_name} IS TESTED\n")
                    print("To test another one or go to the test menu insert anything\n")
                    c = input()
                    continue

#------------------------------------LCD TEST------------------------------------#
def display_test(M:Settings, n2):
    while(n2==3):
        os.system('cls')
        print("-----------LCD Test Menu-----------\n\n")
        print("1- RGB test         2- Pixel test\n")
        print("3- Char test        4- Test menu")
        print("\n\n-----------------------------------\n")
        c = input()

                    # RGB test
        if (c== '1'):
            result_test = 'FUNCAO'

                        # test sucess
            if(result_test == -1):
                os.system('cls')
                print("RGB TEST FAILED\n")
                print("To test another thing or go to the test menu insert anything\n")
                c = input()
                continue

                        # test failed
            else:
                os.system('cls')
                print("RGB TEST IS DONE\n")
                print("To test another thing or go to the test menu insert anything\n")
                c = input()
                continue

                    # Pixel test
        elif (c== '2'):
            result_test = 'FUNCAO'

                        # test sucess
            if(result_test == -1):
                os.system('cls')
                print("PIXEL TEST FAILED\n")
                print("To test another thing or go to the test menu insert anything\n")
                c = input()
                continue

                        # test failed
            else:
                os.system('cls')
                print("PIXEL TEST IS DONE\n")
                print("To test another thing or go to the test menu insert anything\n")
                c = input()
                continue

                    # Char test
        elif (c== '3'):
            result_test = 'FUNCAO'

                        # test sucess
            if(result_test == -1):
                os.system('cls')
                print("CHAR TEST FAILED\n")
                print("To test another thing or go to the test menu insert anything\n")
                c = input()
                continue

                        # test failed
            else:
                os.system('cls')
                print("CHAR TEST IS DONE\n")
                print("To test another thing or go to the test menu insert anything\n")
                c = input()
                continue

                    # Back to test menu
        elif(c== '4'):
            n2 = 0
            break

        else:
            continue

##------------------------------------REPORT------------------------------------#
def generate_report(n2, name_model, report_directory):
    while(n2==4):
        
        # get the current date and time
        now = datetime.now()

        # format the date string
        date_str = now.strftime("%d-%m-%Y")
        hour_str = now.strftime("%H:%M:%S")

        # specify the path and filename of the PDF file with the date string in the title
        report = canvas.Canvas(f'{report_directory}/Report of {name_model}.pdf')

        # add some text to the PDF
        report.drawString(100, 750, f"Report generated on the day {date_str} at {hour_str}")

        # save the PDF file
        report.save()

        os.system('cls')
        print("Report is generated\n")
        print("To go to the Test Menu insert anything\n")
        c = input()

        n2 = 0
        break