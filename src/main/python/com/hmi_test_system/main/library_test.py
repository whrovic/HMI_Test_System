from data.Settings import Settings
from data.DefineAndFillModel import DefineAndFillModel as df
import os
from reportlab.pdfgen import canvas
from datetime import datetime


def test_menu(M: Settings, name_model, test_type):

    if isinstance(name_model, str):
        pass
    else:
        return 3    # invalid argument
    
    if (test_type != 'LCD' or test_type != 'LED' or test_type != 'BUTTON' or test_type is not None)
        return 3    # invalid argument

    # model doesn't exist
    if(df.open_model_xml(M, name_model) is None):
        print(f"{name_model} DOESN'T EXIST\n")
        return 2
    
    # set model ready to test
    else:
        M.reset_model_test()
        M.set_model_test(name_model)
        print(f"{name_model} IS READY TO TEST\n")

        # led test
        if(test_type == "LED"):       
            result_led =led_test(M)
            if(result_led == 0):
                return 0    # test passed
            elif(result_led == -1): 
                return 8   # led test failed
            
        # lcd test
        elif(test_type == "LCD"):       
            result_display =  display_test(M, 4) # 1 - pixel | 2 - rgb | 3- char | 4 - all 
            if(result_display == 0):
                return 0    # test passed
            elif(result_display == -1): 
                return 9   # led test failed  

        # button test
        elif(test_type == "BUTTON"):    
            result_button = button_test(M)
            if(result_button == 0):
                return 0    # test passed
            elif(result_button == -1): 
                return 10   # led test failed


        # default - test all
        elif(test_type is None):                           
            result_led =led_test(M)
            result_display = display_test(M, 4)
            result_button = button_test(M)

            if(result_led + result_display + result_button == 0):
                return 0    # all tests passed
            elif(result_led == -1): 
                return 8   # led test failed
            elif(result_display== -1): 
                return 9   # display test failed 
            elif(result_button == -1): 
                return 10  # button test failed  


#------------------------------------LED TEST------------------------------------#
def led_test(M: Settings):

    M.test.test_led(M.model_test.leds_test)
    result: list[bool] = []
    for i in len(M.model_test.leds_test):
        led_result = M.model_test.leds_test[int(i)].result_test_Led()
        result.append(led_result)
        print(f"{M.model_test.leds_test[int(i)].get_led().get_name()} test: ")
        print("ok" if led_result==1 else "not ok")     

    if sum(result) == len(result): 
        return 0    # test passed
    else:
        return -1   # test failed          


#------------------------------------BUTTON TEST------------------------------------#
def button_test(M:Settings):
    pass
                        
                
#------------------------------------LCD TEST------------------------------------#
def display_test(M:Settings, code: int):
    result = M.test.test_display(M.model_test.display_test, code)
    print("LCD test:")
    print("ok" if result == 0 else "not ok")
    return result   # 0 is sucess | -1 is failure


##------------------------------------REPORT------------------------------------#
def generate_report(M: Settings, name_model):
    
        
    # get the current date and time
    now = datetime.now()

    # format the date string
    date_str = now.strftime("%d-%m-%Y")
    hour_str = now.strftime("%H:%M:%S")

    # specify the path and filename of the PDF file with the date string in the title
    report = canvas.Canvas(f'{M.path.get_report_directory}/Report of {name_model}.pdf')

    # add some text to the PDF
    report.drawString(100, 750, f"Report generated on the day {date_str} at {hour_str}")

    # save the PDF file
    report.save()

    print("Report generated\n")

    return 0