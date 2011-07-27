from collections import deque
from datetime import datetime

class State:
    """This is an internal class that keeps track of the program flow."""

    def __init__(self):
        self.out_stack = deque()
        self.state_stack = deque()
        self.global_state = {}
        self.skip = True

    def output(self, something):
        if not self.skip:
            self.out_stack.append(something)

STATE = State()

# We define the main expressions of our language.

class BEGIN:

    def __init__(self):
        STATE.skip = False
        STATE.global_state['now'] = datetime.now()


class END:

    def __init__(self):
        STATE.skip = True
        # Error checking
        if len(STATE.state_stack) > 0:
            raise Exception('Error')
        else:
            # Output everything
            for element in STATE.out_stack:
                print(element, end="")


class PRINT:
    
    def __init__(self, msg):
        STATE.output('{0}\n'.format(msg))


class WHEN:

    def __init__(self, condition):
        if condition:
            STATE.state_stack.append('w')
        else:
            STATE.state_stack.append('o')
            STATE.skip = True


class OTHERWISE:

    def __init__(self):
        self.check_otherwise(STATE.state_stack, -1)

    def check_otherwise(self, state, index):
        # This is mostly error checking...
        if len(state) == 0:
            raise Exception('Error!')
        else:
            try:
                code = state[index]
            except Exception:
                raise Exception ('Error')

        # This is the real treatment of the otherwise expression.
        if code == 'w':
            STATE.skip = True
        elif code == 'o':
            STATE.skip = False
        else:
            self.check_otherwise(state, index-1)


class ENDWHEN:

    def __init__(self):
        self.endwhen(STATE.state_stack)

    def endwhen(self, state):
        try:
            code = state.pop()
            if code not in {'w', 'o'}:
                self.endwhen(state)
            else:
                STATE.skip = False
        except Exception:
            raise Exception('Error!')


class MORNING:

    def __bool__(self):
        return STATE.global_state['now'].hour < 12


class AFTERNOON:

    def __bool__(self):
        return 12 <= STATE.global_state['now'].hour < 17


class EVENING:

    def __bool__(self):
        return 17 <= STATE.global_state['now'].hour
