import json
import os

class DataManager:
    def __init__(self):
        self.folder = "user_data"
        if not os.path.exists(self.folder):
            os.makedirs(self.folder)
        
        self.filepath = os.path.join(self.folder, "users.json")
        self.data = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filepath):
            return {} 
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except:
            return {}

    def save_data(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.data, f, indent=4)

    def get_user_list(self):
        return list(self.data.keys())

    def register_user(self, username):
        if username not in self.data:
            self.data[username] = {
                "EASY": {"best_score": 0, "history": []},
                "NORMAL": {"best_score": 0, "history": []},
                "HARD": {"best_score": 0, "history": []}
            }
            self.save_data()
            return True 
        return False 

    def add_score(self, username, score, difficulty_level):
        if username in self.data:
            if difficulty_level not in self.data[username]:
                self.data[username][difficulty_level] = {"best_score": 0, "history": []}
            
            user_diff = self.data[username][difficulty_level]
            user_diff["history"].append(score)
            if score > user_diff["best_score"]:
                user_diff["best_score"] = score
            self.save_data()

    def delete_user(self, username):
        if username in self.data:
            del self.data[username]
            self.save_data()