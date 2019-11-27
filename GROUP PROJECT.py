print('''WELCOME TO CYBER TEENS QUIZ)
             Which quiz would you like:
              (1) Sciences
              (2) Arts
              (3) Commercial ''')
#users_response = input('Your response: ').lower()
#def user_response(users_response):
 #   while users_response != 'stop':
  #      if users_response == 'sciences' or users_response == 'science' or users_response == '1':
   #         pass
    #    elif users_response == 'arts' or users_response == 'art' or users_response == '2':
     #       pass
      #  elif users_response == 'commercial' or users_response == '3':
       #     pass
def questions():
    score = 0
    sciences =['''What is the full meaning of L.C.M :
                  (a) Lowest converter multitude
                  
                  (b) Lowest common multiple
                  
                  (c) Low common mutiple  \n Your answer: ''',

               '''Which of the following is the correct definition for diffusion :
                  (a) It is the movement of molecules from region of lower concentration 
                      to higher concentration.
 
                  (b) It is the movement of molecules from region of lower concentration 
                      to higher concentration involving a semi permeable membrane.
                  (c) It is the movement of molecules from region of higher concentration
                      to lower concentration till they are evenly seperated. \n Your answer:  ''',

              '''In the periodic table the 20th element is :
                  (a) pottasium
                  
                  (b) argon
                  
                  (c) calcium \n Your answer ''',

              '''Issac newton's first law of motion(inertia) states that :
                  (a) A body continues to be at motion unless an external force is
                      applied.
                  (b) A body continues to be at rest untill an external force is 
                      applied.
                  (c) The rate of change of a body is directly proportional to
                      the impressed or applied force that takes place in the
                      direction of force. \n Your answer:  ''',

              '''Ships haves line painted on thier hulls which must be above water to dectect if 
                 the upthrust is equal to the total weight of the ship, this line is called :
                  (a) Buoyancy
                  (b) Plimsol line
                  (c) Cargo line \n Your answer:  ''',

              '''Seisometers are used to measure? :
                  (a) Days of the year
                 
                  (b) Transverse wave
                  (c) Huge amount of energy many thousands of kilometers
                     underground. \n Your answer:  ''',             

              '''A diagonal matrix is :
                  (a) A matrix which has a 1 in every element of the leading diagonal,
                     and 0 elsewhere.
                  (b) A square matrix which all the elements are 0 except those on the 
                     the diagonal from the top to bottom right.
                  
                  (c) A matrix with all elements 0. \n Your answer: ''',

              '''Among the listed formulas below which is the correct formula for the 
                 total surface area of a pyramid:
                 
                  (a) 1/3 base area x height
                 
                  (b) area of triangular cross-section x lenght/height
                  (c) sum of the area of four congruent triangular faces and
                       area of the base. \n Your answer:  ''',

             '''Calculate the rate percent per annum at which #4500 will earn
                #500 in 4 years:
                 (a) 2.89%
                 (b) 2.78%
                 (c) 3% \n Your answer:  ''',

             '''The first stage of cell division is :
                 (a) Metaphase
                 (b) Interphase
                 (c) Anaphase \n Your answer:  ''',


             '''When male gamete and the female gamete fuse it forms :
                 (a) White blood cells
                 (b) Zygote
                 (c) Placenta \n Your answer:  ''',

             '''The full meaning of DNA is :
                 (a) Deribionucliec antigens
                 (b) Deoxyribonucliec acid
                 
                 (c) Deoxrybonucliec acid \n Your answer:  ''',

             '''Which of the following element is an alkali earth metal :
                 (a) Mg
                 (b) Rb
                 (c) Li  \n Your answer:  ''',
               
             '''The center of the earth is very hot
                 (a) True
                 (b) False
                 (c) Not sure \n Your answer:  ''',
             '''The continents in which we live in have been stagnant sinse the begin of the world
                 (a) True
                 (b) False
                 (c) Not sure \n Your answer: ''',
             '''Which of this statements is true
                 (a) The sun goes around the earth
                 (b) The earth goes around the sun
                 (c) The earth and the sun goes around the moon \n Your answer: ''',
             '''How many bones do sharks have in their body
                 (a) 1023
                 (b) 452
                 (c) 0 \n Your answer: ''',
             '''The molten rock that comes from a volcano after it has erupted is known as what
                 (a) Lava
                 (b) sedimentary
                 (c) Non of the stated \n Your answer: ''',

             '''What is the closest star to the earth
                 (a) Sun
                 (b) Acrux
                 (c) Edasich \n Your answer: ''', 
             '''What is thr radius of the sun
                 (a) 695632
                 (b) 695359
                 (c) 695143 \n Your answer: ''',
               ]
    answers= ['b','c','c','b','b','c','b','c','b','b','b','b','a','a','b','b','c','a','a','b']
    for check in range(len(sciences)) :
        user_answer = input(sciences[check]).lower()
        confirmation = sciences.index(sciences[check])
        correct_answer = answers[confirmation]
        if user_answer == correct_answer:
            score += 1
        elif user_answer != correct_answer :
            score += 0

    print(' ')
    print(f'Your final score is {score}')
    return

questions()     
