from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        client = MongoClient('mongodb://localhost:27017/')
        db = client['octofit_db']

        # Test data for users
        users = [
            {"email": "user1@example.com", "name": "User One", "age": 25},
            {"email": "user2@example.com", "name": "User Two", "age": 30},
        ]
        db.users.insert_many(users)

        # Test data for teams
        teams = [
            {"name": "Team Alpha", "members": ["user1@example.com", "user2@example.com"]},
        ]
        db.teams.insert_many(teams)

        # Test data for activities
        activities = [
            {"user": "user1@example.com", "activity": "Running", "duration": 30},
        ]
        db.activity.insert_many(activities)

        # Test data for leaderboard
        leaderboard = [
            {"team": "Team Alpha", "points": 100},
        ]
        db.leaderboard.insert_many(leaderboard)

        # Test data for workouts
        workouts = [
            {"name": "Morning Run", "description": "A quick 5km run to start the day."},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
