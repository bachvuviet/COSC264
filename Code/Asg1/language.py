# coding= utf-8
# DT Language Structure (language.py)
# Bach Vu
# 01/08/2020

from datetime import datetime

class DT_Language:
    def __init__(self, langMode, outputType, time):
        # (0x0001:Eng, 0x0002:Maori, 0x0003:Ger)
        self.language = langMode - 1
        self.mode = outputType - 1
        self.time = time
        self.stringFormats = [
            ["Today's date is {} {}, {}", "The current time is {:02d}:{:02d}"],
            ["Ko te ra o tenei ra ko {} {}, {}", "Ko te wa o tenei wa {:02d}:{:02d}"],
            ["Heute ist der {}. {} {}", "Die Uhrzeit ist {:02d}:{:02d}"]
        ]
        self.Months = [
            ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
            ["Kohitātea", "Hui-tanguru", "Poutū-te-rangi", "Paenga-whāwhā", "Haratua", "Pipiri", "Hōngongoi", "	Here-turi-kōkā", "Mahuru", "Whiringa-ā-nuku", "	Whiringa-ā-rangi", "Hakihea"],
            ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
        ]
        
    def DTtoString(self):
        day, month, year = self.time[2], self.time[1], self.time[0]
        hour, minute = self.time[3], self.time[4]
        output = self.stringFormats[self.language][self.mode]
        
        if self.mode == 0:
            month_str = self.Months[self.language][month-1]
            if self.language != 2:
                output = output.format(month_str, day, year)
            else:
                output = output.format(day, month_str, year)  
        elif self.mode == 1:
            output = output.format(hour, minute)            
        return output
    
def test():
    dt = [2020,8,8,7,0]
    lang1 = DT_Language(0x0001, 0x0001, dt)
    print(lang1.DTtoString())
    lang1 = DT_Language(0x0001, 0x0002, dt)
    print(lang1.DTtoString())
    lang1 = DT_Language(0x0002, 0x0001, dt)
    print(lang1.DTtoString())
    lang1 = DT_Language(0x0002, 0x0002, dt)
    print(lang1.DTtoString())
    lang1 = DT_Language(0x0003, 0x0001, dt)
    print(lang1.DTtoString())
    lang1 = DT_Language(0x0003, 0x0002, dt)
    print(lang1.DTtoString())  
    
if __name__ == "__main__":
    test()