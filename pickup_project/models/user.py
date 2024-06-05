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
        results = connectToMySQL('soccer_pickup_db').query_db(query)
        users = []
        
        for user in results:
            users.append(cls(user))
            
        return users

    @classmethod
    def insert(cls,data):
        query = """INSERT INTO users(first_name,last_name,email,password)
            VALUES(%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL('soccer_pickup_db').query_db(query,data)
    
    @classmethod
    def get_one_user(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('soccer_pickup_db').query_db(query,data)
        return cls(result[0])
    
    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM user WHERE email = %(email)s;"
        results= connectToMySQL('soccer_pickup_db').query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL('soccer_pickup_db').query_db(query,data)