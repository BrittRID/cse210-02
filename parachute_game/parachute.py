
class Parachute:

    # def __init__(self):
    def stages(stage_level):

        stages = [
            """
                 ___
                /___\ 
                \   /
                 \ /
                  O
                / | \ 
                 / \ 

        ^^^^^^^^^^^^^^^^^^^^^
            """,
            """
                 
                /___\ 
                \   /
                 \ /
                  O
                / | \ 
                 / \ 

        ^^^^^^^^^^^^^^^^^^^^^
            """,
            """
                 
                 
                \   /
                 \ /
                  O
                / | \ 
                 / \ 

        ^^^^^^^^^^^^^^^^^^^^^
            """,
            """
    
                
                
                 \ /
                  O
                / | \ 
                 / \ 

        ^^^^^^^^^^^^^^^^^^^^^
            """,
            """
                
                
                
                
                  X
                / | \ 
                 / \ 

        ^^^^^^^^^^^^^^^^^^^^^
            """,
        ]

        # self._parachute = stages
        # return self._parachute
        return stages[stage_level]