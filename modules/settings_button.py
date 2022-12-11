from modules.lists import *
from modules.fonts import font1
def resize_buttons(name, width, height):
    name.setMaximumWidth(width)
    name.setMaximumHeight(height)
width = 56
height = 56
def customize_buttons():
    for el in range(3, 8):
        list_Symbols_Button[el].setStyleSheet(
            f'''background-color: rgb(47,79,79);
                font-size: 28px;
                color: rgb(225,225,225);
                max-width: {width}px;
                max-height: {height}px;

            '''
        )
    for el in range(0, 3):
        list_Symbols_Button[el].setStyleSheet(
            f'''background-color: rgb(70,102,102);
                font-size: 28px;
                color: rgb(225,225,225);
                max-width: {width}px;
                max-height: {height}px;
            '''
        )
    for el in range(1, len(list_numButtons)):
        list_numButtons[el].setStyleSheet(
            f'''
                background-color: rgb(90,122,122);
                font-size: 28px;
                color: rgb(225,225,225);
                max-width: {width}px;
                max-height: {height}px;
                border-color: rgb(80,80,80);
            '''
        )
    list_Symbols_Button[-1].setStyleSheet(
        f'''background-color: rgb(90,122,122);
            font-size: 28px;
            color: rgb(225,225,225);
            max-width: {width}px;
            max-height: {height}px;
        '''
    )
    list_numButtons[0].setStyleSheet('''
        background-color: rgb(100,149,237);
        font-size: 28px;
        color: rgb(225,225,225);
        max-width: 120px;
        max-height: 56px;
    ''') 