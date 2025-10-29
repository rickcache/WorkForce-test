import json

class DataLoad:

    def json_load_admin_login(self, file_name):
        with open(file_name) as f:
            data = json.load(f)
            return [
                (
                    item["username"],
                    item["email"],
                    item["password"]
                )
                for item in data["users"]
            ]
            
            
    def json_load_register(self, file_name):
        with open(file_name) as f:
            data = json.load(f)
            return [
                (
                    item["fullname"],
                    item["regi_email"],
                    item["regi_password"],
                    item["regi_address"],
                    item["regi_phone"]
                )
                for item in data["users"]
            ]
            
    def json_load_edit_employee(self, file_name):
        with open(file_name) as f:
            data = json.load(f)
            return [
                (
                    item["edit_name"],
                    item["edit_email"],
                    item["edit_phone"],
                    item["edit_address"]
                )
                for item in data["users"]
            ]        
            
    def json_load_employee_login(self, file_name):
        with open(file_name) as f:
            data = json.load(f)
            return [
                (
                    item["e_email"],
                    item["e_password"]
                )
                for item in data["users"]
            ]           
            
    def json_load_leave_request(self, file_name):
        with open(file_name) as f:
            data = json.load(f)
            return [
                (
                    item["from_date"],
                    item["to_date"],
                    item["reason"]
                )
                for item in data["users"]
            ]                   