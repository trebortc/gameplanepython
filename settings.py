class Settings():
    def __init__(self):
        #Initialize the game´s settings
        #Screen settings
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        #Ship
        self.ship_speed_factor = 1.5

        #Bullet
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 255, 60)
        self.bullets_allowed = 3

        #Alien
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represents right -1 represents left
        self.fleet_direction = 1
