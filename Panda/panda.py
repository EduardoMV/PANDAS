import pandas
import pyautogui
import time
import pyperclip
import keyboard

def getSKU(x):
    dataProducts = pandas.read_csv( "productsData.csv" )
    sku = dataProducts["sku"][x]
    return sku

def openFireFox():
    pyautogui.hotkey("win")
    time.sleep(1)
    pyautogui.typewrite("Chrome")
    time.sleep(1)
    pyautogui.hotkey("enter")
    time.sleep(1)
    pyautogui.click(285, 135)
    time.sleep(1)

def goToAmazon(sku):
    pyautogui.hotkey("f6")
    url = "https://www.amazon.com.mx/Master-hack/dp/"
    pyautogui.typewrite(url + sku + "\n")
    time.sleep(2)

def getProductName():
    pyautogui.click(1026, 389)
    time.sleep(0.20)
    pyautogui.click(1026, 389)
    time.sleep(0.20)
    pyautogui.click(1026, 389)
    time.sleep(0.20)
    
    pyautogui.hotkey("ctrl", "c", interval = 0.50)
    productName = pyperclip.paste()
    return productName

def getProductPrice():
    pyautogui.click(1607, 394)
    time.sleep(0.20)
    pyautogui.click(1607, 394)
    time.sleep(0.20)
    
    pyautogui.hotkey("ctrl", "c", interval = 0.50)
    productPrice = pyperclip.paste()
    return productPrice

def modifyCSV(productName, productPrice, x):
        dataProducts = pandas.read_csv("productsData.csv")
        print(dataProducts)
        dataProducts = dataProducts.loc[:, ~dataProducts.columns.str.contains('^Unnamed')]
        dataProducts.loc[x, "name"] = productName
        dataProducts.loc[x, "price"] = productPrice
        print(dataProducts)
        dataProducts.to_csv("productsData.csv")
        
def excel():
    pyautogui.hotkey("win")
    time.sleep(1)
    pyautogui.typewrite("Excel")
    time.sleep(1)
    pyautogui.hotkey("enter")
    time.sleep(4)
    pyautogui.click(748, 620)
    time.sleep(1)
        
def main():
    x=0
    openFireFox()
    while x<7:
        sku = getSKU(x)
        goToAmazon(sku)
        productName = getProductName()
        productPrice = getProductPrice()
        modifyCSV(productName, productPrice, x)
        
        x=x+1
    
main()

excel()