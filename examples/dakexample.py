from daktronics import DakUDP, Daktronics

if __name__ == '__main__':
    print("UDP MULTICAST 21000")
    dak_data = DakUDP(21000)
    dak = Daktronics("hockey/lacrosse", dak_data)
    while True:
        dak.update()
        print("--------------------------------------------------------------")
        print(dak['Main Clock Time (mm:ss/ss.t )'])
        print(dak['Home Team Name'], dak['Home Team Score'])
        print(dak['Guest Team Name'], dak['Guest Team Score'])
        print("--------------------------------------------------------------")
