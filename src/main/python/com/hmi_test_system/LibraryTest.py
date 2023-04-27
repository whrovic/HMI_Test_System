from data.Settings import Settings
from data.DefineAndFillModel import DefineAndFillModel as df
import os
from reportlab.pdfgen import canvas
from datetime import datetime



def model_menu(M: Settings):
     
    #------------------------------------MODEL TEST------------------------------------#
    while True:
        os.system('cls') 
        print("-------------Test Menu-------------\n\n")
        print("1- Choose model      2- Manual test\n")
        print("3- Automatic test    4- Menu")
        print("\n\n-----------------------------------\n")
        c = input()
        
        # set model test
        if(c == '1'):
            os.system('cls') 
            print('What model do you want to test?')
            print("(to go to the Test Menu insert q)\n" )
            name_model = input()
            
            # back to menu
            if(name_model == 'q'):
                break
            
            # model doesn't exist
            elif(df.open_model_xml(M, name_model) is None):
                os.system('cls') 
                print(f"{name_model} DOESN'T EXIST\n")
                print("To go to the menu insert anything\n")
                c = input()
                continue
            
            # set model ready to test
            else:
                M.reset_model_test()
                M.set_model_test(name_model)
                os.system('cls') 
                print(f"{name_model} IS READY TO TEST\n")
                print("To start the test insert anything\n")
                c = input()
        
        # Manual test
        elif(c == '2'):
            if(len(M.model_test.leds_test) == 0):
                print('Choose a model to test first')
                print("To go to the test menu insert anything\n")
                c = input()
                continue
            else:  
                manual_test(M, name_model)

        # Automatic test
        elif(c == '3'):
            if(len(M.model_test.leds_test) == 0):
                print('Choose a model to test first')
                print("To go to the test menu insert anything\n")
                c = input()
                continue
            else:  
                automatic_test(M, name_model)
            

        # Menu
        elif(c == '4'):
            break

        else:
            continue


#------------------------------------Automatic TEST------------------------------------#
def automatic_test(M: Settings, name_model):
    print("In construction")
    print("  Come later")
    c = input()

#------------------------------------Manual TEST------------------------------------#
def manual_test(M: Settings, name_model):

    M.test.start_test()

    #------------------------------------TEST MENU------------------------------------#
    while True:
        os.system('cls') 
        print("-------------Manual Test-------------\n\n")
        print("1- Led test         2- Button test\n")
        print("3- LCD test         4- Generate report\n")
        print("            5- Menu")
        print("\n\n-------------------------------------\n")
        c = input()

        # led test
        if (c== '1'):
            led_test(M)

        # button test  
        elif (c== '2'):
            print("In construction")
            print("  Come later")
            c = input()
            #button_test(M)

        # lcd test    
        elif (c== '3'):
            display_test(M)

        # report
        elif(c== '4'):
            generate_report(name_model)

        # back to menu
        elif(c== '5'):
            M.test.end_test()
            break
        
        else:
            continue

#------------------------------------LED TEST------------------------------------#
def led_test(M: Settings):
    while True:
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
                result_test = M.test.test_led(M.model_test.leds_test)

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
def button_test(M:Settings):
    while True:
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
def display_test(M:Settings):
    while True:
        os.system('cls')
        print("-----------LCD Test Menu-----------\n\n")
        print("1- Pixel test       2- RGB test\n")
        print("3- Char test        4- Test menu")
        print("\n\n-----------------------------------\n")
        c = input()

                    # Pixel test
        if (c== '1'):
            result_test = M.test.test_display(M.model_test.display_test, int(c))

                        # test failed
            if(result_test == -1):
                os.system('cls')
                print("Pixel TEST FAILED\n")
                print("To test another thing or go to the test menu insert anything\n")
                c = input()
                continue

                        # test sucess
            else:
                os.system('cls')
                print("Pixel TEST IS DONE\n")
                print("To test another thing or go to the test menu insert anything\n")
                c = input()
                continue

                    # RGB test
        elif (c== '2'):
            result_test = M.test.test_display(M.model_test.display_test, int(c))

                        # test failed
            if(result_test == -1):
                os.system('cls')
                print("RGB TEST FAILED\n")
                print("To test another thing or go to the test menu insert anything\n")
                c = input()
                continue

                        # test sucess
            else:
                os.system('cls')
                print("RGB TEST IS DONE\n")
                print("To test another thing or go to the test menu insert anything\n")
                c = input()
                continue

                    # Char test
        elif (c== '3'):
            result_test = M.test.test_display(M.model_test.display_test, int(c))

                        # test failed
            if(result_test == -1):
                os.system('cls')
                print("CHAR TEST FAILED\n")
                print("To test another thing or go to the test menu insert anything\n")
                c = input()
                continue

                        # test sucess
            else:
                os.system('cls')
                print("CHAR TEST IS DONE\n")
                print("To test another thing or go to the test menu insert anything\n")
                c = input()
                continue

                    # Back to test menu
        elif(c== '4'):
            break

        else:
            continue

##------------------------------------REPORT------------------------------------#
def generate_report(M: Settings, name_model):
    while True:
        
        # get the current date and time
        now = datetime.now()

        # format the date string
        date_str = now.strftime("%d-%m-%Y")
        hour_str = now.strftime("%H:%M:%S")

        while True:
            try: 
                # specify the path and filename of the PDF file with the date string in the title
                report = canvas.Canvas(f'{M.path.get_report_directory}/Report of {name_model}.pdf')
                break
            except:
                print("Error path don't exist")
                print("To go to the Test Menu insert anything\n")
                c = input()
                return -1
        

        # add some text to the PDF
        report.drawString(100, 750, f"Report generated on the day {date_str} at {hour_str}")

        # save the PDF file
        report.save()

        os.system('cls')
        print("Report is generated\n")
        print("To go to the Test Menu insert anything\n")
        c = input()

        return 0