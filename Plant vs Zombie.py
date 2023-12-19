# coding: utf-8

# block 4 to 82 is on log_in_method chosen , user can signup , signin or log in as guest
import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the file path relative to the current script
file_path = os.path.join(current_dir, 'Data/user.txt')

print(file_path)


def sign_up(username, password):
    with open(file_path, mode='a') as f:
        f.write(f'{username}----{password}\n')


def check_username_taken(input_username):
    with open(file_path, mode='rt', encoding='utf-8') as f:
        for line in f:
            username, password = line.strip().split('----')
            if input_username == username:
                print('Username Taken, Please choose an another one')
                break
        else:
            return 'y'


def check_user_pass(input_username, input_password):
    with open(file_path, mode='rt', encoding='utf-8') as f:
        for line in f:
            username, password = line.strip().split('----')
            if input_username == username and input_password == password:
                return 'y'

        else:
            print('No account found. Check your username and password. You have to register an account to sign in')


log_in_method = input('Sign up an account enter "U" \n'
                      'Sign in an account enter "I"\n'
                      'Log in as guest enter "G"\n\n'
                      'Please enter your choice here :  ').strip().upper()

asking_log_in_method = True
log_in_as = ''

while asking_log_in_method:
    if log_in_method == 'G':  # log in as guest
        print('Logged in as guest')
        log_in_as = 'Guest'
        asking_log_in_method = False

    elif log_in_method == 'U':  # sign up an account
        while True:
            input_username = input('Enter your username: ').strip()
            res = check_username_taken(input_username)
            if res == 'y':
                input_password = input('Enter your password: ').strip()
                print('Successfully registered')
                break

        sign_up(input_username, input_password)


    elif log_in_method == 'I':
        while True:
            input_username = input('Enter your username: ').strip()
            input_password = input('Enter your password: ').strip()
            res = check_user_pass(input_username, input_password)
            if res == 'y':
                print('Logged in')
                break

        log_in_as = input_username
        asking_log_in_method = False

    else:
        print('Please key in the correct symbol')





import pygame
from sys import exit
import time

pygame.init()  # starting code

screen = pygame.display.set_mode((1000, 600))  # screen size
pygame.display.set_caption('Plant vs Zombie')  # title name
clock = pygame.time.Clock()
game_active = True

welcome_surface = pygame.image.load('Picture/welcome.webp').convert()
welcome_surface = pygame.transform.scale(welcome_surface, (1000, 600))

white_surface = pygame.image.load('Picture/white_screen.jpeg').convert()
white_surface = pygame.transform.scale(white_surface, (400, 100))
white_rectangle = white_surface.get_rect(topleft=(500, 90))

username_font = pygame.font.Font(None, 30)
username_surface = username_font.render(log_in_as, None, 'White')
username_rectangle = username_surface.get_rect(center=(210, 100))

# game_start_rectangle =

background_surface = pygame.image.load('Picture/background.webp').convert()
background_surface = pygame.transform.scale(background_surface, (1000, 600))

game_start = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and white_rectangle.collidepoint(event.pos):
            game_start =True



    if game_active:
        screen.blit(white_surface,white_rectangle)
        screen.blit(welcome_surface, (0, 0))
        screen.blit(username_surface, username_rectangle)
        if game_start :
            time.sleep(1)
            screen.blit(background_surface, (0, 0))

    pygame.display.update()
    clock.tick(60)
