import pandas
import pyautogui
import time
import pyperclip
import keyboard

def getSKU(x):
    dataProducts = pandas.read_csv("productsData.csv")
    sku= dataProducts["sku"][x]
    return(sku)
    
def openBrowser():
    pyautogui.hotkey('win')
    time.sleep(1)
    pyautogui.typewrite("google\n")
    time.sleep(2)
    pyautogui.hotkey('win','up')
    pyautogui.hotkey('\n')

def goToAmazon(sku):
    time.sleep(3)
    url = "https://amazon.com.mx/Advanced-Programming/dp/"
    finalUrl= url + sku + "\n"
    pyautogui.typewrite(finalUrl)
    time.sleep(2)

def getProductName():
    pyautogui.click(774, 307.2)
    time.sleep(.2)
    pyautogui.click(774, 307.2)
    time.sleep(.1)
    pyautogui.click(774, 307.2)
    
    pyautogui.hotkey("ctrl", "c", interval = 0.15)
    productName = pyperclip.paste()
    return productName

def getProductPrice():
    pyautogui.click(1133, 317)
    time.sleep(.2)
    pyautogui.click(1133, 317)
    time.sleep(.2)
    pyautogui.click(1133, 317)
    
    pyautogui.hotkey("ctrl", "c", interval = 0.15)
    productPrice = pyperclip.paste()
    return productPrice

def modifyCSV(productName, productPrice,x):
    dataProducts = pandas.read_csv("productsData.csv")
    #print(dataProducts)
    dataProducts.loc[x, "name"] = productName
    dataProducts.loc[x, "price"] = productPrice
    #print(dataProducts)
    dataProducts.to_csv("productsData.csv")
    
def main():
    x=0
    openBrowser()
    while x<7:
        sku= getSKU(x)
        #print(sku)
        pyautogui.click(157,53)
        goToAmazon(sku)
        productName = getProductName()
        productPrice = getProductPrice()
        modifyCSV(productName, productPrice, x)
        x=x+1

main()


