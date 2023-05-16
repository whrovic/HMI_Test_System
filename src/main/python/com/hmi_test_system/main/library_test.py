from data.settings import Settings
from data.define_and_fill_model import DefineAndFillModel as df
import os
import sys
from data.model.model import Model
from data.model.led import Led 
from data.model.display import Display
from data.model.button import Button


def test_menu(M: Settings):

    name_model = sys.argv[0]

    if isinstance(name_model, str):
        pass
    else:
        exit_code = 3
        return exit_code    # invalid argument

    # model doesn't exist
    if(df.open_model_xml(M, name_model) is None):
        print(f"{name_model} DOESN'T EXIST\n")
        exit_code = 2
        return exit_code

    
    model = M.call_model(name_model)
    leds = model.get_leds()
    buttons = model.get_buttons()
    display = model.get_display()
    leds_name = []
    buttons_name = [] 


    # specific tests
    if len(sys.argv) >= 2:
        args = []

        for i in len(sys.argv)-1:
            args[i] = sys.argv[i+1]

        test_type = []

        for i in len(args):

            if (args[i] == 'led' or args[i] == 'display' or args[i] == 'key'):
                test_type[i] = args[i]

                # could have optional arg
                if(test_type[i] == 'led'):
                    for t in len(args)-i:
                        ok = 0
                        
                        # verify if the arg is optional
                        if (args[i+1+t] != 'led' or args[i+1+t] != 'display' or args[i+1+t] != 'key'):
                            
                            # verify if led name exists in the model
                            for y in len(leds):
                                name = leds[int(y)].get_name()
                                if(name == args[i+1+t]):
                                    ok = 1
                                    leds_name[t] = args[i+1+t]
                            
                            # led name doesn´t exist in the model
                            if(ok == 0):
                                exit_code = 3   # invalid argument
                                return exit_code
                        
                        # it's not an optional arg
                        else:
                            i = i+1+t
                            break
                
                # could have optional arg
                elif(test_type[i] == 'key'):
                    for t in len(args)-i:

                        # verify if the arg is optional
                        if (args[i+1+t] != 'led' or args[i+1+t] != 'display' or args[i+1+t] != 'key'):
                            
                            # verify if button name exists in the model
                            for y in len(buttons):
                                name = buttons[int(y)].get_name()
                                if(name == args[i+1+t]):
                                    ok = 1
                                    buttons_name[t] = args[i+1+t]
                            
                            # button name doesn´t exist in the model
                            if(ok == 0):
                                exit_code = 3   # invalid argument
                                return exit_code
                        
                        # it's not an optional arg
                        else:
                            i = i+1+t
                            break

            else: 
                exit_code = 3   # invalid argument
                return exit_code    
               
        
        
        for i in len(test_type):

            # led test
            if(test_type[i] == "led"):

                # if user doesnt't choose the leds
                if(len(leds_name) == 0):
                     for i in len(leds):
                        leds_name[i] = leds[int(i)].get_name()
     
                result_led = led_test(M, model, leds_name)
                if(result_led == 0):
                    exit_code = 0     # test passed
                elif(result_led == -1): 
                    exit_code = 8     # led test failed


            # lcd test
            elif(test_type[i] == "display"):   
                
                result_display =  display_test(M, model, display, 4) # 1 - pixel | 2 - rgb | 3- char | 4 - all 
                if(result_display == 0):
                    exit_code = 0     # test passed
                elif(result_display == -1): 
                    exit_code = 9     # lcd test failed  


            # button test
            elif(test_type[i] == "key"):
                
                # if user doesnt't choose the buttons
                if(len(buttons_name) == 0):
                    for i in len(buttons):
                        buttons_name[i] = buttons[int(i)].get_name()
                    
                result_button = button_test(M, model, 1, buttons_name) # 1 - sp | 2 - dsp | 3- all
                if(result_button == 0):
                    exit_code = 0     # test passed
                elif(result_button == -1): 
                    exit_code = 10    # button test failed
    
    # default -> all tests
    else:

        # get all leds name
        for i in len(leds):
            leds_name[i] = leds[int(i)].get_name()
        
        # get all buttons name
        for i in len(buttons):
            buttons_name[i] = buttons[int(i)].get_name()

        result_led = led_test(M, model, leds_name)
        result_display = display_test(M, model, display, 4)
        result_button = button_test(M, model, 1, buttons_name)

        if(result_led + result_display + result_button == 0):
            exit_code = 0     # all tests passed
        elif(result_led == -1): 
            exit_code = 8     # led test failed
        elif(result_display== -1): 
            exit_code = 9     # display test failed 
        elif(result_button == -1): 
            exit_code = 10    # button test failed                        
                


    return exit_code



#------------------------------------LED TEST------------------------------------#
def led_test(M: Settings, model: Model, leds_name: list[str] = []):

    result = M.test.seq_led(model, leds_name)
    
    return result
         


#------------------------------------BUTTON TEST------------------------------------#
def button_test(M:Settings,  model: Model, code: int, buttons_name: list[str] = []):

    if code == 1:
        result = M.test.seq_button(model, buttons_name, 1, 0)

    elif code == 2:
        result = M.test.seq_button(model, buttons_name, 0, 1)

    elif code == 3:
        result =M.test.seq_button(model, buttons_name, 1, 1)

    return result
 



#------------------------------------LCD TEST------------------------------------#
def display_test(M:Settings, model: Model, display: Display, code: int):
    
    if code == 1:
        result = M.test.seq_display(model, display, 1, 0, 0)

    elif code == 2:
        result = M.test.seq_display(model, display, 0, 0, 1)

    elif code == 3:
        result = M.test.seq_display(model, display, 0, 1, 0)

    elif code == 4:
        result = M.test.seq_display(model, display, 1, 1, 1)

    return result