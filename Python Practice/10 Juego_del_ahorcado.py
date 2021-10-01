import os

def getMyWords():
    words = []
    with open('./files/words.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words.append(line.strip())
    return words

def render_gallow(strikes):
        """Renders the gallow scene based on the strikes.
        
        Strike description:
        - For 0 it will render just the gallow
        - For 1 it will render the head
        - For 2 it will render the torso
        - For 3 it will render the left arm
        - For 4 it will render the right arm
        - For 5 it will render the left leg
        - For 6 it will render the right leg
        """

        template = """
**  **    ***    **   **  *******   **      **    ***    **   **  
**  **   ** **   ***  **  **        ***    ***   ** **   ***  **  
******   *****   **** **  **  ***   ****  ****   *****   **** **  
**  **  **   **  ** ****  **   **   ** **** **  **   **  ** ****  
**  **  **   **  **  ***  *******   **  **  **  **   **  **  ***  
        ||===================
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ||                            
        ==========@          ======== 
        ||                         || 
        ||                         || 
        ||                         || 
        """

        head = (
            (8, 23, '|',),
            (9, 23, '|',),
            (10, 22, '_',),
            (10, 23, '_',),
            (10, 24, '_',),
            (11, 20, '|',),
            (11, 22, '.',),
            (11, 24, '.',),
            (11, 26, '|',),

            (12, 21, '\\',),
            (12, 23, '_',),
            (12, 25, '/',),
        )

        torso = (
            (13, 23, '|',),
            (13, 24, '|',),
            (14, 23, '|',),
            (14, 24, '|',),
            (15, 23, '|',),
            (15, 24, '|',),
            (16, 23, '|',),
            (16, 24, '|',),
        )

        left_arm = (
            (14, 20, '=',),
            (14, 21, '=',),
            (14, 22, '=',),
        )
        right_arm = (
            (14, 25, '=',),
            (14, 26, '=',),
            (14, 27, '=',),
        )

        left_leg = (
            (17, 22, '/',),
            (17, 23, '/',),
            (18, 21, '/',),
            (18, 22, '/',),
        )
        right_leg = (
            (17, 24, '\\',),
            (17, 25, '\\',),
            (18, 25, '\\',),
            (18, 26, '\\',),
        )
        tramp_closed = (
            (19, 19, '=',),
            (19, 20, '=',),
            (19, 21, '=',),
            (19, 22, '=',),
            (19, 23, '=',),
            (19, 24, '=',),
            (19, 25, '=',),
            (19, 26, '=',),
            (19, 27, '=',),
        )
        tramp_opened = (
            (19, 19, '\\',),
            (19, 20, '\\',),
            (20, 20, '\\',),
            (20, 21, '\\',),
            (21, 21, '\\',),
            (21, 22, '\\',),
            (22, 22, '\\',),
            (22, 23, '\\',),
        )

        scene_descriptors = []

        if strikes >= 1:
            scene_descriptors += head
        if strikes >= 2:
            scene_descriptors += torso
        if strikes >= 3:
            scene_descriptors += left_arm
        if strikes >= 4:
            scene_descriptors += right_arm
        if strikes >= 5:
            scene_descriptors += left_leg
        if strikes == 6:
            scene_descriptors += right_leg

        if strikes < 6:
            scene_descriptors += tramp_closed
        else:
            scene_descriptors += tramp_opened

        lines = [list(line) for line in template.splitlines()]

        for descriptor in scene_descriptors:
            lines[descriptor[0]][descriptor[1]] = descriptor[2]

        scene = '\n'.join([''.join(l) for l in lines])
        print(scene)

def run():

    myWords = getMyWords()
    word = dict(enumerate(myWords[0]))
    print('Hi, do you like to play with me? ')
    iteration = int(input('How many iterations would you like to have: '))

    values = []
    hangman = ['_']*len(word.keys())
    strikes = 0
    for i in range(iteration):
        
        render_gallow(strikes)

        add = ''
        for i in range(len(hangman)):
            add += hangman[i] + ' '
        print('Guess the word!') 
        print(add)
        print('')
        getValue = input('Insert one letter: ')

        os.system('clear')
        counHits = 0
        for index,letter in word.items():
            
            if getValue == letter:
                values.append(getValue)
                hangman[index] = getValue
                counHits = 1

        if counHits == 0:
            strikes += 1

        if strikes >= 6:
            print('=========== GAME OVER ===========')
            print(f'WORD: {myWords[0]}')
            input('<press enter to restart the game or ctrl + c to exit>')
            continue

if __name__=='__main__':
    run()