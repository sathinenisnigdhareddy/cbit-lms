from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from db import query

class students(Resource):
   
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('semister',type=str,required=True,help="empno cannot be left blank!")
        parser.add_argument('branch',type=str,required=True,help="empno cannot be left blank!")
        data=parser.parse_args()
      
        try:
           
  
            x= query(f"""SELECT * FROM cbit.lms_stud_details where semister='{data['semister']}' and branch='{data['branch']}' """,return_json=False)
          
          
            if(len(x)>0):
                return query(f"""SELECT * FROM cbit.lms_stud_details where  semister='{data['semister']}' and branch='{data['branch']}' """)
            else:
                return {"message":"details not found"},400
        except:
            return {"message":"There was an error connecting to  database."},500