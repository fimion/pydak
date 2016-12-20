import serial

dakSports = {
    'auto racing': {},
    'baseball': {},
    'basketball': {},
    'cricket': {},
    'event counter': {},
    'football': {
        'dakSize': [1, 295],
        'Main Clock Time [mm:ss/ss.t]': [1, 5],
        'Main Clock Time [mm:ss.t]': [6, 8],
        'Main Clock/Time Out/TOD [mm:ss/ss.t]': [14, 5],
        'Main Clock/Time Out/TOD [mm:ss.t]': [19, 8],
        'Main Clock =0': [27, 1],
        'Main Clock Stopped': [28, 1],
        'Main Clock/Time Out Horn': [29, 1],
        'Main Clock Horn': [30, 1],
        'Time Out Horn': [31, 1],
        'Time Out Time': [32, 8],
        'Time of Day': [40, 8],
        'Home Team Name': [48, 20],
        'Guest Team Name': [68, 20],
        'Home Team Abbreviation': [88, 10],
        'Guest Team Abbreviation': [98, 10],
        'Home Team Score': [108, 4],
        'Guest Team Score': [112, 4],
        'Home Time Outs Left - Full': [116, 2],
        'Home Time Outs Left - Partial': [118, 2],
        'Home Time Outs Left - Television': [120, 2],
        'Home Time Outs Left - Total': [122, 2],
        'Guest Time Outs Left - Full': [124, 2],
        'Guest Time Outs Left - Partial': [126, 2],
        'Guest Time Outs Left - Television': [128, 2],
        'Guest Time Outs Left - Total': [130, 2],
        'Home Time Out Indicator': [132, 1],
        'Home Time Out Text': [133, 4],
        'Guest Time Out Indicator': [137, 1],
        'Guest Time Out Text': [138, 4],
        'Quarter': [142, 2],
        'Quarter Text': [144, 4],
        'Quarter Description': [148, 12],
        'Internal Relay': [160, 1],
        'Ad Panel / Caption Power': [161, 1],
        'Ad Panel / Caption #1': [162, 1],
        'Ad Panel / Caption #2 ': [163, 1],
        'Ad Panel / Caption #3': [164, 1],
        'Ad Panel / Caption #4': [165, 1],
        'Reserved for Future Use': [166, 35],
        'Play Clock Time': [201, 8],
        'Play Clock Horn': [209, 1],
        'Home Possession Indicator': [210, 1],
        'Home Possession Text': [211, 4],
        'Guest Possession Indicator': [215, 1],
        'Guest Possession Text': [216, 4],
        'Ball On': [220, 2],
        'Down': [222, 3],
        'To Go': [225, 2],
        'Home Score - Period 1': [227, 2],
        'Home Score - Period 2': [229, 2],
        'Home Score - Period 3': [231, 2],
        'Home Score - Period 4': [233, 2],
        'Home Score - Period 5': [235, 2],
        'Home Score - Period 6': [237, 2],
        'Home Score - Period 7': [239, 2],
        'Home Score - Period 8': [241, 2],
        'Home Score - Period 9': [243, 2],
        'Home Score - Current Period': [245, 2],
        'Guest Score - Period 1': [247, 2],
        'Guest Score - Period 2': [249, 2],
        'Guest Score - Period 3': [251, 2],
        'Guest Score - Period 4': [253, 2],
        'Guest Score - Period 5': [255, 2],
        'Guest Score - Period 6': [257, 2],
        'Guest Score - Period 7': [259, 2],
        'Guest Score - Period 8': [261, 2],
        'Guest Score - Period 9': [263, 2],
        'Guest Score - Current Period': [265, 2],
        'Home Rushing Yards': [267, 4],
        'Home Passing Yards': [271, 4],
        'Home Total Yards': [275, 4],
        'Guest Rushing Yards': [279, 4],
        'Guest Passing Yards': [283, 4],
        'Guest Total Yards': [287, 4],
        'Home First Downs': [291, 2],
        'Guest First Downs': [293, 2]
    },
    'hockey/lacrosse': {
        'dakSize': [1, 493],
        'Main Clock Time (mm:ss/ss.t )': [1, 5],
        '2 Main Clock Time (mm:ss.t )': [6, 8],
        '3 Main Clock/Time Out/TOD (mm:ss/ss.t )': [14, 5],
        '4 Main Clock/Time Out/TOD (mm:ss.t )': [19, 8],
        '5 Main Clock 0': [27, 1],
        '6 Main Clock Stopped': [28, 1],
        '7 Main Clock/Time Out Horn': [29, 1],
        '8 Main Clock Horn': [30, 1],
        '9 Time Out Horn': [31, 1],
        '10 Time Out Time (mm:ss)': [32, 8],
        '11 Time of Day (hh:mm:ss)': [40, 8],
        '12 Home Team Name': [48, 20],
        '13 Guest Team Name': [68, 20],
        '14 Home Team Abbreviation': [88, 10],
        '15 Guest Team Abbreviation': [98, 10],
        '16 Home Team Score': [108, 4],
        '17 Guest Team Score': [112, 4],
        '18 Home Time Outs Left - Full': [116, 2],
        '19 Home Time Outs Left - Partial': [118, 2],
        '20 Home Time Outs Left - Television': [120, 2],
        '21 Home Time Outs Left - Total': [122, 2],
        '22 Guest Time Outs Left - Full': [124, 2],
        '23 Guest Time Outs Left - Partial': [126, 2],
        '24 Guest Time Outs Left - Television': [128, 2],
        '25 Guest Time Outs Left - Total': [130, 2],
        '26 Home Time Out Indicator': [132, 1],
        '27 Home Time Out Text': [133, 4],
        '28 Guest Time Out Indicator': [137, 1],
        '29 Guest Time Out Text': [138, 4],
        '30 Period': [142, 2],
        '31 Period Text': [144, 4],
        '32 Period Description': [148, 12],
        '33 Internal Relay': [160, 1],
        '34 Ad Panel / Caption Power': [161, 1],
        '35 Ad Panel / Caption #1': [162, 1],
        '36 Ad Panel / Caption #2': [163, 1],
        '37 Ad Panel / Caption #3': [164, 1],
        '38 Ad Panel / Caption #4': [165, 1],
        '39 Reserved for Future Use': [166, 35],
        '40 Shot Clock Time (mm:ss)': [201, 8],
        '41 Shot Clock Horn': [209, 1],
        '42 Inverse Time Clock (mm:ss)': [210, 8],
        '43 Inverse/Main/Time Out/TOD (mm:ss)': [218, 8],
        '44 Home Player #1-Number': [226, 2],
        '45 Home Player #1-Penalty Time (mm:ss)': [228, 8],
        '46 Home Player #2-Number': [236, 2],
        '47 Home Player #2-Penalty Time (mm:ss)': [238, 8],
        '48 Home Player #3-Number': [246, 2],
        '49 Home Player #3-Penalty Time (mm:ss)': [248, 8],
        '50 Home Player #4-Number': [256, 2],
        '51 Home Player #4-Penalty Time (mm:ss)': [258, 8],
        '52 Home Player #5-Number': [266, 2],
        '53 Home Player #5-Penalty Time (mm:ss)': [268, 8],
        '54 Home Player #6-Number': [276, 2],
        '55 Home Player #6-Penalty Time (mm:ss)': [278, 8],
        '56 Guest Player #1-Number': [286, 2],
        '57 Guest Player #1-Penalty Time (mm:ss)': [288, 8],
        '58 Guest Player #2-Number': [296, 2],
        '59 Guest Player #2-Penalty Time (mm:ss)': [298, 8],
        '60 Guest Player #3-Number': [306, 2],
        '61 Guest Player #3-Penalty Time (mm:ss)': [308, 8],
        '62 Guest Player #4-Number': [316, 2],
        '63 Guest Player #4-Penalty Time (mm:ss)': [318, 8],
        '64 Guest Player #5-Number': [326, 2],
        '65 Guest Player #5-Penalty Time (mm:ss)': [328, 8],
        '66 Guest Player #6-Number': [336, 2],
        '67 Guest Player #6-Penalty Time (mm:ss)': [338, 8],
        '68 Home Penalty Indicator': [346, 1],
        '69 Home Penalty Text': [347, 7],
        '70 Guest Penalty Indicator': [354, 1],
        '71 Guest Penalty Text': [355, 7],
        '72 Home Score - Period 1': [362, 2],
        '73 Home Score - Period 2': [364, 2],
        '74 Home Score - Period 3': [366, 2],
        '75 Home Score - Period 4': [368, 2],
        '76 Home Score - Period 5': [370, 2],
        '77 Home Score - Period 6': [372, 2],
        '78 Home Score - Period 7': [374, 2],
        '79 Home Score - Period 8': [376, 2],
        '80 Home Score - Period 9': [378, 2],
        '81 Home Score - Current Period': [380, 2],
        '82 Guest Score - Period 1': [382, 2],
        '83 Guest Score - Period 2': [384, 2],
        '84 Guest Score - Period 3': [386, 2],
        '85 Guest Score - Period 4': [388, 2],
        '86 Guest Score - Period 5': [390, 2],
        '87 Guest Score - Period 6': [392, 2],
        '88 Guest Score - Period 7': [394, 2],
        '89 Guest Score - Period 8': [396, 2],
        '90 Guest Score - Period 9': [398, 2],
        '91 Guest Score - Current Period': [400, 2],
        '92 Home Shots On Goal - Period 1': [402, 2],
        '93 Home Shots On Goal - Period 2': [404, 2],
        '94 Home Shots On Goal - Period 3': [406, 2],
        '95 Home Shots On Goal - Period 4': [408, 2],
        '96 Home Shots On Goal - Period 5': [410, 2],
        '97 Home Shots On Goal - Period 6': [412, 2],
        '98 Home Shots On Goal - Period 7': [414, 2],
        '99 Home Shots On Goal - Period 8': [416, 2],
        '100 Home Shots On Goal - Period 9': [418, 2],
        '101 Home Shots On Goal - Current': [420, 2],
        '102 Home Shots On Goal - Total': [422, 3],
        '103 Home Saves - Period 1': [425, 2],
        '104 Home Saves - Period 2': [427, 2],
        '105 Home Saves - Period 3': [429, 2],
        '106 Home Saves - Period 4': [431, 2],
        '107 Home Saves - Period 5': [433, 2],
        '108 Home Saves - Period 6': [435, 2],
        '109 Home Saves - Period 7': [437, 2],
        '110 Home Saves - Period 8': [439, 2],
        '111 Home Saves - Period 9': [441, 2],
        '112 Home Saves - Current': [443, 2],
        '113 Home Saves - Total': [445, 3],
        '114 Guest Shots On Goal - Period 1': [448, 2],
        '115 Guest Shots On Goal - Period 2': [450, 2],
        '116 Guest Shots On Goal - Period 3': [452, 2],
        '117 Guest Shots On Goal - Period 4': [454, 2],
        '118 Guest Shots On Goal - Period 5': [456, 2],
        '119 Guest Shots On Goal - Period 6': [458, 2],
        '120 Guest Shots On Goal - Period 7': [460, 2],
        '121 Guest Shots On Goal - Period 8': [462, 2],
        '122 Guest Shots On Goal - Period 9': [464, 2],
        '123 Guest Shots On Goal - Current': [466, 2],
        '124 Guest Shots On Goal - Total': [468, 3],
        '125 Guest Saves - Period 1': [471, 2],
        '126 Guest Saves - Period 2': [473, 2],
        '127 Guest Saves - Period 3': [475, 2],
        '128 Guest Saves - Period 4': [477, 2],
        '129 Guest Saves - Period 5': [479, 2],
        '130 Guest Saves - Period 6': [481, 2],
        '131 Guest Saves - Period 7': [483, 2],
        '132 Guest Saves - Period 8': [485, 2],
        '133 Guest Saves - Period 9': [487, 2],
        '134 Guest Saves - Current': [489, 2],
        '135 Guest Saves - Total': [491, 3],
    },
    'judo': {},
    'karate': {},
    'lane timer': {},
    'pitch and speed': {},
    'rodeo': {},
    'soccer': {},
    'strike out count': {},
    'taekwondo': {},
    'tennis': {},
    'track': {},
    'volleyball': {},
    'waterpolo': {},
    'wrestling': {}
}


class Daktronics(object):
    def __init__(self, sport, ser=None):
        if ser is not None:
            self.Serial = ser
        else:
            self.Serial = serial.Serial("COM1", 19200)
        self.header = b''
        self.code = b''
        self.rtd = b''
        self.checksum = b''
        self.text = b''
        self.sport = dakSports[sport]
        self.dakString = " " * self.sport['dakSize'][1]

    def update(self):
        c = b''
        self.rtd = b''
        while c != b'\x16':
            c = self.Serial.read()
        c = b'\x16'
        while c != b'\x17':
            c = self.Serial.read()
            self.rtd += c

        self.header = self.rtd.partition(b'\x16')[2].partition(b'\x01')[0]
        self.code = self.rtd.partition(b'\x01')[2].partition(b'\x02')[0].partition(b'\x04')[0]
        self.text = self.rtd.partition(b'\x02')[2].partition(b'\x04')[0]
        self.checksum = self.rtd.partition(b'\x04')[2].partition(b'\x17')[0]

        code = self.code.decode()
        code = code[-4:]
        text = self.text.decode()
        self.dakString = self.dakString[:int(code)] + text + self.dakString[int(code) + len(text):]

    def __getitem__(self, gikey):
        if gikey in self.sport:
            return self.dakString[self.sport[gikey][0] - 1:self.sport[gikey][1] + self.sport[gikey][0] - 1]
        return ""


if __name__ == '__main__':
    dak = Daktronics("football")
    while True:
        dak.update()
        print("--------------------------------------------------------------")
        print(dak['Main Clock Time [mm:ss/ss.t]'])
        print(dak['Home Team Name'], dak['Home Team Score'])
        print(dak['Guest Team Name'], dak['Guest Team Score'])
        print("--------------------------------------------------------------")
