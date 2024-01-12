from turtle import Turtle, Screen
import pandas

state_map = r"Day 25- Working with CSV Data and the Pandas Library\blank_states_img.gif"
states_data = pandas.read_csv(r'Day 25- Working with CSV Data and the Pandas Library\50_states.csv')
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

guessed_state = []

game_on = True

while len(guessed_state) < 50:
    user_input = screen.textinput(title=f"{len(guessed_state)}/50 States Guessed.", prompt="What's another state name?").title()

    if user_input in all_state_list:
        guessed_state.append(user_input)
        state_data = states_data[states_data.state == user_input]
        display_turt.goto(int(state_data.x),int(state_data.y))
        display_turt.write(f'{user_input}',align='center',font=('arial',12,'normal'))
    
    if user_input == 'exit':
        missing_states = []
        for state in all_state_list:
            if state not in guessed_state:
                missing_states.append(state)
        break




screen.mainloop()