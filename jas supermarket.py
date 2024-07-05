print("welcome to a supermarket")
def dress_section():
    floor=int(input("tell your floor number="))
    if(floor==1):
        print("welcome mam this is girl section:")
        size=int(input("tell your size mam="))
    if(size>=20):
        print("yes this size is  available mam")
        color=input("want you what color mam=")
    if(color=="pink"):
        print("this color is available")
    how_many_dress=int(input("how many you selection mam:"))
    if(how_many_dress<100):
        print("this dress's is okey")   
    rate=int(input("your dress rate is="))  
    if(rate>=1000):
        offer_rate=200
        print(" your dress rate is above thousand and 1 thousand offers is available 20% amount less in your bill mam")
        print("offer_rate:",offer_rate)
        total_rate=offer_rate-(rate*how_many_dress)
        gst=20
        cgst=total_rate*gst/2/100
        sgst=cgst
        total_rate=offer_rate-(rate*how_many_dress+sgst)
        print("gst amount:",gst)
        print("cgst amount:",cgst)
        print("sgst amount:",sgst)
        print("total_rate:",total_rate)
        print(f"finally this is your bill{total_rate}mam")
        print("*thank you mam again come in my shop mam")
        function()
    else:
        print("this not dress section:")
def shoe_section():
     floor=int(input("tell your floor number="))
     if(floor==2):
        print("welcome mam this is shoe section:")
     size=int(input("tell your size mam="))
     if(size>5):
        print("yes this size is available mam")
     color=input("what you want color mam=")
     if(color=="white"):
        print("this color is available")
     how_many_shoe=int(input("how many you selection mam:"))
     if(how_many_shoe>1):
        print("this shoe is okey")
     rate=int(input("your shoe rate is="))    
     if(rate>=300):
        offer_rate=200
        print("your total bill is above 1000 offer is grand")
        print("offer_rate:",offer_rate)
        total_rate=offer_rate-(rate*how_many_shoe)
        gst=20
        cgst=total_rate*gst/2/100
        sgst=cgst
        total_rate=offer_rate-(rate*how_many_shoe+sgst)
        print("gst amount:",gst)
        print("cgst amount:",cgst)
        print("sgst amount:",sgst)
        print("total_rate:",total_rate)
        print(f"finally this is your bill{total_rate}mam")
        print("*thank you mam again come in my shop mam")
        function()
     else:        
        print("this not shoe section:")
def snakes_section():
     floor=int(input("tell your floor number="))
     if(floor==3):
          print("welcome mam this is snakes section:")
          packet=int(input("tell your lazy packet number mam="))
     if(packet>=45):
         print("yes this number of lazy  packet is  available mam")
     color=input("want you what color mam=")
     if(color=="blue"):
          print("this color is available")
     how_many_snakes=int(input("how many you selection mam:"))
     if(how_many_snakes<100):
        print("this snakes is okey")     
     rate=int(input("your snakes rate is="))  
     if(rate==100):
        offer_rate=200
        print("your total bill amount is above 500 offer is granded:")
        print("offer_rate:",offer_rate)
        total_rate=offer_rate-(rate*how_many_snakes)
        gst=20
        cgst=total_rate*gst/2/100
        sgst=cgst
        total_rate=offer_rate-(rate*how_many_snakes+sgst)
        print("gst amount:",gst)
        print("cgst amount:",cgst)
        print("sgst amount:",sgst)
        print("total_rate:",total_rate)
        print(f"finally this is your bill{total_rate}mam")
        print("*thank you mam again come in my shop mam")
        function()
     else:
         print("this not dress shop:")
def function():
    print("welcome to a jas supermarket")
    print("floor_no_1=dress_section")
    print("floor_no_2=shoe_section")
    print("floor_no_3=snaks_section")
    floor_no=int(input("enter your floor number:"))
    if(floor_no==1):
        dress_section()
    elif(floor_no==2):
         shoe_section()
    elif(floor_no==3):
         snakes_section()
    else:
         print("this is  not supermarket:")
function()
