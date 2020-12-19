"""
File:         smart_house.py
Author:       Vu Nguyen
Date:         11/22/2020
Section:      31
E-mail:       vnguye12@umbc.edu
Description:  This program info such as devices--entered by the user
              --and store it into a file. The file can then be called
              or edited based on the user answer.
"""

class Device:
    def __init__(self, name, toggle):
        self.name = name
        self.toggle = toggle  # <-- This indicating whether the device is turn on or off.


class SmartHouse:
    def __init__(self, address):
        self.address = address
        self.home = []  # <-- This list store object(device).
        self.ON = 'on'
        self.TOGGLE = -1

    def add_device(self, device):
        """
        :param device: Take in device as an object in the parameter
        :return: add the device to a list or some.
        """
        self.home.append(device)

    def get_device(self, the_id):
        # This conditional loop retrieve the device given the id/name of that device
        for device in self.home:
            if device.name == the_id:
                return device

    def save_house(self, file_name):
        """
        This write to a file thus updating the list of device.
        :param file_name: the file name that the user want to write to/save
        :return: doesn't return anything. Just write to a new file.
        """
        with open(file_name, 'w') as file_writer:
            for device in self.home:
                if device.toggle:
                    file_writer.write("{} on\n".format(device.name))
                else:
                    file_writer.write("{} off\n".format(device.name))

    def load_house(self, file_name):
        """
        This retrieve info from the file that the device was save in
        and store the info in a list.
        :param file_name: The file that user want to retrieve info from.
        :return: append the device into the list.
        """
        with open(file_name, 'r') as file_reader:
            for line in file_reader.readlines():
                device_info = line.split()  # <-- This store a list (Device name[:-1] or and toggle[-1])
                if device_info[self.TOGGLE] == self.ON:
                    self.home.append(Device(" ".join(device_info[:-1]), True))
                else:
                    self.home.append(Device(" ".join(device_info[:-1]), False))

    def display(self):
        print("For the house at {}".format(self.address))
        for device in self.home:
            if device.toggle:
                print("\t{} is on".format(device.name))
            else:
                print("\t{} is off".format(device.name))


if __name__ == '__main__':
    address = input('What is the address of the house?')
    house = SmartHouse(address)

    command = input('What do you want to do? (add device, toggle device, load <file>, save <file>, display) ').lower()
    while command != 'quit':
        if command == 'add' or command == 'add device':
            the_id = input('What is the device id?')

            # This condition checks to see if the device is not in the home.
            if not house.get_device(the_id):
                yes_no = input('Is the device on? (yes/no)')
                if yes_no == 'yes':
                    house.add_device(Device(the_id, True))
                elif yes_no == 'no':
                    house.add_device(Device(the_id, False))
            else:
                print('There is no device id: {} in the ')

        elif command == 'toggle' or command == 'toggle device':
            the_id = input('What is the device id?')
            the_device = house.get_device(the_id)
            if the_device:
                on_off_toggle = input('On, Off or Toggle? ').lower()
                if on_off_toggle == 'on':
                    the_device.toggle = True
                elif on_off_toggle == 'off':
                    the_device.toggle = False
                elif on_off_toggle == 'toggle':
                    the_device.toggle = not the_device.toggle
            else:
                print('There is no device id: {} in the ')

        elif command == 'load':
            file_name = input('What is the filename to load from? ')
            house.load_house(file_name)

            print('The house has been loaded from {}'.format(file_name))
        elif command == 'save':
            file_name = input('What is the filename to save as? ')
            house.save_house(file_name)

            print('The house has been saved in {}'.format(file_name))
        elif command == 'display':
            house.display()
        else:
            print('unknown command', command)

        command = input('What do you want to do? (add device, toggle device, load <file>, save <file>, display) ').lower()
