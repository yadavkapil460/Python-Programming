telecom = ["Jio","airtel","Starlink","kuiper","V!","BSNL"]
software=["tata docomo"]
telecom.extend(software)
telecom.insert(4,"VSNL")
telecom.append("verizon")
telecom.remove("airtel")
telecom.pop(0)
print(telecom)