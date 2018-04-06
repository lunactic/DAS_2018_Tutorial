import requests
import json
import time
import sys
import os
import base64
from urllib.parse import urlparse


class ExecuteOnDivaServices:

    def main(self):
        url = sys.argv[1]
        input_image = sys.argv[2]
        output_folder = sys.argv[3]

        image_identifier = self.uploadImage(input_image)

        resultLink = self.runBinarization(url, image_identifier)
        result = self.pollResult(resultLink)
        self.saveFile(result['output'][0]['file']['url'],output_folder)
        sys.stdout.write("end")

    def uploadImage(self, input_image):
        url = "http://divaservices.unifr.ch/api/v2/collections"
        with open(input_image, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('ascii')
            file_name = os.path.basename(input_image)
            payload = "{\"files\":[{\"type\":\"image\",\"value\":\"" + encoded_string +  "\",\"name\":\"" + file_name.split('.')[0] + "\"}]}"
            headers = {
                'content-type': "application/json"
            }
            response = json.loads(requests.request("POST", url, data=payload, headers=headers).text)
            return response['collection'] + "/" + file_name

    def runBinarization(self, url, input_image):
        payload = "{\"parameters\":{},\"data\":[{\"inputImage\": \"" + input_image + "\"}]}"
        headers = {
            'content-type': "application/json"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        json_data = json.loads(response.text)
        return json_data['results'][0]['resultLink']

    def pollResult(self, resultLink):
        response = json.loads(requests.request("GET", resultLink).text)
        while(response['status'] != 'done'):
            if(response['status'] == 'error'):
                sys.stderr.write(
                    'Error in executing the request. See the log file at: ' + response['output'][0]['file']['url'])
            time.sleep(1)
            response = json.loads(requests.request("GET", resultLink).text)

        return response

    def saveFile(self, url, output_folder):
        # open in binary mode
        filename = os.path.basename(urlparse(url).path)
        with open(output_folder + filename, "wb") as file:
            # get request
            response = requests.get(url)
            # write to file
            file.write(response.content)


if __name__ == "__main__":
    ExecuteOnDivaServices().main()
