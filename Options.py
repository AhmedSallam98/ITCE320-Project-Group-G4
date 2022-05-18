import json


# noinspection PyMethodMayBeStatic
class options:
    """Class options
    The Class consist of 4 functions each function is performs a single option
     1- The function opens the .json files that saved previously through API function in the Server script
     2- Temp variable open the .json file as a string, Data variable deserialize it to python object to perform search and extraction process.
     3- The function return the requested information in a .json string to eases the transferring and printing process """

    def option1(self):

        with open("group_ID.json", "r") as Data:
            Temp = json.load(Data)
            data = json.loads(Temp)
            requested_Data = []
            for flight in data['data']:
                if flight['flight_status'] == "landed":
                    requested_Data += ['Flight code:', flight['flight']['iata']], \
                                      ["Departure Airport: ", flight['departure']['airport']], \
                                      ["Flight Number:", flight['flight']['number']], \
                                      ["Estimated time of arrival:", flight['arrival']['estimated']], \
                                      ['Arrival Terminal Number:', flight['arrival']['terminal']], \
                                      ['Arrival Gate Number:', flight['departure']['gate']]
            return json.dumps(requested_Data, indent=2)

    def option2(self):
        with open("group_ID.json", "r") as Data:
            Temp = json.load(Data)
            data = json.loads(Temp)
            requested_Data = []
            for flight in data['data']:
                if flight['flight_status'] == "scheduled":
                    requested_Data += ["Flight Number:", flight['flight']['number']], \
                                      ['Flight code:', flight['flight']['iata']], \
                                      ["Departure Airport: ", flight['departure']['airport']], \
                                      ["Departure time:", flight['departure']['scheduled']], \
                                      ['Estimated time of arrival: ', flight['arrival']['estimated']], \
                                      ['Arrival Terminal Number:', flight['arrival']['terminal']], \
                                      ['Arrival Gate Number:', flight['departure']['gate']]
            return json.dumps(requested_Data, indent=2)

    def option3(self, city):
        with open("group_ID.json", "r") as Data:
            Temp = json.load(Data)
            data = json.loads(Temp)
            error_Message = 'Error 404, No flights founded for {} '.format(city)
            requested_Data = []
            for flight in data['data']:
                if flight['departure']['timezone'] == city:
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
