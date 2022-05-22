import json
import requests

class Reader:
    """
                    -----Class Reader-----
     *The Class consist of 5 functions each function is performs a single process
     1- The function opens the .json files that saved previously through API function
     2- Temp variable open the .json file as a string, Data variable deserialize it to python object to perform search and extraction process.
     3- The function return the requested information in a .json string to perform the transferring and printing process """

    def API(self,icao):
        """
             ---- API Function ----

          *Function has one parameter 'icao'
          1-arr_icao is received from the client
          2-Assigning the iao into the request parameters
          3-Retrieves 100 records of a certain Airport
          4-Saves the retrieved information in .json file for testing and evaluation
           *Note: You can obtain a free API-key from  aviationstack.com

        """
        params = {
            'access_key': 'Enter API-Key here ',
            'limit': 100,
            'arr_icao': icao

        }
        api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
        results = json.dumps(api_result.json(), indent=2)
        with open("group_4.json", "w") as storedData:
            json.dump(results, storedData, indent=2, sort_keys=True)


    def option1(self):

        with open("group_ID.json", "r") as Data:
            Temp = json.load(Data)
            data = json.loads(Temp)
            requested_Data = []
            error_Message = 'Error 404, No flights founded '
            for flight in data['data']:
                if flight['flight_status'] == "landed":
                    requested_Data += ['Flight code:', flight['flight']['iata']], \
                                      ["Departure Airport: ", flight['departure']['airport']], \
                                      ["Flight Number:", flight['flight']['number']], \
                                      ["Time of arrival:", flight['arrival']['scheduled']], \
                                      ['Arrival Terminal Number:', flight['arrival']['terminal']], \
                                      ['Arrival Gate Number:', flight['departure']['gate']]
            return error_Message if len(requested_Data) == 0 else json.dumps(requested_Data, indent=2)

    def option2(self):
        with open("group_ID.json", "r") as Data:
            Temp = json.load(Data)
            data = json.loads(Temp)
            requested_Data = []
            error_Message = 'Error 404, No flights founded '
            for flight in data['data']:
                if flight['flight_status'] == "scheduled":
                    requested_Data += ["Flight Number:", flight['flight']['number']], \
                                      ['Flight code:', flight['flight']['iata']], \
                                      ["Departure Airport: ", flight['departure']['airport']], \
                                      ["Departure time:", flight['departure']['scheduled']], \
                                      ['Estimated time of arrival: ', flight['arrival']['estimated']], \
                                      ['Arrival Terminal Number:', flight['arrival']['terminal']], \
                                      ['Arrival Gate Number:', flight['departure']['gate']]
            return error_Message if len(requested_Data) == 0 else json.dumps(requested_Data, indent=2)

    def option3(self, city):
        with open("group_ID.json", "r") as Data:
            Temp = json.load(Data)
            data = json.loads(Temp)
            error_Message = 'Error 404, No flights founded for {} '.format(city)
            requested_Data = []
            for flight in data['data']:
                if flight['departure']['iata'] == city:
                    requested_Data += ["Flight Number:", flight['flight']['number']], \
                                      ['Flight code:', flight['flight']['iata']], \
                                      ["Departure Airport: ", flight['departure']['airport']], \
                                      ["Departure time:", flight['departure']['scheduled']], \
                                      ['Estimated time of arrival: ', flight['arrival']['estimated']], \
                                      ['Flight status is: ', flight['flight_status']], \
                                      ['Arrival Terminal Number:', flight['arrival']['terminal']], \
                                      ['Arrival Gate Number:', flight['departure']['gate']]
            return error_Message if len(requested_Data) == 0 else json.dumps(requested_Data, indent=2)

    def option4(self, flight_Code):
        with open("group_ID.json", "r") as Data:
            Temp = json.load(Data)
            data = json.loads(Temp)
            requested_Data = []
            error_Message = 'Error 404, Flight not found'
            for flight in data['data']:
                if flight['flight']['iata'] == flight_Code:
                    requested_Data += ["Flight Number:", flight['flight']['number']], \
                                      ['Flight code:', flight['flight']['iata']], \
                                      ["Flight Date:", flight['flight_date']], \
                                      ["Departure Airport:", flight['departure']['airport']], \
                                      ["Departure Gate:", flight['departure']['gate']], \
                                      ["Departure Terminal:", flight['departure']['terminal']], \
                                      ["Arrival Airport:", flight['arrival']['airport']], \
                                      ["Arrival Gate:", flight['arrival']['gate']], \
                                      ["Arrival Terminal:", flight['arrival']['terminal']], \
                                      ["Scheduled Departure time:", flight['departure']['scheduled']], \
                                      ["Scheduled arrival time:", flight['arrival']['scheduled']], \
                                      ["Estimated arrival time:", flight['arrival']['estimated']], \
                                      ["Delay:", flight['arrival']['delay']]
            return error_Message if len(requested_Data) == 0 else json.dumps(requested_Data, indent=2)
