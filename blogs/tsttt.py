import requests

url = "https://tech-info.p.rapidapi.com/news"

headers = {
	"X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
	"X-RapidAPI-Host": "tech-info.p.rapidapi.com"
}

response = requests.request.t("GET", url, headers=headers)

print(response.text)