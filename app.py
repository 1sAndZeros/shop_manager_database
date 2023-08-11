from lib.database_connection import DatabaseConnection

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/shop.sql")

    def run(self):
    # "Runs" the terminal application.

    #   * Ask the user to enter some input
    #   * Make some decisions based on that input
        choice = 0
        while not choice in ['1', '2']:
            choice = input('''
            Welcome to the shop management program!

                What do you want to do?
                1 = list all shop items
                2 = create a new item
                3 = list all orders
                4 = create a new order
                
            Enter your choice: 
            ''')
            if choice == '1':
                # artist_repository = ArtistRepository(self._connection)
                # artists = artist_repository.all()

                # for artist in artists:
                #     print(f"{artist.id} - {artist.name} - {artist.genre}")
                pass

            elif choice == '2':
                # album_repository = AlbumRepository(self._connection)
                # albums = album_repository.all()

                # for album in albums:
                #     print(f"{album.id} - {album.title} - {album.release_year}")
                pass
            
            else:
                print('Choice is incorrect. Please choose 1 or 2!')

if __name__ == '__main__':
    app = Application()
    app.run()