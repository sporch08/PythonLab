from datetime import datetime
from operator import attrgetter
import urllib.request as req
import json
import csv
import mypackage

DEFAULT_ROW_COUNT = 1000
DICTIONARY_KEY_FIELDS = "fields"
DICTIONARY_KEY_RECORDS = "records"
DICTIONARY_KEY_TOTAL_RECORDS = "total"
HTTP_RETURN_OK = 200
HTTP_CONTENT_TYPE_JSON = "application/json"
OUTPUT_FILE_NAME = "open_data_aqi_result.csv"

"""
This is the sample code for getting the open data from API calls.
In this code, I will try to use Python to get particulate matter data from the Environmental Protection Administration of Taiwan.
"""


class MyCustomException(Exception):
    def __init__(self, code, message):
        self.code = code
        super().__init__(message)


def get_opendata(api_key, row_count):
    try:
        formatted_url = f"https://data.epa.gov.tw/api/v2/aqx_p_142?format=json&limit={row_count}&api_key={api_key}&filters=itemengname,EQ,PM2.5"
        start_time = datetime.now()
        print(
            f"    {start_time}: Start to request open data, URL is:'{formatted_url}'.")
        with req.urlopen(formatted_url) as res:
            # check the HTTP response status code
            if res.status != HTTP_RETURN_OK:
                raise Exception(
                    f"HTTP return error! response status={res.status}")

            # determine the format of result is JSON or not
            res_content_type = res.headers.get('Content-Type')
            if res_content_type != HTTP_CONTENT_TYPE_JSON:
                error_code = 500
                error_message = f"The API call doesn't return JSON format data. {res.read().decode('utf-8')}"
                raise MyCustomException(error_code, error_message)

            return_data = json.load(res)
        end_time = datetime.now()

        print(
            f"    {end_time}: Start to request open data...Done! {row_count:,} of {int(return_data[DICTIONARY_KEY_TOTAL_RECORDS]):,} records returned. ({(end_time-start_time).total_seconds()} elapsed.)")

        # for debug purpose
        # print(f"\t Here is the meta data:")
        # print(f"\t {'id':15}\t|{'type':5}\t|{'info':20}", sep="")
        # print("\t ============================================================")
        # for row in return_data[DICTIONARY_KEY_FIELDS]:
        #     print(
        #         f"\t {row['id']:15}\t|{row['type']:5}\t|{row['info']['label']}", sep="")
        # print("\t ============================================================")

        num = 1
        processed_list = []
        header = ['rownum', 'sitename', 'itemname', 'itemengname',
                  'itemunit', 'monitordate', 'concentration']
        for row in return_data[DICTIONARY_KEY_RECORDS]:
            sub_dict = {}
            sub_dict["rownum"] = num
            sub_dict["sitename"] = row["sitename"]
            sub_dict["itemname"] = row["itemname"]
            sub_dict["itemengname"] = row["itemengname"]
            sub_dict["itemunit"] = row["itemunit"]
            sub_dict["monitordate"] = row["monitordate"]
            # proceed data pre-processing/data cleaning, specify negative value if concentration is 'x'.
            sub_dict["concentration"] = "-1" if row["concentration"] == "x" else row["concentration"]

            processed_list.append(sub_dict)
            num += 1

        do_sort_list(processed_list)
        # for debug purpose
        # for row in processed_list:
        #     print(f"\t ***{row['rownum']:4d}, {row['monitordate']}, {row['sitename']}, {row['itemname']}, {row['itemengname']}, {row['itemunit']}, {row['concentration']}")

        do_write_result(processed_list, header)

    except Exception as e:
        # raise in here represents throw exception to outer function handle.
        raise


def do_sort_list(processed_list):
    print(
        f"    {datetime.now()}: Start to sort the result by date accending then by concentration descending...")
    try:
        # sort the data of the list by one or more keys.
        # return sorted(processed_list, key=lambda x: (x['monitordate'], x['concentration']), reverse=True)
        processed_list.sort(key=lambda x: (x['concentration']), reverse=True)
        processed_list.sort(key=lambda x: (x['monitordate']))
        # processed_list.sort(key=attrgetter('monitordate', 'concentration'))

        # for debug purpose
        # for row in processed_list:
        #     print(f"\t {row['rownum']:4d}, {row['monitordate']}, {row['sitename']}, {row['itemname']}, {row['itemengname']}, {row['itemunit']}, {row['concentration']}")
        # processed_list = sorted_list
    except Exception as e:
        # raise in here represents throw exception to outer function handle.
        raise
    print(
        f"    {datetime.now()}: Start to sort the result by date accending then by concentration descending...Done!")


def do_write_result(processed_list, header):
    print(
        f"    {datetime.now()}: Start to save the result into {OUTPUT_FILE_NAME}...")
    try:
        with open(OUTPUT_FILE_NAME, mode="w", newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=header)
            writer.writeheader()
            # you can export a list which contains multiple rows to csv writer directly.
            # writer.writerows(processed_list)

            # since we would like to reorder the result, so we use loop to export records one by one.
            num = 1
            for row in processed_list:
                row["rownum"] = num
                writer.writerow(row)
                num += 1

    except Exception as e:
        print(f"\tOops! We got errors! {{error message: {str(e)}}}")
    print(
        f"    {datetime.now()}: Start to save the result into {OUTPUT_FILE_NAME}...Done!")


# Main Function
if __name__ == "__main__":
    var_api_key = ""
    try:
        while True:
            mypackage.common.clean_screen()
            print(
                f"In this demonstration, the program will get AQI information on Taichung through API requests.")
            # ask user input from keyboard.
            var_api_key = input(
                "  First, please input the API key which is mandatory: ")
            var_row_count = int(input(
                "  Then give a number to tell API how many records you want get? [optional, max/default=1000]: ") or DEFAULT_ROW_COUNT)

            if len(var_api_key) > 0:
                break
            else:
                input(
                    "\n Error! The API key is mandatory information but you didn't give, try again.")

        if var_row_count > DEFAULT_ROW_COUNT:
            var_row_count = DEFAULT_ROW_COUNT
        elif var_row_count == 0:
            var_row_count == 0

        get_opendata(var_api_key, var_row_count)
        print(f"Program end gracefully.\n\n")
    except Exception as e:
        print(f"\tOops! We got errors! {{error message: {str(e)}}}")
