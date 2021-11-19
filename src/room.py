class Room:
    def __init__(self, name):
        self.name = name
        self.guest_list = []
        self.song_list = []
        self.room_space = 2


    def num_of_guests(self):
        return len(self.guest_list)

    def check_in_guest(self, guest):
        self.guest_list.append(guest)

    def check_out_guest(self, guest):
        self.guest_list.remove(guest)

    def add_song_to_room(self, song):
        self.song_list.append(song)
        return len(self.song_list)

    def check_room_space(self):
        if self.num_of_guests() < self.room_space:
            return True
        else:
            return False