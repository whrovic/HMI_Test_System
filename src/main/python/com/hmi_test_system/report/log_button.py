
class LogButton:
    def button_test_display(button_name, test_result):
      print("Display Test Results:")
      print(f"Button '{button_name}': {'Passed' if test_result else 'Failed'}")

   
    def button_test_serial(button_name, test_result):
      print("Serial Port Test Results:")
      print(f"Button '{button_name}': {'Passed' if test_result else 'Failed'}")


    def button_test_combined(button_name, display_result, serial_result):
      print("Combined Test Results:")
      print(f"Button '{button_name}':")
      print(f"- Display Test: {'Passed' if display_result else 'Failed'}")
      print(f"- Serial Port Test: {'Passed' if serial_result else 'Failed'}")
