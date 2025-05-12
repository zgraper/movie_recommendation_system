# movies_data.py

movies = [
    {
        "title": "Inception",
        "genre": ["Sci-Fi", "Thriller"],
        "synopsis": "A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O., but his tragic past may doom the project and his team to disaster.",
        "director": "Christopher Nolan",
        "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt"],
        "year": 2010,
        "imdb_link": "https://www.imdb.com/title/tt1375666/"
    },
    {
        "title": "The Matrix",
        "genre": ["Sci-Fi", "Action"],
        "synopsis": "When a beautiful stranger leads computer hacker Neo to a forbidding underworld, he discovers the shocking truth--the life he knows is the elaborate deception of an evil cyber-intelligence.",
        "director": "Lana Wachowski, Lilly Wachowski",
        "cast": ["Keanu Reeves", "Laurence Fishburne"],
        "year": 1999,
        "imdb_link": "https://www.imdb.com/title/tt0133093/"
    },
    {
        "title": "Interstellar",
        "genre": ["Sci-Fi", "Drama"],
        "synopsis": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft, along with a team of researchers, to find a new planet for humans.",
        "director": "Christopher Nolan",
        "cast": ["Matthew McConaughey", "Anne Hathaway"],
        "year": 2014,
        "imdb_link": "https://www.imdb.com/title/tt0816692/"
    },
    {
        "title": "The Shawshank Redemption",
        "genre": ["Drama", "Crime"],
        "synopsis": "A banker convicted of uxoricide forms a friendship over a quarter century with a hardened convict, while maintaining his innocence and trying to remain hopeful through simple compassion.",
        "director": "Frank Darabont",
        "cast": ["Tim Robbins", "Morgan Freeman"],
        "year": 1994,
        "imdb_link": "https://www.imdb.com/title/tt0111161/"
    },
    {
        "title": "The Godfather",
        "genre": ["Crime", "Drama"],
        "synopsis": "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
        "director": "Francis Ford Coppola",
        "cast": ["Marlon Brando", "Al Pacino"],
        "year": 1972,
        "imdb_link": "https://www.imdb.com/title/tt0068646/"
    },
    {
        "title": "12 Angry Men",
        "genre": ["Psychological", "Drama"],
        "synopsis": "The jury in a New York City murder trial is frustrated by a single member whose skeptical caution forces them to more carefully consider the evidence before jumping to a hasty verdict.",
        "director": "Sidney Lumet",
        "cast": ["Henry Fonda", "Lee J. Cobb"],
        "year": 1957,
        "imdb_link": "https://www.imdb.com/title/tt0050083/"
    },
    {
        "title": "The Lord of the Rings: The Return of the King",
        "genre": ["Fantasy", "Drama"],
        "synopsis": "Gandalf and Aragorn lead the World of Men against Sauron's army to draw his gaze from Frodo and Sam as they approach Mount Doom with the One Ring.",
        "director": "Peter Jackson",
        "cast": ["Elijah Wood", "Viggo Mortensen"],
        "year": 2003,
        "imdb_link": "https://www.imdb.com/title/tt0167260/"
    },
    {
        "title": "Pulp Fiction",
        "genre": ["Crime", "Thriller"],
        "synopsis": "The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.",
        "director": "Quentin Tarantino",
        "cast": ["John Travolta", "Uma Thurman"],
        "year": 1994,
        "imdb_link": "https://www.imdb.com/title/tt0110912/"
    },
    {
        "title": "The Good, the Bad and the Ugly",
        "genre": ["Western", "Epic"],
        "synopsis": "A bounty-hunting scam joins two men in an uneasy alliance against a third in a race to find a fortune in gold buried in a remote cemetery.",
        "director": "Sergio Leone",
        "cast": ["Clint Eastwood", "Eli Wallach"],
        "year": 1966,
        "imdb_link": "https://www.imdb.com/title/tt0060196/"
    },
    {
        "title": "Forrest Gump",
        "genre": ["Romance", "Drama"],
        "synopsis": "The history of the United States from the 1950s to the '70s unfolds from the perspective of an Alabama man with an IQ of 75, who yearns to be reunited with his childhood sweetheart.",
        "director": "Robert Zemeckis",
        "cast": ["Tom Hanks", "Robin Wright"],
        "year": 1994,
        "imdb_link": "https://www.imdb.com/title/tt0816692/"
    },
    {
        "title": "Fight Club",
        "genre": ["Psychological", "Thriller"],
        "synopsis": "An insomniac office worker and a devil-may-care soap maker form an underground fight club that evolves into much more.",
        "director": "David Fincher",
        "cast": ["Brad Pitt", "Edward Norton"],
        "year": 1999,
        "imdb_link": "https://www.imdb.com/title/tt0137523/"
    },
    {
        "title": "One Flew Over the Cuckoo's Nest",
        "genre": ["Psychological", "Drama"],
        "synopsis": "In the Fall of 1963, a Korean War veteran and criminal pleads insanity and is admitted to a mental institution, where he rallies up the scared patients against the tyrannical nurse.",
        "director": "Milos Forman",
        "cast": ["Jack Nicholson", "Louise Fletcher"],
        "year": 1975,
        "imdb_link": "https://www.imdb.com/title/tt0073486/"
    },
    {
        "title": "Se7en",
        "genre": ["Crime", "Psychological"],
        "synopsis": "Two detectives, a rookie and a veteran, hunt a serial killer who uses the seven deadly sins as his motives.",
        "director": "David Fincher",
        "cast": ["Brad Pitt", "Morgan Freeman"],
        "year": 1995,
        "imdb_link": "https://www.imdb.com/title/tt0114369/"
    },
    {
        "title": "It's a Wonderful Life",
        "genre": ["Romance", "Drama"],
        "synopsis": "An angel is sent from Heaven to help a desperately frustrated businessman by showing him what life would have been like if he had never existed.",
        "director": "Frank Capra",
        "cast": ["James Stewart", "Donna Reed"],
        "year": 1946,
        "imdb_link": "https://www.imdb.com/title/tt0038650/"
    },
    {
        "title": "The Silence of the Lambs",
        "genre": ["Psychological", "Drama"],
        "synopsis": "A young F.B.I. cadet must receive the help of an incarcerated and manipulative cannibal killer to help catch another serial killer, a madman who skins his victims.",
        "director": "Jonathan Demme",
        "cast": ["Jodie Foster", "Anthony Hopkins"],
        "year": 1991,
        "imdb_link": "https://www.imdb.com/title/tt0102926/"
    },
    {
        "title": "Saving Private Ryan",
        "genre": ["War", "Drama"],
        "synopsis": "Following the Normandy Landings, a group of U.S. soldiers go behind enemy lines to retrieve a paratrooper whose brothers have been killed in action.",
        "director": "Steven Spielberg",
        "cast": ["Tom Hanks", "Matt Damon"],
        "year": 1998,
        "imdb_link": "https://www.imdb.com/title/tt0120815/"
    },
    {
        "title": "The Green Mile",
        "genre": ["Crime", "Drama"],
        "synopsis": "A death row guard learns that a gentle giant in his charge possesses a mysterious gift.",
        "director": "Frank Darabont",
        "cast": ["Tom Hanks", "Michael Clarke Duncan"],
        "year": 1999,
        "imdb_link": "https://www.imdb.com/title/tt0120689/"
    },
    {
        "title": "Terminator 2: Judgment Day",
        "genre": ["Action", "Thriller"],
        "synopsis": "A cyborg, identical to the one who failed to kill Sarah Connor, must now protect her ten year old son John from an even more advanced and powerful cyborg.",
        "director": "James Cameron",
        "cast": ["Arnold Schwarzenegger", "Linda Hamilton"],
        "year": 1991,
        "imdb_link": "https://www.imdb.com/title/tt0103064/"
    },
    {
        "title": "Star Wars: Episode IV - A New Hope",
        "genre": ["Sci-Fi", "Action"],
        "synopsis": "Luke Skywalker joins forces with a Jedi Knight, a cocky pilot, a Wookiee and two droids to save the galaxy from the Empire's world-destroying battle station, while also attempting to rescue Princess Leia from the mysterious Darth Vader.",
        "director": "George Lucas",
        "cast": ["Mark Hamill", "Harrison Ford"],
        "year": 1977,
        "imdb_link": "https://www.imdb.com/title/tt0076759/"
    },
    {
        "title": "Back to the Future",
        "genre": ["Adventure", "Sci-Fi"],
        "synopsis": "Marty McFly, a 17-year-old high school student, is accidentally sent 30 years into the past in a time-traveling DeLorean invented by his close friend, the maverick scientist Doc Brown.",
        "director": "Robert Zemeckis",
        "cast": ["Michael J. Fox", "Christopher Lloyd"],
        "year": 1985,
        "imdb_link": "https://www.imdb.com/title/tt0088763/"
    },
    {
        "title": "Gladiator",
        "genre": ["Action", "Epic"],
        "synopsis": "A former Roman General sets out to exact vengeance against the corrupt emperor who murdered his family and sent him into slavery.",
        "director": "Ridley Scott",
        "cast": ["Russell Crowe", "Joaquin Phoenix"],
        "year": 2000,
        "imdb_link": "https://www.imdb.com/title/tt0172495/"
    },
    {
        "title": "The Lion King",
        "genre": ["Animated", "Adventure"],
        "synopsis": "Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.",
        "director": "Roger Allers",
        "cast": ["Matthew Broderick", "Jeremy Irons"],
        "year": 1994,
        "imdb_link": "https://www.imdb.com/title/tt0110357/"
    },
    {
        "title": "Psycho",
        "genre": ["Psychological", "Horror"],
        "synopsis": "A secretary on the run for embezzlement takes refuge at a secluded California motel owned by a repressed man and his overbearing mother.",
        "director": "Alfred Hitchcock",
        "cast": ["Anthony Perkins", "Janet Leigh"],
        "year": 1960,
        "imdb_link": "https://www.imdb.com/title/tt0054215/"
    },
    {
        "title": "The Departed",
        "genre": ["Crime", "Drama"],
        "synopsis": "An undercover cop and a mole in the police attempt to identify each other while infiltrating an Irish gang in South Boston.",
        "director": "Martin Scorsese",
        "cast": ["Leonardo DiCaprio", "Matt Damon"],
        "year": 2006,
        "imdb_link": "https://www.imdb.com/title/tt0407887/"
    },
    {
        "title": "American History X",
        "genre": ["Crime", "Drama"],
        "synopsis": "Living a life marked by violence, neo-Nazi Derek finally goes to prison after killing two black youths. Upon his release, Derek vows to change; he hopes to prevent his brother, Danny, who idolizes Derek, from following in his footsteps.",
        "director": "Tony Kaye",
        "cast": ["Edward Norton", "Edward Furlong"],
        "year": 1998,
        "imdb_link": "https://www.imdb.com/title/tt0120586/"
    },
]
