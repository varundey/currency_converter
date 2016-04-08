import requests
from bs4 import BeautifulSoup as bs

def inputs():
	c_from = raw_input("Enter the currency to convert from: ").upper()
	c_to = raw_input("Enter the currency to convert to: ").upper()
	c_amount = raw_input("Enter the amount to convert: ")
	b(c_amount, c_from, c_to)

def b(c_amount, c_from, c_to):
	c_url = (url +"="+ c_amount +"&from="+ c_from +"&to="+ c_to)
	soup = bs(requests.get(c_url).content, "lxml")
	find_currency(soup,c_amount,c_from,c_to)

def find_currency(soup,c_amount,c_from, c_to):
	print c_amount +" "+ c_from +" = "+ soup.find("span",{"class":"bld"}).text

if __name__ == "__main__":
	url = "https://www.google.com/finance/converter?a"
	inputs()