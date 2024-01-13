from turtle import Turtle, Screen
import pandas,os

state_map = r"Day 25 - Working with CSV Data and the Pandas Library\blank_states_img.gif"
states_data = pandas.read_csv(r'Day 25 - Working with CSV Data and the Pandas Library\50_states.csv')
all_state_list = states_data.state.tolist()

display_turt = Turtle()
display_turt.hideturtle()
display_turt.speed('fastest')

screen = Screen()
turtle = Turtle()

screen.title('U.S. States Game')
screen.addshape(state_map)
screen.setup(730,496)
turtle.shape(state_map)

gss_state = []

path = 'Day 25 - Working with CSV Data and the Pandas Library'

def check_guessed_states():
    global guessed_states
    if os.path.isfile('Day 25 - Working with CSV Data and the Pandas Library\guessed_states.csv') == False:
        pass
    else:
        guessed_states = pandas.read_csv('Day 25 - Working with CSV Data and the Pandas Library\guessed_states.csv')['0'].tolist()
        display_guessed(guessed_states)

def display_guessed(guessed_states):
    global gss_state
    for state in guessed_states:
        gss_state.append(state)
        all_state_list.pop(all_state_list.index(state))
        
    for state in gss_state:
        state_data = states_data[states_data.state == state]
        display_turt.goto(int(state_data.x),int(state_data.y))
        display_turt.write(f'{state}',align='center',font=('arial',12,'normal'))

check_guessed_states()

while len(gss_state) < 50:
    user_input = screen.textinput(title=f"{len(gss_state)}/50 States Guessed.", prompt="What's another state name?").title()

    print(user_input)
    if user_input in all_state_list:
        gss_state.append(user_input)
        state_data = states_data[states_data.state == user_input]
        display_turt.goto(int(state_data.x),int(state_data.y))
        display_turt.write(f'{user_input}',align='center',font=('arial',12,'normal'))
    
    if user_input == 'Exit':
        to_csv_data = pandas.DataFrame(gss_state)
        to_csv_data.to_csv(path+'\guessed_states.csv',index=False)
        break

screen.mainloop()