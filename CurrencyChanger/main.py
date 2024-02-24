from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options

'''
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)
driver.get("https://canlidoviz.com/doviz-kurlari")

table  = driver.find_element(By.TAG_NAME , 'tbody')
row = table.find_elements(By.TAG_NAME , 'tr')
for i in row:
    print(rf"Satıs {i.find_elements(By.TAG_NAME , 'td')[0].find_element(By.TAG_NAME , 'div').find_element(By.CLASS_NAME , 'highlight').text}")
    print(rf"Satıs {i.find_elements(By.TAG_NAME , 'td')[2].find_element(By.TAG_NAME , 'div').text}")
    print("-----")'''
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(options=options)
driver.get("https://canlidoviz.com/")
WebDriverWait(driver,3).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/header/section[2]/div/nav/ul/li[1]/a")))
exchange_button = driver.find_element(By.XPATH,"/html/body/header/section[2]/div/nav/ul/li[1]/a")
exchange_button.click()

WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/main/div/div[3]/section[1]/div/div[1]/div/div[2]/table/tbody")))
exchange_list=driver.find_element(By.XPATH,"/html/body/main/div/div[3]/section[1]/div/div[1]/div/div[2]/table/tbody")
#CURRENCY NAMES İS LİSTED
currency_name=[]
a=len(exchange_list.text.splitlines())
for i in range(1,a,7):
    currency_name.append(exchange_list.text.splitlines()[i])
#print(currency_name)

#CURRENCY PRİCES İS LİSTED
currency_price=[]
for i in range(4,a,7):
    currency_price.append(exchange_list.text.splitlines()[i])
#print(currency_price)

currency={}
# b=len(exchange_list.text.splitlines())/7
# b=int(b)
for y in range(0,len(currency_price)):
    currency[currency_name[y]] = currency_price[y]

#GUI
window = Tk()
window.title("EXCHANGE")
window.config(bg='black')
window.minsize(350,500)

photo=PhotoImage(file="4.png")
border_color=Frame(window,background='black')
photo_label =Label(border_color,image=photo,bd=0)
photo_label.pack()
border_color.pack(padx=1,pady=1)

first_currency_title=Label(text="Choose a currency and how much")
first_currency_title.config(bg='black',fg='white')
first_currency_title.pack()

first_price_entry=Entry(width=10)
first_price_entry.place(x=100,y=340)

#first_currency_entry=Entry(width=20)
#first_currency_entry.place(x=166,y=340)

second_price_entry=Entry(width=10)
second_price_entry.place(x=100,y=380)

#second_currency_entry=Entry(width=17)
#second_currency_entry.place(x=166,y=380)


currency_list=currency_name
currency1=StringVar()
currency1.set("Select any currency")

currency_list2=currency_name
currency2=StringVar()
currency2.set("Select any currency")

drop=OptionMenu(window,currency1,*currency_list)
drop.place(x=166,y=340)

drop2=OptionMenu(window,currency2,*currency_list2)
drop2.place(x=166,y=380)

def exchange_calculate():
    result=0
    if(first_price_entry.get()==0 and second_price_entry.get()==0):
        messagebox.showinfo(title="ERROR",message="Please enter all data")
    elif(first_price_entry.get()==0 and second_price_entry.get()!=0):
        if(second_price_entry.get().isdigit()):
            result = int(second_price_entry.get()*int(currency[currency2.get()]))/int(currency[currency1.get()])
            a=str(result)
            first_price_entry.insert(0,a)

    elif(first_price_entry.get()!=0 and second_price_entry.get()==0):
        if(first_price_entry.get().isdigit()):
            result = first_price_entry.get()*int(currency[currency1.get()])



window.mainloop()