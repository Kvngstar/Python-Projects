from urllib import request

input_url = input("Input Url: ")

def main(url):
    print("Checking Connectivity ...")
    response = request.urlopen(url)
    print("connected to "+ url)
    print("connectivity: "+ str(response.getcode()))
    
main(input_url)