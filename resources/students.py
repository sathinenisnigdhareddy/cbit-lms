from flask_restful import Resource,reqparse
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token,jwt_required
from db import query

class students(Resource):
   
    def get(self):
        parser=reqparse.RequestParser()
        parser.add_argument('semister',type=str,required=True,help="semister cannot be left blank!")
        parser.add_argument('branch',type=str,required=True,help="branch cannot be left blank!")
        data=parser.parse_args()
      
        try:
           
  
            x= query(f"""SELECT * FROM cbit.lms_stud_details where semister='{data['semister']}' and branch='{data['branch']}' """,return_json=False)
          
          
            if(len(x)>0):
                return query(f"""SELECT * FROM cbit.lms_stud_details where  semister='{data['semister']}' and branch='{data['branch']}' """)
            else:
                return {"message":"details not found"},400
        except:
            return {"message":"There was an error connecting to  database."},500

class course_details(Resource):
   
    def post(self):
        parser=reqparse.RequestParser()
        parser.add_argument('semister',type=str,required=True,help="semister cannot be left blank!")
        parser.add_argument('branch',type=str,required=True,help="branch cannot be left blank!")
        parser.add_argument('sub1',type=str,required=True,help="branch cannot be left blank!")
        parser.add_argument('sub2',type=str,required=True,help="branch cannot be left blank!")
        parser.add_argument('sub3',type=str,required=True,help="branch cannot be left blank!")
        parser.add_argument('sub4',type=str,required=True,help="branch cannot be left blank!")
        data=parser.parse_args()
      
      
           

        x= query(f"""SELECT * FROM cbit.lms_courses where semister='{data['semister']}' and branch='{data['branch']}' """,return_json=False)
        
        y=query("select * from cbit.lms_courses",return_json=False)
        a=len(y)
        a+=1
        if(len(x)>0):
            print('hello')
            return {"message":"semister and branch already exists"},400
        else:
            print('semister=',data['semister'],'branch=',data['branch'],'sub1=',data['sub1'],'sub2=',data['sub2'],'sub3=',data['sub3'],'sub4=',data['sub4'])
            
          
            query(f"""INSERT INTO cbit.lms_courses VALUES({a},
                                                   '{data['semister']}',
                                                    '{data['branch']}',
                                                    '{data['sub1']}',
                                                    '{data['sub2']}',
                                                    '{data['sub3']}',
                                                    '{data['sub4']}' )""")
           
  
      