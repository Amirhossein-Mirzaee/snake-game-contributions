# commit_daily.py
import subprocess
from datetime import datetime, timedelta

def commit_and_push(message):
    subprocess.run(['git', 'add', 'snake_game.py'])
    subprocess.run(['git', 'commit', '-m', message])
    subprocess.run(['git', 'push'])

def generate_snake_movement(day):
    return f'# Day {day}: Snake moves\n'

# Set the start date and the number of days to commit
start_date = datetime(2022, 1, 1)
num_days = 365

for day in range(1, num_days + 1):
    current_date = start_date + timedelta(days=day - 1)
    commit_message = f"Day {day}: Snake Game Update - {current_date.strftime('%Y-%m-%d')}"
    snake_movement = generate_snake_movement(day)

    with open('snake_game.py', 'a') as file:
        file.write(snake_movement)

    commit_and_push(commit_message)
