from random import choice as pick

qs_sport = ['How many feet separate the stakes in a game of horseshoes?', 'Forty',
            'What is a golfer said to have if he is entitled to tee off first?', 'Honor',
            'In bowling, “beer frame” is best defined as?',
            'Frame after which the bowler has to buy beers for all others',
            'In what sport would you use a pen grip to hold your sandwich bat?', 'Table Tennis',
            'Which sport has a penalty shot?', 'Football/Soccer',
            'What world champ was the first figure skater ever to star in her own video game?', 'Michelle Kwan',
            'Which famous fighter appeared in the film “Requiem for a Heavyweight?', 'Cassius Clay',
            'Which auto racing term is defined as the signal for a driver to come into the pits”?', 'Black Flag',
            'Which bowling term is defined as movements and contortions of the body intended to steer the ball?',
            'Body English', ' Which golf term is defined as the putting green?', 'Dance Floor']

qs_techno = ['What has facilitated the easy access to information to so many of us?', 'Broadband Internet',
             'What has Microsoft technology designed to allow an easy combination of HTML, scripts, and ActiveX?',
             'Active Server Pages', 'Which security group grew out of the chaos caused by the Morris worm?', 'CERT',
             'What is the name of the Apple OS X email client?', 'Apple Mail or Mail',
             'Which Internet browser includes “Search Engine Manager”?', 'Mozilla Firefox',
             'Which Windows-compatible Internet browser offered a built-in BitTorrent client?', 'Opera 9',
             'Which browser employs a built-in spell-checker for text boxes?', 'Firefox 2',
             'Which company created the massively multiplayer online game World of WarCraft?', 'Blizzard Entertainment',
             'What organization accredits Top-Level Domain or TLD registrars on the internet?', 'ICANN',
             ' What was Google’s instant messaging program called?', 'Google Tal']

qs_science = ['What happens when a scientist’s expectations change how the results of an experiment are viewed?',
              'Bias', 'What is the mass per unit volume of material called?', 'Density',
              'Name the factor that affects the measure of another variable as it changes.', 'Independent variable',
              'In science, what word means a smaller representation of an object or event?', 'Model',
              'Which scientist did research with peanuts and helped southern farmers?', 'George Washington Carver',
              'What is the freezing point in Fahrenheit?', '32', 'What are the two major elements making up the sun?',
              'Hydrogen and Helium', 'What is the speed of light in a vacuum?', '299792458 Meters per second',
              'The definition “the region of the earth located between the Tropic of Cancer and the Tropic of Capricorn” best fits which science term?',
              'Tropics', ' Which scientist explained the concepts of gravity and motion?', 'Isaac Newto']

qs_medizin = ['The African nation of Benin is located in which imaginary “belt” where meningitis epidemics are common?',
              'Meningitis Belt', 'A nutrition label will base the information on how many calories per day?', '2000',
              'Which fruit has the highest fiber content?', 'Raspberries (1 cup contains 8 gm fiber!)',
              'Which organ is responsible for regulating metabolism?', 'Lungs',
              'Which new fitness trend from Oslo debuted at the IDEA World Fitness Convention in August 2011?',
              'Corebar', 'Food energy is expressed in what form?', 'Calories',
              'Which Switzerland-based organization monitors health around the world?', 'World Health Organization',
              'What is the typical heart rate in a healthy adult?', '60-80 bpm',
              'What did rural residents in Zambia initially do with the distributed mosquito nets?',
              'Used them to make wedding dresses',
              ' What watch-like fitness-calorie-sleep tracking device did Hitachi unveil at a 2011 Tokyo health fair?',
              'Hitachi Life Microscop']

qs_geo = ['What metropolitan area, not bordering a body of water, is the largest in the world?',
          'Johannesburg, South Africa', 'What city lies on the western shore of the Caspian Sea?', 'Istanbul, Turkey',
          'What sea does the Jordan River empty into?', 'Dead Sea',
          'What is the largest island in the Mediterranean Sea?', 'Sicily',
          'The Kaliningrad Oblast borders which body of water?', 'Baltic Sea',
          'Which country has the fewest people per square mile?', 'Namibia',
          'The Hanging Gardens of Babylon are located approximately 50 km south of which Arab Capital?', 'Baghdad',
          'What is the second deepest depth in the world?', 'Puerto Rico Trench',
          'Which country is known as the “Hashemite Kingdom”?', 'Jordan', ' What is the capital city of Mauritania?',
          'Nouakchot']

qs_literatur = ['The Haiku, a three-line poem that utilizes images from nature, originated in which country?', 'Japan',
                'Who wrote “The Scarlet Letter”?', 'Nathaniel Hawthrone',
                '“Crime and Punishment”, “Anna Karenina,” and “Dr. Zhivago” all belong to which kind of literature?',
                'Russian', '“And that has made all the difference” is the final line in which Robert Frost poem?',
                'The Road Not Taken',
                'Gregor Samsa is the main character in which of the short stories by Franz Kafka?', 'The Metamorphosis',
                'In Edgar Allan Poe’s poem “Annabelle Lee”, where is the subject’s kingdom located?', 'By the sea',
                'This George Orwell novel begins with the words “It was a bright cold day in April”. What’s it called?',
                '1984', 'In “The Wasteland”, which month does T.S. Eliot called “the cruelest”?', 'April',
                'Which Spanish-speaking writer was executed under Generalissimo Franco’s regime?', 'Lorca',
                ' Which of Ian Fleming’s 007 novels was first sold in the U.S. as “Too Hot To Handle”?', 'Moonrake']

qs_pol = ['Theocracy is a government recognizing whom as the supreme civil ruler?', 'God',
          'Anarchism is a political movement that rejects all what?', 'Authority',
          'Robocracy is based on the concept of government by superior what?', 'Machine Rule',
          'What is the birth name of Yugoslavia President Tito?', 'Josip Broz',
          'Which Mexican political party was voted out of office in 2000?',
          'The PRI or Institutional Revolutionary Party', 'What year did Lech Walesa become president of Poland?',
          '1990', 'What bill did Obama Veto?', 'Keystone Pipeline',
          'Who is the longest-serving president in the world?',
          'Teodoro Obiang Nguema Mbasogo, the President of the Republic of Equatorial Guinea since 1979.',
          'Which German political leader was known as the “Iron Chancellor”?', 'Otto von Bismarck',
          ' Where was the United Nations charter drawn up in 1945?', 'San Francisc']

qs_education = ['Who established a normal school?', 'Reverend Samuel Hall',
                'Which exam deals with reading, writing, and math?', 'Praxis Exam',
                'Where was the first normal school location established?', 'Champagne, France',
                'What is considered an average for an IQ Test?', '100', 'What is an IDEA?',
                'Individual Disability Education Act', 'What is pedagogy?', 'The art and science of teaching',
                'What term for an institution of higher learning comes from a Latin word meaning “the whole”?',
                'University', 'What does NJEA stand for?', 'New Jersey Education Association',
                'What views intelligence as ability-focused, finite, and determined at birth?', 'Fixed Mindset',
                ' Who developed the concept of Montessori Education?',
                'Italian physician and educator Maria Tecla Artemisia Montessor']

qs_food = ['How many calories does a bar of chocolate have?', 'About 500',
           'Which of these is in the vegetable group of the USDA 2005 MyPyramid?', 'Beets',
           'In culinary terms, what is one half of the body of an animal called?', 'Side',
           'In what form can food contamination be?', 'Physical, chemical, and biological',
           'What does the skin of the grape contain?', 'Natural yeast',
           'What kind of fats should an average person avoid if they are following USDA guidelines?', 'Saturated fats',
           'Focaccia al Rosmarino is a food item of what type of cuisine?', 'Italian',
           'Pancakes are a food item of what type of cuisine?', 'American',
           'Discretionary calories make up what part of the food pyramid diet?', 'Allowable Extra Calories',
           ' What’s the country of origin of French Fries?', 'Belgiu']

qs_gen = ['Which Spanish Explorer searched (in vain) for the seven cities of Cibola?', 'Coronado',
          'The cargo ship, SS Culross, was originally called what?', 'SS Empire Antigua',
          'Who is the author of the classic horror novel Frankenstein?', 'Mary Shelly',
          'What types of government did ancient Rome go through?', 'Monarchy, Republic, Empire',
          'Which is the fastest fish in the sea?', 'Sailfish', 'Which famous battle ended the Napoleonic Wars?',
          'Waterloo', 'What does UAV stand for?', 'Unmanned Aerial Vehicle',
          'Which composer composed the song “William Tell, Overture”?', 'Gioacchino Rossini',
          'Andy Warhol is well known for making a film (called “Sleep”) of his friend sleeping. What’s the duration of the film?',
          '5 hours and 20 minutes', ' Which country gives Magsaysay awards?', 'Philippine']

game = True

while game:
    print("Welcome to the quiz show!\n")
    possible = [question for question in qs_sport if qs_sport.index(question) % 2 == 0]
    the_question = pick(possible)

    print("Your question has been choosen!")
    answer = input(f"{the_question} \nAnswer: ")
    index_of_answer = qs_sport.index(the_question) + 1
    correct_answer = qs_sport[index_of_answer]
    if answer.lower() == correct_answer.lower():
        print("Correct!")
    else:
        print(f"Wrong!\nThe Correct Answer was: '{correct_answer}'")
