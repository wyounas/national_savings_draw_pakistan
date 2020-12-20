"""
Search your prize-bonds in draws at National Savings (http://savings.gov.pk/draw-search/).

Store all your prize bond numbers in the NUMBERS list below. And then run the script from command line (assuming
you've Python 3 and virtual environment enabled.):

> python prize_bonds.py
"""

import time
import requests

# Add all your prize-bond numbers in the following `NUMBERS` list
NUMBERS = [
    12345, 67890
]


def get_results():
    url = "http://savings.gov.pk/latest/results.php"
    failure_msg = 'OOPS! Try again later draws'
    headers = {'user-age': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

    for number in NUMBERS:
        response = requests.post(url, data=dict(
            country=4, state='all', range_from='', range_to='', pb_number_list=number, btnsearch='Search'
        ), headers=headers)
        if failure_msg in response.text:
            print("No prize for the {number}".format(number=number))
        else:
            print("YES! Looks like a prize for {number}".format(number=number))
        time.sleep(1)


if __name__ == "__main__":
    get_results()
