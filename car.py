import gym
import universe
import random

# reinforcement learning step


def determine_turn(turn, observation_n, step, total_sum, prev_total_sum, reward_n):
    # for every 15 iterations, sum the total observations and take the average
    # if lower than 0, change the duration
    # if we go 15+ iterations and get a reward each step, we're doing something right
    if(step >= 15):
        if(total_sum / step) == 0:
            turn = True
        else:
            turn = False

        # reset vars
        total_sum = 0
        step = 0
        prev_total_sum = total_sum
        total_sum = 0
    else:
        turn = False

    if(observation_n != None):
        # increment counter and reward sum
        step += 1
        total_sum += reward_n
    return(turn, step, total_sum, prev_total_sum)


def main():
    # init env
    env = gym.make('flashgames.CoasterRacer-v0')
    observation_n = env.reset()

    # init variables of the game iterations
    n = 0
    step = 0
    # sum of observations
    total_sum = 0
    prev_total_sum = 0
    turn = False

    # define our turns or keyboard actions
    left = [('KeyEvent', 'ArrowUp', True), ('KeyEvent',
                                            'ArrowLeft', True), ('KeyEvent', 'ArrowRight', False)]
    right = [('KeyEvent', 'ArrowUp', True), ('KeyEvent',
                                             'ArrowLeft', False), ('KeyEvent', 'ArrowRight', True)]
    forward = [('KeyEvent', 'ArrowUp', True), ('KeyEvent',
                                               'ArrowLeft', False), ('KeyEvent', 'ArrowRight', False)]

    # main logic
    # for _ in range(100):
    while True:
        # increment a counter for number of iterations
        n += 1

        # if at least one iteration is made, check if turn is needed
        if(n > 1):
            # if at least one iteration, check if turn
            if(observation_n[0] != None):
                # should we turn?
                if(turn):
                    # pick a random event where to turn?
                    event = random.choice([left, right])
                    # perform an action
                    action_n = [event for ob in observation_n]
                    # set turn to false
                    turn = False
        elif (~turn):
            # if no turn is needed, go straight
            action_n = [forward for ob in observation_n]

        # if there is an observation, game has started, check if turn needed
        if(observation_n[0] != None):
            turn, step, total_sum, prev_total_sum = determine_turn(
                turn, observation_n[0], step, total_sum, prev_total_sum, reward_n[0])
        # save new variables for each iteration
        observation_n, reward_n, done_n, info = env.step(action_n)
        print("Observation {}".format(observation_n))
        # print("Observation %s reward %s done %s info %s".format(
        #     observation_n, reward_n, done_n, info))
        env.render()


if __name__ == '__main__':
    main()
