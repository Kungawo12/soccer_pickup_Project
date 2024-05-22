from pickup_project.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def get_all_users(cls):
        query= "SELECT * FROM users"
        results = connectToMySQL('pickup_project').query_db(query)
        users = []
        
        for user in results:
            users.append(cls(user))
            
        return users

    @classmethod
    def insert(cls,data):
        query = """INSERT INTO users(first_name,last_name,email,password)
            VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL('pickup_project').query_db(query,data)
    
    @classmethod
    def get_one_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('pickup_project').query_db(query,data)
        return cls(result[0])