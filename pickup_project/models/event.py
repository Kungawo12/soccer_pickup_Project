from pickup_project.config.mysqlconnection import connectToMySQL
from pickup_project.models.user import User
from flask import flash

class Event:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location_name = data['location_name']
        self.date= None
        data['user'] = data['user']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def insert_new(cls,data):
        query = """INSERT INTO events(name,location_name,date)
            VALUES(%(name)s, %(location_name)s, %(date)s);
        """
        return connectToMySQL('soccer_pickup_db').query_db(query,data)

    @classmethod
    def get_all_events(cls):
        query =  """SELECT * FROM events
            LEFT JOIN users on events.user_id = users.id
        """
        
        results = connectToMySQL('soccer_pickup_db').query_db(query)
        
        users_events = []
        for row in results:
            events_data = Event(row)
            user_data = User({
                "id": row["user_id"],
                "first_name": row["first_name"],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                "created_at": row["created_at"],
                "updated_at": row['updated_at']
            })
            events_data.user = user_data
            
            users_events.append(events_data)
        return users_events