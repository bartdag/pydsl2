from simpledsl.timeprint import *

(BEGIN(),
    PRINT('This is the beginning.'),
    WHEN(MORNING() or AFTERNOON()),
        PRINT('This is morning or afternoon.'),
        WHEN(MORNING()),
            PRINT('This is the morning.'),
            PRINT('This is the start of a new day!'),
        OTHERWISE(),
            PRINT('This is the afternoon.'),
            PRINT('Still the evening to go through!'),
        ENDWHEN(),
    OTHERWISE(),
        PRINT('This is probably evening!'),
    ENDWHEN(),
    PRINT('This is the end.'),
END())
